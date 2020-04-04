### covid19-italy
Map and charts data visualization of __Covid19__ cases in Italy.

Now available in web version hosted on Google Cloud Platform : (https://cov19-it.appspot.com/)

Built in Python 3.8, using [pandas](https://github.com/pandas-dev/pandas) for data manipulation and [plotly](https://github.com/plotly/plotly.py) for interactive visualization, renders in browser using [dash](https://github.com/plotly/dash) to output some HTML and React; CSS is added to dash externally.

Data is pulled from [DPC](https://github.com/pcm-dpc/COVID-19), which is doing a great job at data storing!

The [script.py](script.py) works like this:
- You have to edit lines 92 and 100 in main.py, first inserting the name of a province then one of a region to plot the last two graphs (the defaults are "Firenze" and "Toscana").
- Starts a local server and there you go!

Also included the [.idea](.idea) folder for direct project configuration in PyCharm, before using make sure that you have installed all the necessary packages in your compiler for ```script.py```  :  ```import pandas, plotly, dash```

#### Attached images

##### Not updated since there is an updated web version 

![img1](/img1.png)
![img2](/img2.png)
![img3](/img3.png)
![img4](/img4.png)
![img5](/img5.png)
![img6](/img6.png)
