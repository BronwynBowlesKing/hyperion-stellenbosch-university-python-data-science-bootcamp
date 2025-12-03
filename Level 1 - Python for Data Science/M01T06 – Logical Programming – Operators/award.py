# Triathlon Award Program
swim_time = float(input("Enter the swimming time in minutes: "))
cycle_time = float(input("Enter the cycling time in minutes: "))
run_time = float(input("Enter the running time in minutes: "))
total_time = swim_time + cycle_time + run_time

print(f"Total time to complete the triathlon: {total_time} minutes")

def determine_award(total_time):
    if 0 <= total_time <= 100:
        return "Provincial Colours"
    elif 101 <= total_time <= 105:
        return "Provincial Half Colours"
    elif 106 <= total_time <= 110:
        return "Provincial Scroll"
    elif 111 <= total_time:
        return "None"

award = determine_award(total_time)
print(f"Award: {award}")