
import requests
import json
from os import walk







class YaUploader:
    def __init__(self, token: str):
        self.token = token





    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = next(walk("C:\\kot\\кот\\"), (None, None, []))[2]
        for file_name in file_list:
            full_path = file_path + file_name

            with open(full_path, mode="rb") as file:
              open_file = file.read()

            headers = {
                "Content-Type": "application/json",
                "Authorization": self.token
            }

            params = {'path': file_name}

            path = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
            new_link = requests.get(path, headers=headers, params=params).json()["href"]

            put_file = requests.put(new_link, data=open_file)
            print(put_file)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\kot\\кот\\"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


