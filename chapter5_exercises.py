#! /usr/bin/env python

import sys
import random   

def add(num1, num2):
        """
        Chapter 5. Question 2a
        """
        a, b = coerce(num1, num2)  # this isn't necessary, Python automatically coerces numbers of different types
        return (a + b)

def product(num1, num2):
        """
        Chapter 5. Question 2b
        """
        a, b = coerce(num1, num2)
        return (a * b)

#-------------------------------------------------------------#

def test_scores(input_file_name, output_file_name):
        """
        Chapter 5. Question 3
        """
        try:
                in_file = open(input_file_name, "r")
                out_file = open(output_file_name, "w")
        except:
                print >> sys.stderr, "Error: Unable to open file."
                sys.stderr.flush()
                print sys.exc_info()
                return None

        lines = in_file.readlines()
        in_file.close()

        for line in lines:
                contents = line.split(" ")
                contents[1] = float(contents[1])
                out_file.write(contents[0]+": ")
                if contents[1] >= 90:
                        out_file.write("A\n")
                elif 80 <= contents[1] <= 89:
                        out_file.write("B\n")
                elif 70 <= contents[1] <= 79:
                        out_file.write("C\n")
                elif 60 <= contents[1] <= 69:
                        out_file.write("D\n")
                else:
                        out_file.write("F\n")

        out_file.close()

#------------------------------------------------------#


def leap_year_check(year):
        """
        Chapter 5. Question 4
        """
        if (year % 4) == 0:
                if ((year % 100) == 0) and (year % 400) != 0:
                        return False
                else:
                        return True
        else:
                return False
        
#-------------------------------------------------------#


def coins(amount):
        """
        Chapter 5. Question 5
        """
        penny = 1
        nickel = 5
        dime = 10
        quater = 25

        count = {"pennies": 0, "nickels": 0, "dimes": 0, "quaters": 0}

        amount = int(amount)        # just to make sure, amount is of type int, since integer division is required for the next part
        if (amount % quater) > 0:
                count["quaters"] = amount / quater         # this is integer division, the fractional part of the result will be discarded
                amount = amount - (count["quaters"] * quater)
                if (amount % dime) > 0:
                        count["dimes"] = amount/dime
                        amount = amount - (count["dimes"]*dime)
                        if (amount % nickel) > 0:
                                count["nickels"] = amount/nickel
                                amount = amount - (count["nickels"]*nickel)

                                count["pennies"] = amount         #these will be the pennies left after all the other denominations have been taken out
                        else:
                                count["nickels"] = amount/nickel
                else:
                        count["dimes"] = amount/dime
        else:
                count["quaters"] = amount/quater


        names = count.keys()
        retval = ""
        for name in names:
                if count[name] > 0:
                        retval = retval + name +": "+str(count[name])+" "

        return retval


#------------------------------------------------------------#

def calculator(input_str):
        """
        Chapter 5. Question 5
        Returns None on error
        """

        data = input_str.split()
        N1 = float(data[0])
        OP = data[1]
        N2 = float(data[2])

        if OP == "+":
                return (N1 + N2)
        elif OP == "-":
                return (N1 - N2)
        elif OP == "*":
                return (N1 * N2)
        elif OP == "/":
                return (N1 / N2)
        elif OP == "**":
                return pow(N1, N2)
        else:
                print >> sys.stderr, ("unrecognised operator: %s." %(OP))
                return None


#-------------------------------------------------------------#

def tax_calculator(full_price):
        """
        Chapter 5. Question 7
        Separates full price into actual price and tax. Returns a tuple: (actual_price, tax)
        """
        tax_rate = 0.14       #14%
        actual_price = full_price / (1+tax_rate)
        tax = full_price - actual_price

        return round(actual_price, 2), round(tax, 2)

#-------------------------------------------------------------#

import math

def area_and_volume(value, description):
        """
        Chapter 5. Question 8
        Returns None, on error
        """
        description_err = description      #store description in it's original form, for communication with caller, in case an error occurs
        
        description = description.lower()  # so, Square, SQUARE and square will all be recognised as 'square'. to make the description case-insensitive

        if description == "square":
                return (value ** 2)    #length * breadth
        elif description == "cube":
                return (value ** 3)    #length * breadth * height
        elif description == "circle":
                return (math.pi * (value**2))  #pi * r^2
        elif description == "sphere":
                return (  (4.0/3.0)*math.pi*(value**3) )  # 4/3*pi*r^3
        else:
                print >> sys.stderr, ("Unrecognised description: %s." %(description))
                return None


#------------------------------------------------------------#

def fahr_to_celc(fahr):
        """
        Chapter 5. Question 10 a
        """
        celcius = (fahr - 32.0)*(5.0/9.0)
        return celcius

def celc_to_fahr(celc):
        """
        Chapter 5. Question 10 b
        """
        fahrenheit = celc * (9.0/ 5.0) + 32.0
        return fahrenheit


#------------------------------------------------------------#

