class Solution:
    #T: O(np) where n is number of nodes/courses and p is prereqs
    #because visit all nodes of course but also have to check all prereqs
    #but don't have to check again because empty it after
    #M: O(np) because recursive stack is at most size of tree which is at most size of the graph
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #GENIUS WAY to fill hashmap with empty lists initially for each possible course
        preMap = {i: [] for i in range(numCourses)}

        #fill from prequisite list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #set becuase no duplicates and O(1) search
        visiting = set()

        def dfs(crs):
            #visiting, is ones visited on this dive down the tree (since is dfs, and makes a tree, imagine we are going down one sub-branch_
            #so if see same one again, is a loop
            if crs in visiting:
                return False
            #once get empty list, means can finish this chain/path down the tree (got to the bottom of the tree)
            if preMap[crs] == []:
                return True

            #officially visitnig this on this path
            visiting.add(crs)
            #go through prereqs
            for pre in preMap[crs]:
                if not dfs(pre): #recursive call, but check if false to immediately exit if get loop
                    return False
            #remove (reset essentially) because done going down this path/chain/part of the tree
            visiting.remove(crs)
            #set to empty so know reached end and can do this chain of courses
            preMap[crs] = []
            #DID IT!
            return True

        #have to do this because what if unconnected graph
        #1 -> 2
        #3 -> 4
        for c in range(numCourses):
            if not dfs(c): #instant checking for if found loop
                return False
        return True
