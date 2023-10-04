def printingData(codeName,*args, **kwargs):
    print("i am",codeName)
    for arg in args:
        print("I am ",arg)
    for keyWord in kwargs.items():
        print("i am kwarg ",keyWord)
    
printingData('007','agent',firstName='James',lastName='Bond')