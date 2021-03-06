import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net:443'
        params = {'path': 'Requests/test.txt', 'overwrite': 'true'}
        headers = {"Authorization": token}
        url_file = requests.get(url+'/v1/disk/resources/upload', headers=headers, params=params).json()['href']
        response = requests.put(url_file, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return f'Файл загружен на яндекс диск'


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ''  #Токен для яндекс диск API
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

    print(result)