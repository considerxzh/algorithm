"""
给定一个长度为N的序列A1到An,求所有区间的极差之和
"""
import sys
def psum(num,L):
    if num<=0 or num!=len(L):
        return None
    value = 0
    for i in range(0, num-1):
        for j in range(i+1,num):
            value += max(L[i:j+1])-min(L[i:j+1])
    return value
if __name__=='__main__':
    first  = int(input())
    line = sys.stdin.readline().strip()
    L = list(map(int, line.split(' ')))
    print(psum(first,L))