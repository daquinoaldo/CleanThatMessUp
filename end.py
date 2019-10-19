import matplotlib.pyplot as plt
import pandas as pd
import geopandas
from geopandas import GeoDataFrame
from shapely.geometry import Point

# dataset
COLS = ['elon', 'elat']
df = pd.read_csv("data/end.csv", usecols=COLS)
print(f"read {len(df)}")

pd.to_numeric(df.elon)
pd.to_numeric(df.elat)
print("to_numeric")

df.drop_duplicates(['elon', 'elat'])
print(f"drop {len(df)}")

#df = df[(df['elon']<=180) & (df['elon']>=-180)]
#df = df[(df['elat']<=90) & (df['elat']>=-90)]
#print(f"filter {len(df)}")

df.elon = df.elon.apply(lambda x : x if x <= 180 else x - 360)
print(f"mod {len(df)}")

#df = df.sample(frac=.05, random_state=42)
#print(f"sample {len(df)}")


# dataset to map
gdf = GeoDataFrame(
    df.drop(['elon','elat'], axis=1),
    crs={'init': 'epsg:4326'},
    geometry=[Point(xy) for xy in zip(df.elon, df.elat)])
print("geo")

# plot settings
fig, ax = plt.subplots()
ax.set_aspect('equal')

# plot
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot(ax=ax, color='white', edgecolor='black', linewidths=0.1)
gdf.plot(ax=ax, color='red', markersize=0.0001, alpha=0.5)
print("plot")

# save fig
plt.savefig("img/end.png", dpi=1200, bbox_inches = "tight")
plt.savefig("img/end.svg", dpi=1200, bbox_inches = "tight")
plt.clf()