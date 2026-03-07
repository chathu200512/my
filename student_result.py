def main():
    # Ask for student's name
    name = input("Enter student's name: ")

    # Ask for 3 subject marks
    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))
        
        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3
        
        print(f"\nStudent Name: {name}")
        print(f"Average Mark: {average:.2f}")
        
        # Display grade based on average
        if average >= 75:
            print("Result: Grade A")
        elif average >= 60:
            print("Result: Grade B")
        elif average >= 40:
            print("Result: Grade C")
        else:
            print("Result: Fail")
            
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")

if __name__ == "__main__":
    main()
