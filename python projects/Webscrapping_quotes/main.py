import requests
import bs4

base_url = "https://quotes.toscrape.com/page/{}/"
# funtion to set authors name
name = set()
def get_name(author):
    for names in author:
        name.add(names.text)
## function to collect quotes of each page
quotes = []
def get_quote(text):
    for quote in text:
        quotes.append(quote.text)

##function of side box tag
tags = set()
def get_tag(url):
    url=url.format(1)
    req = requests.get(url)
    tag_soup = bs4.BeautifulSoup(req.text,"lxml")
    for tag in tag_soup.select('.tag-item'):
        tags.add(tag.text)
    return tags

num = 1
while True:
        req = requests.get(base_url.format(num))
        soup = bs4.BeautifulSoup(req.text, "lxml")
        author = soup.select('.author')  ## changes in each loop
        text = soup.select('.text')
        if not text:
            break
        get_name(author)
        get_quote(text)
        num += 1



##for better results and readability use for loop to pritn results.

print("Author Names:",name)
print("Quote Texts:", quotes)
get_tag(base_url)
print("tags",tags)




#ignroe
##set of author
# name = set()
#
# for names in soup.select('.author'):
#     name.add(names.text)
#
# print(name)

### list of quote of current and previous page
# qoutes = list()
#
# for quote in soup.select('.text'):
#     qoutes.append(quote.text)
#
# print(qoutes)

###tags
# tags = set()
# for tag in soup.select('.tag-item'):
#     tags.add(tag.text)
#
# for x in tags:
#     print(x)


# base_url = 'https://quotes.toscrape.com/page/{}/'
# req = requests.get(base_url)
# soup = bs4.BeautifulSoup(req.text,"lxml")
# print(soup.select('.author')[0].text)
#ignore
