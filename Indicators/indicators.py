import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series


def calc_line(df:DataFrame,period:int)->float:
    return (df['high'].rolling(window=period).max() + df['low'].rolling(window=period).min()) / 2

def calculate_conversion_line(df: DataFrame, period = 9):
    df['conversion_line'] =  calc_line(df,period)

def calculate_base_line(df: DataFrame, period = 26):
    df['base_line'] = calc_line(df,period)

def calculate_leading_span_a(df: DataFrame):
    df['leading_span_a'] = (df['conversion_line']+df['base_line'])/2

def calculate_leading_span_b(df: DataFrame, period = 52):
    df['leading_span_b'] = calc_line(df,period)

def calculate_lagging_span(df: DataFrame, period = 26):
    df['lagging_span'] = df['close'].shift(-period)

def ema(series: Series, period:int) -> Series:
    return series.ewm(span=period,adjust=False).mean()

def sma(series: Series, period:int) -> Series:
    return series.rolling(window=period).mean()

def calculate_macd(df: DataFrame):
    df['macd'] = ema(df['close'],12) - ema(df['close'],26)
    df['macd_signal_line'] = ema(df['macd'],9)
    df['macd_histogram'] = df['macd'] - df['macd_signal_line']

def calculate_ao(df: DataFrame):
    df['median_price'] = (df['high'] + df['low']) / 2
    df['ao'] = sma(df['median_price'],5) - sma(df['median_price'],34)

def calculate_ac(df: DataFrame):
    df['ac'] = df['ao'] - sma(df['ao'],5)

