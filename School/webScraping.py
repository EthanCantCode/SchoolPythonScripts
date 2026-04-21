import requests, os, bs4

counter = 0

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    counter += 1
    if counter >= 10:
        break

#TODO Download the page
    res = requests.get(url)
    res.raise_for_status()
#TODO Find the URL of the comic image
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
#TODO Download the image
        res = requests.get(comicUrl)
        res.raise_for_status()
#TODO Save the image to ./xkcd
        if counter >= 10:
            imageFile = open(os.path.join('./xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
#TODO Get the Prev button's url
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')


    print('done')

print(f'the counter is {counter}')