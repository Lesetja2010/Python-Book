#! /usr/bin/env python

import sys
import os

def display_lines():
        """
        Chapter 10. Exercese 1
        """
        file_name = raw_input("Please enter file name: ")

        fp = open(file_name, "r")
        for line in fp:
                new_line = line.lstrip()    #incase there are whitespace characters before the pound sign
                if new_line[0] != "#":
                        print line,


#--------------------------------------#

def display_N_from_F():
        """
        Chapter 10. Exercese 2
        """

        file_name = raw_input("Please enter filename: ")
        number_of_lines = int( raw_input("Enter ther number of lines to print from the file: ") ) 
        
        try:
                fp = open(file_name)
        except Exception as ex:
                print >> sys.stderr, "An error occured while trying to open the specified file."
                print >> sys.stderr, str(ex)
                return None

        counter = 1
        while counter <= number_of_lines:
                line = fp.readline()
                print line,            # adding comma at the end of print statement, because readline() retains the newline character
                counter += 1

                
#----------------------------------------#

                
def count_lines():
        """
        Chapter 9. Exercise 3
        """
        file_name = raw_input("Enter file name: ")

        try:
                input_file = open(file_name, "r")
        except Exception as ex:
                print >> sys.stderr, "Error opening file: ", file_name
                print str(ex)
                return None

        lines = 0
        for line in input_file:
                lines += 1

        input_file.close()
        print "The file,", file_name, "has", lines, "lines in it."


#-----------------------------------------#


def pager_prog():
        """
        Chapter 9. Exercise 4
        """

        file_name = raw_input("Enter filename: ")
        input_file = open(file_name, "r")

        count = 0
        for line in input_file:
                count += 1
                print line,
                if count == 2:
                        count = 0       #resetting count
                        response = raw_input("enter c, to continue, and s, to stop: ")
                        if response == "s":
                                break
                        

        input_file.close()


#------------------------------------------#


"""
Chapter 9. Exercise 5, already done
"""

#-------------------------------------------#


def display_result(line_number, column_number):
        print "The two files provided are not identical. They differ at:"
        print "line:", line_number, ", column:", column_number


def file_comparison(file_1, file_2):     #to run this, open two files, and pass them as parameters to the function
        """
        Chapter 9. Exercise 6
        """

        file_1_line = file_1.readline()
        file_2_line = file_2.readline()

        line_number = 1
        column_number = 0

        while file_1_line and file_2_line:     #neither of the lines is null
                line_length = len(file_1_line)      #whether I use file_1_line or file_2_line does not affect the final outcome.

                while column_number < line_length:
                        if file_1_line[column_number] != file_2_line[column_number]:
                                
                                display_result(line_number, column_number + 1)
                                return None         #files are not the same, exit the function.
                        column_number += 1

                file_1_line = file_1.readline()
                file_2_line = file_2.readline()

                line_number += 1
                column_number = 0

        if (file_1_line == "") and (file_2_line == ""):
                print "The two files are identical."
        else:
                display_result(line_number, column_number)

                
#---------------------------------------#

def parse_ini_file(input_file):     #open the .ini file in conversational mode and pass it as a parameter to the function
        """
        Chapter 9. Question 7

        find and check structure of a .ini file.
        """

#----------------------------------------#


import inspect

def module_attributes():
        """
        Chapter 9. Question 8 
        """

        module_name = raw_input("Enter module name: ")
        try:
                input_module = __import__(module_name)
        except Exception as ex:
                print >> sys.stderr, "Unable to open, the specified module."
                print >> sys.stderr, str(ex)
                return None

        module_objects = inspect.getmembers(input_module)
        
        for item in module_objects:
                print item[0], item[1]
                

#--------------------------------------------#

def collect_doc_string(input_file):

        doc_string = ""
        doc_string += input_file.read(3)    # collecting the first three quotation marks
        while True:
                char = input_file.read(1)
                doc_string += char
                if char == '"':
                        more_chars = input_file.read(2)
                        doc_string += more_chars
                        if more_chars == '""':
                                break

        return doc_string



