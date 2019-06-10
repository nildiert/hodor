from lxml import html
import requests
import time

def req_values(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    me = tree.xpath(next_val)
    return ([page, tree, me])

try:
    url = 'http://158.69.76.135/level1.php'
    data = {'id':'730','holdthedoor':'submit'}
    next_val = '//td[contains(text(), "730")]/following-sibling::node()/text()'

    page, tree, me = req_values(url)
    data.update({"key":page.cookies["HoldTheDoor"]})
    while ("".join(me) != '\n4095    '):
        page, tree, me = req_values(url)
        data.update({"key":page.cookies["HoldTheDoor"]})
        status = requests.post(url, data, cookies=page.cookies)
        print("{} {}".format(status ,me))
except Exception as e:
    print(e)
