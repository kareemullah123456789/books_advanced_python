# Write your code here :-)
class Time:
    """Represents the time of day."""
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
start = Time()

start.hour = 9
start.minute = 45
start.second = 00
#first method
Time.print_time(start)
#Second Method
start.print_time()
