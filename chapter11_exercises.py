#! /usr/bin/env python

import sys
import types
import string
import time
import operator


def combo_function(num_1, num_2):
        """
        Chapter 11. Question 2
        function returns (sum, product)
        """
        return (num_1 + num_2, num_1 * num_2)


#--------------------------------------------------#


def max2(arg_1, arg_2):
        """
        Chapter 11. Question 3a(1)
        """
        if cmp(arg_1, arg_2) > 0:
                return arg_1
        else:
                return arg_2

def min2(arg_1, arg_2):
        """
        Chapter 11. Question 3a(2)
        """
        if cmp(arg_1, arg_2) < 0:
                return arg_1
        else:
                return arg_2

def my_max(seq):
        """
        Chapter 11. Question 3b(1)
        """
        biggest = seq[0]

        for item in seq[1:]:
                if max2(biggest, item) != biggest:
                        biggest = item

        return biggest

def my_min(seq):
        """
        Chapter 11. Question 3b(2)
        """
        smallest = seq[0]

        for item in seq[1:]:
                if min2(smallest, item) != smallest:
                        smallest = item

        return smallest


#--------------------------------------------------#


def min_to_hr_and_min(minutes):
        """
        Chapter 11. Question 4
        """

        hours = int(minutes/60)
        minutes = minutes % 60

        print "hours: %d, minutes: %d" % (hours, minutes)



#---------------------------------------------------#
        
def sales_tax_calculator(price, tax_rate = 0.14):
        """
        Chapter 11. Question 5
        """
        return price + (price * tax_rate)



#---------------------------------------------------#

def printf(format_str, *extra_args):
        """
        Chapter 11. Question 6
        """

        format_chars = "sfdc"
        print_str = ""
        
        extra_args_index = 0
        length = len(format_str)
        index = 0

        while(index < length):
                if format_str[index] != "%":
                        print_str += format_str[index]
                elif not (format_str[index + 1] in format_chars):
                        print_str += format_str[index]

                else:
                        if format_str[index + 1] == "f":
                                if type(extra_args[extra_args_index]) == type(2.2):      #types.FloatType
                                        print_str += str(extra_args[extra_args_index])
                                else:
                                        print >> sys.stderr, "string format operator: %f doesn't correspond with the value: " + str(extra_args[extra_args_index])
                                        return None
                                
                        elif format_str[index + 1] == "d":
                                if type(extra_args[extra_args_index]) == type(1):     #types.IntType
                                        print_str += str(extra_args[extra_args_index])
                                else:
                                        print >> sys.stderr, "string format operator: %d doesn't correspond with the value: " + str(extra_args[extra_args_index])
                                        return None
                                        
                        else:
                                if type(extra_args[extra_args_index]) == type("c"):    #types.StringType#   #Python doesn't differentiate between a string and a character
                                        print_str += extra_args[extra_args_index]
                                else:
                                        "string format operator: %s or %c doesn't correspond with the value: " + str(extra_args[extra_args_index])

                        extra_args_index += 1
                        index += 1
                                
                                
                index += 1       ##NB##


        print print_str

#---------------------------------------------------------#


def merge_lists(seq_1, seq_2):
        """
        Chapter 11. Question 7.
        """

        ret_val = map(None, seq_1, seq_2)
        print ret_val



#----------------------------------------------------------#


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
        


def filter_leap_years(func, years):
        """
        Chapter 11. Queston 8.
        """
        leap_years = filter(func, years)
        print leap_years


#-----------------------------------------------------------#


def my_average(seq):
        """
        Chapter 11. Question 9.
        """

        the_sum = reduce(lambda x, y: x+y, seq)
        average = the_sum/len(seq)

        print "average:", average


#-----------------------------------------------------------#


def statement_holder():
        """
        Chapter 11. Question 10.
        """

        files = filter(lambda x: x and x[0] != '.', os.listdir(folder))

        #stores a list of files in folder directory, whose names don't begin with, "."


#----------------------------------------------------------#


def clean_file(read_file, write_file = None):
        """
        Chapter 11. Question 11.
        """

        try:
                r_file = open(read_file, "r")
        except IOError, ioe:
                print "unable to open file:", read_file
                print "reason:", str(ioe)
                return None

        if write_file != None:
                w_file = open(write_file, "w")


        lines = r_file.readlines()             #assuming file isn't too big. Otherwise, this is going to eat up a lot of memory
        r_file.close()

        edited_lines = map(string.strip, lines)
        index = 0
        lines_length = len(edited_lines)

        while index < lines_length:
                edited_lines[index] = edited_lines[index] + "\n"
                index += 1
        

        if write_file != None:
                w_file.writelines(edited_lines)
        else:
                for line in edited_lines:
                        print line,
                


#--------------------------------------------------------------#


def time_it(func, *nkw_args, **kw_args ):
        """
        Chapter 11. Question 12.
        """

        start_time = time.time()
        apply(func, nkw_args, kw_args)
        end_time = time.time()

        print "function return time:", end_time - start_time


#--------------------------------------------------------------#

def mult(x, y):
        """
        Chapter 11. Question 12a.
        """

        return operator.mul(x, y)

def factorial_1(func, number):
        """
        Chapter 11. Question 12b.
        """

        fact = reduce(func, range(1, number + 1) )
        return fact


def factorial_2(number):
        """
        Chapter 11. Question 12c.
        """        
        return reduce(lambda x, y: operator.mul(x, y), range(1, number + 1))



def check_times():
        """
        Chapter 11. Queston 12d.
        """

        print "factorial_1"
        time_it(factorial_1, operator.mul, 100)
        print "*-----------------*"

        print "factorial_2"
        time_it(factorial_2, 100)


#----------------------------------------------------------------#

def fibonacci(num_1, num_2, stop):
        """
        Chapter 11. Question 13.
        """

        if num_1 == 1 and num_2 == 1:
                print "1\n1"

        num_sum = num_1 + num_2
        if num_sum > stop:
                return
        else:
                print num_sum
                fibonacci(num_2, num_sum, stop)
                

        


#-----------------------------------------------------------------#

def reverse_string(arg):
        """
        Chapter 11.Question 15.
        """

        if len(arg) == 1:
                return arg
        elif len(arg) == 2:
                return arg[1]+arg[0]
        else:
                return arg[-1] + reverse_string(arg[1:-1]) + arg[0]
        


































        





















































        
        
























            
        
        

