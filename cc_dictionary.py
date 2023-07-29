inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow:
        total_inches = total_inches + sum(inches_snow.values())
        print(f"Total snowfall inches: {total_inches}")
        return total_inches

print_total_snowfall(inches_snow)

thursday_snow = int(input("How many inches of snow feel on Thursday?"))
inches_snow.update({ "Thursday": thursday_snow })

print_total_snowfall(inches_snow)