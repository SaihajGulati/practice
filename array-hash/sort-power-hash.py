class Solution:
   #same time complexity as other solution but slightly worse because have to convert keys to list separately first and use lambda instead of operator item getter
    def getKth(self, lo: int, hi: int, k: int) -> int:
        stepList = {}
        for i in range(lo, hi + 1):
            x = i
            steps = 0
            while x != 1:
                steps += 1
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3 * x + 1
            stepList[i] = steps
        
        keysList = list(stepList.keys())
        sortedList = sorted(keysList, key = lambda x: (stepList[x], x))

        return sortedList[k-1]
            

        
