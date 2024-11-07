class MyTime:
    def __init__(self, *args):

        if len(args) == 1 and isinstance(args[0], str):
            time_parts = args[0].split(':')
            self.hours = int(time_parts[0])
            self.minutes = int(time_parts[1])
            self.seconds = int(time_parts[2])

        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]

        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds

        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        self.normalize()


    def normalize(self):

        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60


        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60


        self.hours = self.hours % 24

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)



time1 = MyTime("14:15:16")
time2 = MyTime(14, 15, 16)
time3 = MyTime(time1)
time4 = MyTime(23, 59, 61)
print(time1)
print(time2)
print(time3)
print(time1 == time2)
print(time1 > time2)
print(time4)