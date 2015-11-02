# encoding=utf8
from httplib import *
from bs4 import BeautifulSoup
import time
from datetime import datetime
 
url = "www.xiaomi.com"
con = HTTPConnection(url)
 
def get_ctn():
    #return html
    con.connect()
    con.request('get', '/static/mi2abranchs')
    resp = con.getresponse()
    dat = resp.read()
    print 'get ctn sts', resp.status
    return dat
 
def get_sts():
    ctn = get_ctn()
    sp = BeautifulSoup(ctn)
    cnr = sp.find('div', id='container')
    brh = cnr.find('li', class_='branch_1s_li_01')
    itm = brh.find('p', class_='branch_1s_list_item2')
    gds = itm.find('span', class_='home_btn_nogoods')
    if gds:
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), gds.get_text()
    else:
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'),itm
         
def lp_ck():
    while True:
        get_sts()
        time.sleep(60 * 30)
lp_ck()
print "DONE"
