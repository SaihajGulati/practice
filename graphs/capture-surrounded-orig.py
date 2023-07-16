class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #T: O(mn*(possibly mn)) M: O(mn) and that's issue too
        visited = set()

        def dfsChange(r, c, region):
            #means region ended at edge
            if r == len(board) or c == len(board[0]) or r < 0 or c < 0:
                return False
            #means ended up with not off edge, so surrounded on this side by X
            elif board[r][c] == "X":
                return True
            elif (r, c) in region:
                return True

            visited.add((r, c))
            region.add((r,c))

            return dfsChange(r - 1, c, region) and dfsChange(r + 1, c, region) and dfsChange(r, c - 1, region) and dfsChange(r, c + 1, region)

    ####outside of inner function
        surroundedOnes = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = set()
                    #pass new set as region
                    #better to do check out here bc is only checking first
                    if(dfsChange(r, c, region)):
                        surroundedOnes.update(region)

        for r, c in surroundedOnes:
            board[r][c] = "X"
