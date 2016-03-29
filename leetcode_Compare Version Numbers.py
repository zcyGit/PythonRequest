#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def compareVersion(self, version1, version2):

    	ver1list=version1.split('.');
    	ver2list=version2.split('.');

    	ver1Count=len(ver1list);
    	ver2Count=len(ver2list);

    	for i in range(ver1Count):
	    	ver1=int(ver1list[i]);
	    	if i<ver2Count:
	    		ver2=int(ver2list[i]);
	    	else:
	    		ver2=0;

	    	if ver1>ver2:
	    		return 1;
	    	elif ver1<ver2:
	    		return -1

    	if ver2Count>ver1Count:
    		while ver1Count<ver2Count:
    			if int(ver2list[ver1Count])>0:
    				return -1;
    			ver1Count+=1;

    	return 0;
solu=Solution();
ver1='1';
ver2='1.1';
print(solu.compareVersion(ver1,ver2))