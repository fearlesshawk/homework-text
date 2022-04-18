from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disc(self, disk_file_path, filename):
        ref = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(ref, data=open(filename, 'main.py'))
        response.raise_for_status()
        if response.status_code == 200:
            print('Success')

yd = YaUploader('__')
#pprint(yd.get_files_list())

yd.upload_file_to_disc('Netology/main.py', 'main.py')
