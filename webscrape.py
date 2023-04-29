import requests
from bs4 import BeautifulSoup
import time
import json 

def main():

    name_arr = []
    img_arr = []
    price_arr = []

        
    api_url = 'https://steamcommunity.com/market/search/render/'

    params = {
        "query": "",
        "start": 0,
        "count": 10,
        "search_descriptions": "0",
        "sort_column": "popular",
        "sort_dir": "desc",
        "appid": "730",
        "category_730_ItemSet[]": "any",
        "category_730_ProPlayer[]": "any",
        "category_730_StickerCapsule[]": "any",
        "category_730_TournamentTeam[]": "any",
        "category_730_Weapon[]": "any",
        "category_730_Exterior[]": "tag_WearCategory2",
        "category_730_Quality[]": ["tag_normal", "tag_unusual"],
    }


    with requests.session() as s: #used to get identical outputs when not using .session() - THANKS TO https://stackoverflow.com/users/10035985/andrej-kesely
        s.get('https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=tag_WearCategory2&category_730_Quality%5B%5D=tag_normal&category_730_Quality%5B%5D=tag_unusual&appid=730')

        for params['start'] in range(0, 1680, 10):  # <-- 1680 is the amount of items that exist with the given params

            data = s.get(api_url, params=params)

            #prevents running into multiple 429s (Too many requests)
            if data.status_code > 229 or data.status_code < 199:
                time.sleep(60)
                print("one page went missing")
                break
            #prettier console output
            print("----------------------------------------------------------------------------------------------------------------" + str(data.status_code))
            data = data.json()
            soup = BeautifulSoup(data['results_html'], 'html.parser')

            

            for item in soup.select('.market_listing_row_link'):

                name = item.select_one('.market_listing_item_name').text.replace("(Field-Tested)", "").replace("\u2605", "").replace("\u2122", "").strip().strip() #item name only, no unicode stars or StatTrack symbol
                name_arr.append(name)

                icon_a = item.select_one('.market_listing_item_img')
                img = icon_a['src'] #link to the image
                img = img.replace("62fx62f", "620fx620f").strip() # increase image size
                img_arr.append(img)
                img_short = img[250:] # just for console log

                price = item.select_one('[data-price]').text.replace("USD", "").replace(",", "").strip() #remove currency, easier convert to double later
                price_arr.append(price)

                print('{:<50} {:<5} {}'.format(name, price, img_short)) #pretty console log

            time.sleep(15)

    # Write the array to file as JSON
    with open('name_output.json', 'w') as f:
        json.dump(name_arr, f)

    with open('price_output.json', 'w') as f:
        json.dump(price_arr, f)

    with open('img_output.json', 'w') as f:
        json.dump(img_arr, f)


if __name__ == "__main__":
    main()






