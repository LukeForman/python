class Television:
    """
    The Television Class
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize television status, mute, volume, and channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Flip state of status (i.e. T-->F, F-->T), turn tv on or off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        If status true, flip state of mute (i.e. T-->F, F-->T).
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        If status true and tv at max channel, set to min channel, otherwise increase channel by one.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        If status true and tv at min channel set to max channel, otherwise decrease channel by one.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        If status true and tv muted, unmute, and if volume less than max, increase volume by one.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        If status true and tv muted, unmute, and if volume greater than min, decrease volume by one.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Sets Volume to min value if muted, and current value if not. Then returns a string.

        :return: returns status(tv on/off), channel number, and volume number.
        """
        display_volume = 0
        if self.__status and self.__muted:
             display_volume = Television.MIN_VOLUME
        else:
             display_volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}'