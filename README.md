# Generic Real Estate Consulting Project

Group Number: Group 60

Names: Bolin Zheng, Xiaohan Guo, BohanSu
Student IDs: 1079347, 1174455, 1174197

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

School Location data: from

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

* The information needd to be preprocessed first by using the notebook `notebooks/Prepare_distance_to_nowProperty.ipynb`  and the notebook `notebooks/Prep` .
* Then using he python script `APINowData.py` to get the Information needed by calling the API.

### 2. Feature Prediction

### 3. Data Preprocessing

### 4. Modelling

👀️All plots could save into `plots`.

Since the folium graph cannot be saved to the computer, using the built-in print function in the web browser to print out the pictures.
