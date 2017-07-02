'''
This is a variation of the chapter 15 system which estimates rather than uses
fixed parameters

A system consists of a system, plus a config

'''
from pysystemtrade.sysdata.csvdata import csvFuturesData
from pysystemtrade.systems.account import Account
from pysystemtrade.systems.basesystem import System
from pysystemtrade.systems.forecast_combine import ForecastCombine
from pysystemtrade.systems.forecast_scale_cap import ForecastScaleCap
from pysystemtrade.systems.forecasting import Rules
from pysystemtrade.systems.futures.rawdata import FuturesRawData
from pysystemtrade.systems.portfolio import Portfolios
from pysystemtrade.systems.positionsizing import PositionSizing

from pysystemtrade.sysdata.configdata import Config


def futures_system(data=None,
                   config=None,
                   trading_rules=None,
                   log_level="terse"):
    """

    :param data: data object (defaults to reading from csv files)
    :type data: sysdata.data.Data, or anything that inherits from it

    :param config: Configuration object (defaults to futuresconfig.yaml in this directory)
    :type config: sysdata.configdata.Config

    :param trading_rules: Set of trading rules to use (defaults to set specified in config object)
    :param trading_rules: list or dict of TradingRules, or something that can be parsed to that

    :param log_level: Set of trading rules to use (defaults to set specified in config object)
    :type log_level: str

    """

    if data is None:
        data = csvFuturesData()

    if config is None:
        config = Config(
            "systems.provided.futures_chapter15.futuresestimateconfig.yaml")

    rules = Rules(trading_rules)

    system = System([
        Account(), Portfolios(), PositionSizing(), FuturesRawData(),
        ForecastCombine(), ForecastScaleCap(), rules
    ], data, config)

    system.set_logging_level(log_level)

    return system


if __name__ == '__main__':
    import doctest
    doctest.testmod()
