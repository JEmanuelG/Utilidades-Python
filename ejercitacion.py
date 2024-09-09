n=25

col = 0
control_col = n
print(n)

for x in range(n):
    for y in range(n):
        col += 1
        if x == y and col != control_col:
            print('X', end='')

        elif col == control_col:
             print('X', end='')
             control_col -= 1

        else:
            print('_', end='')


        if col == n:
            print('\n')
            col = 0