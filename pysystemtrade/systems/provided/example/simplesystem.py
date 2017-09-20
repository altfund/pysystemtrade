from pysystemtrade.sysdata.csvdata import csvFuturesData
from pysystemtrade.systems.account import Account
from pysystemtrade.systems.basesystem import System
from pysystemtrade.systems.forecast_combine import ForecastCombine
from pysystemtrade.systems.forecast_scale_cap import ForecastScaleCap
from pysystemtrade.systems.forecasting import Rules
from pysystemtrade.systems.portfolio import Portfolios
from pysystemtrade.systems.positionsizing import PositionSizing

from pysystemtrade.sysdata.configdata import Config


def simplesystem(data=None, config=None, log_level="on"):
    """
    Example of how to 'wrap' a complete system
    """
    if config is None:
        config = Config("systems.provided.example.simplesystemconfig.yaml")
    if data is None:
        data = csvFuturesData()

    my_system = System([
        Account(), Portfolios(), PositionSizing(), ForecastCombine(),
        ForecastScaleCap(), Rules()
    ], data, config)

    my_system.set_logging_level(log_level)

    return my_system
