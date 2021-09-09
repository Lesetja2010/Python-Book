
import string
import time
import random

def order_keys():
        """
        Chapter 7. Question 3a
        """

        a_dict = {"apple": 34, "banana": 3.0, "grapes": 98.43, "watermelon": 424, "orange": 76.9, "mango": 4}
        keys = a_dict.keys()
        keys.sort()
        print keys

        #Question 3b

        for key in keys:
                print str(key)+" : "+str(a_dict[key])+";",    # keys list is already sorted

        print

        #Question 3c
        copy_dict ={}
        for key in keys:
                copy_dict[a_dict[key]] = key

        copy_dict_keys = copy_dict.keys()
        copy_dict_keys.sort()

        
        
        for key in copy_dict_keys:
                print str(key)+" : "+str(copy_dict[key])+";",    # keys list is already sorted
                


#------------------------------------------------------------------------#

def lists_to_dict():
        """
        Chapter 7. Question 4
        """

        a_dict = {}
        
        letters = string.letters[:26]
        letters_list = []
        numbers_list = []
        
        for index in range(2, 27, 2):
                letters_list.append(letters[ index - 2 : index])
                numbers_list.append(float(index/2))
        
        list_length = len(numbers_list)

        for index in range(list_length):
                a_dict[ numbers_list[index] ] = letters_list[index]

        print a_dict



#------------------------------------------------------------------------#

user_db = {}
admin_password = "abc123"
db_file  = open("database.txt", "r+")

def new_user():
        prompt = "Enter a user name"

        while True:
                user_name = raw_input(prompt)
                if user_db.has_key(user_name):
                        prompt = "That user name has already been taken, try a different one."
                else:
                        break

        user_db[user_name] = []
        password = raw_input("Enter a password for new account: ")
        user_db[user_name].append(password)
        user_db[user_name].append(time.time())
                


def old_user():
        user_name = raw_input("Enter your username: ")
        if user_db.has_key(user_name):
                user_info = user_db.get(user_name)
        else:
                print "Error: Invalid username."
                return None

        password = raw_input("enter password: ")
        if password != user_db[user_name][0]:
                print "Error: Invalid password."
                return None

        logout_delay = 4.0 * 60.0 * 60.0  #4 hours  
        if time.time() <= (user_db[user_name][1] + logout_delay ):
                print "You are already logged in, %s." %(user_name)
                print "previous login: %s" %(time.ctime( user_db[user_name][1] ))
                user_db[user_name][1] = time.time()     #updating last login/activity on account
        else:
                print "You have successfully logged in, %s." %(user_name)
                print "previous login: %s" %(time.ctime( user_db[user_name][1] ))
                user_db[user_name][1] = time.time()


def display_db_contents():
        keys = user_db.keys()

        for key in keys:
                print key, user_db[key][0], time.ctime(user_db[key][1])


def admin_account():
        password = raw_input("enter administrator password: ")
        if password != admin_password:
                print "Incorrect password."
                return None

        prompt = """
                make a selection:
                (1) display a list of all users and their passwords
                (2) remove a user
        """
        selection = raw_input(prompt)[0]
        selection = int(selection)

        if selection == 1:
                display_db_contents()
        
        elif selection == 2:
                user_name = raw_input("enter thr username associated with the user to be removed.")
                if user_db.has_key(user_name):
                        del(user_db[user_name])
                else:
                        print "there is no account associated with the username: %s" %(user_name)
        else:
                print "%d, is not a valid option." %(selection)


def write_to_db_file():
        keys = user_db.keys()
        for key in keys:
                line = key + " " + user_db[key][0] + " " + str(user_db[key][1])
                db_file.write(line)
                


def user_pswd():
        """
        Chapter 7. Question 5. ( a and b )
        """
        #format of a line in database.txt:
        # john911 abc123 <time> 

        #db_file is external 
        for line in db_file:
                line = line.rstrip()    #stripping the newline character at the end of the line
                line_data = line.split(" ")
                user_db[line_data[0]] = line_data[1:3] #line_data[1:3] is user password and last login time stamp


        prompt = """
                Make a selection:

                (A)dministrator login
                (N)ew user                
                (O)ld user
                (Q)uit
        """

        while True:
                try:
                        user_input = raw_input(prompt)[0]
                except (KeyboardInterrupt, EOFError):
                        user_input = "q"

                if user_input not in "anoq":
                        print "Invalid selection, please try again."
                        continue

                if user_input == "q":
                        write_to_db_file()
                        db_file.close()
                        return None
                elif user_input == "n":
                        new_user()
                elif user_input == "o":
                        old_user()
                else:
                        admin_account()

        
