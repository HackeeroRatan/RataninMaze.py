# Coded by RatanPrakash A17 ECE
# last Updated on 20/01/2022

import os, time

puzzle = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]]

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
    copyMaze = Maze
    copyMaze[0][0] = "S"
    copyMaze[-1][-1] = "E"
    draw = ""
    draw += "█" * (len(Maze[0]) + 2)                ##Here we are visualizing
    draw += '\n'                                    ##the maze by converting it
    for i in copyMaze:                              ##into a string and then 
        # temp = i                                  ##printing it
        draw += "█"
        for j in i:
            if j == 0:
                draw += "█"
            elif j == 1:
                draw += " "
            else:
                draw += str(j)
        draw += "█"
        draw += '\n'
    draw += "█" * (len(Maze[0]) + 2)
    print(draw)

def Safe(maze, aVis, x, y):               ##checks whether the next block is accessible
    sizeX = len(maze)
    sizeY = len(maze[0])
    return((x <= sizeX - 1 and y <= sizeY -1) and maze[x][y] != 0 and (x >= 0 and y >= 0) and aVis[x][y] != 1)

def Solve(maze, Vis, ans, X, Y, moveList):                 ##MAIN RECURSIVE FUNCTION WHICH SOLVES THE PUZZLE - along with simulation
    
    time.sleep(0.3)
    os.system('clear')
    printMaze(maze)
    print("The path to end is : \n", movLst, '\n')

    if Vis[-1][-1] == 1:                        ##termination condition for recursive function
        return 1
    else: 
        if Safe(maze, Vis, X+1, Y):
            Vis[X+1][Y] = 1
            maze[X+1][Y] = '↓'
            moveList.append('D')
            Solve(maze, Vis, ans, X+1, Y, moveList)

        elif Safe(maze, Vis, X, Y+1):
            Vis[X][Y+1] = 1
            maze[X][Y+1] = '→'
            moveList.append('R')
            Solve(maze, Vis, ans, X, Y+1, moveList)

        elif Safe(maze, Vis, X-1, Y):
            Vis[X-1][Y] = 1
            maze[X-1][Y] = '↑'
            moveList.append('U')
            Solve(maze, Vis, ans, X-1, Y, moveList)

        elif Safe(maze, Vis, X, Y-1):
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



movLst = ['S']                     #keeps a ledger of every move by the Micromouse
os.system('clear')
printMaze(puzzle)
time.sleep(3)

visited[0][0] = 1
puzzle[0][0] = '↓'
Solve(puzzle, visited, Answer, 0, 0, movLst)







