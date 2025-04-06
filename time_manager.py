import datetime


class TimeManager:
    """
    TimeManager is a utility class for managing and manipulating time.
    Attributes:
        time (datetime.datetime): The current date and time.
    Methods:
        __init__():
            Initializes the TimeManager instance with the current date and time.
        advance_minute():
            Advances the current time by one minute.
        advance_hour():
            Advances the current time by one hour.
        advance_day():
            Advances the current time by one day.
        get_formatted_time():
            Returns the current time formatted as a string in the format "dd/MM/yyyy, HH:mm".
    """

    def __init__(self):
        self.time = datetime.datetime.now()  # Initialize with the current date and time

    def advance_minute(self):
        """Advance the time by one minute."""
        self.time += datetime.timedelta(minutes=1)

    def advance_hour(self):
        """Advance the time by one hour."""
        self.time += datetime.timedelta(hours=1)

    def advance_day(self):
        """Advance the time by one day."""
        self.time += datetime.timedelta(days=1)

    def get_formatted_time(self):
        """Return the current time formatted as dd/MM/yyyy, HH:mm."""
        return self.time.strftime("%d/%m/%Y, %H:%M")
