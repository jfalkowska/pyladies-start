print()
for a in range(10):
    print(' ' * (10-a) + '/' * a + '\\' * a)

print()
for a in range(10):
    print(' ' * (10-a) + '*' * a + '*' * a)

print()
for a in range(12):
    branch = ' ' * (10-a)
    if a == 0:
        branch = (' ' * (10 - a) + '^')
    elif a % 2 == 0:
        branch = (' ' * (10-a) + '/' * a + '|' + '\\' * a)
    elif a == 11:
        branch = (' ' * (a-2) + '| |')
    else:
        branch = (' ' * (10-a) + '*' * a + '*' + '*' * a)
    print(branch)