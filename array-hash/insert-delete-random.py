class RandomizedSet:
    
    def __init__(self):
        self.numMap = {}
        self.nums = [] #need list so can do random in O(1) time

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        last = self.nums[-1]
        self.nums[idx] = last #this is smart way, switch with end and then pop from end so O(1) average
        self.numMap[last] = idx
        self.nums.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
