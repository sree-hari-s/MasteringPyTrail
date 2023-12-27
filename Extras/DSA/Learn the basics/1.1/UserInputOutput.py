"""
Find Character
https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""

character = input()
if character.islower():
    print("0")
elif character.isupper():
    print("1")
else:
    print("-1")