import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
from scipy import stats
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plt.style.use('ggplot')
plotly.tools.set_credentials_file(username='jasonwangnyc', api_key='Hj8g8HlNlJaIr2s78vig')

#import data
youtube = pd.read_csv('youtuber_top5000.csv')

#set subcribers as index and sort by it
youtube = youtube.sort_values('Subscribe_Rank').set_index('Subscribe_Rank')

#order the columns
youtube = youtube[['Username','Country','Type','Created_Date','Subscribers','Views','Views_Rank','Uploads','Estimated_Yearly_Earning']]

#changing subscribers and Views to integer
youtube['Subscribers'] = youtube['Subscribers'].apply(lambda x: re.sub("\D", "", x)).astype(int)
youtube['Views'] = youtube['Views'].apply(lambda x: re.sub("\D", "", x)).astype(int)
youtube['Uploads'] = youtube['Uploads'].apply(lambda x: re.sub("\D", "", x)).astype(int)

#create a new df for count of youtube channel of each country
x = youtube['Country'].value_counts().dropna()
x = x.reset_index(level=0, inplace=False)
x = x[0:10]
x.loc[10] = ["others",747]


#######graphing########

# create pie chart for country
labels = x['index']
values = x['Country']

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart'

#create df for Types
y = youtube['Type'].value_counts().dropna()
y = y.reset_index(level=0, inplace=False)

#create pie chart for Types 
labels2 = y['index']
values2 = y['Type']

type1 = go.Pie(labels=labels2, values=values2)

py.iplot([type1], filename='basic_pie_chart')

#exclude nan from veiws and subscribers
subs = np.array(youtube['Subscribers'])
views = np.array(youtube['Views'])
ups = np.array(youtube['Uploads'])
a=np.isnan(subs)==False
b=np.isnan(views)==False
d=np.isnan(ups)==False
c=np.logical_and(a,b)
e=np.logical_and(a,d)
subs2 = subs[c]
views2 = views[c]
subs3 = subs[e]
ups2 = views[e]

#create scatter plot for views and subscribers with regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(subs2, views2)
line = slope*youtube['Subscribers'] + intercept
youtube = youtube[youtube!=0]
trace1 = go.Scatter(
    x = youtube['Subscribers'],
    y = youtube['Views'],
    mode = 'markers',
    name = 'Data')
trace2 = go.Scatter(
    x = youtube['Subscribers'],
    y = line,
    mode = 'lines',
    name = 'Regression Line'
)
layout = go.Layout(
    xaxis=dict(
        title='Subscribers',
        titlefont=dict(
            size=18
        )
    ),
    yaxis=dict(
        title='Views',
        titlefont=dict(
            size=18
        )
    )
)
data = [trace1,trace2]
data1 = go.Figure(data=data, layout=layout)
py.iplot(data1, filename='basic-scatter')

#correlation of views and subscribers
youtube[['Views','Subscribers']].corr()

#create scatter plot for Uploads and subscribers
youtube = youtube[youtube!=0]
trace3 = go.Scatter(
    x = youtube['Subscribers'],
    y = youtube['Uploads'],
    mode = 'markers',
    name = 'Data')

layout1 = go.Layout(
    xaxis=dict(
        title='Subscribers',
        titlefont=dict(
            size=18
        )
    ),
    yaxis=dict(
        title='Uploads',
        titlefont=dict(
            size=18
        )
    )
)
scatter_su = [trace3]
scatter_su1 = go.Figure(data=scatter_su, layout=layout1)
py.iplot(scatter_su1, filename='basic-scatter')



#create scatter plot for views and Uploads
youtube = youtube[youtube!=0]
trace4 = go.Scatter(
    x = youtube['Views'],
    y = youtube['Uploads'],
    mode = 'markers',
    name = 'Data')

layout2 = go.Layout(
    xaxis=dict(
        title='Views',
        titlefont=dict(
            size=18
        )
    ),
    yaxis=dict(
        title='Uploads',
        titlefont=dict(
            size=18
        )
    )
)
scatter_vu = [trace4]
scatter_vu1 = go.Figure(data=scatter_vu, layout=layout2)
py.iplot(scatter_vu1, filename='basic-scatter')

#create a country-views bar chart
bar_cv = [go.Bar(
            x= youtube['Country'],
            y= youtube['Views']
    )]
layout3 = go.Layout(
    yaxis=dict(
        title='Views',
        titlefont=dict(
            size=18
        )
    )
)
py.iplot(bar_cv, layout=layout3,filename='basic-bar')


#create a country-subscribers bar chart
bar_cs = [go.Bar(
            x= youtube['Country'],
            y= youtube['Subscribers']
    )]
layout4 = go.Layout(
    yaxis=dict(
        title='Subscribers',
        titlefont=dict(
            size=18
        )
    )
)
py.iplot(bar_cs, layout=layout4,filename='basic-bar')

#create a Type-subscribers bar chart
bar_ts = [go.Bar(
            x= youtube['Type'],
            y= youtube['Subscribers']
    )]
layout5 = go.Layout(
    yaxis=dict(
        title='Subscribers',
        titlefont=dict(
            size=18
        )
    )
)
py.iplot(bar_ts, layout=layout5,filename='basic-bar')


#create a Type-Views bar chart
bar_tv = [go.Bar(
            x= youtube['Type'],
            y= youtube['Views']
    )]
layout6 = go.Layout(
    yaxis=dict(
        title='Views',
        titlefont=dict(
            size=18
        )
    )
)
py.iplot(bar_tv, layout=layout6,filename='basic-bar')

