#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import xlrd
from newspaper import Article
import queue
import threading
import time

#解析excel,{"官网地址"："页面文件名"}
def getCollegeList():
    data = xlrd.open_workbook('C:/Users/SweetCandy/OneDrive/Code/Python/list.xlsx')
    table = data.sheets()[0]
    rows = table.nrows
    urlInfor = {}
    for i in range(1,rows):
        #获取该行的值，以数组形式
        row = table.row_values(i)
        if row:
            urlInfor[row[6]] = row[9]
    return urlInfor

# 解析网页
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
# 获取简介路径
def getIntroduceUrl(url):
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html,"html.parser")
        a = soup.find_all("a",text=re.compile("^.*(学校概况|学校简介|学校介绍|学院概况|学院简介|学院介绍|)$"))
        for i in a:
            href = i.attrs['href']
        if(href.find("www") == -1):
            return url+"/"+href
        else:
            return href
    except:
        return ""

# 获取主要内容
def getMainContent(url):
    try:
        a = Article(url,language="zh") 
        a.download()
        a.parse()
        return a.text
    except:
        return ""

count = 0
def thr():
    global q
    global collegeList
    global count
    while not q.empty():
        url=q.get()
        introduceUrl = getIntroduceUrl(url)
        #introduceUrl = url
        if(introduceUrl == ""):
            continue
        content = getMainContent(introduceUrl)
        fpath = "C:/Users/SweetCandy/OneDrive/Code/Python/CollegeList/"+collegeList[url]
        with open(fpath, "w",encoding='utf-8', errors = 'ignore') as f:
            f.write(content)
        count = count + 1
        print("[finishd][%d]"%(count) + introduceUrl)

q = queue.Queue()
collegeList = getCollegeList()
for url in collegeList.keys():
    q.put(url)
for i in range(0,200):
    threading.Thread(target=thr).start()
    print(i)
    time.sleep(0.1)
while True:
    time.sleep(1)
print("Successful")



"""
count = 0
collegeList = getCollegeList()
for url in collegeList.keys():
    try:
        print(count)
        count = count + 1
        introduceUrl = getIntroduceUrl(url)
        print(introduceUrl)
        if(introduceUrl == ""):
            continue
        content = getMainContent(introduceUrl)
        fpath = "C:/Users/SweetCandy/OneDrive/Code/Python/CollegeList/"+collegeList[url]
        with open(fpath, "w",encoding='utf-8', errors = 'ignore') as f:
            f.write(content)
    except:
        continue
print("Successful")
"""