'''
Created on 11 lis 2018

@author: ewelina
'''
def listDiff(list1, list2):
    diffrences = list(set(list1).symmetric_difference(set(list2)))
    diffrences.sort()
    return diffrences