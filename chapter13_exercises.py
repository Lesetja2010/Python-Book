#! /usr/bin/env python

import time
import math
import sys

def dollarize(amount):
        """
        Chapter 13. Question 3.
        """
        if amount < 0:
                negative = True
                amount = abs(amount)
        elif amount >= 0:
                negative = False

        if amount == 0:
                return "R"+str( float(amount) )

        cents = amount % 1
        dollars = amount - cents
        cents = round(cents, 2)

        ret_val = ""
        while dollars > 0:
                piece = int( dollars % 1000 )      # this is so str() function returns an int, ie 123 instead of a float: 123.0 
                dollars = dollars - piece
                dollars = dollars / 1000
                ret_val = "," + str(piece) + ret_val

        ret_val = ret_val[1:]                      # eliminating the leading ','(comma), at the beginning of the string
        ret_val = "R" + ret_val + str(cents)[1:]
        if negative:
                ret_val = "-" + ret_val

        return ret_val


class MoneyFmt:
        """
        Chapter 13. Question 3.
        """
        def __init__(self, amount):
                self.amount = amount

        def update(self, new_amount):
                self.amount = new_amount

        def __nonzero__(self):
                if self.amount != 0:
                        return True
                else:
                        return False

        def __repr__(self):
                return str(float(self.amount))

        def __str__(self):
                return dollarize(self.amount)

        
#--------------------------------------------------------------#

class UserDB:
        """
        Chapter 13. Question 4.
        """
        def __init__(self):
                self.data_file = open("db_file.txt", "r+")
                self.user_info = {}
                for line in self.data_file:
                        line_data = line.split()
                        self.user_info[ line_data[0] ] = [line_data[1], float(line_data[2])]    #dictionary entry --> user_name: [password, timestamp]         


        def __del__(self):
                self.data_file.truncate(0)
                self.data_file.close()
                self.data_file = open("db_file.txt", "r+")
                user_names = self.user_info.keys()
                for name in user_names:
                        self.data_file.write(name+" "+self.user_info[name][0] + " " + str( self.user_info[name][1]) +"\n" )

                self.data_file.close()
                
                

        def add_new_user(self):
                user_name = raw_input("Enter new user_name (with no whitespace characters): ")
                password = raw_input("Enter password for %s: " % (user_name))
                self.user_info[user_name] = [password, 0]

        def update(self):
                user_name = raw_input("Enter the details of the user, whose info is to be updated: ")
                if user_name in self.user_info:
                        change_user_name = raw_input("change user_name? ")
                        if change_user_name in "Yy":
                                new_user_name = raw_input("Enter new username: ")
                                self.user_info[new_user_name] = self.user_info[user_name]
                                self.user_info.pop(user_name)
                                user_name = new_user_name

                        change_password = raw_input("change user password? ")
                        if change_password in "Yy":
                                new_password = raw_input("Enter new password: ")
                                self.user_info[user_name][0] = new_password

        
                                
#-----------------------------------------------------------------------#


class Point:
        """
        Chapter 13. Question 5.
        """
        def __init__(self, x = 0, y = 0):
                self.x = x
                self.y = y


#-----------------------------------------------------------------------#

class Line:
        """
        Chapter 13. Question 6.
        """

        def __init__(self, point_1, point_2):
                self.point_1 = point_1
                self.point_2 = point_2


        def get_slope(self):
                slope = (point_1.y - point_2.y) / (point_1.x - point_2.x)
                return slope

        def get_length(self):
                if self.point_1.x > self.point_2.x:
                        x = self.point_1.x - self.point_2.x
                else:
                        x = self.point_2.x - self.point_1.x

                if self.point_1.y > self.point_2.y:
                        y = self.point_1.y - self.point_2.y
                else:
                        y = self.point_2.y - self.point_1.y

                length = math.sqrt(x**2 + y**2)
                return length

        def __repr__(self):
                return ((point_1.x, point_1.y), (point_2.x, point_2.y) )

        
#----------------------------------------------------------------------#


