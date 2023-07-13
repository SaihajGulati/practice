class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1
        result = []

        #do both less than to skip garbage cases of ending that are too hard to handle otherwise
        while l < r and t < b:
            #fill in top row
            #r not r+1 because exclusivity helps here so next loop can fill
            for i in range(l, r):
                result.append(matrix[t][i])
            
            #fill in right column
            for i in range(t, b):
                result.append(matrix[i][r])
            
            #fill in bottom row
            #need bigger num to be inclusive here but smaller not, so custom range is better than reversed
            for i in range(r, l, -1):
                result.append(matrix[b][i])

            #fill in left column
            #same as above where need bigger num inclusive but smaller not
            for i in range(b, t, -1):
                result.append(matrix[i][l])

            l += 1
            r -= 1
            t += 1
            b -= 1
            
        if (l < r and t == b): #means one row left
            for i in range(l, r + 1):
                result.append(matrix[t][i])
        elif (t < b and l == r): #means column left
            for i in range(t, b + 1):
                result.append(matrix[i][r])
        elif (t == b and l == r): #both equal so literally one value left
            result.append(matrix[t][l])
        #if get here, is just good to go as both are out of bounds
        return result
