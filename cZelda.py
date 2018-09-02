#! python3
#downloadXkcd.py - Downloads most recent pictures of Zelda

import requests, os, bs4

url = 'https://twitter.com/CuriousZelda'         # starting url
os.makedirs('curious_zelda', exist_ok = True)    # store pics in ./curious_zelda


# Download the page
print('Downloading kitty pics')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# Find the URL of the comic image.
picDiv = soup.select('.js-adaptive-photo ')

for pic in picDiv:
    picUrl = pic.get('data-image-url')
    if picUrl == None:
        print('Could not find Zelda')
    else:
        # Download the image
        print('Downloading image %s' % (picUrl))
        res = requests.get(picUrl)
        res.raise_for_status()

        # Save the image to ./curious_zelda
        imageFile = open(os.path.join('curious_zelda', os.path.basename(picUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done.')
