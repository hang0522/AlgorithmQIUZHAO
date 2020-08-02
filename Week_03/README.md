学习笔记
用二分查找旋转有序数组中第一个无序的数：
思路：
即找到旋转有序数组的最小值的索引
left, right = 0, len(nums) - 1
while left < right:
    mid = (left + right) >> 1
        if nums[mid] > nums[right]:         
            left = mid + 1
        else:                               
             right = mid
return left
