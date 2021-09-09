
import keyword
import string
import sys
import random

def id_check():
        """
        Chapter 6. Question 2
        """

        letters = string.letters + "_"
        digits = string.digits

        inp = raw_input("Enter an identifier name: ")
        if inp in keyword.kwlist:
                print "Invalid identifier: %s is a python keyword." %(inp)
                return None

        if (inp[0] not in letters) and (inp[0] not in letters.upper() ):
                print "Invalid keyword: %s, does not begin with an alphabetic character or an underscore." %(inp)
                return None
        
        if len(inp) == 1:
                print "%s is a valid pyhton identifier." %(inp)
                return None

        for other_char in inp[1:]:
                if (other_char not in letters) and (other_char not in letters.upper()) and (other_char not in digits):
                        print "Invalid keyword: the character: %s, is not permitted in a python identifier." %(other_char)
                        return None

        else:
                print "%s, is a valid python identifier." %(inp)




#----------------------------------------------------------------#
def swap(lst, index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]


def quick_sort(lst, low, hi):
        if (low >= hi):
                return
               
        middle_index = int(((hi - low)/2 )+low)    
        pivot = lst[middle_index]
        swap(lst, low, middle_index)
        pivot_index = low
        
        list_index = low+1
        
        while list_index <= hi:
                print lst
                if lst[list_index] < pivot:
                        swap(lst, pivot_index + 1, list_index)
                        swap(lst, pivot_index, pivot_index + 1)
                        pivot_index += 1
                        
                list_index += 1
        
        quick_sort(lst, low, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, hi)


def list_sort(arg):
        """
        Chapter 6. Question  3
        """
        quick_sort(arg, 0, len(arg)-1) # This is done, so the user of list_sort doesn't have to supply the numbers hi and low.
                                       # They can just call list_sort(arg) 

        arg.reverse()                   #because the list has to be sorted in descending order


#--------------------------------------------------------------------#

def test_scores():
        """
        chapter 6. Question 4 
        """
        scores = []
        grades = []
        print "Enter student names and test scores. Enter the word, done, to signal the end of the input."

        count = 1
        while True:
                student_name = ""
                student_grade = 0.0
                student_name = (raw_input("Enter student name (enter 'done', to quit): "))
                if student_name.lower() == "done":
                        break
                else:
                        student_grade = float( raw_input("Enter student grade: "))
                        scores.append( [student_name, student_grade] )    #scores is a list that contains lists of the form [student_name, student_grade]

        
        for record in scores:
                if record[1] >= 90:
                        record[1] = "A"
                elif record[1] >= 80:
                        record[1] = "B"
                elif record[1] >= 70:
                        record[1] = "C"
                elif record[1] >= 60:
                        record[1] = "D"
                else:
                        record[1] = "F"
                grades.append(record)

        for record in grades:
                print record[0], ":", record[1]

#----------------------------------------------------------------------#                

def display_string_characters(arg):
        """
        Chapter 6. Question 5a
        """

        index = 0
        length = len(arg)

        while index < length:
                print arg[index],
                index += 1

        index = length-1     # index of the last item in the string

        while index >= 0:
                print arg[index],
                index -= 1


def string_match(str1, str2):
        """
        Chapter 6. Question 5b
        """

        if len(str1) != len(str2):
                print "The two strings are not identical"
                return False

        length = len(str1)
        index = 0

        while index < length:
                if str1[index].lower() != str2[index].lower():
                        print "The two strings are not identical"
                        return False        #Don't just break out of the loop, exit the function.
                index += 1
        
        else:
                print "The two strings are identical"
                return True


def reverse_string(input_string):
        ret_val = ""
        for char in input_string:
                ret_val = char + ret_val

        return ret_val


