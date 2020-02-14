## Purpose of the project
This project will provide you a step-by-step guide to create a Python program to
 import pandas library and read an existing csv file, calculate the mean of a column and also, save a new csv file



## Task 1: Import pandas library as pd
The library exists in the system after running pip3 install requirements.txt

## Task 2:
There is a csv in the data folder called winequality-red.csv.
The purpose of this task is to correctly read this file into a dataframe variable called wine using the pandas function read_csv()
Since the header is the first row, in the function, set the header parameter to 0, header=0.

## Task 3: Inspect Dataframe
Find the dimensions of the dataframe using the shape property of the wine dataframe. The shape should be (1599, 12)

## Task 4: Get all rows of the chloride column
Using the loc function, select all rows and the specific chlorides column. Assign the newly sliced data to the variable chlorides

## Task 5: Get mean of a specific column of the wine dataframe
Select the chlorides column and get the mean. Use the mean function for dataframe columns. Assign value to chloride_mean.
General example df.column_name.mean()

## Task 6: Save dataframe to file as csv
For the last task, save the data created in task 4 as a new csv file. use the dataframe.to_csv function. Ensure the new csv is in the data folder.dataframe
The name of the new csv should be chlorides.csv