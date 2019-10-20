# CleanThatMessUp

### Dataset
The dataset used is the [gdp_interpolated_drifter](http://osmc.noaa.gov/erddap/tabledap/gdp_interpolated_drifter.html), offered by the [NOAA](https://www.noaa.gov/) agency. The project uses a [restricted version](http://osmc.noaa.gov/erddap/tabledap/gdp_interpolated_drifter.csv?ID%2Celat%2Celon&distinct()) of the dataset in which only end coordinates and ID have been used.
The dataset is used in the article [Garbage Patch Visualization Experiment] (https://svs.gsfc.nasa.gov/4174) from NASA.
### Install
```bash
pip3 install -r requirements.txt
mkdir data img
wget -O ./data/small.csv http://osmc.noaa.gov/erddap/tabledap/gdp_interpolated_drifter.csv?ID%2Celat%2Celon&distinct()
```

### Run
```
$ python3 compute_coast_dist.py
$ python3 plot_coast.py
```

### Results
![Target coasts](/img/coast.png)