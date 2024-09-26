import calendar

# Define the starting month and total years
start_month = 2  # May
total_years = 2  # Number of years (including the first partial year)
total_months = 12 * total_years  # Total months to loop through
print(total_months)

# Loop through all months starting from the specified month
for i in range(total_months):
    # # Calculate the current month number, wrapping around after December
    month_num = (start_month + i - 1) % 12 + 1
    # # Calculate the year by determining how many times we've gone through 12 months
    year = 1 + (start_month + i - 1) // 12

    if year > total_years:
        break
    # # Get the month name
    # month_name = calendar.month_name[month_num]
    # print(f"Year {year}, Month {month_num}: {month_name}")

    print(i, month_num, year)
