# Question:Q.1. Write a program that asks the user how many days are in a particular month, and what day of
# the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for
# that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
#         1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24  25
# 26 27 28 29 30







def print_calendar(days_in_month, starting_day):
    print("S  M  T  W  T  F  S")

    # Print leading spaces for the first week
    print("   " * starting_day, end='')

    # Initialize the day counter
    current_day = 1

    # Print the first week
    for i in range(starting_day, 7):
        print(f"{current_day:2}", end=" ")
        current_day += 1

    print()

    # Print the rest of the weeks
    while current_day <= days_in_month:
        for i in range(0, 7):
            if current_day > days_in_month:
                break
            print(f"{current_day:2}", end=" ")
            current_day += 1
        print()


days_in_month = int(input("Enter the number of days in the month: "))
starting_day = int(input("Enter the starting day of the week (0 for Sunday, 1 for Monday, etc.): "))

print_calendar(days_in_month, starting_day)
