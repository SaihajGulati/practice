class Solution:
    # T: O(nlogn) bc of sort, O(n) for rest of it
    # M: O(n) bc of stack and pair array
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #make list of pairs of position and speed
        #zip creates tuples out of two lists
        pair = [(p, s) for p, s in zip(position, speed)]
        #sort it in reverse order, so is going by last position to first position  
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            #add it to the stack, for first automatically
            #means second which is position before last one, will be checked if it catches up, and if so, will be popped which is why stack is useful since is last one added (one position farther back than last one)
            #works because relative ordre will never be changed as cars can't be passed
            #AND bc for instance farthest back on can't catch up to third without catching up to second and going at that speed first, so first chcking if second catches up to third is more valid
            #AND poppping farther back on is valid bc farther back one will always have faster speed than farther ahead one if they collide, that's maths
            
            #appending the time it'll end
            stack.append((target - p) / s)

            #if the length of the stack is at least 2 and the last one added (which is actually NOT closest to end but second closest to end as closest to end was seen/added first) will reach end before one added before which is closer in position to end, then need to combine into a fleet
            #since assumes slower speed, pop top which removes the one farther from end which was going at a faster speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
