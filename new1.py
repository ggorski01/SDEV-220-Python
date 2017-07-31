import random

def main():

  random_numbers = open('ran_numbers.txt', 'w')
  qty_numbers = int(input('Input how many random numbers should be written to the file: '))
  create_file(qty_numbers,random_numbers)
  
def create_file(qty_numbers,random_numbers):
  for count in range (qty_numbers):
    number = random.randint(1,500)
    random_numbers.write(str(number)+ '\n')
  random_numbers.close()
main()