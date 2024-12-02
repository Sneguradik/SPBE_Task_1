import os.path
from random import randint

from pandas import DataFrame
import matplotlib.pyplot as plt



def init_plot(df: DataFrame, ticker:str, output:str):

    if not os.path.exists(output):
        os.makedirs(output)

    # candlestick plot
    candlestick_plot(df,ticker,output)

    #ichimoku
    ichimoku_plot(df,ticker,output)

    #others
    other_indicators_plot(df,ticker,output)


def candlestick_plot(df: DataFrame,ticker:str, output:str):
    f_candle = plt.figure()
    ax_candle = f_candle.add_subplot(111)

    up = df[df.close >= df.open]
    down = df[df.close < df.open]

    col1 = 'red'
    col2 = 'green'

    width = 0.8
    width2 = 0.1

    ax_candle.bar(up.index, up.close - up.open, width, bottom=up.open, color=col2)
    ax_candle.bar(up.index, up.high - up.close, width2, bottom=up.close, color=col2)
    ax_candle.bar(up.index, up.low - up.open, width2, bottom=up.open, color=col2)


    ax_candle.bar(down.index, down.close - down.open, width, bottom=down.open, color=col1)
    ax_candle.bar(down.index, down.high - down.open, width2, bottom=down.open, color=col1)
    ax_candle.bar(down.index, down.low - down.close, width2, bottom=down.close, color=col1)

    ax_candle.set_title(f'Candlestick {ticker} Chart')

    f_candle.savefig(os.path.join(output,f'{ticker}_candlestick{randint(1,100000)}.png'),dpi=600)

def ichimoku_plot(df: DataFrame,ticker:str, output:str):
    f_ichimoku = plt.figure()
    ax_ichimoku = f_ichimoku.add_subplot(111)

    ax_ichimoku.plot(df['conversion_line'], label='Conversion Line', color='blue', linewidth=1)
    ax_ichimoku.plot(df['base_line'], label='Base Line', color='red', linewidth=1)
    ax_ichimoku.plot(df['lagging_span'], label='Lagging Span', color='green', linestyle='--', linewidth=1)

    ax_ichimoku.fill_between(df.index, df['leading_span_a'], df['leading_span_b'],
                     where=df['leading_span_a'] >= df['leading_span_b'], color='lightgreen', alpha=0.4,
                     label='Bullish Cloud')
    ax_ichimoku.fill_between(df.index, df['leading_span_a'], df['leading_span_b'],
                     where=df['leading_span_a'] < df['leading_span_b'], color='lightcoral', alpha=0.4,
                     label='Bearish Cloud')

    ax_ichimoku.set_title(f'Ichimoku {ticker} Chart')
    ax_ichimoku.legend()

    f_ichimoku.savefig(os.path.join(output,f'{ticker}_ichimoku{randint(1,100000)}.png'),dpi=600)

def other_indicators_plot(df: DataFrame,ticker:str, output:str):
    fig, axes = plt.subplots(4,1, sharex=True)

    axes[0].plot(df['close'], label='Close Price', color='black', linewidth=1.5)
    axes[0].set_title('Close Price', fontsize=14)
    axes[0].legend()

    axes[1].plot(df['macd'], label='MACD Line', color='green', linewidth=1.5)
    axes[1].plot(df['macd_signal_line'], label='Signal Line', color='red', linewidth=1.5)
    axes[1].bar(df.index, df['macd_histogram'], label='Histogram', color='gray', alpha=0.5)
    axes[1].set_title('MACD', fontsize=14)
    axes[1].legend()

    axes[2].bar(df.index, df['ao'], label='Awesome Oscillator', color='purple', alpha=0.8)
    axes[2].set_title('Awesome Oscillator (AO)', fontsize=14)
    axes[2].legend()

    axes[3].bar(df.index, df['ac'], label='Accelerator Oscillator (AC)', color='orange', alpha=0.8)
    axes[3].set_title('Accelerator Oscillator (AC)', fontsize=14)
    axes[3].legend()

    fig.tight_layout()
    fig.savefig(os.path.join(output,f'{ticker}_other{randint(1,100000)}.png'),dpi=600)


