#dataset source
#https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),# initial value
        marks={str(year): str(year) for year in df['year'].unique()}
    )
])


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),#.Output('id', 'figure')
    [dash.dependencies.Input('year-slider', 'value')]) #Input('id','value')
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year] #The dataset filtered by 'year' label in 'df' will be saved in 'filtered_df' list.
    traces = []
    for i in filtered_df.continent.unique(): # polling each continent members
        df_by_continent = filtered_df[filtered_df['continent'] == i] # The dataset filtered by 'continent' label
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'], #國內人均生產總值
            y=df_by_continent['lifeExp'], #平均壽命
            text=df_by_continent['country'], #國家名
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i # 洲名

        ))

    return { # Output
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]}, # y軸名稱 & 邊界
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)