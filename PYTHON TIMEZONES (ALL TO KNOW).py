import datetime
import pytz

# YOU CAN LIST ALL THE AVAILABLE TIMEZONES WITH pytz.common_timezones and pytz.all_timezones :
# In [45]: len(pytz.common_timezones)
# Out[45]: 403
# In [46]: len(pytz.all_timezones)
# Out[46]: 563

# create timezone objects
Africa_Algiers_timezone = pytz.timezone("Africa/Algiers")
US_Eastern_timezone = pytz.timezone("US/Eastern")
US_Pacific_timezone = pytz.timezone("US/Pacific")

my_timestamp_no_tz = datetime.datetime.now(
    tz=None)  # my_timestamp.tzname() == None
my_timestamp_with_tz = datetime.datetime.now().astimezone()
my_timestamp_with_tz = datetime.datetime.now(
    tz=pytz.timezone("Africa/Algiers"))

#     print( datetime.datetime.now().astimezone().tzinfo) # == Romance Standard Time
#     print( datetime.datetime.now(tz= pytz.timezone("Africa/Algiers")).tzinfo) # == Africa/Algiers

print("my_timestamp_no_tz   ::: ", my_timestamp_no_tz)
print("my_timestamp_with_tz ::: ", my_timestamp_with_tz)

localized_timestamp = Africa_Algiers_timezone.localize(my_timestamp_no_tz)
new_timezone_timestamp = localized_timestamp.astimezone(US_Pacific_timezone)

print(Africa_Algiers_timezone, ":", localized_timestamp)
print(US_Pacific_timezone, ":", new_timezone_timestamp)
