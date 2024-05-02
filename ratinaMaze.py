import os, time

puzzle = [[1, 0, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1]]

def creaMaze(aMaze):
    for i in puzzle:
        temp = []
        for j in i:
            temp.append(0)
        aMaze.append(temp)

visited = []
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
    Vis[X][Y] = 1
    ans[X][Y] = 1

    time.sleep(2)
    os.system('clear')
    printMaze(ans)
    
    if ans[-1][-1] == 1:                        ##termination condition for recursive function
        return 1
    else: 
        if Safe(maze, Vis, X+1, Y):
            # Vis[X+1][Y] = 1
            # ans[X+1][Y] = 1
            moveList.append('D')
            Solve(maze, Vis, ans, X+1, Y, moveList)

        elif Safe(maze, Vis, X, Y+1):
            # Vis[X][Y+1] = 1
            # ans[X][Y+1] = 1
            moveList.append('R')
            Solve(maze, Vis, ans, X, Y+1, moveList)

        elif Safe(maze, Vis, X-1, Y):
            # Vis[X-1][Y] = 1
            # ans[X-1][Y] = 1
            moveList.append('U')
            Solve(maze, Vis, ans, X-1, Y, moveList)

        elif Safe(maze, Vis, X, Y-1):
            # Vis[X][Y-1] = 1
            # ans[X][Y-1] = 1
            moveList.append('L')
            Solve(maze, Vis, ans, X, Y-1, moveList)
        
        else:                              ##if no block is accessible then going back to find another route (BACKTRACKING)
            if moveList.pop() == 'D':
                ans[X][Y] = 0
                Solve(maze, Vis, ans, X-1, Y, moveList)
            elif moveList.pop() == 'R':
                ans[X][Y] = 0
                Solve(maze, Vis, ans, X, Y-1, moveList)
            elif moveList.pop() == 'U':
                ans[X][Y] = 0
                Solve(maze, Vis, ans, X+1, Y, moveList)
            elif moveList.pop() == 'L':
                ans[X][Y] = 0
                Solve(maze, Vis, ans, X, Y+1, moveList)



movLst = []                     #keeps a ledger of every move by the rat

Solve(puzzle, visited, Answer, 0, 0, movLst)
print(movLst)



