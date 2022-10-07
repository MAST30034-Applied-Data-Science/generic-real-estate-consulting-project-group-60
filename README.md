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

All location data file include: school, police station and train station will be saved into the `data/Geo_data`

* School Location: Train station location data: from stored at ___
* Police Station:
* Train Station:

School Location data: from

The `requirements.txt`is attached in the root directory, which is produced by the command `pip3 list --format=freeze > requirements.txt`.

To run the pipeline, please visit the `scripts` directory first and then visit the `notebooks` directory.

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
