
# http://www.31xiaoshuo.org/17/17545/


import requests,time
from bs4 import BeautifulSoup

name,href,book=[],[],[]  #节名,href,小说名
def html(url):
    r=requests.get(url)
    #print(r)
    # soup转换
    soup=BeautifulSoup(r.text,"html.parser")
    #print(soup)
    section = soup.select('div#list dl dd a')
    # print(len(section)) #<a href="/17/17545/11904841.html">第一章 门派弃徒</a>
    # 获取章节名称
    book_name = soup.select('div#info h1')[0].text  #仙武帝尊
    book.append(book_name)

    # name,href,book=[],[],[]
    for i in range(len(section)):
        section_name=section[i].text #第一章 门派弃徒
        name.append(section_name)
    # 获取章节href
        section_href=section[i].get('href')
        href.append(section_href)
    # /17/17545/11904841.html   or :sectionhref'])
    # return name,href
def zhangjie():
    print('总章节数：'+str(len(href)))
    start=int(input('你正准备下载小说：【'+book[0]+'】,确认需开始的章节：'))
    total=int(input('一共'+str(len(href))+'章，要下至多少章？'))

    if total<=len(href):
        # print(href[start],start)
        sleep=0
        for i in range(start-1,total-1):
            book_url = 'http://www.31xiaoshuo.org' + href[i]
            # print(start,start+total,href[i],book_url)
            header = {
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_29a352f58f525381803e1ef14929689d=1603441754,1603462717,1603498391; bdshare_firstime=1603441753801; tongji=1; _ga=GA1.2.633931289.1603441755; _gid=GA1.2.96401951.1603441755; Hm_lpvt_29a352f58f525381803e1ef14929689d=1603498396; _gat_gtag_UA_139602484_1=1',
                'Referer': 'http://www.31xiaoshuo.org/17/17545/',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
            }
            r = requests.get(book_url, headers=header)
            # print(r.text)
            soup = BeautifulSoup(r.text, "html.parser", exclude_encodings='utf-8')

            # book_name=soup.select('div.con_top a')[1].text #仙武帝尊
            zhangjie_name = soup.select('div.bookname h1')[0].text  # 第一章 门派弃徒
            zhangjie_content = soup.select('div#content p')  # [<p>“外门弟子叶辰。。。
            # zhangjie_content1=soup.select('div#content p')[56].text

            # print(book_name)
            if sleep%10==0:
                time.sleep(2)
            else:
                sleep = sleep + 1

            print('正在下载章节：' + zhangjie_name)
            f = open(book[0] + '.txt', "ab+")  # 打开小说文件
            # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
            f.write(('\t\r' + zhangjie_name + '\r\n\n').encode('UTF-8'))  # 回车+换行：\r\n
            # 以二进制写入章节内容
            for t in range(len(zhangjie_content)):
                f.write((zhangjie_content[t].text + '\r').encode('UTF-8'))
            f.close()  # 关闭小说文件
            # 关闭小说文件
    else:
        print('WARRING...输入超过总章节，出错！请重新输入，重新运行!')



if __name__ == '__main__':
    url = 'http://www.31xiaoshuo.org/17/17545/'
    html(url)
    # print(name[0],href[0],book[0],href[150])
    zhangjie()


    # print(req(url)[0][0],req(url)[1][0])


