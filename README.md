# Generic Real Estate Consulting Project

Group Number: Group 60

Names: Bolin Zheng, Xiaohan Guo, Bohan Su
Student IDs: 1079347, 1174455, 1174197

**Research Goal:** Recommend which region are most likely to increase in rental prices.

**Timeline:** The timeline for the research area is 01/01/2017 - 30/12/2025.

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

### 2. Feature Prediction(Steven+Cecily)

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



👀️All plots could save into `plots`.

Since the folium graph cannot be saved to the computer, using the built-in print function in the web browser to print out the pictures.

爬数据->数据预处理->merge population,income->merge distance->merge hospital->数据预处理