def check_palindrome(input_string):
        """
        Chapter 6. Question c
        """

        length = len(input_string)

        first_half = input_string[: int(length/2)]
        if (length % 2) == 0:
                second_half = input_string[int(length/2):]
        else:
                second_half = input_string[int(length/2) + 1 :]  #we're excluding the character in the middle of the string.

        second_half = reverse_string(second_half)

        if string_match(first_half, second_half):    # string_match() is  Chapter 6. Question 5b's answer
                print "The string %s, is a palindrome." %(input_string)
        else:
                print "The string %s is not a palindrome." %(input_string)

        

def create_palindrome(input_string):
        """
        Chapter 6. Question 5d
        """

        addition = reverse_string(input_string)
        return input_string+addition


#---------------------------------------------------------------------#


def lr_strip(input_string):
        """
        Chapter 6. Question 6.
        """

        l_index = 0
        r_index = len(input_string) - 1

        left_done = False
        right_done = False

        while True:
                if not left_done:
                        if not input_string[l_index].isspace():
                                left_done = True
                        else:
                                l_index += 1
                if not right_done:
                        if not input_string[r_index].isspace():
                                right_done = True
                        else:
                                r_index -= 1
                if left_done and right_done:
                        break

        #both r_index and l_index now point to the first character that isn't a whitespace character, from the right and left respectively.
        return input_string[l_index:r_index + 1]


#---------------------------------------------------------------#

def factors():
        """
        Chapter 6. Question 7
        """
        user_number = int( raw_input("Enter a number: ") )
        fac_list = range(1, user_number + 1)
        factors = []
        print "Before: \n", fac_list

        i = 0
        length = len(fac_list)

        while i < length:
                if (user_number % fac_list[i]) == 0:
                        factors.append(fac_list[i])
                i += 1

        print "After: \n", factors

        
#---------------------------------------------------------------#

def english_translation(number):
        """
        Chapter 6. Question 8
        """
        
        units     = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        tens      = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        hundreds  = []
        thousands = ["one thousand"]

        teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seveteen", "eighteen", "nineteen"]
        teens_numbers = []

        for i in range(11, 20, 1):
                teens_numbers.append(i)

        for i in units[1:]:
                hundreds.append(i+" "+"hundred")


        if number in teens_numbers:
                index = teens_numbers.index(number)
                return teens[index]

        val_holder = 0
        i = 10
        ret_val = ""
        while number > 0:
                val_holder = (number % i)                           
                number -= val_holder
                if i == 10:
                        ret_val = units[val_holder]
                elif i == 100:
                        val_holder = val_holder/10      #so we can use val_holder as an index into the tens list
                        ret_val = tens[val_holder - 1] +"-"+ ret_val
                elif i == 1000:
                        val_holder = val_holder/100
                        ret_val = hundreds[val_holder - 1] + "-" + ret_val
                elif i == 10000:
                        ret_val = thousands[0]+"-"+ret_val
                        
                i *= 10

        return ret_val


#--------------------------------------------------------------------------#

def minutes_to_hours_converter(minutes):
        """
        Chapter 6. Question 9
        """

        minutes_remaining = minutes % 60
        minutes = minutes - minutes_remaining
        hours = minutes / 60

        print "%d:%d" %(hours, minutes_remaining)


#-------------------------------------------------------------------------#

def case_invert(arg):
        """
        Chapter 6. Question 10
        """

        ret_val = ""
        for char in arg:
                if ord("A") <= ord(char) <= ord("Z"):
                        ret_val += chr(ord(char) + (ord("a") - ord("A")))
                elif ord("a") <= ord(char) <= ord("z"):
                        ret_val += chr( ord(char) - ( ord("a") - ord("A") ) )
                else:
                        ret_val += char

        return ret_val


#------------------------------------------------------------------------#

def int_to_ip(num):
        """
        Chapter 6. Question 11a
        """

        num = long(num)
        if not ( 100000000000L <= num <= 999999999999L ):
                print >> sys.stderr, "The number supplied is out of the acceptable range." 
                return None

        ret_val = ""

        while num > 0:
                val_holder = (num % 1000)
                num -= val_holder
                num /= 1000
                ret_val = "." + str(val_holder) + ret_val

        ret_val = ret_val[1:]
        return ret_val



