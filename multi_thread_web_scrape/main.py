
import requests
from bs4 import BeautifulSoup
import json


if __name__ == "__main__":
    instagram_url = 'https://www.instagram.com'
    profile_url = 'huibobbbean'
    response = requests.get(instagram_url + '/' + profile_url)
    if response.ok:
        html = response.text
        bs_html = BeautifulSoup(html, features='lxml')

        scripts = bs_html.findAll("script", {"type": "application/ld+json"})
        scripts_content = json.loads(scripts[0].string.strip())
        follwers_count = scripts_content['mainEntityofPage']['interactionStatistic']['userInteractionCount']
        print(follwers_count)
    else:
        print('profile not found')
        exit

      