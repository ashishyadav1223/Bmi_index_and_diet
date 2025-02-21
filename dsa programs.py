import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI and show diet plan
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = f"BMI: {bmi}\nCategory: Underweight\nDiet Plan: High-calorie diet with more carbs and protein."
        elif 18.5 <= bmi < 24.9:
            result = f"BMI: {bmi}\nCategory: Normal weight\nDiet Plan: Balanced diet with fruits, vegetables, and lean proteins."
        elif 25 <= bmi < 29.9:
            result = f"BMI: {bmi}\nCategory: Overweight\nDiet Plan: Low-calorie diet with focus on whole grains and vegetables."
        else:
            result = f"BMI: {bmi}\nCategory: Obese\nDiet Plan: Low-calorie diet with regular exercise, focus on fiber-rich foods."
        
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place the widgets
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="Enter your height (m):")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Start the main loop
window.mainloop()
