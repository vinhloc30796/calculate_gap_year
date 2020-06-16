def is_leap_year(year):
    """
    Check if input `year` is a leap year
    Input:
    - year (int)
    Output:
    - leap (boolean): True if is leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def next_five_leap(year):
    """Return the next five leap years after input `year`
    Input:
    - year (int)
    Output:
    - result (list of int): list of 5 years that are leap years
    """
    result = {}
    count = 0
    while count < 5:
        year += 1
        if is_leap_year(year):
            result[year] = True
            count += 1
        if year % 100 == 0 and not is_leap_year(year):
            result[year] = False
    return result
