# _*_ coding:UTF-8 _*_

import requests  # 导入requests 模块
from bs4 import BeautifulSoup, NavigableString  # 导入BeautifulSoup 模块
import sys

host = 'http://www.biqu6.com'
path = '/30_30058/19949289.html'
name = u'九星毒奶'
trims = (u"新笔趣阁", u"笔趣阁", u"-", u"_", u"正文卷", u"玄幻小说", u"科幻小说", u"修真小说", u"重回仙界", u"初来乍到",)
char_set = 'UTF-8'


def start(_file, _host, _path):
    r = requests.get(_host + _path, headers=headers)
    r.encoding = char_set
    html = BeautifulSoup(r.text, 'lxml')
    title = html.find('title').string.replace(name, '')
    for trim in trims:
        title = title.replace(trim, '')
    title = title.strip()
    # 有效章
    title_find = title.find(u" ")
    if title_find > 0:
        if title.find(u"第") != 0:  # 开通+第
            title = u"第%s" % (title,)
        i = title.find(u"章")
        if i < 0 or i > title_find:  # 中间插入章
            title = title.replace(u" ", u"章 ", 1)
    _file.write('\n\n\n' + title + '\n\n\n')
    content_tag = html.find(id='content')
    if content_tag and content_tag.contents and len(str(content_tag.contents)) > 500:
        for content in content_tag.contents:
            if type(content) == NavigableString:
                f.write(content.replace('&nbsp;', '').replace('“', '"').replace('”', '"').replace('，', ',').strip())
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
