#-*- coding:utf-8 -*-
import urllib
import  re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#输出内容是Utf-8的格式
#打开网址，获取源码
def page(pg):
    url="http://www.pengfu.com/index_%s.html"%pg
    html=urllib.urlopen(url).read()
    return html
#匹配图片名称
def title(html):
    reg=re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')#提高效率
    item=re.findall(reg,html)
    return item
#匹配图片地址
def content(html):
    reg1=re.compile(r'<img src=".*?" width=".*?" height=".*?" gifsrc="(.*?)">')
    reg2=re.compile(r'<img src="(.*?)" width=')
    if(re.findall(reg1,html)):
        item=re.findall(reg1,html)
    else:
        itrm=re.findall(reg2,html)
    return item
#下载
def download(url,name):
    #decode以文件保存对内容进行解码，encode转换成gbk格式
    if url=="*.jpg":
        path='img\%s.jpg'%name.decode('utf-8').encode('gbk')
    else:
        path = 'img\%s.gif' % name.decode('utf-8').encode('gbk')
    urllib.urlretrieve(url,path)

#多页
for i in range(5,8):
    html=page(i)#获得网页源码
    title_list=title(html)#匹配图片名称
    content_list=content(html)#匹配图片路径
    for i,z in zip(title_list,content_list):#zip函数
        download(z,i)





