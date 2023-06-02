for i in range(ord('!'), ord('~')+1):
    print(chr(i), end=' ')
    if (i - ord('!') + 1) % 10 == 0:
        print()