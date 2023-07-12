class Solution:

  #this is a dfs/backtrack essentially since try to keep going until fail
  #T: O(n^2) in worst case if have to check all n each time for each n
  #M: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gasLeft = gas[i]
            failed = False
            for j in range(1, 1 + len(gas)):
                gasLeft = gasLeft - j[i + j]
                if gasLeft < 0:
                    failed = True
                    break
            #if get here and never failed
            if not failed:
                return i
        return -1
