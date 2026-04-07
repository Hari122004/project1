import datetime

today = datetime.date.today()
now = datetime.datetime.now()

# Calculate yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
print("Now:", now)