def evens():
        """
        Chapter 5. Question 11 a
        """
        
        i = 0
        evens = []
        
        while i <= 20:
                if (i % 2) == 0:
                        evens.append(i)
                i += 1
                
        return evens


def odds():
        """
        Chapter 5. Question 11 b
        """
        odds = []
        for i in range(21):
                if (i % 2) == 1:
                        odds.append(i)
                        
        return odds

#------------------------------------------------------------#

def check_div():
        """
        Chapter 5. Question 11d 
        """
        dividend = float( raw_input("Please enter the dividend: ") )
        divisor = float( raw_input("Please enter the divisor: ") )

        #instead of doing: (dividend % divisor) == 0; here's a different approach
        result = dividend/divisor    #floating point division
        int_result = int(result)   #fractional part of result will be discarded
        if (result - int_result) == 0.0:
                return True
        else:
                return False


#-------------------------------------------------------------#

def limits():
        """
        Chapter 5. Question 12
        """
        print "maxint: ", sys.maxint
        print "float_info: ", sys.float_info


#-------------------------------------------------------------#

def time_converter(time_period):
        """
        Chapter 5. Question 13
        time_period has to be a string in the form: hr:mn, ie. 02:34; where 00:00 was the start time
        """

        period = time_period.split(":")
        hours = int(period[0], 10)
        minutes = int(period[1], 10)
        total_minutes = minutes + (hours*60)
        return total_minutes


#--------------------------------------------------------------#
        
def account_interest(percentage):
        """
        Chapter 5. Question 14
        """
        start = 1.0
        percentage = percentage/100.0
        for i in range(365):
                start = start + (start * percentage)

        start -= 1    #minus the 1, we started with. the only thing left in start now is the effects of the increments
        start = start*100   #converting to percentage
        print ("the total percentage increase: %f" %(start))
        


#---------------------------------------------------------------#

def get_divisors(num):
        divisors = []
        div = 1
        while div <= abs(num):      #in case num is a negative number
                if (num % div) == 0:
                        divisors.append(div)
                div += 1

        return divisors


def get_multiples(num, max_multiple):
        num = abs(num)
        max_multiple = abs(max_multiple)
        multiples = []
        multiple = 0
        count = 1
        while multiple < max_multiple:
                multiple = count * num
                multiples.append(multiple)
                count += 1

        return multiples

#
#        POSSSIBLE FIX: double-check that the calculations are done right for negative numbers
#
def GCD_and_LCM(num1, num2):
        """
        Chapter 5. Question 15
        """
        LCM = 0
        GCD = 1
        GCD_found = False
        LCM_found = False
        max_multiple = abs(num1 * num2) #when looking for the LCM, this is the highest possible value you can get
        
        num1_multiples = get_multiples(num1, max_multiple)
        num2_multiples = get_multiples(num2, max_multiple)
        
        num1_divisors = get_divisors(num1)    #get_divisors returns a list of divisors
        num2_divisors = get_divisors(num2)

        num1_divisors.reverse()      #so the biggest item is at the beginning of the list
        num2_divisors.reverse()

        for item1 in num1_divisors:
                for item2 in num2_divisors:
                        if item1 == item2:
                                GCD = item1
                                GCD_found = True
                                break
                if GCD_found:
                        break


        for item1 in num1_multiples:
                for item2 in num2_multiples:
                        if item1 == item2:
                                LCM = item1
                                LCM_found = True
                                break

                        if LCM_found:
                                break

        print num1_divisors
        print num2_divisors
        print num1_multiples
        print num2_multiples
        
        print "LCM: %d, GCD: %d" %(LCM, GCD)        


#-----------------------------------------------------#

def statement():
        """
        Chapter 5. Question 16
        this function, instead of taking a fixed monthly payment, generates monthly payments randomly
        """
        report = open("Statememt.txt", "w")

        openning_balance = float( raw_input("Enter openning balance: "))
        balance = openning_balance
        records =[]
        monthly_payment = 0
        for month in range(1, 13, 1):
                monthly_payment = random.randint(0, 20) + round(random.random(), 2)       #random module was imported at the beginning of this module
                balance = balance - monthly_payment
                record = (month, monthly_payment, balance)
                records.append(record)
        

        print >> report, ("Openning balance: $%.2f\n%5s\t%6s\t%8s" %(openning_balance, "Pymnt#", "Paid", "Balance")  )

        for record in records:
                print >> report, ("%5d\t$%5.2f\t$%7.2f" % (record[0], record[1], record[2]))
        
#---------------------------------------------------------#


def randoms():
        """
        Chapter 5. Question 17
        Generates a list of size: 0<=N<=100 (list size is random), of random numbers: (0<=n<=2^32 - 1).
        Randomly selects a subset of these numbers, sorts the subset and prints it.      
        """ 
        numbers = []
        list_size = random.randint(0, 100)
        for i in range(list_size):
                rand_num = random.randint(0, 2**31 - 1) + round(random.random(), 2)
                numbers.append(rand_num)

        subset = random.sample(numbers, random.randint(0, list_size))
        subset.sort()
        print subset


#--------------------------------------------------------#














        












        











                

