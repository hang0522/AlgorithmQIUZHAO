class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        #solution1 
        #return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
        #第一个排序准则是x是否在arr2中，如果在则key=0，先排，否则key=1，后排
        #第二个排序准则是在arr2中的下标或者x本身的大小
        return sorted(arr1, key=lambda x:(0,arr2.index(x)) if x in arr2 else(1,x))
        #solution2
        # in_arr2 = []
        # not_in_arr2 = []
        # for i in arr1:
        #     if not i in arr2:
        #         not_in_arr2.append(i)
        #         arr1.remove(i)
        # not_in_arr2.sort()
        # in_arr2 = sorted(arr1, key = lambda x:arr2.index(x))
        # return in_arr2+not_in_arr2