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


    def __add__(self, other):
        if isinstance(other, MyTime):
            return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
        raise TypeError("Можно складывать только с другим объектом MyTime")


    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def __sub__(self, other):
        if isinstance(other, MyTime):
            total_seconds_self = self.to_seconds()
            total_seconds_other = other.to_seconds()
            diff = total_seconds_self - total_seconds_other
            return MyTime.from_seconds(diff)
        raise TypeError("Можно вычитать только другой объект MyTime")


    def __mul__(self, number):
        if isinstance(number, (int, float)):
            total_seconds = self.to_seconds() * number
            return MyTime.from_seconds(total_seconds)
        raise TypeError("Можно умножать только на число")

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)





time1 = MyTime("14:15:16")
time2 = MyTime(2, 15, 16)
time3 = MyTime(time1)
time4 = MyTime(23, 59, 61)
time5 = time1 + time2
time6 = time4 - time1
time7 = time1 * 2
print(time1)
print(time2)
print(time3)
print(time1 == time2)
print(time1 != time2)
print(time1 > time2)
print(time4)
print(time5)
print(time6)
print(time7)