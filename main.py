'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''


'''
Write a Python Program that calculates the number of hours,
minutes and seconds in a number of days
'''

one_minute_in_seconds = 60    # One minute is equal to 60 Seconds
one_hour_in_seconds = one_minute_in_seconds * 60    # One hour is equal to 60 minutes which is 60 by 60 in seconds
one_day_in_seconds = one_hour_in_seconds * 24    # One day is equal to 24 hours which is 24 by 60 by 60 in seconds

# Enter the number of days to calculate the total of number seconds
days = input("Enter the number of days to calculate the total seconds: \n")
days_int = int(days)
days_in_seconds = one_day_in_seconds * days_int
if days_int == 1:
    print(f'{days} day_in_seconds is evaluated as {days_in_seconds}')
else:
    print(f'{days} days_in_seconds is evaluated as {days_in_seconds}')