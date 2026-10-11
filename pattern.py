BLACK = '\u001b[44m'
RESET = '\u001b[0m'
h = 10
w = 10

for i in range(h):
    for j in range(w):
        if (i == 0 or i == 2) and (j == 0 or j == 2):
           
            print( f'{BLACK}  {RESET}', end="")
        elif i == 1 and j == 1:
            print(f'{BLACK}  {RESET}', end="")
        else:
            print("  ", end='')
    print()
