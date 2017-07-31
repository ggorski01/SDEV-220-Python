# Program name: ggFileAnalysis.py
# Author: Giovanna Gorski
# Date last updated: 07/06/2017
# Purpose: The program read an input file name, thus, count the average of words per line in the file

def main():
#Open the file textFile1 and textFile2
    openFile1= open('textFile1.txt','r')
    openFile2= open('textFile2.txt','r')
#Lists in which will receive the read contents from the files
    L1=list()
    L2=list()

#Loops that read the contents and append to the Lists
    for line in openFile1.readlines():
        line=line.rstrip('\n')
        L1.append(line)

    
    for line in openFile2.readlines():
        line=line.rstrip('\n')
        L2.append(line)

#Copy the list to sets
    set1 = set(L1)
    set2 = set(L2)

#Display the contents of each set separate
    print('Words in first file: ',set1)
    print('Words in second file: ',set2)
#Display unique words in both files    
    setResult = set1.union(set2)
    print('Unique words: ',setResult)
#Display words that exist in both files  
    setResult = set1.intersection(set2)
    print('Words in both files: ',setResult)
#Display the words from the file 1 in which are not found in the file 2   
    setResult = set1.difference(set2)
    print('Words in first file, not second: ',setResult)
#Display the words from the file 2 in which are not found in the file 1    
    setResult = set2.difference(set1)
    print('Words in second file, not in first: ',setResult)
#Display the words that are found in one file but not in both
    setResult = set2.symmetric_difference(set1)
    print('Words in only one file, not both: ',setResult)
    
#closes the file
    openFile1.close()
    openFile2.close()
main()
wait=input('\nPress enter to exit...')
