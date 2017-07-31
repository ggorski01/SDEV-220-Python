# Program name: AverageWordCount.py
# Author: Giovanna Gorski
# Date last updated: 07/06/2017
# Purpose: The program read an input file name, thus, count the average of words per line in the file

def main():
#The user input the name of the file to be opened
                file=input('Please enter the file name to be read without its file extension(.txt): ')
#Bellow we call the method to open the file for read
                textFile= open(file+'.txt', 'r')
#Bellow are the variable countW and countL in which are counters for number of words and number of lines
                countW=0
                countL=0
#Create a list called L in which will be populate with contents from the file
                L=list()
#A loop that run through the file reading all its contents
                for line in textFile.read():
#Bellow is the statement in which append at the list L all the contents in the file
                        L.append(line)
                        if line==' ':
#Every iteration of the loop it will be check if there's a white space between the words, therefore, if yes the variable counter for Word will be incremented by one
                                countW+=1
#If a new line be found the counter for word and line will be incremented by one
                        if line=='\n':
                                countW+=1
                                countL+=1
#The average variable will calculate the average of words per line
                average=countW/countL
#The statement below will display all the results, and the average will be display with 1 decimal place
                print('\nThe file: ',file+'.txt ','has:\nNumber of words: ' ,countW,'\nNumber of lines: ',countL,'\nAverge of words per line: ',format(average,',.1f'))
#The statement below close the file.
                textFile.close()
main()
wait=input('Press enter to exit')
