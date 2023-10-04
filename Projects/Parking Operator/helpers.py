from os import system
def clear_display():

    try: 
        system("clear")
    except:
        system("cls")