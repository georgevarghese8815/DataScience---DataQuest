import read
import dateutil

df = read.load_data()
times = df['submission_time']

def get_hour(time_input):
    return dateutil.parser.parse(time_input).hour

hours = times.apply(get_hour)
hour_counts = hours.value_counts()

for name, row in hour_counts.items():
    print("{0}: {1}".format(name, row))