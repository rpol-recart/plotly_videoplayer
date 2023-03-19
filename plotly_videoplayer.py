import os
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from dash_player import DashPlayer
import dash_core_components as dcc
from datetime import datetime


# Define the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])


# Define the layout
app.layout = dbc.Container([
    html.H1('Video Player'),
    dbc.Row([
        dbc.Col([
            html.Label('Select Date Range'),
            html.Br(),
            dcc.DatePickerRange(
                        id='date-range-picker',
                        min_date_allowed=datetime(2022, 1, 1),
                        max_date_allowed=datetime.now(),
                        start_date=datetime.now(),
                        end_date=datetime.now(),
                        display_format='MMM Do, YYYY',
                        style={'margin-bottom': '10px'}
                    ),
            html.Hr(),
            html.Label('Select Camera'),
            html.Br(),
            dbc.RadioItems(
                id='camera-selection',
                options=[
                    {'label': 'Camera 1', 'value': 'camera1'},
                    {'label': 'Camera 2', 'value': 'camera2'}
                ],
                value='camera1'
            ),
            html.Hr(),
            html.Br(),
            dcc.Dropdown(
                id='video-selection',
                options=[{'label': f, 'value': f} for f in os.listdir('assets/video')],
                value=os.listdir('assets/video')[0]
            ),
            html.Hr(),
            html.Br(),
            dbc.Button('Previous', id='prev-video-button', color='primary', className='mr-1',style={'margin-right': '10px', 'margin-left': '10px'}),
            dbc.Button('Next', id='next-video-button', color='primary', className='mr-1'),
        ], md=3),
        dbc.Col([
            DashPlayer(
                id='video-player',
                url='/assets/video/'+os.listdir('video')[0],
                controls=True,
                width=800,
                height=600
            )
        ], md=9)
    ])
], fluid=True)


# Define the callbacks
@app.callback(
    Output('video-selection', 'value'),
    Input('prev-video-button', 'n_clicks'),
    Input('next-video-button', 'n_clicks'),
    State('video-selection', 'value'),
    State('camera-selection', 'value')
)
def update_video_selection(prev_clicks, next_clicks, current_file, camera):
    if prev_clicks is not None:
        # Get the list of video files for the selected camera
        video_files = [f for f in os.listdir('assets/video') if f.startswith(camera)]
        # Get the index of the current file in the list
        current_index = video_files.index(current_file)

        # Get the index of the previous file in the list
        previous_index = current_index - 1 if current_index > 0 else len(video_files) - 1
        # Get the previous file name
        previous_file = video_files[previous_index]
        return previous_file
    elif next_clicks is not None:
        # Get the list of video files for the selected camera
        video_files = [f for f in os.listdir('assets/video') if f.startswith(camera)]
        print(camera)
        print(video_files)
        # Get the index of the current file in the list
        current_index = video_files.index(current_file)
        print(current_index,current_file)
        # Get the index of the next file in the list
        next_index = (current_index + 1) % len(video_files)
        # Get the next file name
        next_file = video_files[next_index]
        return next_file
    else:
        return current_file


# Define the callback for updating the video player
@app.callback(
    Output('video-player', 'url'),
    Input('video-selection', 'value')
)
def update_video_player(url):
    return '/assets/video/' + url


if __name__ == '__main__':
    app.run_server(debug=True)
