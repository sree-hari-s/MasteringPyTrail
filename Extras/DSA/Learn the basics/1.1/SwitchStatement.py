"""
Switch Statements
https://www.codingninjas.com/studio/problems/switch-case-statement_8357244?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""
from typing import *
from math import pi
def areaSwitchCase(ch: int, a: List[float]):
    if ch==1:
        return "%.5f" %round(pi*a[0]*a[0],5)
    else:
        return "%.5f" %round(a[0]*a[1],5)
        
print(areaSwitchCase(1,[12]))