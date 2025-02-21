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
        weight = float(entry_weight_cal.get())
        height = float(entry_height_cal.get())
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
window.configure(bg="#DDEEFF")  # Set background color

# Frame for BMI Calculation
frame_bmi = tk.Frame(window, bg="#FFDDDD", padx=10, pady=10, bd=5, relief=tk.GROOVE)
frame_bmi.pack(pady=10)

label_bmi_title = tk.Label(frame_bmi, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#FF7777")
label_bmi_title.pack()

label_weight = tk.Label(frame_bmi, text="Enter your weight (kg):", bg="#FFDDDD")
label_weight.pack()

entry_weight = tk.Entry(frame_bmi)
entry_weight.pack()

label_height = tk.Label(frame_bmi, text="Enter your height (m):", bg="#FFDDDD")
label_height.pack()

entry_height = tk.Entry(frame_bmi)
entry_height.pack()

calculate_bmi_button = tk.Button(frame_bmi, text="Calculate BMI", command=calculate_bmi, bg="#FF7777", fg="white", font=("Arial", 10, "bold"))
calculate_bmi_button.pack(pady=5)

# Frame for Calorie Maintenance Calculation
frame_calories = tk.Frame(window, bg="#DDFFDD", padx=10, pady=10, bd=5, relief=tk.GROOVE)
frame_calories.pack(pady=10)

label_calorie_title = tk.Label(frame_calories, text="Calorie Maintenance Calculator", font=("Arial", 16, "bold"), bg="#77FF77")
label_calorie_title.pack()

label_weight_cal = tk.Label(frame_calories, text="Enter your weight (kg):", bg="#DDFFDD")
label_weight_cal.pack()

entry_weight_cal = tk.Entry(frame_calories)
entry_weight_cal.pack()

label_height_cal = tk.Label(frame_calories, text="Enter your height (m):", bg="#DDFFDD")
label_height_cal.pack()

entry_height_cal = tk.Entry(frame_calories)
entry_height_cal.pack()

label_age = tk.Label(frame_calories, text="Enter your age:", bg="#DDFFDD")
label_age.pack()

entry_age = tk.Entry(frame_calories)
entry_age.pack()

label_gender = tk.Label(frame_calories, text="Select your gender:", bg="#DDFFDD")
label_gender.pack()

gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(frame_calories, text="Male", variable=gender_var, value="Male", bg="#DDFFDD")
radio_male.pack()

radio_female = tk.Radiobutton(frame_calories, text="Female", variable=gender_var, value="Female", bg="#DDFFDD")
radio_female.pack()

label_activity = tk.Label(frame_calories, text="Select your activity level:", bg="#DDFFDD")
label_activity.pack()

activity_var = tk.StringVar(value="Sedentary")
activity_menu = tk.OptionMenu(frame_calories, activity_var, "Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active")
activity_menu.pack()

calculate_calories_button = tk.Button(frame_calories, text="Calculate Calories", command=calculate_calories, bg="#77FF77", fg="white", font=("Arial", 10, "bold"))
calculate_calories_button.pack(pady=5)

# Start the main loop
window.mainloop()
