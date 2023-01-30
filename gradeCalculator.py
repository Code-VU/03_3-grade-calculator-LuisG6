def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

try:
    hrs = float(input("Enter score: "))

    if hrs >= 0.9 and hrs <= 1.0:
        print("A")
    elif hrs >= 0.8 and hrs < 0.9:
        print("B")
    elif hrs >= 0.7 and hrs < 0.8:
        print("C")
    elif hrs >= 0.6 and hrs < 0.7:
        print("D")
    elif hrs < 0.6:
        print("F")
    else:
        print("Bad Score")
        
except:
    print("Bad score")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
