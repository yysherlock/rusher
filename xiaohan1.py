cnt = 1
found = False
while not found:
    if cnt % 2 == 1 and cnt % 3==0 and cnt % 4 == 1 \
            and cnt % 5 == 4 and cnt % 6 == 3 and cnt % 7 == 0 and cnt % 8 == 1 \
            and cnt % 9 == 0:
                found = True
                print cnt
    else:
        cnt += 1
