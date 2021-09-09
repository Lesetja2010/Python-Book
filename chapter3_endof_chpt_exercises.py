#! /usr/bin/env python
"""
Counts the number of occurences of the search_string in the input_file, and prints the lines containing the search_string.
command line options:
-i conducts a case 'insensitive' search, ie. "text", "Text", "TEXT", etc. will all be counted
-m counts multiple occurences of the search string in one line, without '-m', only one occurence per line is counted.
--help prints this doc string, along with a usage message.
"""

import sys
import getopt

help_message = """
Counts the number of occurences of the search_string in the input_file, and prints the lines containing the search_string.
command line options:
-i conducts a case 'insensitive' search, ie. "text", "Text", "TEXT", etc. will all be counted
-m counts multiple occurences of the search string in one line, without '-m', only one occurence per line is counted.
--help prints this doc string, along with a usage message.
"""

def usage():
        print >> sys.stderr, "Usage: fgrepwc [-i] [-m] search_string file_name."
        print >> sys.stderr, "Or try, fgrepwc --help, for more information."
        exit(1)

def find_all(search_string, file_name, case_insensitive = False, multiple_occurences = False): 
        try:
                f_handle = open(file_name, "r")
        except:
                print >> sys.stderr, ("Error openning file %s." %(file_name))
                print >> sys.stderr, sys.exc_info()
                exit(2)

        count = 0
        index = 0
        original_line = ""
        lines = f_handle.readlines()
        f_handle.close()

        for line in lines:
                line = line.rstrip()                #getting rid of the newline character at the end of the line
                if case_insensitive:
                        original_line = line
                        search_string = search_string.lower()
                        line = line.lower()
                        
                line_length = len(line)    
                if multiple_occurences:  
                       index = 0
                       while line.find(search_string, index, line_length) > -1:
                               count += 1
                               if index == 0:
                                       print original_line
                                      
                               index = line.find(search_string, index, line_length) + len(search_string)
                              
                               
                                       
                else:
                        if line.find(search_string) > -1:
                                count += 1
                                print line

        print count


#---------------------------------------------------------------------------------------------------------#

def check_args():
        m = False
        i = False
        argc = len(sys.argv)
        if argc < 2:
                usage()
                
        if argc == 2:
                if (sys.argv[1]).lower() == "--help":
                        print >> sys.stderr, help_message
                        usage()
                else:
                        usage()

        options, args = getopt.getopt(sys.argv[1:], "-i-m")
        if options:
                for a, b in options:    # Since options is a list of tuples (using 'multuple' assignment). b in this case will always be a null string.
                        if a == "-i":
                                i = True
                        elif a == "-m":
                                m = True
                        else:
                                print >> sys.stderr, ("Unrecognised command line option: "+a+".")#this part is not necessary 
                                                                                                 #because getopt() throws an exception when it finds an unrecognised option
                
        find_all(args[0], args[1], i, m)
             


if __name__ == "__main__":
        check_args()
