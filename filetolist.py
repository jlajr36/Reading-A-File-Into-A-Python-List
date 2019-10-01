#import libraries
import random

#open the file
with open('quotes.txt','r') as fp:
    #read in the lines
    read_lines = fp.readlines()
    #remove end of line character of each line
    read_lines = [line.rstrip('\n') for line in read_lines]
    #store the number of lines read
    lines = len(read_lines)
    
#stop loop variable
stop = True
#input compare variable
_quit = 'q'

while stop: #while stop is true
    #print random quote and prompt user
    print('Here is a quote:')
    print() #print a space
    print(read_lines[random.randint(0,lines-1)])
    print() #print a space
    print('Enter to get another or q to quit')
    #store user input
    state = input()
    #if user enters a q quit else continue
    if state == _quit:
        break
