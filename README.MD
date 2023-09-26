<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=salesp07.RideMate">


## RideMate version 1.0.
This version of RideMate is to develop a web application to display occupance and weather infor mation for [Dublin Bikes](http://www.dublinbikes.ie).

## Introduction
The repository is for the Dublin bikes app. The website had to be shutdown LOW [AWS EC2](https://aws.amazon.com/pm/ec2/) balance
- The project scrapped data from [JCDecauxAPI](https://developer.jcdecaux.com/#/home) and [OpenWeather API](https://openweathermap.org/api) to get data bikes data for 3 months.
- The Scrapper ran in an [AWS EC2](https://aws.amazon.com/pm/ec2/) instance and stored data in an [AWS RDS](https://aws.amazon.com/rds/) ([MySQL](https://www.mysql.com/))
- An ML model was developed with data and deployed on a [Flask](https://flask.palletsprojects.com/en/2.3.x/) instance

### This is Dublin Bikes a webapp for our DBbikes system. 
<!-- ![avatar](static/RideMate.png) -->

<p align="center">
  <img width="929" alt="db_1" src="static/complete_ui.png">
</p>

### Features
1. Display bike stations and occupancy information on a map. 
Each bike station is a marker on the map, with its color ranges from clear (no available bike) to light blue (very few available bikes) to darker blue (more available bikes) and to red (many available bikes).
When hovering on the marker (in the shape of bike), user can see some information on the info window.
<p align="center">
  <img width="929" alt="db_1" src="static/heatmap_windowinfo.gif">
</p>

2. Show weather and historical availability
When user click on a marker, the information about weather (current and in the next 24 hours) and historical average availability of bikes and bikestands (by day of week and by hour in the same weekday) shows up on the right sidebar.
<p align="center">
  <img width="929" alt="db_1" src="static/view_detail.gif">
</p>

3. Predict available bikes
When user choose a time of today or tomorrow, they can get the prediction of available bikes for that time. 
<p align="center">
  <img width="929" alt="db_1" src="static/view_prediction.gif">
</p>

4. Find 5 nearest stations
When user types in the search box, the search box is auto completed based on Google Places API. 
User can choose their desired location from the dropdown list. 
When five nearest stations to the chosen location are shown, user can click on each options to locate the station and interact with the corresponding marker.
<p align="center">
  <img width="929" alt="db_1" src="static/five_nearest_stations.gif">
</p>

## Installation
The files can be downloaded and run using:

```shell
$ git clone https://github.com/yuanindublin/RideMate.git
$ cd dublinbikes/dublinbikes
$ python run.py
```
Then open localhost:5000 in your browser to view the webpage. Clicking on a station marker will show the necessary information and provide more options.


## Running Test
Test file can be run using pytest:

```shell
$ pytest -s
```

## Contributors
[Yingyuan Li](https://github.com/yuanindublin)

<a href="url"><img src="https://avatars.githubusercontent.com/yuanindublin" height="auto" width="200" style="border-radius:50%"></a>

[Fei Gao](https://github.com/Fei117117)

[Ly M Nguyen](https://github.com/minhlynguyen)

## License
