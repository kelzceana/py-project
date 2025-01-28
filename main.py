#Function to convert minutes to hours

def convert_min_to_hours(minutes):
    hours = minutes / 60
    print (f'{minutes} mins is {hours} hours')
    return hours

# validate user input
def validate_user_input():
    try:
        while True:
            user_input = int(input("Enter number of minutes to convert into hours: \n"))
            if user_input > 0:
                calculate_hours = convert_min_to_hours(user_input)
                print(calculate_hours)
                break # exit loop
            elif user_input == 0:
                print('The number of minutes cannot be zero')
            else:
                print('Number cannot be negative')
    except:
        print('Invalid input')



validate_user_input()