"""
Use what you've learnt about exception handling to prevent the program from crashing.

Example Input
[{'Likes': 21, 'Comments': 2}, 
{'Likes': 13, 'Comments': 2, 'Shares': 1}, 
{'Likes': 33, 'Comments': 8, 'Shares': 3}, 
{'Comments': 4, 'Shares': 2},
{'Comments': 1, 'Shares': 1}, 
{'Likes': 19, 'Comments': 3}]
Using the eval() function we can create a list of dictionaries that looks like this:

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]
Example Output
86
-------------------------------------------------------------------------------------
# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    total_likes = total_likes + post['Likes']


print(total_likes)
"""

# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    try:  
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes+= 0

print(total_likes)