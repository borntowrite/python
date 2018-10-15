
def paint(screen, color, x, y):
    if screen[y][x] != 'black':
        return False
    return paint_helper(screen, color, x, y)
def paint_helper(screen, color, x, y):
    if x < 0 or x > (len(screen[0])-1) or y < 0 or y > (len(screen)-1):
        return False
    if screen[y][x] == 'black':
        screen[y][x] = color
        paint_helper(screen, color, x-1, y)
        paint_helper(screen, color, x+1, y)
        paint_helper(screen, color, x, y-1)
        paint_helper(screen, color, x, y+1)
    return screen

screen = [['black', 'black', 'black', 'black', 'black'],
          ['black', 'red', 'black', 'black', 'red'],
          ['red', 'black', 'black', 'black', 'black'],
          ['black', 'black', 'black', 'red', 'black'],
          ['black', 'red', 'black', 'black', 'black']]

print(paint(screen, 'white', 2, 3))
print(paint(screen, 'white', 1, 1))