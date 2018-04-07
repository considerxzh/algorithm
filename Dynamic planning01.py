#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
给定一个m*n的方格，起始点为方格的最左上方，终点为方格的最右下方，
一个机器人只能向下以及向右移动，需要求出机器人从起始点到终点一共
有多少种不重复的路径。问题的输入为方格的长度m以及宽度n，输出为不
同路径的数量。
思路：这里每个点的是由左边和上边的点来的，所以为上面两个之和
"""
def uniquePath(m,n):
    A = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        A[i][0]=1
    for j in range(n):
        A[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            A[i][j]=A[i-1][j] + A[i][j-1]
    return A[m-1][n-1]
if __name__=='__main__':
    m=4
    n=4
    sum=uniquePath(m,n)
    print(sum)