def ip_to_int(ip):
        """
        Chapter 6. Question 11b
        """

        ret_val = 0
        i = 0
        multiplier = 1
        while i <= 3:
                print ip[:-4]
                ret_val = ret_val + (multiplier * int( ip[-3:]))  
                ip = ip[:-4]
                multiplier *= 1000
                i += 1

        return ret_val
        

#------------------------------------------------------------------------#


def check_match(string1, string2):
        print string1, string2
        if len(string1) != len(string2):
                return False
        
        length = len(string1)

        i = 0
        while i < length:
                if string1[i] != string2[i]:
                        return False
                i += 1

        else:
                return True

        

def findchar(string, char ):
        """
        Chapter 6. Question 12a
        """

        length = len(string)
        i = 0
        search_string_length = len(char)

        while i < length:
                if string[i] == char[0]:
                        if check_match(string[i: i+search_string_length], char):
                                return i

                i += 1

        return -1     #no match found


def subchar(string, origchar, newchar):
        """
        Chapter 6. Question 12c
        """

        index = findchar(string, origchar)
        if index == -1:
                return None

        origchar_length = len(origchar)

        while index != -1:
                string = string[:index] + newchar + string[ (index + origchar_length): ]
                index = findchar(string, origchar)
                
        return string


#----------------------------------------------------------------------#

def atoc(string):
        """
        Chapter 6. Question 13
        """

        i = 0
        operators = ["+", "-"]
        length = len(string)
        
        #The + or - operator that is between 2 digits, is the operator that separates the real and imaginary parts of the complex number
        while i < length:
                if string[i] in operators:
                        if string[i-1].isdigit() and string[i+1].isdigit():
                                real = float(string[:i])
                                img = float(   (string[i:])[:-1]   )    #the [:-1] in this line is to exclude the trailing j, in the img part of the number
                                return complex(real, img)
        
                i += 1



#----------------------------------------------------------------------#


def rock_paper_scissors():
        """
        Chapter 6. Question 14
        """

        user_choice = raw_input("Choose: rock, paper or scissors: ")

        options = ["rock", "scissors", "paper"]

        computer_choice = random.choice(options)
        user_number = options.index(user_choice)

        if user_choice == "rock":
                if computer_choice == "scissors":
                        print "user wins"
                elif computer_choice == "paper":
                        print "computer wins"
                else:
                        print "user and computer tie"
        elif user_choice == "paper":
                if computer_choice == "rock":
                        print "user wins"
                elif computer_choice == "scissors":
                        print "computer wins"
                else:
                        print "user and computer tie"
        elif user_choice == "scissors":
                if computer_choice == "rock":
                        print "computer wins"
                elif computer_choice == "paper":
                        print "user wins"
                else:
                        print "user and computer tie"

        print "user: %s, computer:  %s" %(user_choice, computer_choice)
       
                                
#------------------------------------------------------------------------# 


def is_leap_year(year):
        if (year%4) == 0:
                if (year % 100)==0 and (year % 400)!=0:
                        return False
                else:
                        return True
        else:
                return False



def dates(start_date, end_date):
        """
        Chapter 6. Question 15
        """
        #date format: DD/MM/YYYY

        non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_year     = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        s_day   = int(start_date[0:2])
        s_month = int(start_date[3:5])
        s_year  = int(start_date[6:])

        e_day   = int(end_date[0:2])
        e_month = int(end_date[3:5])
        e_year  = int(end_date[6:])

