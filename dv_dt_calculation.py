def calculate_time(speed, distance):
    time_in_hours = distance / speed
    time_in_seconds = time_in_hours * 3600  # Converting hours to seconds
    return time_in_seconds, distance

def after_five_sec(speed, distance):
    total_time, distance = calculate_time(speed, distance)
    total_intervals = total_time / 5
    km_per_second = distance / total_time
    km_in_5_seconds = km_per_second * 5

    print("Total time taken:", total_time, "seconds")
    print("Total T for after every 5 seconds:", total_intervals)
    print('Every 5 seconds, the EV will travel {:.5f} km'.format(km_in_5_seconds))
    return total_intervals, km_in_5_seconds

def calculate_acceleration(speed, distance):
    total_intervals, km_in_5_seconds = after_five_sec(speed, distance)
    time_in_seconds, _ = calculate_time(speed, distance)
    distance_t5 = 0
    distance_t10 = 5
    sum_dv_dt = 0

    while distance_t5 <= time_in_seconds:
        distance_t5 += 5
        distance_t10 += 5
        x5 = (km_in_5_seconds / 5) * distance_t5
        x6 = (km_in_5_seconds / 5) * distance_t10
        dv_dt = (x6 - x5) / 5  # Calculate acceleration
        sum_dv_dt += dv_dt  # km/h^2
    ac = sum_dv_dt * (1 / 3.6)  # m/s
    print('dv/dt= {:.5f} m/s'.format(ac))  # m/s
    return ac

# Input
speed = float(input('Enter EV speed (km/h): '))
distance = float(input('Enter your distance (km): '))

calculate_acceleration(speed, distance)


# Calculate over all equation
import math
M = 1800  # value for Mass
m = 1.1   # value for mass factor
g = 9.8  # Acceleration due to gravity (m/s^2)
f = 0.01  #
alpha_deg = float (input('Enter Angle degree value:'))  # value for alpha in degrees
p = 1.205  # value for p
c = 0.6  #
A = 3.50 #
v0 = speed  # vehicle speed
dv_dt0=calculate_acceleration(speed, distance)
d=114 #total distance


# Calculate cosine and sine of alpha
cos_alpha=math.cos(math.radians(alpha_deg))
sin_alpha=math.sin(math.radians(alpha_deg))

# Calculate the equation
E = (1/3600) * (M * g * (f * cos_alpha + sin_alpha) + 0.0386 * (p * c * A * v0**2) + (M + m) * dv_dt0)*d

print("Toral Energy Consumption={:.5f} kWh".format(E))
