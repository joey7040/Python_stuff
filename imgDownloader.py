import random
import requests

get = str(input("enter url of the img you want to download : "))

def download_image(url):
    print("downloading ...")
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpeg"
    r = requests.get(url, stream = True)
    with open (full_name, 'wb') as f:
        f.write(r.content)
    return "download completed and saved as :" + full_name

print(download_image(get))