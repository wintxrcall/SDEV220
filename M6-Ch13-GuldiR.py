# Renee Guldi
# M6, Ch 13 - 13.1, 13.2, 13.3
# February 24, 2024
# SDEV220 - Prof. Chris Francis

import datetime

# 13.1 - Write the current date as a string to the text file: "today.txt"
with open("today.txt", "w") as file:
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    file.write(current_date)

# 13.2 - read the text file "today.txt" into the string "today_string"
with open("today.txt", "r") as file:
    today_string = file.read()

# 13.3 parse the date from today_string
parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")
