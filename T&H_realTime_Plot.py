import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import os

# Serial port configuration
SERIAL_PORT = 'COM3'  # Change to your serial port
BAUD_RATE = 9600

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sensor_data.txt')

# Open a file for writing data in append mode
data_file = open(file_path, 'a')
data_file.write('Timestamp,Temperature (°C),Humidity (%)\n')  # Write headers

# Lists to store the data
timestamps = []
temperatures = []
humidities = []

# Initialize the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Initialize the figures and axes for temperature and humidity
fig_temp, ax_temp = plt.subplots(figsize=(10, 5))
fig_hum, ax_hum = plt.subplots(figsize=(10, 5))

# Initialize empty plot lines
line_temp, = ax_temp.plot([], [], 'b-', label='Temperature (°C)')
line_hum, = ax_hum.plot([], [], 'r-', label='Humidity (%)')

def init_temp():
    ax_temp.set_xlabel('Time')
    ax_temp.set_ylabel('Temperature (°C)', color='tab:blue')
    ax_temp.legend(loc='upper left')
    ax_temp.set_xlim(0, 1)  # Set initial limits for x-axis
    ax_temp.set_ylim(19, 40)  # Adjust the y-axis limit as needed
    ax_temp.grid(True)  # Enable grid
    return line_temp,

def init_hum():
    ax_hum.set_xlabel('Time')
    ax_hum.set_ylabel('Humidity (%)', color='tab:red')
    ax_hum.legend(loc='upper left')
    ax_hum.set_xlim(0, 1)  # Set initial limits for x-axis
    ax_hum.set_ylim(0, 100)  # Adjust the y-axis limit as needed
    ax_hum.grid(True)  # Enable grid
    return line_hum,

def update_data(timestamp, temperature, humidity):
    # Save data to file
    data_file.write(f"{timestamp},{temperature},{humidity}\n")
    data_file.flush()  # Ensure data is written immediately

def update_temp(frame):
    line = ser.readline().decode('utf-8').strip()
    if line:
        timestamp, value_type, value = parse_line(line)
        if timestamp:
            # Update timestamp index
            if timestamp not in timestamps:
                timestamps.append(timestamp)
                temperatures.append(None)  # Placeholder for temperature
                humidities.append(None)  # Placeholder for humidity

            index = timestamps.index(timestamp)
            if value_type == 'T':
                temperatures[index] = float(value)
            elif value_type == 'H':
                humidities[index] = float(value)

            # Update the plot lines
            line_temp.set_data(timestamps, temperatures)
            ax_temp.set_xlim(min(timestamps), max(timestamps))
            ax_temp.relim()
            ax_temp.autoscale_view()

            # Update data file
            update_data(timestamp, temperatures[index], humidities[index])

    return line_temp,

def update_hum(frame):
    line = ser.readline().decode('utf-8').strip()
    if line:
        timestamp, value_type, value = parse_line(line)
        if timestamp:
            # Update timestamp index
            if timestamp not in timestamps:
                timestamps.append(timestamp)
                temperatures.append(None)  # Placeholder for temperature
                humidities.append(None)  # Placeholder for humidity

            index = timestamps.index(timestamp)
            if value_type == 'T':
                temperatures[index] = float(value)
            elif value_type == 'H':
                humidities[index] = float(value)

            # Update the plot lines
            line_hum.set_data(timestamps, humidities)
            ax_hum.set_xlim(min(timestamps), max(timestamps))
            ax_hum.relim()
            ax_hum.autoscale_view()

            # Update data file
            update_data(timestamp, temperatures[index], humidities[index])

    return line_hum,

def parse_line(line):
    try:
        parts = line.split()
        timestamp_str = f"{parts[0]} {parts[1]}"  # e.g., "15:13:10 23/08"
        timestamp = datetime.strptime(timestamp_str, "%H:%M:%S %d/%m")
        value_type = parts[2][0]  # 'T' or 'H'
        value = parts[3]
        return timestamp, value_type, value
    except Exception as e:
        print(f"Error parsing line: {e}")
        return None, None, None

# Create the animations
ani_temp = FuncAnimation(fig_temp, update_temp, init_func=init_temp, blit=False, interval=1000)
ani_hum = FuncAnimation(fig_hum, update_hum, init_func=init_hum, blit=False, interval=1000)

# Show the plots
plt.show()

# Close the data file when finished
data_file.close()