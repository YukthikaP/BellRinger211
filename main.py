from datetime import datetime

current_time = datetime.now()
target_date = datetime(current_time.year, 2, 14, 0, 0, 0) 

if current_time > target_date:
    target_date = datetime(current_time.year + 1, 2, 14, 0, 0, 0) 

time_difference = target_date - current_time

hours_remaining = int(time_difference.total_seconds() // 3600)

print(f"Time remaining until February 14th, 12:00 AM: {hours_remaining} hours")
