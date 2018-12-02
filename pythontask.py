import csv


def saveinfo(information):
    """
        this function save the information the user enters
        parameters :
        information: list of dictionaries each represents one entry by the user

    """
    #open the file
    with open("info.csv","wb") as file:
        #write the header of the file from the sample dictionary
        writer = csv.DictWriter(file,sample.keys())
        writer.writeheader()
        #loop over the list and save each item in a row
        for info in information:
            writer.writerow(info)


#intialization of variables
information=[]
sample={"name":"","email":"","university":"","major":"","mobile":""}
stop = False
stopstr="(to stop enter 'stop') "
print(stopstr)

# the main loop of the program
while(not stop):
    #the dictionary representing the user entry
    info = {"name":"","email":"","university":"","major":"","mobile":""}
    #loop over the dictionary keys and get user input
    for key in sample.keys():
        s=str(raw_input("Enter your {} : ".format(key)))
        print("you entered {}".format(s))
        # the stoping condition
        if s=="stop":
            stop=True
            print(information)
            #handle when the user exits ehile in the middle of the loop
            if key != "mobile":
                information.append(info)
            break
        #save the information in the dictionary
        else:
            info[key]=s
    #save the information
    saveinfo(information)
    information.append(info)
