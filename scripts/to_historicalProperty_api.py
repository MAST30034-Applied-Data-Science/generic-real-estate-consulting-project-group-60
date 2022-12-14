# This script will read the data 
# after preprocessing by the notebook "notebooks/Prepare_distance_to_historicalProperty.ipynb"
# ANd Get the 'real distance' and time spend of each property(Duration) to both the nearest School and train station
# For the historical data

import pandas as pd
from datetime import datetime
from time import sleep
import openrouteservice
import random




new_data = pd.read_csv("../data/curated/historical_property.csv")
new_data = new_data.drop(columns=['Unnamed: 0'])


# 15895  rows total

client = openrouteservice.Client(key='YOUR_API_KEY',retry_timeout = 60, timeout= 60) # Specify your personal API key

count = 0

a = datetime.now()

for index in range(0,15895):
    

    try:
        
        
        from_coor = [new_data.iloc[index,2],new_data.iloc[index,1]]

        to_Sch_coor_X = new_data.iloc[index,8]
        to_Sch_coor_Y = new_data.iloc[index,7]

        Sch_coords = ((from_coor[0],from_coor[1]),(to_Sch_coor_X,to_Sch_coor_Y))

        sch_routes = client.directions(Sch_coords, profile='driving-car')


        school_distance_txt = round(sch_routes['routes'][0]['summary']['distance']/1000,1)
        school_duration_txt = round(sch_routes['routes'][0]['summary']['duration']/60,1)

        new_data.iloc[index,14] = school_distance_txt
        new_data.iloc[index,15] = school_duration_txt
        count+=1

        if(count%39 == 0):
            b = datetime.now()
            if((b-a).seconds <= 45):
                sleep(random.uniform(20.4,25.34))
                client = openrouteservice.Client(key='YOUR_API_KEY',retry_timeout = 50, timeout= 50)
                a = datetime.now()

        if (count >= 9999):
                break

        to_Station_coor_X = new_data.iloc[index,12]
        to_Station_coor_Y = new_data.iloc[index,11]

        Sta_coords = ((from_coor[0],from_coor[1]),(to_Station_coor_X,to_Station_coor_Y))

        sta_routes = client.directions(Sta_coords, profile='driving-car')


        station_distance_txt = round(sta_routes['routes'][0]['summary']['distance']/1000,1)
        station_duration_txt = round(sta_routes['routes'][0]['summary']['duration']/60,1)

        new_data.iloc[index,16] = station_distance_txt
        new_data.iloc[index,17] = station_duration_txt
        count+=1

        if(count%39 == 0):
            b = datetime.now()
            if((b-a).seconds <= 45):
                sleep(random.uniform(20.4,25.34))
                client = openrouteservice.Client(key='YOUR_API_KEY',retry_timeout = 50, timeout= 50)
                a = datetime.now()

        if (count >= 9999):
                break

    except:

        try:

            from_coor = [new_data.iloc[index,2],new_data.iloc[index,1]]

            to_Sch_coor_X = new_data.iloc[index,8]
            to_Sch_coor_Y = new_data.iloc[index,7]

            Sch_coords = ((from_coor[0],from_coor[1]),(to_Sch_coor_X,to_Sch_coor_Y))

            sch_routes = client.directions(Sch_coords, profile='driving-car')


            school_distance_txt = round(sch_routes['routes'][0]['summary']['distance']/1000,1)
            school_duration_txt = round(sch_routes['routes'][0]['summary']['duration']/60,1)

            new_data.iloc[index,14] = school_distance_txt
            new_data.iloc[index,15] = school_duration_txt
            count+=1

            if(count%39 == 0):
                b = datetime.now()
                if((b-a).seconds <= 45):
                    sleep(random.uniform(20.4,25.34))
                    client = openrouteservice.Client(key='YOUR_API_KEY',retry_timeout = 50, timeout= 50)
                    a = datetime.now()
            if (count >= 9999):
                break

            to_Station_coor_X = new_data.iloc[index,12]
            to_Station_coor_Y = new_data.iloc[index,11]

            Sta_coords = ((from_coor[0],from_coor[1]),(to_Station_coor_X,to_Station_coor_Y))

            sta_routes = client.directions(Sta_coords, profile='driving-car')


            station_distance_txt = round(sch_routes['routes'][0]['summary']['distance']/1000,1)
            station_duration_txt = round(sch_routes['routes'][0]['summary']['duration']/60,1)

            new_data.iloc[index,16] = station_distance_txt
            new_data.iloc[index,17] = station_duration_txt
            count+=1

            if(count%39 == 0):
                b = datetime.now()
                if((b-a).seconds <= 45):
                    sleep(random.uniform(20.4,25.34))
                    client = openrouteservice.Client(key='YOUR_API_KEY',retry_timeout = 50, timeout= 50)
                    a = datetime.now()
            
            if (count >= 9999):
                break
            


        except openrouteservice.exceptions.ApiError:
            new_data.iloc[index,14] = 'school_distance_txt'
            new_data.iloc[index,15] = 'school_duration_txt'
            new_data.iloc[index,16] = 'station_distance_txt'
            new_data.iloc[index,17] = 'station_duration_txt'
        
        except KeyError:
            new_data.iloc[index,14] = 'school_distance_txt'
            new_data.iloc[index,15] = 'school_duration_txt'
            new_data.iloc[index,16] = 'station_distance_txt'
            new_data.iloc[index,17] = 'station_duration_txt'



        


new_data.to_csv("../data/curated/historical_property.csv")


