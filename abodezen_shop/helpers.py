import requests
import requests_cache
import json



#setup our api cache location(this is going to make a temporary datavase storage for our api calls)
requests_cache.install_cache('image_cache', backend='sqlite')

def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
        "X-RapidAPI-Key": "55def16c37mshf2200fdea0b6328p1d9d57jsn0004b8652316",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url 