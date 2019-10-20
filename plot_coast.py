import matplotlib.pyplot as plt
import pandas as pd
import geopandas

# dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
gdf_dists = pd.read_pickle('data/coast_dist')
print(f"all {len(gdf_dists)}")

coasts_pts = gdf_dists[gdf_dists['coast_dist'] < 30]
print(f"coast {len(coasts_pts)}")

# plot settings
fig, ax = plt.subplots()
ax.set_aspect('equal')

# plot all over in blue and coasts in red
world.plot(ax=ax, color='white', edgecolor='black', linewidths=0.1)
#gdf_dists.plot(ax=ax, color='blue', markersize=0.01, alpha=0.5)  # all over in blue
coasts_pts.plot(ax=ax, color='red', markersize=0.01, alpha=1)     # only on coasts in red
print("plot end")

# save fig
plt.savefig("img/coast.png", dpi=3600, bbox_inches = "tight")
plt.savefig("img/coast.svg", dpi=3600, bbox_inches = "tight")
plt.clf()
print("save fig coast")