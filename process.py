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
# sales_reports(log_file)


list_of_deliveries = []


def list_to_string(list):
    str1 = " "
    return (str1.join(list))


def print_list_greater_than_ten(log_file):
    for line in log_file:
        line = line.rstrip('\n').split(' ')
        list_of_deliveries.append(line)

    for item in list_of_deliveries:
        melon_count = int(item[2])
        if melon_count > 10:
            print(list_to_string(item))

print_list_greater_than_ten(log_file)
