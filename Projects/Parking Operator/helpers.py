import os 
import platform

def clear_display() -> None:
    """Helps clear the previous text on the command line."""
    
    if platform.system() == 'Darwin': # Checks operating system
        os.system("clear") # Runs clear command appropriate for Mac
        return 

    os.system("cls") # Runs clear command appropriate for Windows
