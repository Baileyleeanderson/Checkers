x = "*"
y = ' '
# temp = ''

for i in range(8):
    cool = ('{0}{1}{0}{1}{0}{1}{0}{1}').format(x,y)
    temp = x
    x = y
    y = temp
    print cool

    

    
    
    
