# Author: Khang V. Tran, Lacee Xu
# Lab5


"""
a = []
a1 = "a b c"
a2 = "d e f"
a.append(a1)
a.append(a2)
for i in range(len(a)) : print(a[i].split())

print(len("  $10"))
print("%5s" %"$10")

#print(len("Row  ========================================"))
#print(len("Row  "))

#for i in range(len(seatingChart)) : print(seatingChart[i])
#print(seatingChart[1])
#print(seatingChart[1][1])
#print(len(seatingChart[1]))

fileName = input("Enter a file name or hit Enter to use lab5input2.txt: ")
try:
    with open(fileName, "r") as infile:
        print("abc")
except FileNotFoundError as e:
    fileName = input("Enter a file name or hit Enter to use lab5input2.txt: ")
"""




"""
print the seating chart in the desired format
"""
def printChart(seatingChart):
    numRow = len(seatingChart)
    numCol = len(seatingChart[0])
    print("Price Chart".center((numCol+1)*5))
    print("Column".center((numCol+1)*5))             # print 'Column'
    print("Row  " +  "="*5*numCol)         # print Row ==================
    print(" "*5, end = "")                   
    for i in range(0, numCol) : print( "%5s"  %str(i+1), end = "")     
    print("\n")
    for row in range(numRow):
        print(str(row+1) + "  | ", end = "") 
        for col in range(numCol):
            if (seatingChart[row][col] != "X"):
                print("%5s"  %str("$" + seatingChart[row][col]), end = "")
            else:
                print("%5s"  %str(seatingChart[row][col]), end = "")
        print("\n")



"""
readChart prompt user to enter file name
if file doesn't exist, handle exception and prompt again 
if user enters, use lab5input.txt as default
call printchart() to print the seating chart
"""
def readChart():
    try:
        fileName = input("Enter a file name or hit Enter to use lab5input2.txt: ")
        if fileName == "" : fileName = "lab5input2.txt"
        seatingChart = []
        with open(fileName, "r") as infile:
            for line in infile:
                seatingChart.append(line.split())
        printChart(seatingChart)           # call printChart() function
        return(seatingChart)               # return the chart into global environment
    except FileNotFoundError as e:       
        print("Can't open" + str(e))
        readChart()


"""
this function reads in the seating chart from readChart()
It looks user to enter the their choice until stopping with 0
Exception: Non int input, input out of bound
If seat taken: announce the user
Compute, then print the total cost and number of seats
"""
def buySeat(seatingChart):
    numRow = len(seatingChart)
    numCol = len(seatingChart[0])
    takenSeat = []
    seatCount = 0
    totalPrice = 0
    print(type(int(seatingChart[0][0])))
    
    while(True):
        seat = input("Enter row,col for seat %d or enter 0 to end: " %(seatCount + 1)) 
        if(seat == "0"): break
        try:
            seat = seat.split(",")
            row = int(seat[0]) - 1
            col = int(seat[1]) - 1
            if ((row, col) in takenSeat):
                print("Sorry, that seat is not available.")
            else:
                takenSeat.append((row, col))
                seatCount += 1;
                totalPrice += int(seatingChart[row][col])
                seatingChart[row][col] = "X"
        except ValueError:
            print("Row and column must be numbers")
        except IndexError:
            print("Invalid row or column")
    
    # print price
    print("Your total: $%d" %totalPrice)
    # print location  
    print("Your %d seat(s) at " %seatCount, end = "")
    for seat in takenSeat:
        print(seat, end = " ")
    print("are marked with 'X'")
    #print updated chart
    printChart(seatingChart)





### Driver Code ###        
seatingChart = readChart()
buySeat(seatingChart)


    