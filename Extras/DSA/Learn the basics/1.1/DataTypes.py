"""
Data Type
https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""

import sys

def dataTypes(type: str):
    if type == 'Integer':
        return 4
    elif type == 'Long':
        return 8
    elif type == 'Float':
        return 4
    elif type == 'Double':
        return 8
    elif type == 'Character':
        return 1
    else:
        return -1


print(dataTypes("Integer"))