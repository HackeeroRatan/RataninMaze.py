import os, time

puzzle = [[1, 0, 0, 1, 0, 0, 1, 0, 0],
          [1, 0, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0, 0],
          [1, 1, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 0, 1, 1, 1]]

def creaMaze(aMaze):                   ##creates two identical empty maze to work with
    for i in puzzle:
        temp = []
        for j in i:
            temp.append(0)
        aMaze.append(temp)

visited = []                           ##Creating two empty Maze here
Answer = []
creaMaze(visited)
creaMaze(Answer)

# visited = [[0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
# Answer =  [[0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0]]


def printMaze(Maze):                ##this function prints the maze
    for i in Maze:
        temp = i
        print('\n')
        for j in temp:
            print(j, end='  ')
    print('\n')

def Safe(maze, aVis, x, y):               ##checks whether the next block is accessible
    sizeX = len(maze)
    sizeY = len(maze[0])
    return((x <= sizeX - 1 and y <= sizeY -1) and maze[x][y] != 0 and (x >= 0 and y >= 0) and aVis[x][y] != 1)

def Solve(maze, Vis, ans, X, Y, moveList):                 ##MAIN RECURSIVE FUNCTION WHICH SOLVES THE PUZZLE - along with simulation
    
    time.sleep(0.5)
    os.system('clear')
    printMaze(maze)
    print(movLst, '\n')

    if Vis[-1][-1] == 1:                        ##termination condition for recursive function
        return 1
    else: 
        if Safe(maze, Vis, X+1, Y):              ## DOWN
            Vis[X+1][Y] = 1
            maze[X+1][Y] = '↓'
            moveList.append('D')
            Solve(maze, Vis, ans, X+1, Y, moveList)

        elif Safe(maze, Vis, X, Y+1):            ## RIGHT
            Vis[X][Y+1] = 1
            maze[X][Y+1] = '→'
            moveList.append('R')
            Solve(maze, Vis, ans, X, Y+1, moveList)

        elif Safe(maze, Vis, X-1, Y):            ## UP
            Vis[X-1][Y] = 1
            maze[X-1][Y] = '↑'
            moveList.append('U')
            Solve(maze, Vis, ans, X-1, Y, moveList)

        elif Safe(maze, Vis, X, Y-1):           ## LEFT
            Vis[X][Y-1] = 1
            maze[X][Y-1] = '←'
            moveList.append('L')
            Solve(maze, Vis, ans, X, Y-1, moveList)
        
        else:                              ##if no block is accessible then going back to find another route (BACKTRACKING)
            if moveList[-1] == 'D':
                maze[X][Y] = 1
                moveList.pop()
                Solve(maze, Vis, ans, X-1, Y, moveList)
            elif moveList[-1] == 'R':
                maze[X][Y] = 1
                moveList.pop()
                Solve(maze, Vis, ans, X, Y-1, moveList)
            elif moveList[-1] == 'U':
                maze[X][Y] = 1
                moveList.pop()
                Solve(maze, Vis, ans, X+1, Y, moveList)
            elif moveList[-1] == 'L':
                maze[X][Y] = 1
                moveList.pop()
                Solve(maze, Vis, ans, X, Y+1, moveList)

            else:
                print("The rat couldn't find any route and eventually died!! \n All because of you, Shame on you...!!\n")



movLst = ['S']                     #keeps a ledger of every move by the rat
os.system('clear')
printMaze(puzzle)
time.sleep(3)

visited[0][0] = 1
puzzle[0][0] = '↓'
Solve(puzzle, visited, Answer, 0, 0, movLst)




