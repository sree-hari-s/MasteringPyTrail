file = open('text_file.txt')
contents = file.read()
print(contents)
file.close()

"""
closes as soon as the task is completed
"""
with open('text_file.txt') as file:
    contents = file.read()
    print(contents)
    
"""
mode `a` appends data to the existing file keeping the previous data also
"""
with open('text_file.txt',mode="a") as file:
    file.write("\nI am currently learning Python")
    
"""
if a file does not exist python creates a new file in the same directory
with the name provided 
Only works in the write mode and when file does not exist
"""

with open('new_file.txt',mode="w") as file:
    file.write("New file created")
    
    
"""
Absolute File Path
It is always relative to the root of your computer
And 
Relative File Path
Is to your current working directory,so it depends on where you are currently.
"""