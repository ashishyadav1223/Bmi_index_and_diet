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

# Function to calculate daily calorie maintenance
def calculate_calories():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        age = int(entry_age.get())
        activity_level = activity_var.get()

        # Simple BMR calculation using the Mifflin-St Jeor Equation
        if gender_var.get() == "Male":
            bmr = 10 * weight + 6.25 * height * 100 + 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height * 100 + 5 * age - 161
        
        # Adjusting BMR based on activity level
        if activity_level == "Sedentary":
            calories = bmr * 1.2
        elif activity_level == "Lightly active":
            calories = bmr * 1.375
        elif activity_level == "Moderately active":
            calories = bmr * 1.55
        elif activity_level == "Very active":
            calories = bmr * 1.725
        else:
            calories = bmr * 1.9
        
        calories = round(calories, 2)
        result = f"Calorie Maintenance: {calories} calories/day"
        messagebox.showinfo("Calorie Maintenance", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight, height, and age.")

# Create the main window
window = tk.Tk()
window.title("BMI & Calorie Calculator")

# BMI Section
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="Enter your height (m):")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

calculate_bmi_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_bmi_button.pack()

# Calorie Maintenance Section
label_age = tk.Label(window, text="Enter your age:")
label_age.pack()

entry_age = tk.Entry(window)
entry_age.pack()

label_gender = tk.Label(window, text="Select your gender:")
label_gender.pack()

gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
radio_female.pack()

label_activity = tk.Label(window, text="Select your activity level:")
label_activity.pack()

activity_var = tk.StringVar(value="Sedentary")
activity_menu = tk.OptionMenu(window, activity_var, "Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active")
activity_menu.pack()

calculate_calories_button = tk.Button(window, text="Calculate Calories", command=calculate_calories)
calculate_calories_button.pack()

# Start the main loop
window.mainloop()
