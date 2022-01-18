# Calculates the Damerau-Levensthein or Levensthein edit distance between given strings str1 and str2.
# str1: string
# str2: string
# editType: type of the edit distance. if "damerau", then Damerau-Levensthein formula is used. Otherwise Levensthein edit distance is assumed.
# returns the distance between str1 and str2
def edit_distance(str1, str2, editType):
    n = len(str1)
    m = len(str2)

    # parents and operations are 2d arrays with the same dimension as distanceTable (n+1 x m+1)
    # parents[i][j] stores the parent cell's coordinates
    # operations[i][j] stores the operation in the form of string, indicating with which operation current cell is reached from the immediate parent
    parents = [[0 for x in range(0, m+1)] for y in range(0, n+1)]
    operations = [[0 for x in range(0, m+1)] for y in range(0, n+1)]

    copyOrReplace = insert = delete = transposition = 0

    # base conditions
    for i in range(0, n+1):
        distanceTable[i][0] = i
        operations[i][0] = "delete " + str1[i-1]
        parents[i][0] = (i-1,0)
    for j in range(0, m+1):
        distanceTable[0][j] = j
        operations[0][j] = "insert " + str2[j-1]
        parents[0][j] = (0,j-1)

    # fill tables distanceTable, operations, and parents bottom up
    for i in range(1, n+1):
        for j in range(1, m+1):

            # calculate cost of each operation
            
            # check if current characters are the same
            if(str1[i-1] == str2[j-1]):
                # cost of copy
                copyOrReplace = distanceTable[i-1][j-1]
            else:
                # cost of replace
                copyOrReplace = distanceTable[i-1][j-1] + 1
            
            # cost of insert
            insert = distanceTable[i][j-1] + 1

            # cost of delete
            delete = distanceTable[i-1][j] + 1

            # cost of transposition
            transposition = distanceTable[i-2][j-2] + 1
            
            alternatives = [copyOrReplace, insert, delete]
            
            # consider transposition only if Damerau-Levensthein edit is asked and last two characters are suitable 
            if(editType == "damerau" and i>1 and j>1 and str1[i-2] == str2[j-1] and str1[i-1] == str2[j-2]):
                alternatives.append(transposition)
            
            # find minimum distance among the alternatives
            minDist = min(alternatives)
            
            # store the operation selected
            # store the parent selected
            if (copyOrReplace == minDist):
                if(str1[i-1] == str2[j-1]):
                    operations[i][j] = "copy " + str1[i-1]
                else:
                    operations[i][j] = "replace " + str1[i-1] + " with " + str2[j-1]
                parents[i][j] = (i-1,j-1)
            elif (insert == minDist):
                operations[i][j] = "insert " + str2[j-1]
                parents[i][j] = (i,j-1)
            elif (delete == minDist):
                operations[i][j] = "delete " + str1[i-1]
                parents[i][j] = (i-1,j)
            else:
                # transposition == minDist
                operations[i][j] = "transpose " + str1[i-1] + " with " + str2[j-1]
                parents[i][j] = (i-2,j-2)

            # store the calculated minimum cost in distanceTable[i][j]
            distanceTable[i][j] = minDist

    # starting from the down-right corner of the operations, add all operations needed to reach that cell
    i = len(str1)
    j = len(str2)
    while(i>0 or j>0):
        result.append(operations[i][j])
        # find next coordinates using parents table
        i_new = parents[i][j][0]
        j_new = parents[i][j][1]
        i = i_new
        j = j_new
 
    result.reverse()
    
    return d[n][m]


# take strings whose distance is to be calculated
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# initialise a global distance table (n+1 x m+1)
distanceTable = [[0 for x in range(0, len(str2)+1)] for y in range(0, len(str1)+1)]

# initialise a global list to store sequence of operations
result = []

print("\nLevensthein edit distance:")
print(edit_distance(str1, str2, "levensthein"))
print("\nThe table:")
print(distanceTable)
print("\nSequence of operations:")
print(result)

distanceTable = [[0 for x in range(0, len(str2)+1)] for y in range(0, len(str1)+1)]
result = []

print("\nDamerau Levensthein edit distance:")
print(edit_distance(str1, str2, "damerau"))
print("\nThe table:")
print(distanceTable)
print("\nSequence of operations:")
print(result)
