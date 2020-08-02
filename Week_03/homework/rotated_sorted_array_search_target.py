class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if len(n)==0:
        if not nums:
            return -1
        # if len(n)==1:
        #     return nums[0]==target?0:-1
        left = 0
        right = len(nums)-1
        while left<=right:
            #mid = left + (right-left)//2
            #mid = (left + right) >> 1
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]: 
                #if nums[mid]>target and nums[left]<=target:
                #if nums[0]<=target<nums[mid]:
                if nums[mid]>target and nums[left]<=target:
                  right = mid-1
                else:
                  left = mid+1
            #elif nums[mid]<nums[right]:
            else:
                #if nums[mid]<target and nums[right]>=target:
                #if nums[mid]<target<=nums[len(nums)-1]:
                if nums[mid]<target and nums[right]>=target:
                  left= mid+1
                else:
                  right = mid-1
        return -1