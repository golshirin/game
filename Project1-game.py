print('Welcome to the game.\nPlease use w, s, a, d keys for up, down, left and right .\nPlease be careful of the two crocodiles in your path.\n')
t0 = '••'
t1 = '  '
t2 = '  '
t3 = '  '
t4 = '  '
t5 = '  '
t6 = '  '
t7 = '  '
t8 = '  '
t9 = '  '
t10 = '  '
t11 = '  '
t12 = '  '
t13 = '  '
t14 = '  '
t15 = ' -> '
global x 
global y 
x = 0
y = 0
Dummy = [0,0]
Table_1 = [[0, 0, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[1, 0, 0, 3]]
Table_2 = [[0, 0, 0, 0],[0, 0, 0, 1],[0, 0, 0, 0],[0, 0, 1, 3]]
def direction(n):
    global x
    global y
    if n == 'd'and y < 3:
        y += 1
    elif n == 's'and x < 3:
        x += 1
    elif n == 'w'and x > 0:
        x -= 1
    elif n == 'a'and y > 0:
        y -= 1
    else:
        print('There is no way')
    return([x,y])   
print("Please press enter to start the game: ", end =  ' ')
key = str(input())
print("%s  %s  %s  %s " %(t0,t1,t2,t3))
print("%s  %s  %s  %s " %(t4,t5,t6,t7))
print("%s  %s  %s  %s " %(t8,t9,t10,t11))
print("%s  %s  %s  %s " %(t12,t13,t14,t15))
while key != ' ':
    key = str(input())
    if key =='w' or key =='s' or key =='d' or key =='a':
        Dummy = direction(key)       
        if Table_1[x][y] == 1:
            if x == 3 and y == 0 :
                t12 = '@_@'
                t0 = '••'
                t1 = '  '
                t3 = '  '
                t4 = '  '
                t5 = '  '
                t6 = '  '
                t7 = '  '
                t8 = '  '
                t9 = '  '
                t10 = '  '
                t11 = '  '
                t2 = '  '
                t13 = '  '
                t14 = '  '
                t15 = ' -> '
            if x == 0 and y == 2:
                t2 = '@_@'
                t0 = '••'
                t1 = '  '
                t3 = '  '
                t4 = '  '
                t5 = '  '
                t6 = '  '
                t7 = '  '
                t8 = '  '
                t9 = '  '
                t10 = '  '
                t11 = '  '
                t12 = '  '
                t13 = '  '
                t14 = '  '
                t15 = ' -> '
            Dummy = [0,0]
            x = 0
            y = 0
            print('Unfortunately,you were eaten by a crocodile and returned to the first house!')
        elif Table_1[x][y] == 3:
            print("••  ••   @_@  ••")
            print("••  ••  ••  ••")
            print("••  ••  ••  ••")
            print("@_@   ••  ••  ••")
            Dummy = [0,0]
            x = 0
            y = 0
            print('Congratulations, you have successfully completed the first step.\nNew game started, move again: ')
            t0 = '••'
            t1 = '  '
            t2 = '  '
            t3 = '  '
            t4 = '  '
            t5 = '  '
            t6 = '  '
            t7 = '  '
            t8 = '  '
            t9 = '  '
            t10 = '  '
            t11 = '  '
            t12 = '  '
            t13 = '  '
            t14 = '  '
            t15 = ' -> '
            print("%s  %s  %s  %s" %(t0,t1,t2,t3))
            print("%s  %s  %s  %s" %(t4,t5,t6,t7))
            print("%s  %s  %s  %s" %(t8,t9,t10,t11))
            print("%s  %s  %s  %s" %(t12,t13,t14,t15))
            while key != ' ':
                key_2 = str(input())
                if key_2 =='w' or key_2 =='s' or key_2 =='d' or key_2 =='a':
                    Dummy = direction(key_2)
                    if Table_2[x][y] == 1:
                        if x == 3 and y == 2 :
                            t14 = '@_@'
                            t0 = '••'
                            t1 = '  '
                            t3 = '  '
                            t4 = '  '
                            t5 = '  '
                            t6 = '  '
                            t7 = '  '
                            t8 = '  '
                            t9 = '  '
                            t10 = '  '
                            t11 = '  '
                            t12 = '  '
                            t13 = '  '
                            t2 = '  '
                            t15 = ' -> '
                        if x == 1 and y == 3:
                            t7 = '@_@'
                            t0 = '••'
                            t1 = '  '
                            t3 = '  '
                            t4 = '  '
                            t5 = '  '
                            t6 = '  '
                            t2 = '  '
                            t8 = '  '
                            t9 = '  '
                            t10 = '  '
                            t11 = '  '
                            t12 = '  '
                            t13 = '  '
                            t14 = '  '
                            t15 = ' -> '
                        Dummy = [0,0]
                        x = 0
                        y = 0
                        print('Unfortunately,you were eaten by a crocodile and returned to the first house!')
                    elif Table_2[x][y] == 3:
                        print("••  ••  ••  ••")
                        print("••  ••  ••  @_@")
                        print("••  ••  ••  ••")
                        print("••  ••  @_@   ••")  
                        Dummy = [0,0]
                        x = 0
                        y = 0
                        print('Congratulations, you win ')
                        t0 = '••'
                        t1 = '  '
                        t2 = '  '
                        t3 = '  '
                        t4 = '  '
                        t5 = '  '
                        t6 = '  '
                        t7 = '  '
                        t8 = '  '
                        t9 = '  '
                        t10 = '  '
                        t11 = '  '
                        t12 = '  '
                        t13 = '  '
                        t14 = '  '
                        t15 = ' -> '
                        break
                    else:
                        print('continue: ')
                    if x == 0 and y == 1:
                        t1 = '••'
                    if x == 0 and y == 2:
                        t2 = '••'
                    if x == 0 and y == 3:
                        t3 = '••'
                    if x == 1 and y == 0:
                        t4 = '••'
                    if x == 1 and y == 1:
                        t5 = '••'
                    if x == 1 and y == 2:
                        t6 = '••'
                    if x == 2 and y == 0:
                        t8 = '••'
                    if x == 2 and y == 1:
                        t9 = '••'
                    if x == 2 and y == 2:
                        t10 = '••'
                    if x == 2 and y == 3:
                        t11 = '••'
                    if x == 3 and y == 0:
                        t12 = '••'
                    if x == 3 and y == 1:
                        t13 = '••'                    
                    print("%s  %s  %s  %s" %(t0,t1,t2,t3))
                    print("%s  %s  %s  %s" %(t4,t5,t6,t7))
                    print("%s  %s  %s  %s" %(t8,t9,t10,t11))
                    print("%s  %s  %s  %s" %(t12,t13,t14,t15))
                else:
                    print('Please use w, s, d and a keys.') 
        else:
            print('continue: ') 
        if x == 0 and y == 1:
            t1 = '••'        
        if x == 0 and y == 3:
            t3 = '••'
        if x == 1 and y == 0:
            t4 = '••'
        if x == 1 and y == 1:
            t5 = '••'
        if x == 1 and y == 2:
            t6 = '••'
        if x == 1 and y == 3:
            t7 = '••'
        if x == 2 and y == 0:
            t8 = '••'
        if x == 2 and y == 1:
            t9 = '••'
        if x == 2 and y == 2:
            t10 = '••'
        if x == 2 and y == 3:
            t11 = '••'        
        if x == 3 and y == 1:
            t13 = '••'
        if x == 3 and y == 2:
            t14 = '••'        
        print("%s  %s  %s  %s" %(t0,t1,t2,t3))
        print("%s  %s  %s  %s" %(t4,t5,t6,t7))
        print("%s  %s  %s  %s" %(t8,t9,t10,t11))
        print("%s  %s  %s  %s" %(t12,t13,t14,t15))
    else:
        print('Please use w, s, d and a keys.')    

