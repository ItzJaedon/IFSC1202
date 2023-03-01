import math
def isEven(num):
    return num % 2 == 0
def isOdd(num):
    return num % 2 != 0
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
with open('06.06 Numbers.txt', 'r') as input_file:
    with open('(06.06 Evennumbers.txt', 'w') as even_file, \
         open('06.06 Oddnumbers.txt', 'w') as odd_file, \
         open('(06.06 Primenumbers.txt', 'w') as prime_file:
        for line in input_file:
            num = int(line.strip())
            if isEven(num):
                even_file.write(str(num) + '\n')
            if isOdd(num):
                odd_file.write(str(num) + '\n')
            if isPrime(num):
                prime_file.write(str(num) + '\n')
input_file.close()
even_file.close()
odd_file.close()
prime_file.close()
with open('06.06 Numbers.txt', 'r') as input_file, \
     open('(06.06 Evennumbers.txt', 'r') as even_file, \
     open('06.06 Oddnumbers.txt', 'r') as odd_file, \
     open('(06.06 Primenumbers.txt', 'r') as prime_file:
    input_count = sum(1 for line in input_file)
    even_count = sum(1 for line in even_file)
    odd_count = sum(1 for line in odd_file)
    prime_count = sum(1 for line in prime_file)
    print(f"{even_count} even numbers")
    print(f"{odd_count} odd numbers")
    print(f"{prime_count} prime numbers")
    print(f"{input_count} numbers read")
input_file.close()
even_file.close()
odd_file.close()
prime_file.close()
