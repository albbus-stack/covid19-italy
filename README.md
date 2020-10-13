# covid19-italy
![GPLv3 License](https://img.shields.io/badge/%20License-GPL%20v3-yellow?style=flat-square)
![Plotly](https://img.shields.io/badge/%20-Plotly-blue?style=flat-square)

Map and charts data visualization of __Covid19__ cases in __Italy__, kindly hosted by [Heroku](https://heroku.com) on https://cov-19-it.herokuapp.com/.

Built in Python 3.8, using [pandas](https://github.com/pandas-dev/pandas) for data manipulation and [plotly](https://github.com/plotly/plotly.py) for interactive visualization, renders in browser using [dash](https://github.com/plotly/dash) to output some HTML and React; CSS is added to dash externally.

Data is pulled from [DPC](https://github.com/pcm-dpc/COVID-19), which is doing a great job at data storing!

### Compile it yourself

1. Install all the [requirements](requirements.txt).

2. Change the province you want to visualize in line 119 and 130 inside [main.py](main.py).

3. Run the file with the last line changed and a server will start locally (on http://127.0.0.1:8080/).

### Screenshot

![screenshot](/screenshot.png)
