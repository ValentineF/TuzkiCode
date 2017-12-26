import requests
import re
from bs4 import BeautifulSoup
import queue
import threading
import time
import os
from lxml import etree
import multiprocessing

def get_html_text(url):
    try:
        #模拟浏览器访问
        kv ={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
        r = requests.get(url,timeout = 1,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print(r.statue_code)
        return ""

def download_picture(url,path):
    try:
        picture = requests.get(url,timeout = 1)
        with open(path,"wb") as f:
            f.write(picture.content)
    except:
        pass

# 获取详情链接
def get_detail_url(url):
    try:
        detail_list = []
        html = get_html_text(url)
        soup = BeautifulSoup(html,"html.parser")
        count = 1
        for i in soup.select("ul li a[href]"):
            if("tag" not in str(i)):
                if(".html" in str(i)):
                    if("http:" in str(i)):
                        detail_list.append(i.attrs["href"])
        return detail_list
    except:
        return

# 获取页面总数和标题
def get_page(url):
    try:
        html = get_html_text(url)
        soup = BeautifulSoup(html,"html.parser")
        page = str(soup.select('li[class="AppLI"] a')[0])
        page = page[4:]
        page = page[:-7]
        title = str(soup.find("h1").string)
        return int(page),title
    except:
        print("get_page error")

# 获取图片链接
def get_image_url(url):
    try:
        html = get_html_text(url)
        soup = BeautifulSoup(html,"html.parser")
        href = str(soup.select('p[align="center"] img')[0])
        return href.split('"')[1]
    except:
        print("get_image_url error")
        return ""

def thr(start,end,task):
    for t in range(start,end):
        url_list = "http://www.duotoo.com/meinvtupian/meinvtupian_"+str(t)+".html"
        detailList = list(set(get_detail_url(url_list)))
        for i in detailList:
            pages,titles = get_page(i)
            print("Task",task,"  :   ",titles)
            path = "D:/image/"+titles+"/"
            os.makedirs(path)
            for j in range(1,pages+1):
                urls = i[:-5] +"_"+str(j)+".html"
                download_picture(get_image_url(urls),path+str(j)+".jpg")

def main():
    for t in range(1,349):
        try:
            url_list = "http://www.duotoo.com/meinvtupian/meinvtupian_"+str(t)+".html"
            detailList = list(set(get_detail_url(url_list)))
            if(detailList):
                for i in detailList:
                    pages,titles = get_page(i)
                    print(titles)
                    path = "D:/image/"+titles+"/"
                    os.makedirs(path)
                    for j in range(1,pages+1):
                        urls = i[:-5] +"_"+str(j)+".html"
                        download_picture(get_image_url(urls),path+str(j)+".jpg")
        except:
            continue

if __name__ =="__main__":
    main()
    print("All Was Done!!!!!!!!!")
