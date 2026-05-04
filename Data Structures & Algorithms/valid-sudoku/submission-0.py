from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #I could make a set of every column, row and sub box O(n) O(n) brute force
        # I could make a dictionary key num val row, col, box also brute force On On
        # I could iterate and check if a row/col is valid O O1
        soduko_filled = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                sub_box = i//3 + (j//3)*3
                curr_num = board[i][j]
                print(curr_num, sub_box, i, j, )
                if  curr_num != ".":
                    if curr_num in soduko_filled[str(i)+"row"]:
                        print(soduko_filled)
                        
                        return False
                    else:
                        print(curr_num, curr_num != ".", curr_num != '.')
                        soduko_filled[str(i)+"row"].add(curr_num)
                    if curr_num in soduko_filled[str(j)+"col"]:
                        print(soduko_filled)
                        return False
                    else:
                        soduko_filled[str(j)+"col"].add(curr_num)
                    if curr_num in soduko_filled[str(sub_box)+"box"]:
                        print(soduko_filled)
                        return False
                    else:
                        soduko_filled[str(sub_box)+"box"].add(curr_num)
        return True
        