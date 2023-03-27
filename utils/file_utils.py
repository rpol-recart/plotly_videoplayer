import os


def get_video_files(folder_path):
    """
    Получает список видео файлов в заданной директории
    и возвращает список значений для выпадающего списка.
    """
    video_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.mov', '.avi'))]
    return [{'label': f, 'value': os.path.join(folder_path, f)} for f in video_files]