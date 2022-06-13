import requests
from pprint import pprint
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {'Authorization': self.token, 'Content-Type':
            'application/json'}
        params = {'path': os.path.basename(file_path), 'overwrite': 'True'}
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        resp = requests.get(url, headers=headers, params=params)
        with open('1.txt', 'rb') as file:
            rresp = requests.put(resp.json()['href'], files={'file': file})
            if rresp.status_code == 201:
                print('Загрузка файла прошла успешно')
            else:
                print('Возможна ошибка, проверьте данные')

if __name__ == '__main__':
    path_to_file = 'r' + str(input('Введите путь до файла, который хотите загрузить'))
    token = 'OAuth ' + str(input('Введите токен'))
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

