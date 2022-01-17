import requests
import os
urls = ['https://www.google.com/', 'https://yandex.ru/', 'https://www.bing.com/']

directory = 'html_download_files'
if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
for url in urls:
    response = requests.get(url).text
    with open(directory + f'/{i}.html', 'w') as f:
        f.writelines(response)
    i += 1