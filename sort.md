#  Sort Algorithm
+ C++用法
>1、sort函数可以三个参数也可以两个参数，必须的头文件#include < algorithm>和using namespace std;  
2、它使用的排序方法是类似于快排的方法，时间复杂度为n*log2(n)  
3、Sort函数有三个参数：（第三个参数可不写）  
（1）第一个是要排序的数组的起始地址。  
（2）第二个是结束的地址（最后一位要排序的地址）  
（3）第三个参数是排序的方法，可以是从大到小也可是从小到大，还可以不写第三个参数，此时默认的排序方法是从小到大排序。  

##  **Quick Sort** C++
*  函数`Partition`选择一个数字并将大于它的放右边，小于它的放左边 
```
int Partition(int data[], int length, int start, int end)
{
    if (data==nullptr||length<=0||start<0||end>=length)
        throw new std::exception("Invalid Parameters");
    int index = RandominRange(start, end);
    int small = start-1;
    Swap(&data[index], &data[end]);
    for(index=start; index<end; ++index)
    {
        if(data[index]<data[end])
        {
            ++small;
            Swap(&data[index],&data[small]);
        }
    }
    ++small;
    Swap(&data[small],&data[index]);
    
    returm small;
}
```
+  Quick Sort函数用递归的形式进行排序  
```
void QuickSort(int data[],int length,int start,int end)
{
    if(start==end)
        return;
    int index=Partition(data,length,start,end);
    if(index>start)
        QuickSort(data,length,start,index-1);
    if (index<end)
        QuickSort(data,length,index+1,end)
}
```

