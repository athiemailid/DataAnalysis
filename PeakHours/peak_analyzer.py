import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rnd
from scipy.stats import norm

# read the simulation data from the file and return list of dictionaries item
def read_peak_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError as e:
        print(f"File not found: {filename}")
        return None

filename = "wait_times.csv"
wait_times_data = read_peak_data(filename)

wait_times = [float(x[0]) for x in wait_times_data]

mean = np.mean(wait_times)
median = np.median(wait_times)
std_dev = np.std(wait_times)
percentile_90 = np.percentile(wait_times, 90)
long_waits = [time for time in wait_times if time > 20]  # customers who waited more than 20 minutes.
percent_long_waits = (len(long_waits) / len(wait_times)) * 100

print(f"Mean: {mean:.2f} minutes")
print(f"Median: {median:.2f} minutes")
print(f"Standard Deviation: {std_dev:.2f} minutes")
print(f"90th Percentile: {percentile_90:.2f} minutes")
print(f"Percentage of customers waiting over 20 minutes: {percent_long_waits:.2f}%")

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)
plt.title("Simulated Customer Wait Times")
plt.xlabel("Wait Time (minutes)")
plt.ylabel("Probability Density")
plt.show()