#         Covid19 - Italy - AI          #
#                 ----                  #
#           by albbus_stack             #

import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import glob, os
from dash.exceptions import PreventUpdate
import plotly.express as px

# CSV reading data from dpc
df = pd.read_csv("COVID-19/dati-province/dpc-covid19-ita-province-latest.csv", sep=',', usecols=['lat','long','denominazione_provincia','totale_casi'])
df1 = pd.read_csv("COVID-19/dati-province/dpc-covid19-ita-province-latest.csv", sep=',', usecols=['denominazione_provincia','totale_casi'])
dfr = pd.read_csv("COVID-19/dati-regioni/dpc-covid19-ita-regioni-latest.csv", sep = ',')
dfg = pd.read_csv("COVID-19/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv", sep = ',')

#Dataframe sorting and filtering
dfr = dfr.sort_values(by ='totale_ospedalizzati', ascending = False)
df1 = df1[df1.totale_casi != 0]
df1 = df1[df1.denominazione_provincia != 'In fase di definizione/aggiornamento']
df1 = df1.sort_values(by ='totale_casi', ascending = False)
df = df[df.totale_casi != 0]

#CSV merging for timed data
path = 'COVID-19/dati-province'
all_files = glob.glob(os.path.join(path, "*.csv"))
all_df = []
for f in all_files:
    dF = pd.read_csv(f, sep=',')
    dF['file'] = f.split('/')[-1]
    all_df.append(dF)
merged_df = pd.concat(all_df, ignore_index=True)
merged_df = merged_df.sort_values(by ='data')

path = 'COVID-19/dati-andamento-nazionale'
all_files = glob.glob(os.path.join(path, "*.csv"))
all_df = []
for f in all_files:
    dF = pd.read_csv(f, sep=',')
    dF['file'] = f.split('/')[-1]
    all_df.append(dF)
d_df = pd.concat(all_df, ignore_index=True)
d_df = d_df.sort_values(by ='data')

#Chart plotting
fig1 = go.Figure(go.Scatter(x = d_df.data, y = d_df.totale_casi, mode='lines', line_color = 'deepskyblue'))
fig1.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='National positive cases', xaxis_rangeslider_visible=True)

fig2 = go.Figure(go.Scatter(x = d_df.data, y =d_df.totale_ospedalizzati, mode='lines', line_color = 'lightgreen'))
fig2.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='National ospedalized', xaxis_rangeslider_visible=True)

fig3 = go.Figure(go.Scatter(x = d_df.data, y =d_df.deceduti, mode='lines', line_color = 'red'))
fig3.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='National deaths', xaxis_rangeslider_visible=True)

fig4 = go.Figure(go.Scatter(x = d_df.data, y = d_df.nuovi_attualmente_positivi, mode='lines', line_color = 'deepskyblue'))
fig4.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='New positive cases', xaxis_rangeslider_visible=True)

fig5 = go.Figure(go.Scatter(x = d_df.data, y =d_df.dimessi_guariti, mode='lines', line_color = 'lightgreen'))
fig5.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='National survived', xaxis_rangeslider_visible=True)

fig6 = go.Figure(go.Scatter(x = d_df.data, y =d_df.tamponi, mode='lines', line_color = 'red'))
fig6.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='National tampons', xaxis_rangeslider_visible=True)

print('Insert province denomination (i.e. Firenze) :')
inp = input()
merged_df = merged_df[merged_df.denominazione_provincia == inp]
fig7 = go.Figure(go.Scatter(x = d_df.data, y =merged_df.totale_casi, mode='lines', line_color = 'orange'))
fig7.update_layout(paper_bgcolor = 'rgb(232, 232, 232)',title_text='Provincial cases of '+inp, xaxis_rangeslider_visible=True)

#Map plotting
fig = go.Figure()
color = 'rgb(219, 17, 13)'
fig.add_trace(go.Scattergeo(
        hoverinfo = "text",
        lon = df['long'],
        lat = df['lat'],
        text = df['denominazione_provincia'],
        mode = 'markers',
        marker = dict(
            size = df['totale_casi']/36,
            color = color,
            line_width = 0
            )))
