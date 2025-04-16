import datetime
import display_utils as dp


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
        is_market_open():
            Checks if the market is currently open based on the opening and closing times.
    """

    def __init__(self, open_time: datetime.time, close_time: datetime.time):
        """
        Initialize the TimeManager with the current date and time.
        Args:
            open_time (datetime.time): The opening time of the market.
            close_time (datetime.time): The closing time of the market.
        """
        self.open_time = open_time
        self.close_time = close_time
        self.time = datetime.datetime.now()  # Set to a specific date and time for testing
        if (self.is_market_open):
            self.advance_day()
        

    def advance_minute(self):
        """Advance the time by one minute."""
        self.time += datetime.timedelta(minutes=1)
        

    def advance_hour(self):
        """Advance the time by one hour."""
        self.time += datetime.timedelta(hours=1)
        

    def advance_day(self):
        """Advance to the next market day."""
        next_day = self.time + datetime.timedelta(days=1)
        self.time = datetime.datetime.combine(next_day, self.open_time)

    def get_formatted_time(self):
        """Return the current time formatted as dd/MM/yyyy, HH:mm."""
        return self.time.strftime("%d/%m/%Y, %H:%M")

    def is_market_open(self):
        """Check if the market is open."""
        current_time = self.time.time()
        return self.open_time <= current_time < self.close_time
