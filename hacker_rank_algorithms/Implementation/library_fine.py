'''
The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
If the book is returned in the same calendar month as the expected return date, Fine = 15 Hackos × Number of late days
If the book is not returned in the same calendar month but in the same calendar year as the expected return date, Fine = 500 Hackos × Number of late months
If the book is not returned in the same calendar year, the fine is fixed at 10000 Hackos.

SAMPLE INPUT:
9 6 2015
6 6 2015
'''

def fine(actual, expected):
    ''' takes two dates and returns library fee based on how overdue it is
    '''
    i1 = actual.index(' ')
    i2 = actual.index(' ', i1 + 1)
    a_day = int(actual[0:i1])
    a_month = int(actual[i1 +1: i2])
    a_year = int(actual[i2 +1:])
    i3 = expected.index(' ')
    i4 = expected.index(' ', i3 + 1)
    e_day = int(expected[0:i3])
    e_month = int(expected[i3 +1: i4])
    e_year = int(expected[i4 +1:])
    if a_year > e_year:
        return 10000
    elif a_month > e_month and a_year == e_year:
        return (a_month - e_month) * 500
    elif a_day > e_day and a_month == e_month:
        return (a_day - e_day) *15
    else:
        return 0

actual = input()
expected = input()
print(fine(actual, expected))
