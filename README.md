### covid19-italy
Map and charts data visualization of __Covid19__ cases in Italy. 

Built in Python 3.8, using [pandas](https://github.com/pandas-dev/pandas) for data manipulation and [plotly](https://github.com/plotly/plotly.py) for interactive visualization, renders in browser using [dash](https://github.com/plotly/dash) to output some HTML and React; CSS is added to dash externally.

Data is pulled from [DPC](https://github.com/pcm-dpc/COVID-19), which is doing a great job at data storing!

The [script.py](script.py) works like this:
- Requires an input from terminal of a province that you want to plot the graph of (remember to write it with the capital letter).
- Starts a local server if the province was correct and there you go!

Also included the [.idea](.idea) folder for direct project configuration in PyCharm, before using make sure that you have installed all the necessary packages in your compiler for ```script.py```  :  ```import pandas, plotly, dash```

#### Attached images

![img1](/readme_img/img1.png)
![img2](/readme_img/img2.png)
![img3](/readme_img/img3.png)
![img4](/readme_img/img4.png)
![img5](/readme_img/img5.png)
