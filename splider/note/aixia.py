import requests;
import urllib;
from pyquery import PyQuery as pq;
import json;


# 获取网页的doc对象
def getHtml():
    url = 'https://www.xiashu.la/type/nan_0_0_allvisit_1.html';
    response = requests.get(url);
    doc = pq(response.content);
    return doc;


 # 获取小说列表
def getNovelList(doc):
    list = []
    # 根据选择器得到子节点
    children = doc("#waterfall").children();
    # 得到子节点的个数
    length = children.length;
    # 遍历子节点
    for i in range(0, length):
        str = '#waterfall > div:nth-child(%d)' % i;
        print(doc(str).text());
        list.append(doc(str).text())
    return list
    #     list.insert(i,doc(str).text())
    # for item in list:
    #     print(item);

# 下载小说  body > div.wrapper > div.content.mt20 > div > p:nth-child(8)
def downloadNovel(url):
    url = 'https://www.xiashu.la/52977/down';
    response = requests.get(url);
    doc = pq(response.content)
    href = doc('body > div.wrapper > div.content.mt20 > div > p:last').html();
    print(href)

    return ;






def main():
    novellist = [];
    url = 'https://www.xiashu.la';
    doc = getHtml();  # 获取网页的doc对象
    #novellist = getNovelList(doc);   # 获取小说列表
    downloadNovel(url);     # 下载小说




if __name__ == '__main__':
    main();