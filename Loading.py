# Loading with dot (Loading.....)
for y in range(5):
    for x in range (6):
        b = "Loading" + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    b = "Loading     "
    print(b, end="\r")
    
#Another loading 
for y in range(5):
    for x in range (0,3):
        b = "Loading(\\)"
        print (b, end="\r")
        time.sleep(0.2)
        b = "Loading(|)"
        print (b, end="\r")
        time.sleep(0.2)
        b = "Loading(/)"
        print (b, end="\r")
        time.sleep(0.2)
        b = "Loading(-)"
        print (b, end="\r")
        time.sleep(0.2)
        b = "Loading(\)"
        print (b, end="\r")

    b = "Loading   "
    print(b, end="\r")
