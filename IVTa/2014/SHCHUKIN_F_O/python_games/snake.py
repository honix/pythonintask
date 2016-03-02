# Snake game
# Can you catch all apples?
#
# Fedya ivt

from sys import stdout as out
from time import sleep

size = 20 # size of game
snake_size = size // 3

# Grid building, vertical line first, then copying
# in to horizontals
grid = []
grid_vert = [0] * size
[grid.append(grid_vert[:]) for i in range(size)] # [:] makes copy of array

# Placing some apples by hands
grid[10][10] = 1
grid[15][5] = 1
grid[5][15] = 1

# Snake start position and controlls defenitions
snake = [[5, 0]]
snake_orients = dict(right=[0, 1],
                     down =[1, 0],
                     left =[0,-1],
                     up   =[-1,0])

snake_orient= snake_orients['right'] # let snake go right

# Drawing function for whole game, nothing interesting here
def draw_grid(grd):
    nm = [snake[0][0] + snake_orient[0],
        snake[0][1] + snake_orient[1]]

    # Out of bounds check
    if 0 > nm[0] or nm[0] >= size:
        nm[0] = 0 if nm[0] >= size else size
    if 0 > nm[1] or nm[1] >= size:
        nm[1] = 0 if nm[1] >= size else size
        
    snake.insert(0, nm) # move this snake

    # We cross some apple?
    if grid[nm[0]][nm[1]] == 1:
        grid[nm[0]][nm[1]] = 0
        snake_size += 1

    # Trimm our snake if it too long
    global snake_size
    if len(snake) > snake_size:
        snake.pop(len(snake)-1)
    
    mes = '\n'
    for ver in range(len(grd)):
        for hor in range(len(grd[ver])):
            for sss in snake:
                if sss == [ver, hor]:
                    t = '8'
                    break
                else:
                    t = '-'
            if grd[ver][hor] == 1:
                t = '@'

            mes += t
        mes += '\n'
    out.write('\n'*40 + 'K = ' + str(k) + mes)
    out.flush()


k = 0 # Our counter, we will use it to controll snake
# Start infinity loop
while True:
    sleep(0.7) # little pause to slowly understand things

    # Controll panel, check counter and do something
    if k == 5:
        snake_orient = snake_orients['down']
    elif k == 10:
        snake_orient = snake_orients['right']

    # ...try to catch all apples
        
    draw_grid(grid)
    
    k += 1
