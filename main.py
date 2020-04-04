#         Covid19 - Italy - AI          #
#                 ----                  #
#           by albbus_stack             #

import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import glob, os
import flask

# CSV reading data from dpc
df = pd.read_csv("cov/dati-provincie/dati-province/dpc-covid19-ita-province-latest.csv", sep=',', usecols=['lat','long','denominazione_provincia','totale_casi'])
df1 = pd.read_csv("cov/dati-provincie/dati-province/dpc-covid19-ita-province-latest.csv", sep=',', usecols=['denominazione_provincia','totale_casi'])
dfr = pd.read_csv("cov/dati-regioni/dati-regioni/dpc-covid19-ita-regioni-latest.csv", sep = ',')
dfg = pd.read_csv("cov/dati-andamento-nazionale/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv", sep = ',')

#Dataframe sorting and filtering
dfr = dfr.sort_values(by ='totale_ospedalizzati', ascending = False)
df1 = df1[df1.totale_casi != 0]
df1 = df1[df1.denominazione_provincia != 'In fase di definizione/aggiornamento']
df1 = df1.sort_values(by ='totale_casi', ascending = False)
df = df[df.totale_casi != 0]
df = df[df.lat != 0]
df = df[df.long != 0]

#CSV merging for timed data
path = 'cov/dati-provincie/dati-province'
all_files = glob.glob(os.path.join(path, "*.csv"))
all_df = []
for f in all_files:
    dF = pd.read_csv(f, sep=',')
    dF['file'] = f.split('/')[-1]
    all_df.append(dF)
merged_df = pd.concat(all_df, ignore_index=True)
merged_df = merged_df.sort_values(by ='data')

path = 'cov/dati-andamento-nazionale/dati-andamento-nazionale'
all_files = glob.glob(os.path.join(path, "*.csv"))
all_df = []
for f in all_files:
    dF = pd.read_csv(f, sep=',')
    dF['file'] = f.split('/')[-1]
    all_df.append(dF)
d_df = pd.concat(all_df, ignore_index=True)
d_df = d_df.sort_values(by ='data')

path = 'cov/dati-regioni/dati-regioni'
all_files = glob.glob(os.path.join(path, "*.csv"))
all_df = []
for f in all_files:
    dF = pd.read_csv(f, sep=',')
    dF['file'] = f.split('/')[-1]
    all_df.append(dF)
merged_df2 = pd.concat(all_df, ignore_index=True)
merged_df2 = merged_df2.sort_values(by ='data')

