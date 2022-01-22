'''
#Todo:2种scrapy cmd运行方式:
#1.scrapy.cmdline
from scrapy import cmdline
#print(('scrapy crawl yu').split())
cmdline.execute('scrapy crawl yu'.split())

'''
#2.subprocess.call
import subprocess
#subprocess.call('pwd',shell=True)#2 s 1
cmd= 'scrapy crawl yu'
subprocess.call(cmd,shell=True)#2 s 1

#3.scrapy项目路径要正确:/storage/emulated/0/01spider/article
#subprocess.call(cmd,shell='python3.8')


