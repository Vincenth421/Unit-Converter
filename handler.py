# Handles operations from display to unit converter
import units


def is_float(num):
    try:
        float(num)
        return True

    except ValueError:
        return False


def convert(amt, from_unit, to_unit):
    return units.conversion_formulas[from_unit][to_unit](amt)


def str_to_num(amt_str, integer):
    """Converts amount string to a number. If integer is true, convert to int. Else convert to float."""

    if is_float(amt_str):

        is_negative = False
        if amt_str[0] == '-':
            is_negative = True
            amt_str = amt_str[1:]

        # Convert to int
        if integer and not amt_str.isnumeric():
            return 0, False

        if amt_str.isnumeric():
            amt = int(amt_str)
        else:
            amt = round(float(amt_str), 2)

        if is_negative:
            amt = -amt

        return amt, True

    else:
        return 0, False


def process_input(amt_str, from_unit, to_unit):

    if from_unit == "None":
        return "Please select a unit to convert from", False

    elif to_unit == "None":
        return "Please select a unit to convert to", False

    elif from_unit == "ft/in":
        splitted = str(amt_str).split("/")
        if len(splitted) != 2:
            return "Invalid feet and inches", False

        ft_str = splitted[0]
        inch_str = splitted[1]

        ft, success = str_to_num(ft_str, True)
        if not success:
            return "Feet must be integer", False

        inch, success = str_to_num(inch_str, True)
        if not success:
            return "Inches must be integer", False

        inches = ft * 12 + inch
        result = round(convert(inches, from_unit, to_unit))

        return str(ft) + " ft " + str(inch) + " in is " + str(result) + " " + to_unit, True

    elif to_unit == "ft/in":
        amt, success = str_to_num(amt_str, False)
        if not success:
            return "Please input number", False
        else:
            inches = round(convert(amt, from_unit, to_unit))
            return str(amt) + " " + from_unit + " is " + str(inches // 12) + " ft " + str(inches % 12) + \
                " in", True

    else:
        amt, success = str_to_num(amt_str, False)
        if not success:
            return "Please input number", False
        else:
            result = round(convert(amt, from_unit, to_unit))
            return str(amt) + " " + from_unit + " is " + str(result) + " " + to_unit, True


if __name__ == '__main__':
    pass
