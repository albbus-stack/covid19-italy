# covid19-italy
[![GPLv3 License](https://img.shields.io/badge/%20License-GPL%20v3-yellow?style=flat-square)](https://opensource.org/licenses/)
[![Plotly](https://img.shields.io/badge/%20-Plotly-blue?style=flat-square)](https://github.com/plotly)
![Committed](https://img.shields.io/github/last-commit/albbus-stack/covid19-italy?label=Committed&color=42c5f5&style=flat-square&logo=heroku&logoColor=42c5f5&logoWidth=17&labelColor=black)

Map and charts data visualization of __Covid19__ cases in __Italy__, kindly hosted by [Heroku](https://heroku.com) on https://cov-19-it.herokuapp.com/.

Built in Python 3.8, using [pandas](https://github.com/pandas-dev/pandas) to handle dataframes and [plotly](https://github.com/plotly/plotly.py) for interactive visualization, renders in browser using [dash](https://github.com/plotly/dash).

## Build it

###### Requirements

* Python 3.8
* Install all the requirements in [requirements.txt](requirements.txt).

###### Steps

1. Change the province you want to visualize in line 119 and 130 inside [main.py](main.py).

2. Change also the last line and a server will start locally (on http://127.0.0.1:8080/).

3. Run and enjoy. :octocat:

## Data Source

All the `.csv` files are pulled from [DPC](https://github.com/pcm-dpc/COVID-19) which updates them daily.

## Screenshot

![screenshot](/screenshot.png)
