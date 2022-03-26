mylist = ['apple','cake','tea']

def listToString(list):
    statement = ""
    for item in list:
        if item == list[-1]:
            statement += "and " + item
        else:
            statement += item + ", "
    print(statement)

listToString(mylist)