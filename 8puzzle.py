
print("Enter the initial state matrix\nExample: 123\n8_4\n765")
class Node:
    def __init__(self, data, level, fvalue):
        # initialize node 
        self.data = data
        self.level = level
        self.fvalue = fvalue

    # locate where the blank space is
    def locate(self, puzzle, x): 
        for i in range(0, len(self.data)):
            for k in range(0, len(self.data)):
                if puzzle[i][k]== x:
                    return i, k
                
    # move the blank space in the direction tasked
    def shuffle(self, puzzle, x1, y1, x2, y2): 
        # check if position is in bounds
        if (len(self.data) >= x2 >= 0) and (len(self.data) > y2 >= 0) :
            temp_puzzle = self.copy(puzzle) # create copy
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1] = temp_puzzle[x1][y1], temp_puzzle[x2][y2]

            return temp_puzzle
        # if the position value is out of limits return none
        else:
            return None

    # create subnodes from given node by moving blank space
    def subnode(self):
        # four directions
        x, y = self.locate(self.data, '_')
        # positions contains moving direction position values for blank space
        positions = [[x, y-1],[x,y+1],[x+1,y]]
        # generate subnodes by shuffling puzzle
        subnodes = []
        for i in positions:
            node1 = self.shuffle(self.data, x, y, i[0], i[1])
            if node1 is not None:
                node2 = Node(node1, self.level + 1, 0)
                subnodes.append(node2)
        return subnodes # return subnode list
    
    # creates a deepcopy of the matrix as a list of lists
    def copy(self, root):
        temp = []
        for i in root:
            temp.append(list(i))
        return temp




class Puzzle:
    def __init__(self, size):
        # puzzle size input for matrix n by n
        self.n = size 
        # created open and closed lists and initialized to empty
        self.open = [] 
        self.closed = []

    def task(self):
        # input the first and last matrix
        print("Enter the initial state matrix\n\nExample:\n1 2 3\n8 _ 4\n7 6 5")
        initial = self.accept()
        print("Enter the goal state matrix \n")
        goal = self.accept()

# 3 x 3 matrix for 8 puzzle
puzzle = Puzzle(3)
puzzle.process()