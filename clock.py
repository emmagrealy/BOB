class Clock(object):
    def __init__(self, hour, minute):
        
        self.hour = (hour + minute // 60) % 24
        while self.hour < 0:
            self.hour += 24

        self.minute = minute % 60
        if self.minute < 0:
            self.minute += 60

    def __repr__(self):
        return str(self.hour).zfill(2)+':'+str(self.minute).zfill(2)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.hour = (self.hour + (self.minute + minutes) // 60) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes):
        hr = minutes // 60
        mins = minutes % 60

        self.hour -= hr
        while self.hour < 0:
            self.hour += 24

        self.minute -= mins
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1
            if self.hour < 0:
                self.hour += 24

        return self