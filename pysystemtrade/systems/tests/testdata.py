from pysystemtrade.sysdata.csvdata import csvFuturesData
from pysystemtrade.systems.account import Account
from pysystemtrade.systems.forecast_combine import ForecastCombine
from pysystemtrade.systems.forecast_scale_cap import ForecastScaleCap
from pysystemtrade.systems.forecasting import Rules
from pysystemtrade.systems.futures.rawdata import FuturesRawData
from pysystemtrade.systems.portfolio import Portfolios
from pysystemtrade.systems.positionsizing import PositionSizing
from pysystemtrade.systems.rawdata import RawData

from pysystemtrade.sysdata.configdata import Config


def get_test_object():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = RawData()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    return (rawdata, data, config)


def get_test_object_futures():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    return (rawdata, data, config)


def get_test_object_futures_with_rules():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    return (rules, rawdata, data, config)


def get_test_object_futures_with_rules_and_capping():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    capobject = ForecastScaleCap()
    return (capobject, rules, rawdata, data, config)


def get_test_object_futures_with_comb_forecasts():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    capobject = ForecastScaleCap()
    combobject = ForecastCombine()
    return (combobject, capobject, rules, rawdata, data, config)


def get_test_object_futures_with_pos_sizing():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    capobject = ForecastScaleCap()
    combobject = ForecastCombine()
    posobject = PositionSizing()
    return (posobject, combobject, capobject, rules, rawdata, data, config)


def get_test_object_futures_with_portfolios():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("pysystemtrade.systems.provided.example.exampleconfig.yaml")
    capobject = ForecastScaleCap()
    combobject = ForecastCombine()
    posobject = PositionSizing()
    portfolio = Portfolios()
    return (portfolio, posobject, combobject, capobject, rules, rawdata, data,
            config)


def get_test_object_futures_with_rules_and_capping_estimate():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("systems.provided.example.estimateexampleconfig.yaml")
    capobject = ForecastScaleCap()
    account = Account()
    return (account, capobject, rules, rawdata, data, config)


def get_test_object_futures_with_pos_sizing_estimates():
    """
    Returns some standard test data
    """
    data = csvFuturesData("sysdata.tests")
    rawdata = FuturesRawData()
    rules = Rules()
    config = Config("systems.provided.example.estimateexampleconfig.yaml")
    capobject = ForecastScaleCap()
    combobject = ForecastCombine()
    posobject = PositionSizing()
    account = Account()
    return (account, posobject, combobject, capobject, rules, rawdata, data,
            config)
