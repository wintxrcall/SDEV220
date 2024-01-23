seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
seconds_per_day = seconds_per_hour * 24
flt_pt_div = seconds_per_day / seconds_per_hour
intg_div = seconds_per_day // seconds_per_hour

print(flt_pt_div)
print(intg_div)

print("3.6: \n Yes, the float point and integer division returned the same result aside from the end .0. /n However, the results returned are still different variable types, Float & Integer.")