#       print s_day, s_month, s_year
#       print e_day, e_month, e_year

        days = 0.0
        year = s_year + 1
        while year < e_year:
                if(is_leap_year(year)):
                        days += 366                      
                else:
                        days += 365

                year += 1


        index = 0        
        if s_year == e_year:
                if (is_leap_year(s_year) ):
                        days += leap_year[s_month - 1] - s_day
                        index = s_month
                        while index < (e_month - 1 ):
                                days += leap_year[index]
                                index += 1
                        else:          #this part will run when index  is e_month -1
                                days += e_day
                else:
                        days += non_leap_year[s_month - 1] - s_day
                        index = s_month
                        while index < (e_month - 1 ):
                                days += non_leap_year[index]
                                index += 1
                        else:          #this part will run when index  is e_month -1
                                days += e_day


        else:      
                if (is_leap_year(s_year)):
                        days = days + leap_year[s_month - 1] - s_day #January's index = 0, Feb's index = 1, March = 2, etc.
                        index = s_month
                        while index <= 11:
                                days += leap_year[index]
                                index += 1
                
                else:
                        days = days + non_leap_year[s_month - 1] - s_day
                        index = s_month
                        while index <= 11:
                                days += non_leap_year[index]
                                index += 1

                index = 0

                if is_leap_year(e_year):
                        while index < (e_month - 1):
                                days += leap_year[index]
                                index += 1
                else:
                        while index < (e_month - 1):
                                days += non_leap_year[index]
                                index += 1


                days += e_day

        print "the total number of elapsed days, from: %s, to %s\nIs: %f" %(start_date, end_date, days)

#--------------------------------------------------------------------------#

def print_matrix(matrix):
        print
        for row in matrix:
                print row
        print


def check_matrices(matrix_A, matrix_B, operation):
        rows_A    = len(matrix_A)
        columns_A = len(matrix_A[0])

        rows_B    = len(matrix_B)
        columns_B = len(matrix_B[0])

        if operation == "add":
                if (rows_A == rows_B) and (columns_A == columns_B):
                        return True
                else:
                        return False
        elif operation == "multiply":
                if (rows_A == columns_B) and (columns_A == rows_B):
                        return True
                else:
                        return False
        else:
                print >> sys.stderr, "Error: unrecognised operation.\nThe valid options are, add or multiply."
                return False


def add_matrices(matrix_A, matrix_B):
        result = []

        row_index = 0
        column_index = 0

        rows = len(matrix_A)
        columns = len(matrix_A[0])

        for i in range(rows):
                result.append([])

        while (row_index < rows):
                column_index = 0 
                while column_index < columns:        
                        res = matrix_A[row_index][column_index] + matrix_B[row_index][column_index]
                        result[row_index].append(res)
                        column_index += 1
                row_index += 1

        return result

def  multiply_matrices(matrix_A, matrix_B):

        result = []
        rows_result = len(matrix_A)
        columns_result = len(matrix_B[0])

        for i in range(rows_result):
                result.append([])

        for column_index in range(columns_result):
                column = []
                for row in matrix_B:
                        column.append(row[column_index])

                for row_index in range(rows_result):
                        dot_product = 0;
                        elements = len(matrix_A[row_index])
                        for i in range(elements):
                                dot_product += ( column[i] * matrix_A[row_index][i] )
                        result[row_index].append(dot_product)

        return result


def matrices(matrix_A, matrix_B, operation):
        """
        Chapter 6. Question 16
        operation in the argument list is either: add or multiply
        a matrix is a list of lists ie. matrix = [[1, 2, 3], [4, 5, 6]], is a 2x3 matrix
        """

        check_matrices(matrix_A, matrix_B, operation)
        
        print "matrix A:"
        print_matrix(matrix_A)
        print "matrix B:"
        print_matrix(matrix_B)

        if operation == "add":
                result = add_matrices(matrix_A, matrix_B)
        elif operation == "multiply":
                result = multiply_matrices(matrix_A, matrix_B)
        
        print "result:"
        print_matrix(result)
        

        
        
#--------------------------------------------------------------------#
        

def my_pop(lst):
        """
        Chapter 6. Question 17
        """
        last_item = lst[-1]
        del(lst[-1])
        return last_item



#------------------------------------------------------------------#

                        


















                        










                






                
























