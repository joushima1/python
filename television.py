class Television:
    MIN_VOLUME = 0
    def __init__(self):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME

    def power(self):
        pass

    def mute(self):
        pass

    def channel_up(self):
        pass

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        pass

    def __str__(self):
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'xxx'