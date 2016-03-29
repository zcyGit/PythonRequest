#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import hashlib


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1(object):
    def maxSubArray(self, nums):
    	self.nums=nums;
    	length=len(nums);
    	sum=0;
    	maxSum=-2147483647 - 1;
    	for i in range(length):
    		sum=sum+nums[i];
    		if sum>maxSum:
    			maxSum=sum;
    		if sum<0:
    			sum=0;
    	return maxSum;

class Solution(object):
    def isBalanced(self, root):
    	if self.DfsTreeHight(root)>=0:
    		return True;
    	else:
    		return False;


    def DfsTreeHight(self,root):
    	if root is None:
    		return 0;

    	leftHight=self.DfsTreeHight(root.left);
    	if leftHight==-1:
    		return -1;

    	rightHight=self.DfsTreeHight(root.left);

    	if rightHight==-1:
    		return -1;

    	if abs(leftHight-rightHight)>1:
    		return -1;
    	else:
    		return max(leftHight,rightHight)+1;


solut=Solution();
solut1=TreeNode(1);
solut2=TreeNode(2);
solut3=TreeNode(3);
solut1.left=solut2;
solut1.right=solut3;

print(solut.isBalanced(solut1));
