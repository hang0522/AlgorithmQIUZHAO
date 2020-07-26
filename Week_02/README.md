# 学习笔记

## 1.树

python 版树的定义

```
    class TreeNode:
      def __init__(self, val):
        self.val=val
        self.left, self.right = None,None  
```

* 遍历方式：前，中，后序遍历 (实现方式：递归，迭代)

## 2. 二叉搜索树

a. 即二叉排序树，有序二叉树，排序二叉树；
b. 左子树所有节点的值均小于其根结点的值，右子树所有阶段的值均大于其根结点的值；
c. 中序遍历为升序排列；
d. 常见操作：查询，插入，删除；时间复杂度平均为O(logn),O(logn),O(logn);

## 3.树的题目为什么都是递归

a.树的结构定义没有后续结构的定义，即为便于循环的结构；
b.遍历时需要对每个节点的左右子树进行相同的操作；

## 堆

a. 常用：大顶堆，小顶堆  
b. 以大顶堆的操作为例的时间复杂度：查找最大值(O(1))，删除最大值(O(logN)),插入(O(logN) or O(1))
c. 二叉堆：完全二叉树实现(ps：不是二叉搜索树)
d. 大顶二叉堆的性质：是一颗完全树；树中任意节点的值总是>=其子节点的值；
e. 在二叉堆中第i个元素为例：
其左孩子的索引：(2*i+1)
其右孩子的索引：(2*i+2)
其父节点的索引：floor((i-1)/2)
f. 大顶二叉堆删除对顶操作的步骤：先将堆尾元素替换到顶部，再依次从根部向下调整整个堆的结构

## 递归模板

```
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
      process_result
      return
    #process logic in current level
    process(level, data...)

    #drill down
    self.recursion(level+1, p1, ...)

    # reverse the current level status if needed
```

### 动态规划

1. 把复杂问题分解成简单的子问题；

2. 分治+最优子结构；

3. 顺推形式：动态递归；

### 分治代码模板

```
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
    print_result
    return

  #prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)

  #conquer subproblems
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)

  #process and generate the final result
  result = process_result(subresult1, subresult2, subresult3)

  #revert the current level states

```

*动态规划的本质就寻找重复性：利用数学归纳法的思想找到最近最简单方法，把问题拆分为可重复可解决的问题*