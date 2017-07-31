def main():
	try:
		random_numbers = open('ran_numbers.txt', 'r')
		number = 0
		total = 0
		read_file(random_numbers,number,total)
	except IOError:
		print('An error occurred trying to read')
		print('the file ran_numbers.txt')
		wait=input('Press enter to exit')
def read_file(random_numbers,number,total):
	print("List of numbers:")
	for line in random_numbers.readlines():
		print(line)
		total = total+int(line)
		number +=1
	print("The total of the numbers = "+str(total))
	print("The number of the random numbers read from the file = "+str(number))
	wait=input('Press enter to exit')
main()