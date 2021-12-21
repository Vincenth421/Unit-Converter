# Generates the display
import tkinter as tk
import handler
import converter


def generate_window():
    """ Generate the GUI and handles passing in unit for conversion """

    def enter_press(_):
        """Clicks convert button when enter key is pressed."""
        convert_button_click()

    def convert_button_click():
        """Gets amount and options and passes to the handler. Displays the result of the conversion."""

        amt_str = input_box.get("1.0", "end-1c").strip()    # get value in text box, ignoring newline character
        from_unit = from_variable.get()
        to_unit = to_variable.get()

        ret, clear = handler.process_input(amt_str, from_unit, to_unit)

        # update the result and clear input text box
        result_label.configure(text=ret)

        if clear:
            input_box.delete("1.0", tk.END)

    def update_dropdown(variable, dropdown, unit):
        # clear "to unit" dropdown options
        variable.set("")
        dropdown["menu"].delete(0, "end")

        # Insert list of new options (tk._setit hooks them up to var)
        new_choices = converter.get_valid_options(unit)
        for choice in new_choices:
            dropdown["menu"].add_command(label=choice, command=tk._setit(variable, choice))

        # Set the default value
        variable.set(new_choices[0])

    def update_to_dropdown(input_unit):
        nonlocal prev_from
        if prev_from != from_variable.get():
            update_dropdown(to_variable, to_dropdown, input_unit)
            prev_from = from_variable.get()

    def update_from_dropdown(input_unit):
        """Changes "from" unit and updates "to" dropdown if "to" dropdown is selected first"""
        if from_variable.get() == "None":
            valid_choices = converter.get_valid_options(input_unit)
            input_unit = valid_choices[0]
            from_variable.set(input_unit)
            update_dropdown(to_variable, to_dropdown, input_unit)

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
    from_options = converter.get_options()
    from_variable = tk.StringVar(main_frame)
    from_variable.set("None")
    prev_from = from_variable.get()
    from_dropdown = tk.OptionMenu(main_frame, from_variable, *from_options, command=update_to_dropdown)
    from_dropdown.pack(padx=2, side=tk.LEFT)

    to_label = tk.Label(main_frame, text="to")
    to_label.pack(side=tk.LEFT)

    # set to unit dropdown
    to_options = converter.get_options()
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
