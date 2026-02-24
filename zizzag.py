import time,sys
indent = 0 # how many spaces to indent
indentIncreasing =True # whether the indent increase or not

try:
    while True: # the main program loop
        print(' '* indent, end='')
        print("********")
        time.sleep(0.1)# pause for 1/10 of a second


        if indentIncreasing:
            # increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction

                indentIncreasing=  False
        else:
            indent = indent - 1

            if indent == 0:
               indentIncreasing = True

except KeyboardInterrupt:
 sys.exit()