import os, time, turtle


puzzle = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]


T = turtle.Turtle()
T.width(10)
T.forward(100)



# def creaMaze(aMaze):                   ##creates two identical empty maze to work with
#     for i in puzzle:
#         temp = []
#         for j in i:
#             temp.append(0)
#         aMaze.append(temp)

# def printMaze(Maze, draw):                ##this function prints the maze
#     copyMaze = Maze
#     copyMaze[0][0] = "S"
#     copyMaze[-1][-1] = "E"
#     draw = ""
#     draw += "█" * (len(Maze[0]) + 2)                ##Here we are visualizing
#     draw += '\n'                                    ##the maze by converting it
#     for i in copyMaze:                              ##into a string and then 
#         # temp = i                                  ##printing it
#         draw += "█"
#         for j in i:
#             if j == 0:
#                 draw += "█"
#             elif j == 1:
#                 draw += " "
#             else:
#                 draw += str(j)
#         draw += "█"
#         draw += '\n'
#     draw += "█" * (len(Maze[0]) + 2)
#     print(draw)

# def Safe(maze, aVis, x, y):               ##checks whether the next block is accessible
#     sizeX = len(maze)
#     sizeY = len(maze[0])
#     return((x <= sizeX - 1 and y <= sizeY -1) and maze[x][y] != 0 and (x >= 0 and y >= 0) and aVis[x][y] != 1)

# def Solve1(maze, Vis, ans, X, Y, moveList, path):                 ##MAIN RECURSIVE FUNCTION WHICH SOLVES THE PUZZLE - along with simulatio, path, path)
    
#     time.sleep(0.1)
#     os.system('clear')
#     printMaze(maze, path)
#     print(movLst1, '\n')

#     if Vis[-1][-1] == 1:                        ##termination condition for recursive function
#         return 1
#     else: 
#         if Safe(maze, Vis, X+1, Y):
#             Vis[X+1][Y] = 1
#             maze[X+1][Y] = '↓'
#             moveList.append('D')
#             Solve1(maze, Vis, ans, X+1, Y, moveList, path)

#         elif Safe(maze, Vis, X, Y+1):
#             Vis[X][Y+1] = 1
#             maze[X][Y+1] = '→'
#             moveList.append('R')
#             Solve1(maze, Vis, ans, X, Y+1, moveList, path)

#         elif Safe(maze, Vis, X-1, Y):
#             Vis[X-1][Y] = 1
#             maze[X-1][Y] = '↑'
#             moveList.append('U')
#             Solve1(maze, Vis, ans, X-1, Y, moveList, path)

#         elif Safe(maze, Vis, X, Y-1):
#             Vis[X][Y-1] = 1
#             maze[X][Y-1] = '←'
#             moveList.append('L')
#             Solve1(maze, Vis, ans, X, Y-1, moveList, path)
        
#         else:                              ##if no block is accessible then going back to find another route (BACKTRACKING)
#             if moveList[-1] == 'D':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve1(maze, Vis, ans, X-1, Y, moveList, path)
#             elif moveList[-1] == 'R':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve1(maze, Vis, ans, X, Y-1, moveList, path)
#             elif moveList[-1] == 'U':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve1(maze, Vis, ans, X+1, Y, moveList, path)
#             elif moveList[-1] == 'L':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve1(maze, Vis, ans, X, Y+1, moveList, path)

#             else:
#                 print("The rat couldn't find any route and eventually died!! \n All because of you, Shame on you...!!\n")

# def Solve2(maze, Vis, ans, X, Y, moveList, path):                 ##MAIN RECURSIVE FUNCTION WHICH SOLVES THE PUZZLE - along with simulatio, path)
    
#     time.sleep(0.1)
#     os.system('clear')
#     printMaze(maze, path)
#     print(movLst2, '\n')

#     if Vis[-1][-1] == 1:                        ##termination condition for recursive function
#         return 1
#     else: 
#         if Safe(maze, Vis, X-1, Y):
#             Vis[X-1][Y] = 1
#             maze[X-1][Y] = '↑'
#             moveList.append('U')
#             Solve2(maze, Vis, ans, X-1, Y, moveList, path)


#         elif Safe(maze, Vis, X, Y+1):
#             Vis[X][Y+1] = 1
#             maze[X][Y+1] = '→'
#             moveList.append('R')
#             Solve2(maze, Vis, ans, X, Y+1, moveList, path)


#         elif Safe(maze, Vis, X, Y-1):
#             Vis[X][Y-1] = 1
#             maze[X][Y-1] = '←'
#             moveList.append('L')
#             Solve2(maze, Vis, ans, X, Y-1, moveList, path)

