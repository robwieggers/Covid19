# Covid-19 Dashboard

This project contains a dashboard for monitoring the spread of Cond-19.
firstly, it will focus on monitoring Dutch data, later on extensions could be possible

The dashboard is open-source and uses publicly available data. The dashboard is written in python and 
uses the dash library to show the interactive dashboard 

## Prerequisites
To use this dashboard, one needs have a system with Python 3 installed. A simple laptop should be sufficient.

## How to run?
### Install python libraries
From the terminal, change directory to the root of the repository and execute

`pip install -r requirements.txt`

### Launch the dashboard
From the terminal, execute:

`python ./src/app.py`

The dashboard will be available in your browser, on a localhost:

`http://127.0.0.1:8050/`