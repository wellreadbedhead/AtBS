mylist = ['apple','cake','tea']

def listToString(list):
    statement = ""
    for item in list:
        if item == list[-1]:
            statement += "and " + item
        else:
            statement += item + ", "
    return statement

print(listToString(mylist))