'''
Created on 14 Dec 2015

@author: rob
'''
import unittest

from pysystemtrade.sysdata.data import Data
from pysystemtrade.systems.basesystem import System
from pysystemtrade.systems.stage import SystemStage

from pysystemtrade.sysdata.configdata import Config


class Test(unittest.TestCase):
    def setUp(self):
        stage = SystemStage()
        stage.name = "test"
        data = Data()
        config = Config(dict(instruments=["another_code", "code"]))
        system = System([stage], data=data, config=config)
        self.system = system

    def test_quicktest(self):
        system = self.system
        instrument_list = system.get_instrument_list()
        self.assertEqual(instrument_list, ["another_code", "code"])

        self.assertEqual(len(system.cache),
                         1)  # get instrument list lives in cache
        self.assertEqual(system, system.test.parent)

        system.set_logging_level("on")
        self.assertEqual(system.test.log.logging_level(), "on")


if __name__ == "__main__":
    unittest.main()
