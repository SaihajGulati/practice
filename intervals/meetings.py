from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#T: O(nlogn)
#M: O(1)
#NOTICE HOW INTERVAL IS A CLASS
#means have to change for loop variable a bit, sort has to have a key, and how you access start and end slightly changes
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda i: i.start)
        prevEnd = float("-inf")

        for i in intervals:
            #means is overlapping since the start is guaranteed to be the same or bigger than last one's start
            if i.start < prevEnd:
                return False
            else: #need to update prevEnd
                prevEnd = i.end
            
        #if get here, can attend all meetings
        return True
