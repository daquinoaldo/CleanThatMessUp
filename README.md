# CleanThatMessUp

### Dataset
The dataset used is the [gdp_interpolated_drifter](http://osmc.noaa.gov/erddap/tabledap/gdp_interpolated_drifter.html), offered by the [NOAA](https://www.noaa.gov/) agency. The project uses a [restricted version](http://osmc.noaa.gov/erddap/tabledap/gdp_interpolated_drifter.csv?ID%2Celat%2Celon&distinct()) of the dataset in which only end coordinates and ID have been used.

### Install
```
pip3 install -r requirements.txt
```

### Run
```
python3 flow.py
python3 end.py
```

### Results
![Target coasts](/img/end.png)
