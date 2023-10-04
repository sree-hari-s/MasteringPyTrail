def my_function():
    return 3*2

output = my_function()
print(output)

def format_name(first_name, last_name):
    """
    Taking a first name and a last name and format to title case version of the name
    """
    #full_name = (first_name[0].upper()+first_name[1:].lower() ) +' '+ (last_name[0].upper()+last_name[1:].lower())
    full_name = (first_name+' '+last_name).title()
    return full_name

# doc string 
new_name = format_name('sreeHari','sR')    
print(new_name)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)



#Print Vs Return
"""
usage of return is to use the output of one function to be utilized in another 
"""