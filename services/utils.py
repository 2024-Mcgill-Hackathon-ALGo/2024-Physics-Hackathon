import math


def convert_year_float(year_float):
    # Constants
    days_in_year = 365
    months_in_year = 12
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60
    days_in_month = days_in_year / months_in_year  # Approx. 30.44 days/month

    # Extract years
    years = int(year_float)
    remaining_year_fraction = year_float - years

    # Convert remaining fraction to months
    total_months = remaining_year_fraction * months_in_year
    months = int(total_months)
    remaining_month_fraction = total_months - months

    # Convert remaining fraction to days
    total_days = remaining_month_fraction * days_in_month
    days = int(total_days)
    remaining_day_fraction = total_days - days

    # Convert remaining fraction to hours
    total_hours = remaining_day_fraction * hours_in_day
    hours = int(total_hours)
    remaining_hour_fraction = total_hours - hours

    # Convert remaining fraction to minutes
    total_minutes = remaining_hour_fraction * minutes_in_hour
    minutes = int(total_minutes)
    remaining_minute_fraction = total_minutes - minutes

    # Convert remaining fraction to seconds
    seconds = remaining_minute_fraction * seconds_in_minute

    return years, months, days, hours, minutes, seconds