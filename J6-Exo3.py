from datetime import *


timezone_offset = 5
ny_timezone = timezone(timedelta(hours=-5))

current_date = datetime.now()
date_in_xx_days = current_date + timedelta(days=42)
time_in_3_hours = current_date + timedelta(hours=3)
current_time = time()
print(current_date)
print(current_time)
print(date_in_xx_days)
print("Dans 3 heures ils sera : " + time_in_3_hours.strftime("%X"))
print(f"Dans la timezone {ny_timezone} il est : " + datetime.now(ny_timezone).strftime("%X"))