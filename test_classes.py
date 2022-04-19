import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv_1 = Television()
        self.tv_2 = Television(0,0,True)
        self.tv_3 = Television(3,2,True)

    def teardown_method(self):
        del self.tv_1
        del self.tv_2
        del self.tv_3

    def test_init(self):
        assert self.tv_1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.tv_2.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        assert self.tv_3.__str__() == "TV status: Is on = True, Channel = 3, Volume = 2"

    def test_power(self):
        self.tv_1.power()
        assert self.tv_1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        self.tv_2.power()
        assert self.tv_2.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.tv_3.power()
        assert self.tv_3.__str__() == "TV status: Is on = False, Channel = 3, Volume = 2"

    def test_channel_up(self):
        self.tv_1.channel_up()
        self.tv_2.channel_up()
        self.tv_3.channel_up()
        assert self.tv_1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.tv_2.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
        assert self.tv_3.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"

    def test_channel_down(self):
        self.tv_1.channel_down()
        self.tv_2.channel_down()
        self.tv_3.channel_down()
        assert self.tv_1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.tv_2.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        assert self.tv_3.__str__() == "TV status: Is on = True, Channel = 2, Volume = 2"

    def test_volume_up(self):
        self.tv_1.volume_up()
        self.tv_2.volume_up()
        self.tv_3.volume_up()
        assert self.tv_1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.tv_2.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        assert self.tv_3.__str__() == "TV status: Is on = True, Channel = 3, Volume = 2"

    def test_volume_down(self):
        self.tv_1.volume_down()
        self.tv_2.volume_down()
        self.tv_3.volume_down()
        assert self.tv_1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.tv_2.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        assert self.tv_3.__str__() == "TV status: Is on = True, Channel = 3, Volume = 1"
