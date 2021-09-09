
import math
import cmath

def safe_open(file_name, arg):
        """
        Chapter 10. Question 6
        """
        
        try:
                f_handle = open(file_name, arg)
        except:
                return None

        return f_handle


#-----------------------------------#


def safe_input(prompt):
        """
        Chapter 10. Question 8
        """
        
        try:
                user_input = raw_input(prompt)
        except:
                return None

        return None



#-------------------------------------#


def safe_sqrt(i):
        """
        Chapter 10. Question 9
        """

        try:
                ret_val = math.sqrt(i)
        except ValueError:
                ret_val = cmath.sqrt(i)

        except:
                ret_val = None

        return None



#-------------------------------------#
