#coding:utf-8

import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def get_web(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0')
    f = urllib2.urlopen(req)
    return f.read()

def get_xueqiu():
    url = 'http://xueqiu.com/today'
    content = get_web(url)

    soup = BeautifulSoup(content)
    titles = soup.select('#part-today .art_list .topic_tit')
    descs = soup.select('#part-today .art_list .topic_desc')

    result = []
    for i in xrange(len(titles)):
        result.append({'href':'http://xueqiu.com'+titles[i]['href'],
            'title':titles[i].string,
            'desc':descs[i].string})
    return result

def get_v2ex():
    url = 'http://v2ex.com'
    content = get_web(url)

    soup = BeautifulSoup(content)
    hots = soup.select('#TopicsHot .item_hot_topic_title a')

    result = []
    for i in xrange(len(hots)):
        result.append({
            'href': url+hots[i]['href'],
            'title': hots[i].string})
    return result

from bottle import route, run, template, static_file

@route('/')
def main():
    xueqiu = get_xueqiu()
    v2ex = get_v2ex()
    return template('index.tpl',xueqiu=xueqiu,v2ex=v2ex)

@route('/static/:fname#.*#')
def static(fname):
    return static_file(fname, root="./static")

run(host='localhost', port=8080, debug=True)
