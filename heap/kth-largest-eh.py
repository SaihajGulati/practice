class Solution:
    #Time complexity is O(n) in best and average case, but O(n^2) in worst so oof typa payoff
    #and bc keep on calling function, does use more memory but extra memory complexity is O(1)
    #personally, and leetcode time and memorywise, the heap solution where i heapify list is most cracked
    def partition(self, left: int, right: int, nums: List[int]) -> int:
        #i is past end of part of list that is less than pivot
        i = left
        pivot = right
        #automatically means don't include last index (right one)
        for j in range(left, right):
            if nums[j] <= nums[pivot]:
                #swap j with the i one that is signpost
                #cracked python way to swap
                nums[i], nums[j] = nums[j], nums[i]
                #when swap, need to move signpost up
                i += 1
                #for loop automatically moves j up so good

        #last i is signpost of where pivot should go
        nums[i], nums[pivot] = nums[pivot], nums[i]
        return i


    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = -1

        #smart to just do this here to make if statement logic easier
        #if want second biggest number of 6 len list, will be in 4th index
        #this will be index we want it in henceforth, need to do bc otherwise index is index + 1 smallest value after each partition as all to left are smaller and all to right are bigger
        k = len(nums) - k

        #could also do while l < r, but will only get there if never get to k = pivot which is not possible
        #commonly also done with l <= r condition but ethen have to add else where breaks but that just seems dumb
        while pivot != k:
            pivot = self.partition(l, r, nums)
            #means pivot is less than one we want
            #so need to look at nums bigger than it, which are now on the right
            if pivot < k:
                l = pivot + 1
            #this means it's too big so look to left
            elif pivot > k:
                r = pivot - 1
            #else is what we want where len(nums) - pivot = k, which means kth largest number
        #if get here, found correct pivot
        return nums[pivot]