def scan_directory_tree(library_path, output_file):   #library_path is the absolute path of a directory
        output_file.write("*** from directory: " + library_path + "***")

        listing = os.listdir(library_path)
        for item in listing:
                item_path = os.path.join(library_path, item)
                if os.path.isdir(item_path):
                        scan_directory_tree(item_path, output_file)
                elif item[-3:] == ".py":               #item is a python module
                        mod_file = open(item_path, "r")
                        doc_string_check = mod_file.read(3)
                        if doc_string_check == '"""':
                                mod_file.seek(0)
                                doc_string = collect_doc_string(mod_file)
                                output_file.write("module name: "+item+":\n")
                                output_file.write("doc string: "+ doc_string)
                        mod_file.close()
                        
                        


def pydoc_scanner(library_path):
        """
        Chapter 9. Question 9
        """

        output_file = open("output_file.txt", "w")     #this will be created in the directory Documents/__Python
        
        scan_directory_tree(library_path, output_file)
        output_file.close()



#--------------------------------------------------#

import time

def get_balance(data_file):
        data_file.seek(0)
        temp = data_file.readline()
        while temp != "":
                line = temp
                temp = data_file.readline()

        balance = (line.split())[-1]
        return float(balance)


def deposits_and_withdrawals(transaction_type, amount):
        pass



def savings_and_checking_account(account_type, data_file):
        print account_type+":", "Make a selection: "
        while True:
                print "(B)alance"
                print "(D)eposit"
                print "(W)ithdrawal"
                print "(S)tatement"
                print "(Q)uit"
                choice = raw_input()
                if choice == "B":
                        print "The current,", account_type, "balance is:", get_balance(data_file)
                elif choice == "D":
                        amount = float(raw_input("Enter deposit amount: "))
                        deposits_and_withdrawals("Deposit", amount, data_file)
                elif choice == "W":
                        amount = float(raw_input("Enter the amount to withdraw: "))
                        deposits_and_withdrawals("Withdrawal", amount, data_file)
                        
                        
                




def money_market():
        pass

def fin_man():
        """
        Chapter 9. Question 10
        """

        print "Please make a selection: "
        print "(S)avings account"
        print "(C)hecking account"
        print "(M)oney market"
        print "(Q)uit"

        choice = raw_input()
        if choice == "S":
                data_file = open("savings_account.txt", "a+")
                savings_and_checking_account("savings", data_file)
                
        elif choice == "C":
                data_file = open("checking_account.txt", "a+")
                savings_and_checking_account("checking", data_file)

        elif choice == "M":
                money_market()
        elif choice == "Q":
                return None
        else:
                print "The selection you have made is invalid. Program exitting"
        

#-------------------------------------------#


import time


def create_new_account(data_file):
        user_name = raw_input("Enter a username for the new account: ")
        password = raw_input("Enter a password for the new account: ")
        last_login = time.time()

        data_file.write(user_name.strip() + ":" + password.strip() + ":" + str(last_login).strip() + "\n")


def account_manager(user_record):
        print "make a selection:"
        print "(D)isplay password"
        print "(C)hange password"
        print "(V)iew last login time"

        choice = raw_input()

        if choice == "D":
                print user_record[1]
        elif choice == "C":
                new_password = raw_input("Enter new password: ")
                user_record[1] = new_password
        elif choice == "V":
                print "Last login time:", user_record[2]



