class Television:
    """
    A class representing a TV remote.
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self, channel = 0, volume = 0, status = False)-> None:
        """
        Constructor to create initial state of a TV.
        :param channel: TV Channel.
        :param volume: TV Volume.
        :param status: TV On/Off status.
        """

        self.__channel = channel
        self.__volume = volume
        self.__status = status

    def power(self) -> None:
        """
        Method to turn the TV on/off.
        :return: None.
        """
        self.__status = not self.__status

    def channel_up(self) -> None:
        """
        Method to adjust the TV channel by incrementing its value.
        :return: None.
        """
        if self.__status and self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
         Method to adjust the TV channel by decrementing its value.
        :return: None.
        """
        if self.__status and self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
        if self.__status and self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to adjust the TV volume by incrementing its value.
        :return: None.
        """
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to adjust the TV volume by decrementing its value.
        :return: None.
        """
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> None:
        """
        Method to return the TV status.
        :return: None.
        """
        return f"TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


