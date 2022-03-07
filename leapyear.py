def utility():
    #The line below takes input
    y= int(input())
    
    isLeap=False
    
    #Your code below
    val1 = y % 4
    val3 = y % 100
    val2 = y % 400
    if( val1 == 0 and (val2 == 0 or val3 != 0)):
    #Assign True or False to isLeap
      isLeap = True
    #Your code above
    
    #The line below prints the output
    print(isLeap)
