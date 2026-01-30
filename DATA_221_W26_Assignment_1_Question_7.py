'''
Question 7

Write a function that converts a given number of seconds since midnight into:
• Hours
• Minutes
• Seconds
• AM or PM
The function should return a formatted string. If the input is invalid, return an appropriate
message.

'''

def convert_seconds_to_clock_time(seconds):

    minutes = seconds // 60
    hours = minutes // 60

    if seconds < 0:
        return "Cannot convert negative seconds."

    elif seconds > 86400:
        return "Cannot convert more than 24 hours (86400 seconds)."

    elif seconds <= 43200:
        return f"{hours} {minutes % 60:02d} {seconds % 60:02d} AM"

    elif seconds > 43200:
        hours -= 12
        return f"{hours} {minutes % 60:02d} {seconds % 60:02d} PM"

print(convert_seconds_to_clock_time(-1))
print(convert_seconds_to_clock_time(0))
print(convert_seconds_to_clock_time(387))
print(convert_seconds_to_clock_time(34567))
print(convert_seconds_to_clock_time(43200))
print(convert_seconds_to_clock_time(67887))
print(convert_seconds_to_clock_time(86400))
print(convert_seconds_to_clock_time(86401))


