import requests
from bs4 import BeautifulSoup
from io import BytesIO
import os
from PIL import Image


def seach_url(query):
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    img_tag = soup.find("img", {"class": "yWs4tf"})

    if img_tag is not None:

        img_link = img_tag.get("src")

        return img_link

    else:
        print("No image found on the page.")

def save_image(url):
    response = requests.get(url)
    responses = BytesIO(response.content)

    img = Image.open(responses)

    size = (img.height * 6, img.width * 6)
    img = img.resize(size)

    save_path = f'D:/програмування/Python/API/task_4/downloads/{query}.jpg'

    img.save(save_path)
    os.startfile(save_path)

query = input("Your input")

seach_url_fun = seach_url(query)
save_image(seach_url_fun)
