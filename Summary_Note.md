# Summary note

## Find relative dataset
Find relative dataset, such as rental prices, public transportation, school location, income, and population. The reason that we need to find datasets for public transportation and school is these features are most relative to the livability of suburbs. The previous rental prices are the y train of the prediction model. Income and population are the features which we think are relative to the rental prices of real estate.

## Scrap data
Information for each houses need to be scraped from Domain.com. We have scrapped 15,000 instances of information for houses. The determined features are Longitude, Latitude, Price per week, property type, house area, room number, postcode, and house price increase rate.

## Use API find distance
Considering that the api is used to find the nearest school or metro station in the area of the house, the requests amount required from the api are limited, making it a very slow efficiency to obtain the data. Using the geolocation formula, the closest school or metro station is calculated directly from the coordinates which is based on the linear distance. The api is then requested to obtain the real distance needed to drive and the estimated road usage time.


## Predict Income and population
We cannot find future data for both income and population. Therefore, for income prediction, we find the previous income data from 2010-2015, we assume the income is increasing linearly. 
For population prediction, we found official forecasts for Year 2026, 2031 and 2036.
Based on the forecasts, we also used linear regression to do the prediction for remaining years. For Year 2026, 2031 and 2036, we simply use the prediction from official forecasts.


## Data merge by SA2 region
We choose to merge dataset base on SA2 region. We have also created a data frame for SA2 region which including the postcodes for each region. 


## Feature selection 



## Prediction
We choose to create our model based on the features from 2017-2022. The merged Data from 2017-2021 will used to train the model. To calculate the model accuracy, Eighty percent of rental prices from 2022 will be the Y train and the remaining data from 2022 will be the Y test.







