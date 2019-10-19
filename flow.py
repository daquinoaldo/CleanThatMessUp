import matplotlib.pyplot as plt
import pandas as pd
import geopandas
from geopandas import GeoDataFrame
from shapely.geometry import Point

# dataset
df = pd.read_csv("data/small.csv")
print(f"read {len(df)}")

pd.to_numeric(df.longitude)
pd.to_numeric(df.latitude)
print("to_numeric")

df = df[(df['longitude']<=180) & (df['longitude']>=-180)]
df = df[(df['latitude']<=90) & (df['latitude']>=-90)]
print(f"filter {len(df)}")

# dataset to map
gdf = GeoDataFrame(
    df.drop(['longitude','latitude'], axis=1),
    crs={'init': 'epsg:4326'},
    geometry=[Point(xy) for xy in zip(df.longitude, df.latitude)])
print("geo")

# plot settings
fig, ax = plt.subplots()
ax.set_aspect('equal')

# plot
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot(ax=ax, color='white', edgecolor='black', linewidths=0.1)
gdf.plot(ax=ax, markersize=0.0001, alpha=0.3)
print("plot")

# save fig
plt.savefig("img/flow.png", dpi=1200, bbox_inches = "tight")
plt.savefig("img/flow.svg", dpi=1200, bbox_inches = "tight")
plt.clf()