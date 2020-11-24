###############################################
#                                             #
#       Author UjjwalSharma 24/11/2020        #
#               Version 1.0                   #
#               							  #
###############################################

# Convert a list to string
def listTostring(givenList):
    string = ""
    for element in givenList:
        string += element
    return string

# # Convert string to list
# # Not used in this program
# def stringToList(givenString):
#     list = []
#     for element in givenString:
#         list += element
#     return list

def sliceAt(emailAsList):
    userName = []
    for character in email:
        if character != "@":
            userName += character
        else:
            break
    return listTostring(userName)

def forMailService(emailAsList):
    mailService = []
    posOfAtSign = 0
    for eachCharacter in emailAsList:
        if eachCharacter != "@":
            posOfAtSign += 1
        else:
            break

    return "www." + listTostring(emailAsList[posOfAtSign+1:int(len(emailAsList))])

# Main function
if __name__ == "__main__":

    email = input("Enter your email : ")

    userName = sliceAt(email)
    mailService = forMailService(email)

    print("User's Name : " + userName)
    print("Mail service used : " + mailService)
