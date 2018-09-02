import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()

# Parses HTML and turns it into a usable BeautifulSoup object that we can use.
noStarchSoup = bs4.BeautifulSoup(res.text)
# Returns <class 'bs4.BeautifulSoup'>
type(noStarchSoup)