class Date:
        """
        Chapter 13. Question 7.
        """
        tmp_date = time.ctime().split()
        day = tmp_date[0]
        month = tmp_date[1]
        year = tmp_date[-1]

        def __init__(self, time = time.time()):
                self.time = time


        def update(self, time = time.time()):
                self.time = time
                
        
        def display(self, date_format = None):
                if date_format == None:
                        return time.ctime()
                
                if date_format == "MM/DD/YY":
                        return Date.month + "/" + Date.day + "/" + Date.year[2:]
                elif date_format == "MM/DD/YYYY":
                        return Date.month + "/" + Date.day + "/" + Date.year
                elif date_format == "DD/MM/YY":
                        return Date.day + "/" + Date.month + "/" + Date.year[2:]
                elif date__format == "DD/MM/YYYY":
                        return Date.day + "/" + Date.month + "/" + Date.year
                

#---------------------------------------------------------#

class Stack:
        """
        Chapter 13. Question 8.
        """
        def __init__(self):
                self.stack = []

        def pop(self):
                if len(self.stack) > 0:
                        return self.stack.pop(-1)
                else:
                        print >> sys.stderr, "Unable to pop(), stack is empty."

        def push(self, item):
                self.stack.append(item)

        def isempty(self):
                if len(self.stack) == 0:
                        return True
                else:
                        return False

        def peek(self):
                return self.stack[-1]
        

#----------------------------------------------------------#

class Queue:
        """
        Chapter 13. Question 9.
        """

        def __init__(self):
                self.queue = []

        def enqueue(self, item):
                self.queue.insert(0, item)

        def dequeue(self):
                return self.queue.pop(-1)


#-----------------------------------------------------------#

def DataContainer:
        """
        Chapter 13. Question 10.
        """
        
        def __init__(self):
                self.struct = []

        def shift(self):
                val = self.struct[0]
                self.struct.remove(val)
                return val

        def unshift(self, item):
                self.struct.insert(0, item)

        def push(self, item):
                self.struct.append(item)

        def pop(self):
                return self.struct.pop(-1)
        


#-----------------------------------------------------------#

class Item:
        """
        Chapter 13. Question 11a.
        """
        def __init__(self, description, price):
                self.description = description
                self.price = price
               


class Cart:
        """
        Chapter 13. Question 11b.
        """
        def __init__(self, cart_number):
                self.cart_number = cart_nuber
                self.items = []               #list of items in the cart
                
        def add_item(self, item):
                self.cart.append(item)

        def remove_item(self):
                self.cart.remove(item)        #the first occurence of item in the list, self.cart.items[] will be removed

        def total_cost(self):
                amount = 0
                for i in self.items:
                        amount = amount + i.price

                return amount
        


class User:
        """
        Chapter 13. Question 11c.
        """
        def __init__(self, user_name = "Unknown"):
                self.user_name = user_name
                self.carts = []       #a user can have more than one cart, carts will be placed in a list
                
        def add_cart(self, cart):
                self.carts.append(cart)

        def remove_cart(self, cart):
                self.carts.remove(cart)

        def get_total_cost(self):
                total = 0
                for cart in self.carts:
                        total = total + cart.total_cost()



#--------------------------------------------------------------------------# 

class Message:
        """
        Chapter 13. Queston 12a.
        """

        def __init__(self, message, recipient): #recepient is either a single recepient, or broadcast
                self.message = message
                self.recepient = recepient

        def change_message(self, new_message):
                self.message = new_message

        def send_message(self):
                #this method will send the message to the intended recepient
                pass
        def view_message(self):
                print self.message



class User:
        """
        Chapter 13. Question 12b.
        """
        def __init__(self, username):
                self.username = username

class Room:
        """
        Chapter 13. Question 12c.
        """
        
        def __init__(self):
                self.users = []


        def add_user(self, user):
                self.users.append(user)

        def remove_user(self, user):
                self.users.remove(user)

        def get_users(self):
                return tuple(self.users)    # convert to tuple so the list of users cannot be modified outside the class


#----------------------------------------------------#


class Stock:
        """
        Chapter 13. Question 13a.
        """
        def __init__(self, company_name, ticker_symbol):
                self.company_name = company_name
                self.ticker_symbol = ticker_symbol

        def puchase(self, purchase_date, purchase_price, number_of_shares):
                self.p_date = purchase_date
                self.p_price = purchase_price
                self.n_shares = number_of_shares


        def annual_retun(self, current_price):
                return current_price - self.p_price 



        

class Portfolio:
        """
        Chapter 13. Question 13b.
        """
        def __init__(self):
                self.stocks = []

        def add_new_stock(self, stock):
                self.stocks.append(stock)
                
        def remove_stock(self, stock):
                 self.stocks.remove(stock)

#-------------------------------------------------------#
















        





                












        













                














        
        
