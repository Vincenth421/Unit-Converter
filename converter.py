# Handles units and conversion

# Available units. Used as reference to make sure all units accounted for in the following dictionaries.
options = ["cm", "ft/in", "in", "kg", "lb(s)", "°C", "°F", "K"]

# valid units to convert from key to value(s). Used as reference for conversion_formulas.
valid_conversions = {"cm": ["ft/in", "in"],
                     "ft/in": ["cm", "in"],
                     "in": ["cm", "ft/in"],
                     "kg": ["lb(s)"],
                     "lb(s)": ["kg"],
                     "°C": ["°F", "K"],
                     "°F": ["°C", "K"],
                     "K": ["°C", "°F"]}

# formulas to convert from key to value
conversion_formulas = {"cm": {"in": lambda cm: cm / 2.54, "ft/in": lambda cm: cm / 2.54},
                       "ft/in": {"cm": lambda inch: inch * 2.54, "in": lambda inch: inch},
                       "in": {"cm": lambda inch: inch * 2.54, "ft/in": lambda inch: inch},
                       "kg": {"lb(s)": lambda kg: kg * 2.205},
                       "lb(s)": {"kg": lambda lb: lb / 2.205},
                       "°C": {"°F": lambda c: c * (9/5) + 32, "K": lambda c: c + 273.15},
                       "°F": {"°C": lambda f: (f - 32) * (5/9),
                              "K": lambda f: f - 32 * (5/9) + 273.15},
                       "K": {"°C": lambda k: k - 273.15, "°F": lambda k: (k - 273.15) * (9/5) + 32}}


def convert(amount, from_unit, to_unit):
    """ Converts to unit with the appropriate formula """

    return round(conversion_formulas[from_unit][to_unit](amount))


def check_keys():
    """ Checks all keys are accounted for. Uses options array as reference """

    valid_keys = valid_conversions.keys()

    formula_keys = conversion_formulas.keys()

    # add values if not in dicts
    not_in_valid_keys = [item for item in options if item not in valid_keys]
    not_in_formula_keys = [item for item in options if item not in formula_keys]

    # make sure all units are included as keys and values in both dicts
    if len(not_in_valid_keys) > 0:
        print("Units not included in valid_conversions keys: " + str(not_in_valid_keys))

    if len(not_in_formula_keys) > 0:
        print("Units not included in conversion_formulas keys: " + str(not_in_formula_keys))

    else:
        print("All units included")


def check_valid_formulas():
    """Checks valid_conversion values match with conversion_formula value dictionaries"""
    ret_dict = {}

    for k, v in valid_conversions.items():
        formula_dict = conversion_formulas[k]
        not_in_list = [key for key in v if key not in formula_dict]

        if len(not_in_list) != 0:
            ret_dict[k] = not_in_list

    if len(ret_dict) != 0:
        print("Unmatched units in conversion_formula: " + str(ret_dict))

    else:
        print("All units matched")


def get_valid_options(from_str):
    return valid_conversions[from_str]


def get_options():
    return options


if __name__ == '__main__':
    check_keys()
    check_valid_formulas()
