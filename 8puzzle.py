
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
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data[0]):
            temp_puzzle = []
            temp_puzzle = self.copy(puzzle) # create copy
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2]= temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            # temp_puzzle[x2][y2], temp_puzzle[x1][y1] = temp_puzzle[x1][y1], temp_puzzle[x2][y2]

            return temp_puzzle
        # if the position value is out of limits return none
        else:
            return None

    # create subnodes from given node by moving blank space
    def subnode(self):
        # four directions
        x, y = self.locate(self.data, '_')
        # positions contains moving direction position values for blank space
        positions = [[x, y-1],[x,y+1], [x+1,y] ]
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

    def action(self):
        # input the first and last matrix
        print("Enter the initial matrix (has one blank space as '_'):\n\nExample:\n1 2 3\n8 _ 4\n7 6 5\n")
        start = self.obtain()
        print("Enter the goal state matrix:\n\n")
        goal = self.obtain()
        start = Node(start, 0, 0)
        start.fvalue = self.f(start, goal)
        # put the initial matrix in the open list
        self.open.append(start)
        print("\n\n")
        while True:
            current = self.open[0] # Get current open list
            print("Next Matrix\n\n")
            # prints everything in current
            for i in current.data:
                for k in i:
                    print(k, end=" ")
                print("")
            # If difference is not 0, we have not reached goal yet
            for i in current.subnode():
                i.fvalue = self.f(i, goal)
                self.open.append(i)
            self.closed.append(current)
            del self.open[0]
            # If difference = 0, we have reached goal matrix
            if (self.h(current.data, goal) == 0):
                break
            # Sort list based on fvalue
            self.open.sort(key=lambda x: x.fvalue, reverse=False)

    # obtains the matrix inputed by user
    def obtain(self):
        puzzle = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puzzle.append(temp)
        return puzzle
    
    # The Heuristic function which calculates the heuristic value
    # f(x) = h(x) + g(x)
    def f(self, start, goal):
        return  self.h(start.data, goal) + start.level
    
    # Calculate difference between the 2 inputed matrixes
    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for k in range(0, self.n):
                # if the start matrix is not same as goal matrix then increase and return temp
                if start[i][k] != goal[i][k] and start[i][k]!= "_":
                    temp += 1
        return temp

        
        



# 3 x 3 matrix for 8 puzzle
print("Welcome to the 8-Puzzle!\n\nAn initial matrix will be shuffled into the goal matrix.\n")
puzzle = Puzzle(3)
puzzle.action()