def existing_user_account(data_file):
        user_info_records = []
        for line in data_file:                 #Reading all the records into memory, would not be a good idea, if data_file was a very big file. (It isn't in this case, though)
                record = line.split(":")
                record[-1] = record[-1].rstrip()       #getting rid of the newline character at the end.
                record[-1] = float(record[-1])
                user_info_records.append(record)

        for i in range(1, 4):
                if i > 1:
                        print "The username you entered, does not exist, try again(try %d of 3): " %(i)
                        
                user_name = raw_input("Enter username: ")
                login_correct = False
                max_password_attempts_exceeded = False

                index = 0
                while index < len(user_info_records):
                        
                        if user_name == user_info_records[index][0]:

                                password_attempt_count = 1
                                while password_attempt_count <= 3:
                                        if password_attempt_count > 1:
                                                print "The password you entered is incorrect, please try again."
                                        password = raw_input("Enter password for user, " + user_name + ("(try %d of 3):" % (password_attempt_count))  )
                                
                                        if password == user_info_records[index][1]:
                                                print "Welcome, " + user_name + "."
                                                user_info_records[index][2] = time.time()
                                                account_manager(user_info_records[index])        #the changes made by account_manager to user_info_records[index], will be reflected in the original, user_info_records      
                                                login_correct = True                
                                                break
                                else:
                                        print "You have entered, an incorrect password, 3 times."
                                        print "Login session closed."
                                        max_password_attempts_exceeded = True


                        if login_correct or max_password_attempts_exceeded:
                                break

                        index += 1
                                
                if login_correct or max_password_attempts_exceeded:
                           break
                 
        else:
                print "You have entered a non-existent username, 3 times."
                print "Login sesson closed."

def administrator_account(data_file):
        admin_record_str = data_file.readline()
        admin_record = admin_record_str.split(":")
        admin_record[-1] = float(admin_record[-1].rstrip() )


        print "Administrator login:"
        password = raw_input("Enter administrator password: ")
        if password == admin_record[1]:
                print "admin password correct."
                





        

def user_logins():
        """
        Chapter 9. Question 12
        """

        data_file = open("password_file.txt", "a+")
        print "Please make a selection:"
        print "(N)ew User."
        print "(E)xisting user"
        print "(A)dministrator login"
        response = raw_input()

        if response == "N":
                create_new_account(data_file)
        elif response == "E":
                existing_user_account(data_file)
        elif response == "A":
                administrator_account(data_file)
        else:
                print "The selection you made is invalid. Program exitting."


        data_file.close()



#-------------------------------------------------------#


def plus(arg_1, arg_2):
        return arg_1 + arg_2

def minus(arg_1, arg_2):
        return arg_1 - arg_2

def multiply(arg_1, arg_2):
        return arg_1 * arg_2

def divide(arg_1, arg_2):
        return arg_1 / arg_2

def power(base, exponent):
        return base ** exponent

def modulus(arg_1, arg_2):
        return arg_1 % arg_2


def calculator():
        """
        Chapter 9. Question 14.
        """

        #sys module has already been imported above
        args = sys.argv[1:]
        output_file = open("calculator_file.txt", "a+")
        
        if len(args) == 1  :
                if args[0] == "print":
                        for line in output_file:
                                print line
                else:
                        print >> sys.stderr, "command to print log file:\nmain.py print"

                return None

        
        if len(args) != 3:
                print >> sys.stderr, "usage: main.py operand operator operand.\nie. main.py 1 + 1"
                return None

        operand_1 = float(args[0])
        operator  = args[1]
        operand_2 = float(args[2])

        operations = {"+": plus, "-": minus, "*": multiply, "/" : divide, "^": power, "%": modulus }

        for key in operations.keys():
                if operator == key:
                        result = operations[operator](operand_1, operand_2)       #remember, operations[operator] is a function
                        print result
                        output_string = args[0] + " " + args[1] + " " + args[2] + "\n" + str(result) + "\n"
                        output_file.write(output_string)
        else:
                print >> sys.stderr, "invalid input format."
                print >> sys.stderr, "usage: main.py operand operator operand.\nie. main.py 1 + 1"


        output_file.close()


if __name__ == "__main__":
        calculator()

        

        

                        
        
                




















        


































        
        




































                


