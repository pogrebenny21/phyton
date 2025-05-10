from LxmlSoup import lxmisetup
import requests
import os

if not os.path.exists("music"):
    os.makedirs("music")

search_url = "https://www.myinstants.com/media/sounds/ia-rodilsia_hGybxEB.mp3"
html = requests.get(search_url).text

soup = lxmlSoup(html)

buttons = soup.find_all("button", class_="small-button")
print(buttons)

for button in buttons:
    url=button.get("onclick").split("")[1]
    print(original_url+url)
    try:
        respone = requests.get(original_url+url)