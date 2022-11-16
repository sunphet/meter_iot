def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    
    print("ผลบวก = ", total)

addition(5, 1000, 20)    