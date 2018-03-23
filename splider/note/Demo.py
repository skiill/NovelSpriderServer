import requests;
from pyquery import PyQuery as pq;
import json;


def writeToFile(data):
    with open('data.txt', 'a',encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n");
def getHtml(url):
    response = requests.get(url);
    doc = pq(response.content.decode('gbk'));
    return doc;
def paserHtml(doc,id):
    content = doc('ul li').eq(id).html();
    index = content.index('/');
    last = content.index('>') - 1;
    url = 'http://www.xntk.net' + content[index:last].replace("amp;", "");
    header = doc('ul li').eq(id).text()
    return [header,url];
def getNum(doc):
    count = doc('ul li').size();
    return count;
def main():
    url = 'http://www.xntk.net/html/19/19576/';
    doc = getHtml(url);
    count = getNum(doc);
    print("共有%d条记录"%count)
    for id in range(0,count):
        data = paserHtml(doc,id);
        writeToFile(data);
        #print('还有%d条记录'%(count-id));



if __name__ == '__main__':
    main()