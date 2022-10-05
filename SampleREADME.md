# MAST30034 Project 1 README.md

- Name: Bolin Zheng
- Student ID: 1079347

## README

**Research Goal:** The analysis on High-Volume For-Hire Services (HVFHS) driver's Income in NYC

**Timeline:** The timeline for the research area is 01/06/2020 - 30/11/2020.

**External datasets:**  [New York 2020-06-01 to 2020-11-30.csv](https://www.visualcrossing.com/weather/weather-data-services)  (By clicking This Link, direct to the website where the Data being provided)

> The external datasets is ***Reference from***: https://www.visualcrossing.com/weather/weather-data-services
>
> Since the dataset could not be downloaded using python script, stored the weather data inside the `data/Outter`

The `requirements.txt`is attached in the root directory, which is produced by the command `pip3 list --format=freeze > requirements.txt`.

To run the pipeline, please visit the `scripts` directory first and then visit the `notebooks` directory.

```
🚀️ Please run the files listed below In Order !!!!:
```

1. `download.py`: This downloads the raw data into the `data/raw` directory. *(Please Becareful with the File path)*
2. `DataPrepare.ipynb`: This notebook details preparition steps and outputs `selected_results` to the `data/curated` directory.
3. `DataPreprocessed.ipynb`: This notebook details preprocessing steps and outputs `Filtered_results` to the `data/curated` directory.
4. `FeatureEngineering.ipynb`: This notebook details FeatureEngineering steps and outputs`Featured_results` to the `data/curated` directory.
5. `Datainvestigation.ipynb`: This notebook details Investigation steps and outputs several files to the `data/curtaed` directory for Graph Drawing.
6. `GraphDrawing.ipynb`: This notebook is used to visualizatio different data sets mainly from the `Datainvestigation.ipynb` and other notebooks.
7. `FeatureEngStep_two.ipynb`: This notebook will use the find out from the graph drawing, adjust features in the data set from `data/curated/Featured_results` and out put the new data set to the `data/curated/Featured_results_two`.
8. `MachineLearning.ipynb`: This notebook will use the data set from `data/curated/Featured_results_two`to analysing and discussing the model.
9. `visualization_after_ML.ipynb`: This notebook will use the data set from `data/curated/Prediction_results_BYRFR`to discuss and visualizing the model.

👀️All plots could save into `plots` during running the pipeline except four plots:

`plots/foliumChoroplethMap_percent_PIkUP.jpg`, `plots/foliumChoroplethMap_TotalIncomeRate.jpg`,

`plots/foliumChoroplethMap_Pred_Total_income_rate.jpg`,and`plots/foliumChoroplethMap_Real_Total_income_rate.jpg`.

Since the folium graph cannot be saved to the computer, using the built-in print function in the web browser to print out the pictures.
