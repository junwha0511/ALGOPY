N = 5

maze = [[]]

for i in range(0,N):
    temp[] = input().split(',')
    maze.append(temp)
#1 is path color
#2 is block color

def findMazePath(x, y):
    if x<0 and y<0 and x>N and y>N:
        return False
    else if maze[x][y] != 1:
        return False;
    else if x==N-1 and y==N-1:
        maze[x][y] = 1;
        return True;

    else:
        maze[x][y] = 1;
        if findMazePath(x-1,y) or findMazePath(x,y+1) or findMazePath(x+1,y) or findMazePath(x,y-1):                                                    
            return True
        
        maze[x][y] = 2;
        return False;
 
pringMaze()
findMazePath(0,0)
pringMaze()