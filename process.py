#opens the sum-server-01 naming it log_file so that it can be manipulated
log_file = open("um-server-01.txt")

# created a function passing in a condition
def sales_reports(log_file):
    #for loop going through each item in log_file
    for line in log_file:
        #removes any trailing characters
        line = line.rstrip()
        #set day equal to the first 3 letters of the file
        day = line[0:3]
        #sets conditional for what day equals
        if day == "Mon":
            #print all lines of log_file if day = Tue
            print(line)

#invoke the function passing in log_file
sales_reports(log_file)
