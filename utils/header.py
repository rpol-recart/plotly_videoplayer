import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
# Создаем верхнюю панель с логотипом и названием приложения

def generate_header():
    header = html.Div(
        className='header',
        children=[
            html.Div(
                className='logo-and-title',
                children=[
                    html.Img(
                        src='https://mzbk-rb.ru/wp-content/uploads/2018/02/logo-1440x720-2.jpg',
                        className='logo',
                    ),
                    html.H1(
                        'Video Labeling',
                        className='title',
                    ),
                ],
            ),

            html.Div(
                className='menu',
                children=[dbc.Container(
                                        [
                                            dbc.Nav(
                                                    [
                                                        dbc.NavLink("Разметка событий", href="/page-1", id="page-1-link"),
                                                        dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
                                                        dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
                                                    ],
                                                    vertical=True,
                                                    pills=True,
                                                ),
                                        ],
                                        
                                        
                                    )
                    
                            ],
                    ),
        ],
    )
    return header