#Chart plotting
fig1 = go.Figure(go.Scatter(x = d_df.data, y = d_df.totale_casi, mode='lines', line_color = 'deepskyblue'))
fig1.update_layout(paper_bgcolor = '#000000',title_text='National positive cases',  xaxis_rangeslider_visible=True,plot_bgcolor = '#222222',titlefont = dict( color = 'white'), font = dict(color = '#767677'), yaxis = dict( autorange = True, fixedrange = False,showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis',  zerolinewidth=1,gridcolor = '#665a73'))

Num = d_df['nuovi_positivi']
Den = d_df['totale_positivi']
Num = Num.to_numpy()
Den = Den.to_numpy()
Res1 = []
for i, j in zip(range(1,len(Num)),range(len(Den))):
    if Den[j] != 0:
        Res1.append(Num[i] / Den[j])

fig9 = go.Figure(go.Scatter(x = d_df.data, y = Res1, mode='lines', line_color = 'deepskyblue'))
fig9.update_layout(paper_bgcolor = '#000000',title_text='Daily national percentual increase',  xaxis_rangeslider_visible=True,plot_bgcolor = '#222222',titlefont = dict( color = 'white'), font = dict(color = '#767677'), yaxis = dict( autorange = True, fixedrange = False,showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis',  zerolinewidth=1,gridcolor = '#665a73'))

fig2 = go.Figure(go.Scatter(x = d_df.data, y =d_df.totale_ospedalizzati, mode='lines', line_color = 'lightgreen'))
fig2.update_layout(paper_bgcolor = '#000000',title_text='National ospedalized',titlefont = dict( color = 'white'),plot_bgcolor = '#222222', xaxis_rangeslider_visible=True, font = dict(color = '#767677'), yaxis = dict( showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis', zerolinewidth=1, gridcolor = '#665a73'))

fig3 = go.Figure(go.Scatter(x = d_df.data, y =d_df.deceduti, mode='lines', line_color = 'red'))
fig3.update_layout(paper_bgcolor = '#000000',title_text='National deaths',titlefont = dict( color = 'white'),plot_bgcolor = '#222222', xaxis_rangeslider_visible=True, font = dict(color = '#767677'), yaxis = dict(showspikes = True, spikemode= 'toaxis',  gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis',  zerolinewidth=1,gridcolor = '#665a73'))

fig4 = go.Figure(go.Scatter(x = d_df.data, y = d_df.nuovi_positivi, mode='lines', line_color = 'deepskyblue'))
fig4.update_layout(paper_bgcolor = '#000000',title_text='New positive cases',titlefont = dict( color = 'white'),plot_bgcolor = '#222222', xaxis_rangeslider_visible=True,font = dict(color = '#767677'), yaxis = dict(showspikes = True, spikemode= 'toaxis',  gridcolor = '#665a73'), xaxis = dict( showspikes = True, spikemode= 'toaxis', zerolinewidth=1,gridcolor = '#665a73'))

fig5 = go.Figure(go.Scatter(x = d_df.data, y =d_df.dimessi_guariti, mode='lines', line_color = 'lightgreen'))
fig5.update_layout(paper_bgcolor = '#000000',title_text='National survived',titlefont = dict( color = 'white'),plot_bgcolor = '#222222', xaxis_rangeslider_visible=True,font = dict(color = '#767677'), yaxis = dict(showspikes = True, spikemode= 'toaxis',  gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis', zerolinewidth=1, gridcolor = '#665a73'))

fig6 = go.Figure(go.Scatter(x = d_df.data, y =d_df.tamponi, mode='lines', line_color = 'red'))
fig6.update_layout(paper_bgcolor = '#000000',title_text='National tampons',titlefont = dict( color = 'white'), plot_bgcolor = '#222222', xaxis_rangeslider_visible=True,font = dict(color = '#767677'), yaxis = dict( showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis', zerolinewidth=1, gridcolor = '#665a73'))

#print('Insert province denomination (i.e. Firenze) :')
inp = "Firenze"
merged_df = merged_df[merged_df.denominazione_provincia == inp]
fig7 = go.Figure(go.Scatter(x = merged_df.data, y =merged_df.totale_casi, mode='lines', line_color = 'orange'))
fig7.update_layout(paper_bgcolor = '#000000',title_text='Provincial cases of '+str(inp), xaxis_rangeslider_visible=True, titlefont = dict( color = 'white'), plot_bgcolor = '#222222',font = dict(color = '#767677'), yaxis = dict(showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis',zerolinewidth=1, gridcolor = '#665a73'))

#print('Insert a region denomination (i.e. Toscana) :')
inp = "Toscana"
merged_df2 = merged_df2[merged_df2.denominazione_regione == inp]
Num = merged_df2['nuovi_positivi']
Den = merged_df2['totale_positivi']
Num = Num.to_numpy()
Den = Den.to_numpy()
Res = []
for i, j in zip(range(1,len(Num)),range(len(Den))):
    if Den[j] != 0:
        Res.append(Num[i] / Den[j])

fig8 = go.Figure(go.Scatter(x = merged_df2.data, y = Res, mode='lines', line_color = 'red'))
fig8.update_layout(paper_bgcolor = '#000000',title_text='Daily percentual increase in '+str(inp),titlefont = dict( color = 'white'), plot_bgcolor = '#222222', xaxis_rangeslider_visible=True,font = dict(color = '#767677'), yaxis = dict( showspikes = True, spikemode= 'toaxis', gridcolor = '#665a73'), xaxis = dict(showspikes = True, spikemode= 'toaxis', zerolinewidth=1, gridcolor = '#665a73'))

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
    dragmode ='pan',
    paper_bgcolor = '#000000',
    margin ={"r":0,"t":0,"l":0, "b":0 },
    title = go.layout.Title(
        font = dict(
            size = 20,
            color = '#DEF2F2'
        ),
        x = 0.5,
        y= 0.985,
        text = 'Covid-19 cases in Italy, Source:<a href="https://github.com/pcm-dpc/COVID-19/tree/master/dati-province">DPC</a>'),
    geo = go.layout.Geo(
        resolution =50 ,
        scope = 'world',
        showframe = False,
        showocean = True,
        oceancolor = '#000f1a',
        showrivers = True,
        rivercolor = '#000f1a',
        lakecolor = '#000f1a',
        showlakes = True,
        showcoastlines = True,
        landcolor = "#2a2a28",
        coastlinecolor = "#665a73",
        projection_type = 'mercator',
        lonaxis_range= [ 5.0, 20.0 ],
        lataxis_range= [ 36.0, 48.0 ],
        domain = dict(x = [ 0.12, 1 ], y = [ 0, 0.949 ])
    ),
)

#Table plotting
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
                line_color='#665a73',
                fill_color='#222222',
                align='center'),
    cells=dict(values=[df1['denominazione_provincia'], df1['totale_casi']],
               font = dict(
                   color = '#767677'
               ),
               line_color='#665a73',
               height=21.1,
               fill_color='#222222',
               align='center')),
)

fig.add_trace(go.Table(
    domain = dict(
            x = (0.01,0.32),
            y = (0.01,0.14),
    ),
    header=dict(values=list(['Total', 'Survived', 'Deaths']),
                font = dict(
                    color = 'white',
                    size = 17,
                ),
                line_color='#665a73',
                fill_color='#222222',
                align='center'),
    cells=dict(values=[dfg['totale_casi'], dfg['dimessi_guariti'],dfg['deceduti']],
               line_color='#665a73',
               fill_color='#222222',
            height = 30,
               font=dict(
                   color='#767677',
                   size=17,
               ),
               align='center'))

)

fig.add_trace(go.Table(
    domain = dict(
            x = (0.01,0.32),
            y = (0.12,0.95),
    ),
    header=dict(values=list(['Area','Ospedalized','Survived','Deaths','New']),
                font = dict(
                    color = 'white',
                    size = 16,
                ),
                line_color='#665a73',
                fill_color='#222222',
                align='center'),
    cells=dict(values=[dfr['denominazione_regione'],dfr['totale_ospedalizzati'], dfr['dimessi_guariti'], dfr['deceduti'], dfr['nuovi_positivi']],
               font = dict(
                   color = '#767677'
               ),
               line_color='#665a73',
               fill_color='#222222',
               height = 23.7,
               align='center'))
)

#Dash rendering
external_css = ['https://codepen.io/albbus-stack/pen/zYGyGKL.css']
app = flask.Flask(__name__)
server = dash.Dash(__name__,server = app, external_stylesheets=external_css)
server.scripts.config.serve_locally = False
server.layout = html.Div([
    dcc.Graph(figure=fig, id = 'map', style = {'margin-top': 0,'margin-left': 0, 'height' : '100vh'}, animate=True),
    dcc.Graph(figure = fig1, id='graph1', style = {'height': '60vh'}),
    dcc.Graph(figure = fig9, id='graph9', style = {'height': '60vh'}),
    dcc.Graph(figure = fig4, id='graph4', style = {'height': '60vh'}),
    dcc.Graph(figure = fig2, id='graph2', style = {'height': '60vh'}),
    dcc.Graph(figure = fig3, id='graph3', style = {'height': '60vh'}),
    dcc.Graph(figure = fig5, id='graph5', style = {'height': '60vh'}),
    dcc.Graph(figure = fig6, id='graph6', style = {'height': '60vh'}),
    dcc.Graph(figure = fig7, id='graph7', style = {'height': '60vh'}),
    dcc.Graph(figure = fig8, id='graph8', style = {'height': '60vh'}),
])
server.css.append_css({'external_url': 'https://codepen.io/albbus-stack/pen/zYGyGKL.css'})
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)



