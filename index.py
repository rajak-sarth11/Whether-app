import tkinter as tk
from tkinter import messagebox
import requests
def get_weather():
    city = city_entry.get()
    api_key = ""  # Replace with your valid API key
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        url = f""
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"] - 273.15  # Kelvin to Celsius
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = (
                f"Weather: {weather}\n"
                f"Temperature: {temp:.2f}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
            )
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", data.get("message", "Unknown error occurred"))
    except Exception as e:
        messagebox.showerror("Error", str(e))
# city_name = 'Pune'
# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=66a7f32bccab33eefcb5b9a8a9251a0a").json()
# print(data)

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#dff6ff")  # Light blue background

# Title Label
tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#dff6ff", fg="#0077b6").pack(pady=20)

# City Entry Label
tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="#dff6ff").pack(pady=(5, 0))

# Entry Field
city_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief="groove")
city_entry.pack(pady=10)
city_entry.focus()

# Get Weather Button
tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#0077b6", fg="white", bd=0, padx=10, pady=5, command=get_weather).pack(pady=10)

# Result Display Frame
result_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
result_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Weather Result Label
result_label = tk.Label(result_frame, text="", font=("Arial", 13), bg="white", fg="#333", justify="left")
result_label.pack(padx=10, pady=10, anchor="w")

# Run main loop
root.mainloop()
