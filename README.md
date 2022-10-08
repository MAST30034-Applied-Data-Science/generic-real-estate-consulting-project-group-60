# Generic Real Estate Consulting Project

Group Number: Group 60

Names: Bolin Zheng, Xiaohan Guo, BohanSu, XinyuanQiao, TianhaoLiu.


Student IDs: 1079347, 1174455, 1174197, 1137963, 1105160.

**Research Goal:** Recommend which region are most likely to increase in rental prices.

**Timeline:** The timeline for the research area is 01/01/2017 - 30/12/2027.

**Datasets:**

* Historical data
* 2022 data

**External datasets:**

All location data file will be saved into the `data/Geo_data`

* School Location: `data/Geo_data/schoolLocations2022.csv` 👀️ From: [https://discover.data.vic.gov.au/dataset/school-locations-2022](https://discover.data.vic.gov.au/dataset/school-locations-2022)
* Police Station: `data/Geo_data/POLICE_STATION.csv` 👀️ From: [https://data.aurin.org.au/dataset/vic-govt-delwp-datavic-vmfeat-police-station-na](https://data.aurin.org.au/dataset/vic-govt-delwp-datavic-vmfeat-police-station-nahttps://)
* Train Station: `data/Geo_data/datasource-VIC_Govt_PTV-VIC_Govt_DELWP_datavic_PTV_METRO_TRAIN_STATION.csv` 👀️ From: [https://data.aurin.org.au/dataset/vic-govt-ptv-datavic-ptv-metro-train-station-na/resource/1497b4cf-883f-4910-ba12-49a45c9e36bd](https://data.aurin.org.au/dataset/vic-govt-ptv-datavic-ptv-metro-train-station-na/resource/1497b4cf-883f-4910-ba12-49a45c9e36bd)
* SA2 area shape file: `data/Geo_data/1270055001_sa2_2016_aust_shape` 👀️ From: [https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.001July%202016?OpenDocument](https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.001July%202016?OpenDocument)

The `requirements.txt`is attached in the root directory, which is produced by the command `pip3 list --format=freeze > requirements.txt`.

To run the pipeline, please visit the `scripts` directory first(since the historical data request website is not allowed to using the web script, the historical data has been saveed into the `data/Property` and then visit the `notebooks` directory.

```
🚀️ Please run the files listed below In Order !!!!:
```

## Steps

### 1. Data Scraping

### Openroute Service API:

Supported by 2022 ***openrouteservice***

Using the open route service API to get the information needed:

* The information needed to be preprocessed first by using the notebook `notebooks/Prepare_distance_to_nowProperty.ipynb`  and the notebook `notebooks/Prepare_distance_to_historicalProperty.ipynb` . Saving to file `data/curated` , called `historical_property.csv` and `new_property.csv`.
* Then using the python script `scripts/to_nowProperty_api.py` and `scripts/to_historicalProperty_api.py` to get the Information needed by calling the API.

After running the the python scripts above, the informnation would be stored into the file `data/curated`. Called `historical_property.csv` and `new_property.csv`.

### 2. Feature Prediction(Steven+Cecily)

* `notebooks/Income_prediction.ipynb*`: Predict income by linear regression

### 3. Data Preprocessing(Kevin+Len+Steven+Aaron)

* `notebooks/Data_preprocess_2017_2021#1`: read the full historic data after scrapping, find the closest SA2 region, merge the population and income into the dataset.
* `notebooks/Data_preprocessing_2022#2`: read the 2022 current data after scrapping, find the closest SA2 region, merge the population and incoem into the dataset.
* `notebooks/produce_23_25_data#3`: Produce the 2025-2025 data, including merge the future population and income.
* `notebooks/Data_preprocess_merge_2017_2022#4`: Merge the 2017-2022 data together with a various of data preprocessing.
* `notebooks/Hospital#5`: Adding the number of hospital nearby inside both 2017-2022 and 2023-2025 data.
* `notebooks/data_cleaning#6`: After all the data preprocessing, remove all the outliers inside the 2017-2022 data, to avoid any invalid results.
* `notebooks/Feature selection#7`: Doing applied the feature selection method using random forest.

### 4. Modelling(Kevin+Len+Steven)

* `notebooks/Random_forest#8`: Random forest model.
* `notebooks/Live__afford_rate.ipynb`: Create livability and affordability rate by the weighted index from feature selection.

👀️All plots could save into `plots`.

Since the folium graph cannot be saved to the computer, using the built-in print function in the web browser to print out the pictures.
