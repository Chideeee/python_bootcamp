'''
Write a Python Program that calculates the number of hours,
minutes and seconds in a number of days
'''

one_minute_in_seconds = 60  # One minute is equal to 60 Seconds
one_hour_in_seconds = one_minute_in_seconds * 60  # One hour is equal to 60 minutes which is 60 by 60 in seconds
one_day_in_seconds = one_hour_in_seconds * 24  # One day is equal to 24 hours which is 24 by 60 by 60 in seconds


def days_to_secs():
    # Enter the number of days to calculate the total of number seconds
    days = input("Enter the number of days to calculate the total seconds: \n")
    days_int = int(days)
    days_in_seconds = one_day_in_seconds * days_int
    if days_int <= 0:
        print("Input can only accept a positive number, kindly enter a positive number")
    elif days_int == 1:
        print(f'{days} day is evaluated as {days_in_seconds} seconds')
    else:
        print(f'{days} days is evaluated as {days_in_seconds} seconds')

# function without arguments


days_to_secs()
days_to_secs()
days_to_secs()