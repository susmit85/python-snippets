#!/usr/bin/python

'''sample argparse code'''

#######################################################################
# copyright (C) 2011, Susmit Shannigrahi
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#######################################################################


import argparse


def read_args():
    '''parses command line arguments'''

    #initiate the parser
    parser = argparse.ArgumentParser(description='Parses command line args.')

    #add options
    parser.add_argument('-f', dest='filename', 
                   help='reads filename from command line', required=True)

    #parse the args
    args = parser.parse_args()

    #prints the arguments    
    print args.filename


    
    
    

if __name__ == "__main__":
# read the commandline arguments()
    read_args()
    
