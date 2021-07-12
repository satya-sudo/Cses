if __name__ == '__main__':
    str = input()
    mx  = 0
    l = 0
    c = str[0]
    for i in str:
        if ( i ==  c):
            l += 1
        else:
            c = i
            mx = max(mx,l)
            l = 1    
    print(max(mx,l))        