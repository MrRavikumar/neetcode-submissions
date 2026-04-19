class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setRow = set()
        setCol = [set() for _ in range(9)]
        setBox = [set() for _ in range(3)]

        for j , row in enumerate(board):
            if j % 3 == 0:
                setBox[0].clear()
                setBox[1].clear()
                setBox[2].clear()
            
            for i, letter in enumerate(row):
                if letter == ".":
                    continue
                else:
                    
                    if letter in setRow:
                        return False
                    else:
                        setRow.add(letter)
                    
                    if letter in setCol[i]:
                        return False
                    else:
                        setCol[i].add(letter)
                    
                    indexSquare = i // 3
                    if letter in setBox[indexSquare]:
                        return False
                    else:
                        setBox[indexSquare].add(letter)
                
            setRow.clear()
        return True
        