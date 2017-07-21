print ("Starting program")
def find (test, target):
    print ("calling function")
    bottom = 0
    top = len(alphabet) - 1
    while (bottom<=top):
        middle = (top + bottom)//2
        midpoint = alphabet[middle]
        print("Top",top,"Bottom",bottom,"Middle",middle)
        if target < midpoint:
            top = middle - 1
            print ("going left")
        if target > midpoint:
            bottom = middle +1
            print ("going right")
        if target == midpoint:
            print ("found it")
            break

alphabet= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
"R","S","T","U","V","W","X","Y","Z"]
find(alphabet,"G")
