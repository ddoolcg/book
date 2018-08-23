# _*_ coding:UTF-8 _*_

import requests  # 导入requests 模块
from bs4 import BeautifulSoup, NavigableString  # 导入BeautifulSoup 模块
import sys

host = 'http://www.biquge.cm'
path = '/9/9661/7604186.html'
name = u'带着仓库到大明'
char_set = 'gbk'


def start(_file, _host, _path):
    r = requests.get(_host + _path, headers=headers)  
    r.encoding = char_set
    html = BeautifulSoup(r.text, 'lxml')
    title = html.find('title').string.replace(name, '').strip()
    _file.write('\n\n\n' + title + '\n\n\n')
    content_tag = html.find(id='content')
    if content_tag and content_tag.contents and len(str(content_tag.contents)) > 500:
        for content in content_tag.contents:
            if type(content) == NavigableString:
                f.write(content.replace('&nbsp;', '').strip())
            elif str(content) == '<br/>':
                f.write('\n')
        f.write('\n')
        print path + title + u'成功'
    for a in html.find_all('a'):
        if a.string == u'下一章' or a.string == u'下一页':
            start(f, _host, a['href'])
            return


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/54.0.2840.99 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
    f = open(name + '.txt', 'w')
    start(f, host, path)
    f.flush()
    f.close()
