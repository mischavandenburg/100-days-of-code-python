import tkinter as tk


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    label_result.config(text=f"{km}")


window = tk.Tk()
window.title("Mile to KM converter")
window.config(padx=40, pady=40)

label_miles = tk.Label(text="Miles", font=("Iosevka", 18, "bold"))
label_is_equal = tk.Label(text="is equal to", font=("Iosevka", 18, "bold"))
label_km = tk.Label(text="Km", font=("Iosevka", 18, "bold"))
label_result = tk.Label(text="0", font=("Iosevka", 18, "bold"))

label_miles.grid(column=2, row=0)
label_is_equal.grid(column=0, row=1)
label_km.grid(column=2, row=1)
label_result.grid(column=1, row=1)


input = tk.Entry(width=7)
input.grid(column=1, row=0)

button = tk.Button(text="click meh", command=miles_to_km)
button.grid(column=1, row=2)

# this line always needs to be at the bottom of the program
window.mainloop()
