# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:30:26 2023

@author: Arslan  lecture#5 assignment 
user defined dictonary
"""

n=int(input('number of task :'))
task={}
for i in range(n):
    key=input('enetr your task: ')
    value=input('enter your finish date: ')
    task[key]=value
print(task)
