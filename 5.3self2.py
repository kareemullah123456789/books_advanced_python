# Write your code here :-)
# inside class Time:

class Time:
    """Represents the time of day."""
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

start = Time()

start.hour = 9
start.minute = 45
start.second = 00


start.print_time()
end = start.increment(1337)
