#在0的位置进行移动到target的位置，每次可以选择向左或者向右，第n次移动n步，问最短移动到target的次数
def reachNumber(target):
    """

    :param target: int
    :return: number
    """
    t = abs(target)
    k = 0
    s = 0
    while s<t:
        k+=1
        s+=k
    dt = s-t
    if dt%2==0:
        return k
    else:
        if k%2==0:
            return k+1
        else:
            return k+2

if __name__=='__main__':
    target = 13
    num=reachNumber(target)
    print(num)