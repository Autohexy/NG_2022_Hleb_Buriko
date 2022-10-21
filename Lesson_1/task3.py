sec = int(input("Write the seconds:"))

minutes = sec // 60
# minutes
sec = sec % 60

hours = minutes // 60
# hours
minutes = minutes % 60

days = hours // 24
# days
hours = hours % 24

print("Days: ", str(days), "\nHours: ", str(hours), "\nMinutes: ", str(minutes), "\nSeconds: ", str(sec))