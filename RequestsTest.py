#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cai yong'

import requests
import re
import uuid
import os

def Getpage(url,flag):
	try:
		response=requests.get(url);
		if flag==True:
			img=response.content;
			fileName='image/'+os.path.basename(url);
			print(fileName);
			with open(fileName, 'wb') as f:
				f.write(img);
			print('OK');
			return 'OK';	
		return response.text;
	except HTTPError as e:
		if hasattr(e,"reason"):
			print(e.reason);
			return None;
		if hasattr(e,"code"):
			print(e.reason);
			return None;
	except Timeout as e:
		print('Timeout');
		return None;

def loadPage(url,pageIndex):
	url1=url+str(pageIndex);
	print(url1);
	return Getpage(url1,False);

url="http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=";
content=loadPage(url,300);
pageNumber=301;

while content is not None:
	imgpattern=re.compile(r'(http:[^\s]*?(jpg|png|gif){1})',re.I);
	result=imgpattern.findall(content);
	for picname, picType in result:
		img=Getpage(picname,True);
	pageNumber=pageNumber+1;	
	content=loadPage(url,pageNumber);	
	print(pageNumber);
