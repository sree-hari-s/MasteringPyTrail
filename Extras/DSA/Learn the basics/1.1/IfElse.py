"""
if-else (Decision Making)
https://www.codingninjas.com/studio/problems/if-else-decision-making_8357235?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
"""

def compareIfElse(a: int, b: int):
    if a>b:
        return "greater"
    elif b>a:
        return "smaller"
    else:
        return "equal"
    
print(compareIfElse(3,3))