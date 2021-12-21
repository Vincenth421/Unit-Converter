import tkinter as tk
import units


def is_float(num):
    try:
        float(num)
        return True

    except ValueError:
        return False


def generate_window():
    """ Generate the GUI and handles passing in unit for conversion """

    def enter_press(_):
        convert_button_click()

    def convert_button_click():
        """ Parses number and converts on button click """

        amount_str = input_box.get("1.0", "end-1c").strip()    # get value in text box, ignoring newline character
        from_unit = from_variable.get()
        to_unit = to_variable.get()
        result_str = "Please input number"
        is_negative = False

        if from_unit == "None":
            result_str = "Please select a unit to convert from"

        elif to_unit == "None":
            result_str = "Please select a unit to convert to"

        elif is_float(amount_str):
            if amount_str[0] == '-':
                is_negative = True
                amount_str = amount_str[1:]

            # Convert to int if possible
            if amount_str.isnumeric():
                amt = int(amount_str)
            else:
                amt = round(float(amount_str), 2)

            if is_negative:
                amt = -amt

            ret = units.convert(amt, from_unit, to_unit)
            result_str = str(amt) + " " + from_unit + " is "

            if to_unit == "in":
                result_str += str(ret // 12) + " ft " + str(ret % 12) + " in"
            else:
                result_str = + str(ret) + " " + to_unit

            input_box.delete("1.0", tk.END)

        else:
            input_box.delete("1.0", tk.END)

        # update the result and clear input text box
        result_label.configure(text=result_str)
        return

    def update_to_dropdown(input_unit):
        """ Updates to dropdown when user selects a unit in from dropdown"""

        # clear "to unit" dropdown options
        to_variable.set("")
        to_dropdown["menu"].delete(0, "end")

        # Insert list of new options (tk._setit hooks them up to var)
        new_choices = to_valid_opts[input_unit]
        for choice in new_choices:
            to_dropdown["menu"].add_command(label=choice, command=tk._setit(to_variable, choice))

        # Set the default value
        to_variable.set(new_choices[0])
        return

    def update_from_dropdown(input_unit):
        """ Updates from dropdown when user selects a unit in to dropdown"""

        # clear "from unit" dropdown options
        from_variable.set("")
        from_dropdown["menu"].delete(0, "end")

        # Insert list of new options (tk._setit hooks them up to var)
        new_choices = to_valid_opts[input_unit]
        for choice in new_choices:
            from_dropdown["menu"].add_command(label=choice, command=tk._setit(to_variable, choice))

        # Set the default value
        from_variable.set(new_choices[0])
        return

    root = tk.Tk()
    root.minsize(410, 100)
    root.bind("<Return>", enter_press)      # Press convert button when enter key pressed
    root.title("Unit Converter")

    title_label = tk.Label(root, text="Welcome to Unit Converter")
    title_label.pack(pady=5)

    # Frame to hold text box, unit dropdowns, and convert button
    main_frame = tk.Frame(root, width=200)
    main_frame.pack(fill=tk.X)

    input_box = tk.Text(main_frame, width=20, height=1)
    input_box.pack(padx=5, pady=5, side=tk.LEFT)

    # set from unit dropdown
    from_options = units.options
    from_variable = tk.StringVar(main_frame)
    from_variable.set("None")
    from_dropdown = tk.OptionMenu(main_frame, from_variable, *from_options, command=update_to_dropdown)
    from_dropdown.pack(padx=2, side=tk.LEFT)

    to_label = tk.Label(main_frame, text="to")
    to_label.pack(side=tk.LEFT)

    # set to unit dropdown
    to_options = units.options
    to_valid_opts = units.valid_conversions
    to_variable = tk.StringVar(main_frame)
    to_variable.set("None")
    to_dropdown = tk.OptionMenu(main_frame, to_variable, *to_options, command=update_from_dropdown)
    to_dropdown.pack(padx=2, side=tk.LEFT)

    convert_button = tk.Button(main_frame, text="Convert!", command=convert_button_click)
    convert_button.pack(padx=2, side=tk.LEFT)

    result_label = tk.Label(root)
    result_label.pack()

    return root


if __name__ == "__main__":
    pass