fig['data'][0].update(mode='markers', textposition='bottom center',
                      text=df['denominazione_provincia']+' : '+df['totale_casi'].map('{:.0f}'.format).astype(str))
fig.update_layout(
    paper_bgcolor = 'rgb(232, 232, 232)',
    margin ={"r":0,"t":0,"l":0, "b":0 },
    title = go.layout.Title(
        font = dict(
            size = 20,
        ),
        x = 0.5,
        y= 0.98,
        text = 'Covid-19 cases in Italy, Source:<a href="https://github.com/pcm-dpc/COVID-19/tree/master/dati-province">DPC</a>'),
    geo = go.layout.Geo(
        resolution =50 ,
       scope = 'world',
      showframe = False,
       showocean = True,
        oceancolor = 'rgb(2, 10, 69)',
        showrivers = True,
        rivercolor = 'rgb(3, 13, 84)',
        lakecolor = 'rgb(3, 13, 84)',
        showlakes = True,
        showcoastlines = True,
        landcolor = "rgb(128, 127, 133)",
        coastlinecolor = "white",
        projection_type = 'mercator',
        lonaxis_range= [ 5.0, 20.0 ],
        lataxis_range= [ 36.0, 48.0 ],
        domain = dict(x = [ 0.12, 1 ], y = [ 0, 0.949 ])
    ),
)


fig.add_trace(
    go.Table(
    domain = dict(
            x = (0.8,0.992),
            y = (0,0.95),
    ),
    header=dict(values=list(['Province','Cases']),
                font = dict(
                    color = 'white',
                    size = 17,
                ),
                fill_color='rgb(3, 13, 84)',
                align='center'),
    cells=dict(values=[df1['denominazione_provincia'], df1['totale_casi']],
               height=21.1,
               fill_color='rgb(212, 212, 212)',
               align='center')),
)

fig.add_trace(go.Table(
    domain = dict(
            x = (0.01,0.32),
            y = (0.01,0.23),
    ),
    header=dict(values=list(['Total', 'Survived', 'Deaths']),
                font = dict(
                    color = 'white',
                    size = 17,
                ),
                fill_color='rgb(3, 13, 84)',
                align='center'),
    cells=dict(values=[dfg['totale_casi'], dfg['dimessi_guariti'],dfg['deceduti']],
               fill_color='rgb(212, 212, 212)',
            height = 30,
               font=dict(
                   color='black',
                   size=17,
               ),
               align='center'))

)

fig.add_trace(go.Table(
    domain = dict(
            x = (0.01,0.32),
            y = (0.25,0.95),
    ),
    header=dict(values=list(['Area','Ospedalized','Survived','Deaths']),
                font = dict(
                    color = 'white',
                    size = 16,
                ),
                fill_color='rgb(3, 13, 84)',
                align='center'),
    cells=dict(values=[dfr['denominazione_regione'],dfr['totale_ospedalizzati'], dfr['dimessi_guariti'], dfr['deceduti']],
               fill_color='rgb(212, 212, 212)',
               height = 23.7,
               align='center'))
)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig, id = 'map', style = {'margin-top': 0,'height' : '100vh'}, animate=True),
    dcc.Graph(figure = fig1, id='graph1', style = {'height': '60vh'}),
    dcc.Graph(figure = fig2, id='graph2', style = {'height': '60vh'}),
    dcc.Graph(figure = fig3, id='graph3', style = {'height': '60vh'}),
    dcc.Graph(figure = fig4, id='graph4', style = {'height': '60vh'}),
    dcc.Graph(figure = fig5, id='graph5', style = {'height': '60vh'}),
    dcc.Graph(figure = fig6, id='graph6', style = {'height': '60vh'}),
    dcc.Graph(figure = fig7, id='graph7', style = {'height': '60vh'}),
])

app.run_server(debug=False, use_reloader=False)
