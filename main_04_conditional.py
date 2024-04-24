speed_limit_max = 100
speed_limit_min = 60

car_speed = 10  # Change this value to see how the printed message changes.

print(f"\nYou're driving at {car_speed} km/h.")

if car_speed > speed_limit_max:  # If you are above the speed limit, then do this.
    print(f"Please slow down to {speed_limit_max} km/h.")
elif car_speed < speed_limit_min:  # Else if the above statement was false, and you are below the speed limit do this.
    print(f"Please speed up to {speed_limit_min} km/h.")
else:  # Else if the above statements were false, do this.
    print("Thank you for driving safely.")

# This is a new if statement, so it will execute when the car_speed is 0 regardless of the logic in the above block.
if car_speed == 0:
    print("\nIf your car has stopped working,\nplease turn on your hazard lights\nwhile waiting for assistance.")
