# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 00:23:51 2023

@author: abcd
"""

#array assignment

task_list=[]
task1=input("enter your task1 :")
task_list.insert(0, task1)
task2=input("enter your task2 :")
task_list.insert(1, task2)
task3=input("enter your task3 :")
task_list.insert(2, task3)
task4=input("enter your task 4 :")
task_list.insert(3, task4)
task_complete=task_list.pop(2)
print(task_list)
print(task_complete)