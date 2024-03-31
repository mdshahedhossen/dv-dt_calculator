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

# Input
speed = float(input('Enter EV speed (km/h): '))
distance = float(input('Enter your distance (km): '))

calculate_acceleration(speed, distance)