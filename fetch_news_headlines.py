import os
import time
from bs4 import BeautifulSoup
import urllib2


proxy = urllib2.ProxyHandler({'https': 'https://edcguest:edcguest@172.31.102.29:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

url="https://news.google.co.in/"
response = urllib2.urlopen(url)
page_data = response.read()
#print page_data
soup=BeautifulSoup(page_data,'html.parser')

cnt = 0
detail=[]
urls=[]
print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Headlines >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
for x,y in zip(soup.find_all('td',class_="esc-layout-article-cell"),soup.find_all('div',class_="esc-lead-snippet-wrapper")):
	#for xi in x.find_all('span',class_="titletext"):
		cnt = cnt + 1
		urls.append(x.a['href'])
		print cnt, " > ", x.text
		detail.append(y.text)
x=len(detail)
while(True):
	s = raw_input('Detail : ')
	if s == "":
		break
	elif int(s) > x or int(s) <= 0:
		continue
	else:
		print detail[int(s)-1]
		print "Click here For Detail : ",urls[int(s)-1]