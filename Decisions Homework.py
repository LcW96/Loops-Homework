'''Create a program that calculates the amount of time saved if you are
traveling with an average speed that is above the speed-limit as compared to
traveling with an average speed exactly at the speed-limit. As the user for
the average speed in miles per hour, speed limit in miles per hour and distance travelled in miles. THE TIME SAVED SHOULD BE REPORTED IN MINUTES. Create a screenshot of output where your average speed is 80 mph, speed limit is 60 mph and distance travelled is 100 miles.
Your answer should indicate that you saved 25 minutes'''

def calculate_time_saved(avg_speed, speed_limit, distance):
    # Calculate time in hours
    time_at_avg_speed = distance / avg_speed
    time_at_speed_limit = distance / speed_limit
    
    # Convert time to minutes and calculate time saved
    time_saved = (time_at_speed_limit - time_at_avg_speed) * 60
    return time_saved

def main():
    try:
        # Input values from user
        avg_speed = float(input("Enter the average speed (in mph): "))
        speed_limit = float(input("Enter the speed limit (in mph): "))
        distance = float(input("Enter the distance traveled (in miles): "))
        
        # Compute time saved
        time_saved = calculate_time_saved(avg_speed, speed_limit, distance)
        
        # Output the result
        print(f"Time saved: {time_saved:.2f} minutes")
        
 
        #except ValueError:
        print("Invalid input! Please enter numeric values for speed and distance.")

if __name__ == "__main__":
    main()

