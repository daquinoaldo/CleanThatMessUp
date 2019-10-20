import pandas as pd
import geopandas
from geopandas import GeoDataFrame
from shapely.geometry import Point, Polygon, LinearRing
from shapely.geometry.multipolygon import MultiPolygon
from math import radians, cos, sin, asin, sqrt
from tqdm import tqdm

tqdm.pandas()

# dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
COLS = ['elon', 'elat']
df = pd.read_csv("data/end.csv", usecols=COLS)
print(f"read {len(df)}")

# normalize
pd.to_numeric(df.elon)
pd.to_numeric(df.elat)
print("to_numeric")

# drop duplicates
df.drop_duplicates(['elon', 'elat'])
print(f"drop {len(df)}")

# filter
#df = df[(df['elon']<=180) & (df['elon']>=-180)]
#df = df[(df['elat']<=90) & (df['elat']>=-90)]
#print(f"filter {len(df)}")

# mod
df.elon = df.elon.apply(lambda x : x if x <= 180 else x - 360)
print(f"mod {len(df)}")

# sample
#df = df.sample(frac=.01, random_state=42)
#print(f"sample {len(df)}")


# dataset to map
gdf = GeoDataFrame(
    df.drop(['elon','elat'], axis=1),
    crs={'init': 'epsg:4326'},
    geometry=[Point(xy) for xy in zip(df.elon, df.elat)])
print("geo")

# map the world into a list of polygons
wpolygs = []
for i in world.geometry:
    if type(i) == Polygon:
        wpolygs.append(i)
    elif type(i) == MultiPolygon:
        wpolygs.extend(i)
    else:
        print(f'Unknown type {type(i)}')

# get the closest point in a polygon wrt a given point
def get_closest_pt(point, polyg):
    pol_ext = LinearRing(polyg.exterior.coords)
    d = pol_ext.project(point)
    p = pol_ext.interpolate(d)
    closest_point_coords = list(p.coords)[0]
    return closest_point_coords

# dist between two points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles. Use 6371 for kilometers
    return c * r

# dist between a point and a coast polygon
def get_dist(point, polyg):
    [x, y] = get_closest_pt(point, polyg)
    dist = haversine(point.x, point.y, x, y)
    return dist

# min dist of that point from a coast
def min_dist(point):
    return min([get_dist(point, p) for p in wpolygs])

# add the coast_dist to the dataset
gdf['coast_dist'] = gdf.geometry.progress_apply(lambda x: min_dist(x))
gdf.to_pickle('data/coast_dist')