#------------------------------------------------------------#

def profit_and_loss(shares_dict):
        keys = shares_dict.keys()
        total_profit_or_loss = 0.0

        print "%-30s %7s %7s %6s %7s %6s" %("stock", "p_price", "c_price", "P/L", "#shares", "P/L_%")

        for key in keys:
                purchase_price = shares_dict[key][1]
                current_price = shares_dict[key][2]
                number_of_shares = shares_dict[key][3]

                profit_or_loss = (current_price - purchase_price) #per share
                percentage_profit_or_loss =  round( (profit_or_loss/purchase_price) * 100, 2)
                profit_or_loss_for_stock = profit_or_loss * number_of_shares

                total_profit_or_loss += profit_or_loss_for_stock
                
                print "%-30s %-7.2f %-7.2f %6.2f %7d %6.2f%%" %(key, purchase_price, current_price, profit_or_loss_for_stock, number_of_shares, percentage_profit_or_loss)

        print "Total profit or loss: %.2f" %(total_profit_or_loss)



def crude_portfolio():
        """
        Chapter 7. Question 6
        """
        #format of data in stock_portfolio.txt
        #company_name\tpurchase_price\tcurrent_price\tnumber_of_shares
        #current price and number of shares will be added with functions from random.py module

        shares = []
        share_info = []

        input_file = open("stock_portfolio.txt", "r+")

        for line in input_file:
                line = line.rstrip() #getting rid of the newline character at the end of the line
                line_data = line.split("\t")
                line_data[1] = float(line_data[1])
                
                current_price = random.randint( int(line_data[1] - 5), int(line_data[1] + 5) )
                current_price += round(random.random(), 2)
                line_data.append(current_price)

                number_of_shares = random.randint(1, 20)
                line_data.append(number_of_shares)

                shares.append(line_data)

        shares_dict = {}
        for individual_stock in shares:
                shares_dict[individual_stock[0]] = individual_stock

        profit_and_loss(shares_dict)


#-----------------------------------------------------------------------#

def key_value_reverse(a_dict):
        """
        Chapter 7. Question 7. 
        """

        keys = a_dict.keys()
        ret_val = {}

        for key in keys:
                ret_val[a_dict[key] ] = key

        return ret_val


#-----------------------------------------------------------------------#

def create_employee_numbers(data_file):
        employees = {}

        for line in data_file:
                rand_num = random.randint(0, 100)
                while rand_num in employees.keys():        #this will loop forever if the number of employees is >= 101
                        rand_num = random.randint(0, 100)

                employees[rand_num] = line.rstrip()

        return employees
        

def print_by_employee_name(employees):
        reversed_dict = key_value_reverse(employees)   #question 7's answer. loses dictionary entries if dict[key1] = dict[key2], where key1 != key2.
        keys = reversed_dict.keys()

        keys.sort()
        for key in keys:
                print key, reversed_dict[key]
                


def employee_database():
        """
        Chapter 7. Question 8
        """
        data_file = open("employees.txt", "r+")

        employees_dict = create_employee_numbers(data_file)

        print_by_employee_name(employees_dict)
        keys = employees_dict.keys()
        data_file.seek(0)
        for key in keys:
                line = str(key)+" "+employees_dict[key]+"\n"
                data_file.write(line)

        data_file.close()
        

#------------------------------------------------------------------------------------#
def tr(srcstr, dststr, string):
        """
        Chapter 7. Question 9
        """
        mapping = {}
        if len(srcstr) == len(dststr):
                index = 0
                length = len(srcstr)
                while index < length:
                        mapping[ srcstr[index] ] = dststr[index]
                        index += 1

        else:
                srclen = len(srcstr)
                dstlen = len(dststr)
                index = 0
                while index < srclen:
                        if index >= dstlen:
                                mapping[ srcstr[index]] = ""
                        else:
                                mapping[ srcstr[index]] = dststr[index]

                        index += 1

        result = ""
        for char in string:
                if char in srcstr:
                        result += mapping[char]
                else:
                        result += char

        return result

























                


















