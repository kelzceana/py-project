#function that coverts days to unit
def days_to_unit(num_of_days, unit):
    if unit == 'hours':
        print(f'{num_of_days} days is {num_of_days * 24} hours.')
    elif unit == 'minutes':
        print(f'{num_of_days} days is {num_of_days * 24 * 60} minutes.')


def validate_and_convert():
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        if user_input_number > 1:
           calculated_val = days_to_unit(user_input_number, days_and_unit_dictionary['units'])
           print(calculated_val)
        elif user_input_number == 0:
            print('Number cannot be 0.')
        else:
            print('Please enter a valid number.')
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = input('Enter number of days and conversion unit \n')
days_and_unit_list = user_input.split(':')
print(days_to_unit)
days_and_unit_dictionary = {'days': days_and_unit_list[0], 'units': days_and_unit_list[1]}
validate_and_convert()