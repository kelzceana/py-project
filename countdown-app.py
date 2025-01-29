#This program accepts a user's input of goal and deadline and lets you know how long you have left ill your deadline
import datetime


def time_to_deadline(deadline):
    #subtract the current date from the deadline
    time_left = deadline - datetime.datetime.now()
    if time_left.days < 0:
        print (f'you are {abs(time_left.days)} days past the deadline')
    elif time_left.days == 0:
        print ('Congratulations, you met your deadline')
    else:
        print(f'you have {time_left.days} days to your deadline')

user_input = input('Enter your goal with a deadline separated by a colon <goal>:<dd.mm.yyyy> \n')
input_list = user_input.split(':')
count_down_dictionary = {'goal': input_list[0], 'deadline': input_list[1]}
user_deadline = datetime.datetime.strptime(count_down_dictionary['deadline'], '%d.%m.%Y')
#print(deadline)
time_to_deadline(user_deadline)

