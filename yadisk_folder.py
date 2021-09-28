import requests


class YaFolder:
    def __init__(self, token : str):
        self.token = token

    def get_headers(self):
        return {"Authorization": f'OAuth {self.token}'}

    def create_yadisk_folder(self, folder_name : str):
        yandex_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": '/' + folder_name}
        response = requests.put(yandex_folder_url, params=params, headers=headers)
        return response