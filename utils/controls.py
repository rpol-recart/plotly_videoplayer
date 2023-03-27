import dash_html_components as html
from dash import dcc
from player_utils.file_utils import get_video_files
import dash_bootstrap_components as dbc


def create_controls(video_folder:str='assets/video'):
    # Создание выпадающего списка для выбора видеофайла
    video_options = get_video_files(video_folder)
    video_dropdown = dcc.Dropdown(
        id='video-dropdown',
        options=video_options,
        value=video_options[0]['value']
    )

    # Создание кнопок для управления видеофайлами
    prev_button = html.Button('Предыдущее видео', id='prev-video-button')
    next_button = html.Button('Следующее видео', id='next-video-button')

    # Создание элемента для отображения текущей метки и списка меток
    label_list = dcc.Dropdown(
        id='label-list',
        options=[],
        value=None
    )

    # Создание кнопок для управления метками
    new_label_button = html.Button('Новая метка', id='new-label-button')
    edit_label_button = html.Button('Изменить метку', id='edit-label-button')
    delete_label_button = html.Button('Удалить метку', id='delete-label-button')

    # Создание элементов для выбора времени начала и конца метки и текста метки
    start_time_button = dbc.Button('Установить', id='start-time-button', color='primary', className='mr-2')
    end_time_button = dbc.Button('Установить', id='end-time-button', color='primary', className='mr-2')

    end_time_input = dcc.Input(
        id='end-time-input',
        type='text',
        value='00:00:00.000'
    )
    label_dropdown = dcc.Dropdown(
            id='label-dropdown',
            options=[
                {'label': 'Option 1', 'value': 'option-1'},
                {'label': 'Option 2', 'value': 'option-2'},
                {'label': 'Option 3', 'value': 'option-3'},
            ],
            value='',
            placeholder='Категория видео'
        )

    # Создание кнопки сохранения метки
    save_button = html.Button('Сохранить', id='save-button')

    # Создание элемента для отображения ошибок
    error_output = html.Div(id='error-output')

    # Собираем элементы управления в один список
    controls = [html.Div('Выбор видео', style={'font-weight': 'bold'}),
                html.Div(video_dropdown),
                html.Div(prev_button),
                html.Div(next_button),
                html.Br(),
                html.Div('Выбор метки', style={'font-weight': 'bold'}),
                html.Div(label_list),
                html.Br(),
                html.Div(new_label_button),
                html.Div(edit_label_button),
                html.Div(delete_label_button),
                html.Div('Редактируется ', id='time-text4', style={'font-weight': 'bold'}),
                html.Br(),
                
                html.Div('Время начала ролика', id='time_text1', style={'font-weight': 'bold'}),
                html.Div(start_time_button),
                html.Br(),
                html.Div('Время конца ролика', id='time_text2',style={'font-weight': 'bold'}),
                html.Div(end_time_button),
                html.Br(),
                html.Div('Текст метки',id='time_text3', style={'font-weight': 'bold'}),
                html.Div(label_dropdown),
                html.Br(),
                html.Div(save_button),
                html.Br(),
                error_output]

    return controls
