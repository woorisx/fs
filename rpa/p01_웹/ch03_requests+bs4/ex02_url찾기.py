'''
<div id="comic">
<img src="//imgs.xkcd.com/comics/husband_and_wife.png" title="Borat came out twenty years ago this year--closer to the breakup of the Soviet Union than to today--but it honestly feels like it's been even longer, somehow." alt="Husband and Wife" srcset="//imgs.xkcd.com/comics/husband_and_wife_2x.png 2x" style="image-orientation:none">
</div>
'''

import requests
import bs4

target_url = "https://xkcd.com"

response = requests.get(target_url)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")
img_ele_list = soup.select("#comic img")
print(img_ele_list)
print(len(img_ele_list))

if not img_ele_list:
    print("만화 이미지가 없습니다.")
else:
    image_url = img_ele_list[0].get("src")
    print(image_url)

    if not image_url.startswith("http"):
        image_url = "https:" + image_url

    print(image_url)