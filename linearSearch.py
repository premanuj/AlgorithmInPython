#linear search function in python
#It looks for a n item in a list

def linearSearch(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position+1
    return found

if __name__=="__main__":
    itemList = ['rice', 'wheat', 'pea', 'banana']
    item = input("Type item name you are looking for: ")
    isitFound = linearSearch(item, itemList)
    if isitFound:
        print('Your item in the list')
    else:
        print('Sorry! item is not available.')