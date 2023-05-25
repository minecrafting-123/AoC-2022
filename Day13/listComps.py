everything = []
total = 0

with open("input.txt", "r") as reader:
    for line in reader:
        everything.append(line)
#Each element here is a pair of lists to compare, seperated by a \n
listOfLists = "".join(everything).split("\n\n")
otherListOfLists = "".join(everything).split("\n")
c = otherListOfLists.count("")
for i in range(c):
    otherListOfLists.remove("")

# def bracketMatch(input):
#     global openCount
#     list = []
#     store = ""
#     letters = enumerate(input)
#     for index, letter in letters:
#         if(letter == "["):
#             openCount += 1
#             inside = bracketMatch(input[index+1:])
#             list.append(inside[0])
#             for num in range(inside[1] + 1):  # skip what was already calced hopefully
#                 next(letters, None)
#             if (openCount is 0):
#                 return list
#         if(letter.isnumeric()):
#             store += letter
#         if(letter == "," and store != ""):
#             list.append(store)
#             store = ""
#         if(letter == "]"):
#             if (store != ""):
#                 list.append(store)
#             openCount -= 1
#             return list, index

def compareLists(list1, list2):
    #print(list1)
    #print(list2)
    
    for i, val in enumerate(list1):
        if i + 1 > len(list2):
            #print("Right side ran out of items")
            return False
        if isinstance(list1[i], int) and isinstance(list2[i], int):
            if list1[i] > list2[i]:
                #print("first list beeger")
                return False
            if list1[i] < list2[i]:
                #print("first list smol")
                return True
        elif isinstance(list1[i], list) and isinstance(list2[i], list):
            if (len(list1[i]) == 0 and len(list2[i]) == 0):
                return compareLists(list1[i+1:], list2[i+1:])
            return compareLists(list1[i], list2[i])
        else:
            if (isinstance(list1[i], int)):
                return compareLists([list1[i]], list2[i])
            else:                
                return compareLists(list1[i], [list2[i]])
    #EXITS LOOP
    #print("exits loop")
    return True

def bubbleSort(arr):

    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not compareLists(eval(arr[j]), eval(arr[j + 1])):

                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

# for index, pair in enumerate(listOfLists):
#     first, last = map(eval, pair.split("\n"))
#     if(compareLists(first, last)):
#         total += index + 1
#         #print(total)
# print(total)

otherListOfLists.insert(0, "[[2]]")
otherListOfLists.insert(0, "[[6]]")

bubbleSort(otherListOfLists)

index1 = otherListOfLists.index("[[2]]") + 1
index2 = otherListOfLists.index("[[6]]") + 1
#print(otherListOfLists)

print(index1 * index2)