#         elif Safe(maze, Vis, X+1, Y):
#             Vis[X+1][Y] = 1
#             maze[X+1][Y] = '↓'
#             moveList.append('D')
#             Solve2(maze, Vis, ans, X+1, Y, moveList, path)
        
#         else:                              ##if no block is accessible then going back to find another route (BACKTRACKING)
#             if moveList[-1] == 'D':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve2(maze, Vis, ans, X-1, Y, moveList, path)
#             elif moveList[-1] == 'R':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve2(maze, Vis, ans, X, Y-1, moveList, path)
#             elif moveList[-1] == 'U':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve2(maze, Vis, ans, X+1, Y, moveList, path)
#             elif moveList[-1] == 'L':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve2(maze, Vis, ans, X, Y+1, moveList, path)

#             else:
#                 print("The rat couldn't find any route and eventually died!! \n All because of you, Shame on you...!!\n")

# def Solve3(maze, Vis, ans, X, Y, moveList, path):                 ##MAIN RECURSIVE FUNCTION WHICH SOLVES THE PUZZLE - along with simulation
    
#     time.sleep(0.1)
#     os.system('clear')
#     printMaze(maze, path)
#     print(movLst3, '\n')

#     if Vis[-1][-1] == 1:                        ##termination condition for recursive function
#         return 1
#     else: 
#         if Safe(maze, Vis, X+1, Y):
#             Vis[X+1][Y] = 1
#             maze[X+1][Y] = '↓'
#             moveList.append('D')
#             Solve3(maze, Vis, ans, X+1, Y, moveList, path)

#         elif Safe(maze, Vis, X, Y-1):
#             Vis[X][Y-1] = 1
#             maze[X][Y-1] = '←'
#             moveList.append('L')
#             Solve3(maze, Vis, ans, X, Y-1, moveList, path)
        
#         elif Safe(maze, Vis, X, Y+1):
#             Vis[X][Y+1] = 1
#             maze[X][Y+1] = '→'
#             moveList.append('R')
#             Solve3(maze, Vis, ans, X, Y+1, moveList, path)

#         elif Safe(maze, Vis, X-1, Y):
#             Vis[X-1][Y] = 1
#             maze[X-1][Y] = '↑'
#             moveList.append('U')
#             Solve3(maze, Vis, ans, X-1, Y, moveList, path)

#         else:                              ##if no block is accessible then going back to find another route (BACKTRACKING)
#             if moveList[-1] == 'D':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve3(maze, Vis, ans, X-1, Y, moveList, path)
#             elif moveList[-1] == 'R':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve3(maze, Vis, ans, X, Y-1, moveList, path)
#             elif moveList[-1] == 'U':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve3(maze, Vis, ans, X+1, Y, moveList, path)
#             elif moveList[-1] == 'L':
#                 maze[X][Y] = 1
#                 moveList.pop()
#                 Solve3(maze, Vis, ans, X, Y+1, moveList, path)

#             else:
#                 print("The rat couldn't find any route and eventually died!! \n All because of you, Shame on you...!!\n")



# draw1 = ""
# visited1 = []                           ##Creating two empty Maze here
# Answer1 = []
# creaMaze(visited1)
# creaMaze(Answer1)
# visited1[0][0] = 1
# movLst1 = ['S']
# puzzle1 = puzzle                     #keeps a ledger of every move by the rat
# Solve1(puzzle1, visited1, Answer1, 0, 0, movLst1, draw1)

# draw2 = ""
# visited2 = []                           ##Creating two empty Maze here
# Answer2 = []
# creaMaze(visited2)
# creaMaze(Answer2)
# visited2[0][0] = 1
# movLst2 = ['S']                     #keeps a ledger of every move by the rat
# puzzle2 = puzzle                     #keeps a ledger of every move by the rat
# Solve2(puzzle2, visited2, Answer2, 0, 0, movLst2, draw2)

# draw3 = ""
# visited3 = []                           ##Creating two empty Maze here
# Answer3 = []
# creaMaze(visited3)
# creaMaze(Answer3)
# visited3[0][0] = 1
# movLst3 = ['S']                     #keeps a ledger of every move by the rat
# puzzle3 = puzzle                     #keeps a ledger of every move by the rat
# Solve3(puzzle3, visited3, Answer3, 0, 0, movLst3, draw3)
# # time.sleep(2)
# os.system('clear')
# printMaze(puzzle, draw1)
# time.sleep(3)

# puzzle[0][0] = '↓'
# print("Shortest path is:", min(movLst1, movLst2, movLst3))



# print(ord('█'))
# movLst4 = ['S']                     #keeps a ledger of every move by the rat
# Solve(puzzle, visited, Answer, 0, 0, movLst4)
# movLst5 = ['S']                     #keeps a ledger of every move by the rat
# Solve(puzzle, visited, Answer, 0, 0, movLst5)
