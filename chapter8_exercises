
def counter():
        """
        Chapter 8. Question 2
        """
        start = int(raw_input("from: "))
        end = int(raw_input("to: "))
        increment = int(raw_input("increment: "))

        for i in range(start, end+1, increment):
                print i,
        print


#------------------------------------------#

def range_caller():
        """
        Chapter 8. Question 3
        """
        for i in range(1, 10, 1):
                print i,
        print

        for i in range(3, 19, 3):
                print i,
        print

        for i in range(-20, 900, 220):
                print i,
        print


#------------------------------------------#

def is_prime(number):
        """
        Chapter 8. Question 4
        returns a list of factors, along with the True, or False answer to is_prime()
        """

        factors = []
        factors.append(1)
        factors.append(number)
        
        divisor = 2
        while divisor <= number/2:
                if (number % divisor) == 0:
                        factors.append(divisor)
                        factors.append
                divisor += 1

        if len(factors) == 2:    #ie. the only factors are number and 1
                return True, factors
        else:
                return False, factors



def get_factors(number):
        """
        Chapter 8. question 5
        """

        prime, factors = is_prime(number)
        factors.sort()
        return factors

#-------------------------------------------#

def prime_factorisation(number):
        """
        Chapter 8. Question 6
        """
        index = 2

        prime_factors = []
        half_number = number/2

        while index <= half_number:
                result = number % index
                while result == 0:
                        number = number / index
                        prime_factors.append(index)
                        result = number % index

                index += 1

        return prime_factors


#------------------------------------------------#

def is_perfect(num):
        """
        Chapter 8. Question 7
        """

        factors = []
        divisor = int(num/2)

        factors.append(1)      # 1 is a factor of any non-zero number
        while divisor > 1:
                if (num % divisor) == 0:
                        factors.append(divisor)

                divisor -= 1

        total = 0
        for factor in factors:
                total += factor
                
        if total == num:
                return True
        else:
                return False
        
        

#--------------------------------------------------#

def factorial(num):
        """
        Chapter 8. Question 8
        """

        result = 1
        for i in range(1, num+1):
                result *= i

        return result


#------------------------------------------------#


def fibonacci(stop):
        """
        Chapter 8. Question 9
        """

        a = 1
        b = 1
        c = a + b
        print a, b, 
        while c <= stop:
                print c, 
                a = b
                b = c
                c = a + b

        print 


#----------------------------------------------#

import string

def isspace(char):
        if char in string.whitespace:
                return True
        else:
                return False
        

#vowels consonants and words counter
def v_c_w_counter():
        """
        Chapter 8. Question 10.
        """
        letters = string.letters[:52]
        vowels = "aeiou"
        vowels = vowels + vowels.upper()

        line = raw_input("Enter a sentence/line: ")

        words = 0   #gonna assume every pair of words is separated by a whitespace character
        vowels_count = 0
        consonants = 0

        in_word = False
        length = len(line)
        index = 0

        while index < length:
                if (line[index] in vowels):
                        vowels_count += 1
                elif line[index] in letters:   #the vowels in the string: letters, will not be counted. because vowels are counted in the if part of this if-elif statement
                        consonants += 1
                if (not in_word) and (not isspace(line[index]) ):
                        words += 1
                        in_word = True

                if isspace(line[index]):
                        in_word = False


                index += 1
        
        
        print "words: %d, vowels: %d, consonants: %d" %(words, vowels_count, consonants)
        
        
        
        

























































                






















