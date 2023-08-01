# Time: log(min(n, m))
#is a binary search through smallest of two arrays until find correct partition
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #A and B are the two arrays given, goal is to have A be smaller one
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        #half is how long we need overall left partition to be
        half = total // 2

        #we want A to be the smaller one
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            #i is current middle essentially of A
            i = (l + r) // 2  # A
            #j is where partition is in B (the longer one)
            #is based on how many left over to get left partition after find spot in A
            #need half - 1 bc it's indexes not length, and i + 1 bc want length of partition from A subtracted as i is an index not length
            # (half - 1) - (i + 1)
            j = half - i - 2  # B

            #ALeft means value in A that is biggest from it in overall left partition
            Aleft = A[i] if i >= 0 else float("-infinity")
            #ARight means value in A that is smallest from it that is in overall right partition
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            #BLeft means value in B that is biggest from it in overall left partition
            Bleft = B[j] if j >= 0 else float("-infinity")
            #BRight means value in B that is smallest from it that is in overall right partition
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd length, then need to simply return middle which is smallest in riight partition which is longer
                if total % 2:
                    return min(Aright, Bright)
                # even length, need to get average of middle two
                #so average biggest in left partition and smallest of right partition
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
