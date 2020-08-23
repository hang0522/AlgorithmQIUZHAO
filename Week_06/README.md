学习笔记
1. 选择排序
   a.找到数组中最小的那个元素；
   b.将这个最小的元素与第一个元素互相交换位置；
   c.在剩下的元素中找到一个最小的元素
   d.将这个最小的元素与第二个元素互相交换
   e.依此类推，直到最后
```
def selectionSort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(len(data)):
            if(data[j]<data[i]):
                min_idx = j
        data[i],data[min_idx] = data[min_idx],data[i]
```
2. 冒泡排序
   a. 比较相邻的元素，如果第一个比第二个大，就交换他们两个；
   b. 对每一对相邻元素做同样的操作；
   c. 针对所有的元素重复以上步骤，除最后一个元素；
```
def bubbleSort(data):
    for i in range(0,len(data)):
        for j in range(0,len(data)-i-1):
            if a[j]> a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
```  
3. 插入排序
   a.从第2个元素开始，对比第2个元素与第1个元素，如果第2个元素比第1个元素小，则交换
   b.第3个元素，和它之前的元素比较，如果第3个元素小，就交换；
```
def insertionSort(data):
    for i in range(1,len(data),1):
        for j in range(1,i,-1):
            if data[j]<data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]
```

不同路径2转移方程：
 store[i][j] =  store[i-1][j]+store[i][j-1]