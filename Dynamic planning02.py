#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
假设装备（0,0）每次通过一次升级可以升级到比原有数任意大小的级别，但是横纵坐标一次只能升级一个，问升级到
（3,3）有多少种方法，例如可以（0,0）升级到（3,0）再升级到（3,3）
思路：（3,3）坐标上的方法和为横纵坐标上（0,3）到（2,3）以及（3,0）到（3,2）的方法之和
"""
def uniquePath2(m,n):
    A = [[0 for col in range(n)] for row in range(m)]
    A[0][0]=1
    for i in range(m):
        for j in range(n):
            for k in range(i):
                A[i][j]+=A[k][j]
            for l in range(j):
                A[i][j]+=A[i][l]
    return A[m-1][n-1],A
if __name__=='__main__':
    m=4
    n=4
    sum,A1=uniquePath2(m,n)
    print(sum)
    print(A1)