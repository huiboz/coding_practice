
import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

def get_followers_count(profile_url, session):
    instagram_url = 'https://www.instagram.com'
    response = session.get(instagram_url + '/' + profile_url)
    if response.ok:
        html = response.text
        bs_html = BeautifulSoup(html, features='lxml')

        scripts = bs_html.findAll("script", {"type": "application/ld+json"})
        scripts_content = json.loads(scripts[0].string.strip())
        follwers_count = scripts_content['mainEntityofPage']['interactionStatistic']['userInteractionCount']
        return follwers_count
    else:
        print('profile not found')
        exit

async def get_followers_async(profiles):
    res = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(executor, get_followers_count, *(profile, session)) for profile in profiles
            ]
            for response in await asyncio.gather(*tasks):
                res.append(response)
    return res

if __name__ == "__main__":
    profiles = ['huibobbbean', 'realdonaldtrump']
    start = time.time()
    for profile in profiles:
        print(profile + " has " + get_followers_count(profile, requests) + " followers")
    end = time.time()
    elapsed = end - start
    print("take " + str(elapsed) + " seconds for sequential")

    start_async = time.time()
    res = asyncio.run(get_followers_async(profiles))

    end_async = time.time()
    elapsed_async = end_async - start_async
    print("take " + str(elapsed_async) + " seconds for async calls")
    print(res)

      