import dash
from dash import dcc, html, Input, Output
import requests

# Fetching weather data function
def fetch_weather_data(latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4a21da3e3b3e649431ffc7ff8c1c277c"
    response = requests.get(url)
    return response.json()

# Default latitude and longitude
DEFAULT_LATITUDE = 44.34
DEFAULT_LONGITUDE = 10.99

# Fetching initial weather data
initial_data = fetch_weather_data(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)

# Creating the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Weather Dashboard"),
    html.Div([
        html.Label("Latitude:"),
        dcc.Input(id='latitude', type='number', value=DEFAULT_LATITUDE, step=0.01),
        html.Label("Longitude:"),
        dcc.Input(id='longitude', type='number', value=DEFAULT_LONGITUDE, step=0.01),
        html.Button(id='submit-button', n_clicks=0, children='Submit'),
    ]),
    html.Div(id='weather-info')
])

# Callback to update weather info
@app.callback(
    Output('weather-info', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('latitude', 'value'),
     dash.dependencies.State('longitude', 'value')]
)
def update_weather_info(n_clicks, latitude, longitude):
    weather_data = fetch_weather_data(latitude, longitude)
    temperature = round(weather_data['main']['temp'] - 273.15, 2)  
    feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']
    
    return html.Div([
        html.Div([
            html.H2("Location"),
            html.P(weather_data['name'])
        ], className='box'),
        html.Div([
            html.H2("Temperature"),
            html.P(f"{temperature}°C")
        ], className='box'),
        html.Div([
            html.H2("Feels Like"),
            html.P(f"{feels_like}°C")
        ], className='box'),
        html.Div([
            html.H2("Description"),
            html.P(description)
        ], className='box'),
        html.Div([
            html.H2("Wind Speed"),
            html.P(f"{wind_speed} m/s")
        ], className='box'),
        html.Div([
            html.H2("Humidity"),
            html.P(f"{humidity}%")
        ], className='box')
    ], className='container')


if __name__ == '__main__':
    app.run_server(debug=True)
