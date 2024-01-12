'''
one_minute_in_seconds = 60  # One minute is equal to 60 Seconds
one_hour_in_seconds = one_minute_in_seconds * 60  # One hour is equal to 60 minutes which is 60 by 60 in seconds
one_day_in_seconds = one_hour_in_seconds * 24  # One day is equal to 24 hours which is 24 by 60 by 60 in seconds


# Enter the number of days to calculate the total of number seconds
days = input("Enter the number of days to calculate the total seconds: \n")
days_int = int(days)
days_in_seconds = one_day_in_seconds * days_int
if days_int == 1:
    print(f'{days} day_in_seconds is evaluated as {days_in_seconds}')
else:
    print(f'{days} days_in_seconds is evaluated as {days_in_seconds}')
'''

'''
Write a Python Program that calculates the number of hours,
minutes and seconds in a number of days
'''
'''
one_minute_in_seconds = 60  # One minute is equal to 60 Seconds
one_hour_in_seconds = one_minute_in_seconds * 60  # One hour is equal to 60 minutes which is 60 by 60 in seconds
one_day_in_seconds = one_hour_in_seconds * 24  # One day is equal to 24 hours which is 24 by 60 by 60 in seconds


def days_to_secs(days):
    # Enter the number of days to calculate the total of number seconds
    #days = input("Enter the number of days to calculate the total seconds: \n")
    #days_int = int(days)
    #days_in_seconds = one_day_in_seconds * days_int
    days_in_seconds = one_day_in_seconds * days
    if days == 1:
        print(f'{days} day_in_seconds is evaluated as {days_in_seconds}')
    else:
        print(f'{days} days_in_seconds is evaluated as {days_in_seconds}')


days_to_secs(12)
days_to_secs(20)
'''

one_minute_in_seconds = 60  # One minute is equal to 60 Seconds
one_hour_in_seconds = one_minute_in_seconds * 60  # One hour is equal to 60 minutes which is 60 by 60 in seconds
one_day_in_seconds = one_hour_in_seconds * 24  # One day is equal to 24 hours which is 24 by 60 by 60 in seconds


def days_to_secs():
    # Enter the number of days to calculate the total of number seconds
    days = input("Enter the number of days to calculate the total seconds: \n")
    days_int = int(days)
    days_in_seconds = one_day_in_seconds * days_int
    if days_int == 1:
        print(f'{days} day_in_seconds is evaluated as {days_in_seconds}')
    else:
        print(f'{days} days_in_seconds is evaluated as {days_in_seconds}')


days_to_secs()
days_to_secs()