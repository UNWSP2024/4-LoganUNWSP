# Logan H's Monthly Average Rain Calculator

# 1st, ask # of years
years = int(input("Enter the number of years: "))

# this will keep track of the total rainfall throughout the whole program starting at 0
total_rainfall = 0

# 2nd, get the year/outer loop
# (ask from year one to the last year)
for year in range(1, years + 1):
    # 3rd, get the month/inner loop
    #  (asks rainfall 12 times, every 12 times ticks the outer loop by 1, sending it to the next range.)
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
        total_rainfall += rainfall

# 4th, Math and Finale
# get the number of months by doing 3rd grade math that doesn't need to be explained
total_months = years * 12

# get the average rainfall amount by doing 4th grade math that could be explained but wouldn't be
average_rainfall = total_rainfall / total_months

# display everything this just did and the total rainfall from the beginning.
print("Total months:", total_months)
print("Total inches of rainfall:", total_rainfall)
print("Average rainfall per month:", round(average_rainfall, 2))
