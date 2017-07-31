# Program name: ggCourseInfo.py
# Author: Giovanna Gorski
# Date last updated: 07/06/2017
# Purpose: The program asks the user to input a course numbe, then displays the room number, instructor and meeting time informations

def main():
#Dictionary with room number information by course number
    roomNumber={
        'CS101':3004,
        'CS102':4501,
        'CS103':6755,
        'NT110':1244,
        'CM241':1411,
        }
#Dictionary with intructor name information by course number
    instructorName={
        'CS101':'Haynes',
        'CS102':'Alvarado',
        'CS103':'Rich',
        'NT110':'Burke',
        'CM241':'Lee',
        }
#Dictionary with meeting time information by course number
    meetingTime={
        'CS101':'8:00 a.m',
        'CS102':'9:00 a.m',
        'CS103':'10:00 a.m',
        'NT110':'11:00 a.m',
        'CM241':'1:00 p.m',
        }
#Variable that controls the while loop
    choice='y'
#The while loop will run until another letter instead of y be entered
    while choice=='y':
#Ask to the user to input the course number to be display the information about it
        key=input('Enter the course number: ')
#For loop that search in the dictionary for room numbers a number in which matches with what the user input
        for i in roomNumber:
#If the run number inputed exist then print the information
            if i==key:
                print('Room number: ',roomNumber[key])
                print('Instructor: ',instructorName[key]) 
                print('Meeting time: ',meetingTime[key])
                found=0
                break
            else:
                found=1
#The if below show a error message if the course number inputed by the user do not exist in the dictionaries
        if found==1:
            print(' No room number found for ',key)
            print(' No instructor found for ',key)
            print(' No meeting time found for ',key)
#Variable choice controls the while loop, therefore, making a infinite loop until another letter differently of y be entered
        choice=input('\n Enter y to keep going, anything else to quit: ')
    
main()
