# Helper to keep track of units

# available units
options = ["cm", "in", "kg", "lb(s)", "°C", "°F", "K", "ft/in"]

# valid units to convert from key to value(s)
valid_conversions = {"cm": ["ft/in", "in"],
                     "ft/in" : ["cm", "in"],
                     "in": ["cm", "ft/in"],
                     "kg": ["lb(s)"],
                     "lb(s)": ["kg"],
                     "°C": ["°F", "K"],
                     "°F": ["°C", "K"],
                     "K": ["°C", "°F"]}

# formulas to convert from key to value
conversion_formulas = {"cm": {"in": lambda cm: cm / 2.54, "ft/in":  lambda cm: cm / 2.54},
                       "in": {"cm": lambda inch: inch * 2.54, "ft/in": lambda inch: inch},
                       "ft/in": {"cm": lambda inch: inch * 2.54},
                       "kg": {"lb(s)": lambda kg: kg * 2.205},
                       "lb(s)": {"kg": lambda lb: lb / 2.205},
                       "°C": {"°F": lambda c: c * (9/5) + 32, "K": lambda c: c + 273.15},
                       "°F": {"°C": lambda f: (f - 32) * (5/9),
                              "K": lambda f: f - 32 * (5/9) + 273.15},
                       "K": {"°C": lambda k: k - 273.15, "°F": lambda k: (k - 273.15) * (9/5) + 32}}


def convert(amount, from_unit, to_unit):
    """ Converts to unit with the appropriate formula """

    return round(conversion_formulas[from_unit][to_unit](amount))


def check():
    """ Checks all keys are accounted for """

    valid_keys = valid_conversions.keys()
    valid_values = valid_conversions.values()
    valid_values = [item for sublist in valid_values for item in sublist]       # flatten list

    formula_keys = conversion_formulas.keys()
    formula_values = conversion_formulas.values()
    formula_values = [key for dic in formula_values for key in dic.keys()]          # get keys from dict list

    # add values if not in dicts
    not_in_valid_keys = [item for item in options if item not in valid_keys]
    not_in_valid_values = [item for item in options if item not in valid_values]
    not_in_formula_keys = [item for item in options if item not in formula_keys]
    not_in_formula_values = [item for item in options if item not in formula_values]

    # make sure all units are included as keys and values in both dicts
    if len(not_in_valid_keys) > 0:
        print("Units not included in valid_conversions keys: " + str(not_in_valid_keys))

    if len(not_in_valid_values) > 0:
        print("Units not included in valid_conversions values: " + str(not_in_valid_values))

    if len(not_in_formula_keys) > 0:
        print("Units not included in conversion_formulas keys: " + str(not_in_formula_keys))

    if len(not_in_formula_values) > 0:
        print("Units not included in conversion_formulas values: " + str(not_in_formula_keys))

    else:
        print("All units included")


if __name__ == '__main__':
    check()
