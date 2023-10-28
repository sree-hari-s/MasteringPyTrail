def my_function():
    """
    Prints a string Hello World!
    """
    print("Hello world!")

my_function()
#------------------------------------------------------------------------------------------------
"""
** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

def domainGet(email):
    """
    Returns the domain name from the email address provided by splitting the string and returning the last element
    """
    domain = email.split('@')[-1]
    return domain

print(domainGet('user@domain.com'))

#------------------------------------------------------------------------------------------------
"""
** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**

    seq = ['soup','dog','salad','cat','great']

**should be filtered down to:**

    ['soup','salad']
"""
seq = ['soup','dog','salad','cat','great']

result = list(filter(lambda word: word.startswith('s'), seq))
print(result)