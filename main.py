import requests

url = 'https://openx.com/sellers.json'
r = requests.get(url, allow_redirects=True)
open('sellers.json', 'wb').write(r.content)
