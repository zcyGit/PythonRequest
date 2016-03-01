#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cai yong'


import urllib.request
import urllib.parse
import urllib.error
import heardersClass
import http.cookiejar
import re
import uuid
import os
# url='http://nfc.q.com/region/CitiesTest'
# values={'name':'zcv'};
# binary_data = urllib.parse.urlencode(values).encode(encoding='UTF8')
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
# cj = http.cookiejar.LWPCookieJar()
# cookie_support = urllib.request.HTTPCookieProcessor(cj)
# opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)

#http://cl.olcl.co/thread0806.php?fid=22
#http://cl.olcl.co/login.php
def Getpage(url,flag):
	try:
		values={'name':'zcv'};
		binary_data = urllib.parse.urlencode(values).encode(encoding='UTF8')
		headers=heardersClass.HeardersClass().GetHearders();
		requstUrl=urllib.request.Request(url,binary_data,headers);
		response=urllib.request.urlopen(requstUrl);
		if flag==True:
			img=response.read();
			fileName='image/'+os.path.basename(url);
			print(fileName);
			with open(fileName, 'wb') as f:
				f.write(img);
			print('OK');
			return 'OK';	
		return response.read().decode('utf-8');
	except urllib.error.HTTPError as e:
		if hasattr(e,"reason"):
			print(e.reason);
			return None;

def loadPage(url,pageIndex):
	url1=url+str(pageIndex);
	print(url1);
	return Getpage(url1,False);

url="http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=";
print(url);
content=loadPage(url,97);
pageNumber=98;

while content is not None:
	imgpattern=re.compile(r'(http:[^\s]*?(jpg|png|gif){1})',re.I);
	result=imgpattern.findall(content);
	for picname, picType in result:
		img=Getpage(picname,True);
	pageNumber=pageNumber+1;	
	content=loadPage(url,pageNumber);
	print(pageNumber);


	# print('OK');
	# with open('test.txt', 'w') as f:
	#     f.write(txt);
