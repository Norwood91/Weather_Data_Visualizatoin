import csv
import matplotlib.pyplot as plt
from datetime import datetime
# ------------------------------------------------ Get data from CSV & use it -------------------------------------
# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as data:
    reader = csv.reader(data)
    header_row = next(reader)

    # Get high temperatures from this file
    dates, high_temps, low_temps = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            high_temps.append(high)
            low_temps.append(low)

# ------------------------------------------------ Visualization Code ---------------------------------------------
# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, high_temps, c='red', alpha=0.5)
ax.plot(dates, low_temps, c='blue', alpha=0.5)
ax.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)

# Format the plot
ax.set_title('Sitka, Alaska Daily High and Low Temperatures, 2018')
ax.set_xlabel('', fontsize=16)
# The autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

