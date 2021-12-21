# Handles operations from display to unit converter
import converter


def is_float(num):
    try:
        float(num)
        return True

    except ValueError:
        return False


def process_input(amt_str, from_unit, to_unit):
    result_str = "Please input number"
    is_negative = False

    if from_unit == "None":
        return "Please select a unit to convert from", False

    elif to_unit == "None":
        return "Please select a unit to convert to", False

    # elif is_float(amount_str):
    #     if amount_str[0] == '-':
    #         is_negative = True
    #         amount_str = amount_str[1:]
    #
    #     # Convert to int if possible
    #     if amount_str.isnumeric():
    #         amt = int(amount_str)
    #     else:
    #         amt = round(float(amount_str), 2)
    #
    #     if is_negative:
    #         amt = -amt


if __name__ == '__main__':
    pass