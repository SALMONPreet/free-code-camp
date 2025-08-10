def add_time(start, duration, starting_day=None):
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    
    dur_hour, dur_minute = map(int, duration.split(':'))

    
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60

    
    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // 24
    end_hour = end_hour % 24

    
    if end_hour == 0:
        final_hour = 12
        final_period = "AM"
    elif end_hour < 12:
        final_hour = end_hour
        final_period = "AM"
    elif end_hour == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = end_hour - 12
        final_period = "PM"

    
    final_minute = f"{end_minute:02}"

    
    if starting_day:
        index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(index + days_later) % 7]
        day_output = f", {new_day}"
    else:
        day_output = ""

    
    if days_later == 0:
        day_suffix = ""
    elif days_later == 1:
        day_suffix = " (next day)"
    else:
        day_suffix = f" ({days_later} days later)"

    
    new_time = f"{final_hour}:{final_minute} {final_period}{day_output}{day_suffix}"
    return new_time
