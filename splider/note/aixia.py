import requests;
import urllib;
from pyquery import PyQuery as pq;
import json;


# 获取网页的doc对象
def getHtml(url,page):

    listUrl = '%s/type/nan_0_0_allvisit_%d.html'%(url,page);
    response = requests.get(listUrl);
    doc = pq(response.content);
    return doc;


 # 获取小说列表
def getNovelList(doc):
    list = {};
    # 根据选择器得到子节点
    children = doc("#waterfall").children();
    # 得到子节点的个数
    length = children.length;
    # 遍历子节点
    for i in range(1, length):
        # 子节点的选择器
        str = '#waterfall > div:nth-child(%d) > div.title > h3 > a' % i;
        countstr = '#waterfall > div:nth-child(%d) > div.num > a.cmt-num'%i;
        # 小说标题
        title = doc(str).text();
        #小说id
        id = doc(str).attr('href')
        readcount = int(doc(countstr).text());
        # 将数据以标题为key，id为值存入字典中
        if 1000000 < readcount:
            list[title] = id;
    return list


# 下载小说  body > div.wrapper > div.content.mt20 > div > p:nth-child(8)
def downloadNovel(url,idList):
    downUrl = url;
    loadUrl = {};
    for idstr in idList:
        id = int(idstr);
        downUrl = '%s/%d/down'%(url,id);
        response = requests.get(downUrl);
        doc = pq(response.content);
        str = '#downlist > ul:nth-child(3) > li:nth-child(1) > span.zip-download > a';
        href = doc(str).attr('href');
        title = doc(str).attr('title')
        if None==href:
            print('很抱歉！本书TXT下载资源已失效或缺失，暂未添加新的下载资源，请选择在线阅读本书或先浏览本站其他书籍。');
        else:
            loadUrl[title] = href;

    return loadUrl;
#获取每本小说的id
def getNovelId(novel):
    idList = [];
    # 以列表的形式返回所有的标题
    titleList = novel.keys();
    for title in titleList:
        idList.append(novel[title][1:-1]);
    return idList;
#把数据写入到文件中
def writeToFile(data ,name):
    with open('%s.txt'%name, 'a',encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n");

def loadBook(loadUrl):
    titleList = loadUrl.keys();
    for title in titleList:
        r = requests.get(loadUrl[title]);
        with open('%s.zip'%title , "wb") as code:
            code.write(r.content)
def main():
    novel = {};
    loadUrl = {}
    idList = [];
    url = 'https://www.xiashu.la';
    totalPage = 6116+1;
    for page in range(1,totalPage):
        doc = getHtml(url,page);  # 获取网页的doc对象
        novel = getNovelList(doc);   # 获取小说列表
        idList = getNovelId(novel)
        loadUrl = downloadNovel(url,idList);     # 下载小说
        # writeToFile(novel,'小说列表');
        writeToFile(loadUrl,'小说下载列表');
        loadBook(loadUrl);


if __name__ == '__main__':
    main();