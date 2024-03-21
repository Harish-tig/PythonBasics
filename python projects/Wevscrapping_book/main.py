### grabbing web page and extraction books of rating 2 and its title with cost of the book using python
import requests
import bs4
import re
Url_2 ="https://books.toscrape.com/catalogue/page-{}.html" # basic link {} for looping
# # print(Url_2.format(num=1))
# res = requests.get(url=Url_2.format(1))## makes sense why dot format
# soup = bs4.BeautifulSoup(res.text,"lxml")  # converting giant html text to readable sense
# Class = soup.select('.product_pod') # brings a argued clss under observation
# book_1 = Class[0] # mostly in format of list or special format of bs4
# price = book_1.select('div')[1].select('.price_color') ### bring class under obs
# print(book_1) # check one
# print('----------------------------------')
# cost = re.search('£.....',str(price)) # check two passed guessing or approx 4 dig value
# print(cost.group())
# name = book_1.select('div a')[1]['title']
# # print(name)
# class_p = book_1.select('.star-rating.Three')
# # print(class_p)
### testing hit and try above codes

# step 1 bring url and observe loop holes
# understand your needs and observe html files carefullly
# grab you necessary cell class and get them under observation
# check for requirements
# divide problems in to sub problems
# solve each sub problems by above method
# extract using .select method and observe loopholes






title_of_twostar = {} # for storing final title and cost
for x in range(1, 51): # by observation there are only 50 page in web
    res = requests.get(url=Url_2.format(x)) #for each page
    soup = bs4.BeautifulSoup(res.text, "lxml")
    Class = soup.select('.product_pod') #obsereved my required details inside class dot product_pod
    for each in Class: #each class has 20 books going through each book
        if len(each.select('.star-rating.Two')) != 0: #little confidential because if the string is not there it returns empty list
            price = str(each.select('div')[1].select('.price_color'))
            cost = re.search('£.....', price)
            title_of_twostar[str(each.select('div a')[1]['title'])] = cost.group()

for key, value in title_of_twostar.items():
    print(key +":",value, end="\n",)