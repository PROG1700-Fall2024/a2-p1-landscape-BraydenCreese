#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: W0491583
#Student Name: Brayden Creese

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # init base charge
    baseCharge = 1000

    # getting user input for all vars. checking for invalid inputs
    while True:
        try:
            houseNum = int(input("Enter house number: "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid house number.")

    while True:
        try:
            propertyDepth = int(input("Enter property depth (feet): "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for property depth (feet).")

    while True:
        try:
            propertyWidth = int(input("Enter property width (feet): "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid number for property width (feet).")

    # checking for only the three types of grass
    while True:
        grassType = input("Enter Type of grass (fescue, bentgrass, campus): ").lower()
        if grassType in ['fescue', 'bentgrass', 'campus']:
            break
        else:
            print("Invalid Input! Please enter a valid house number.")

    while True:
        try:
            treesNum = int(input("Enter number of trees: "))
            break
        except ValueError:
            print("Invalid Input! Please enter a valid house number.")


    #getting cost per tree
    treeCost = treesNum * 100
    # calc for serface area cost
    surfacArea = propertyDepth * propertyWidth

    # adding $500 fee if users surface area is over 5000
    if surfacArea > 5000:
        baseCharge += 500

    # adding cost based off users inputed grass type
    if grassType == 'fescue':
        sqftCost = 0.05
    elif grassType == 'bentgrass':
        sqftCost = 0.02
    elif grassType == 'campus':
        sqftCost = 0.01
    
    # final cacls for grass cost and over all total cost
    grassCost = surfacArea * sqftCost
    totalCost = baseCharge + grassCost + treeCost


    # displaying the output to the user
    print(f"\nTotal cost for house {houseNum} is ${totalCost:.2f}")

    # YOUR CODE ENDS HERE

main()