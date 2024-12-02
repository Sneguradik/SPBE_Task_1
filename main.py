# This is a sample Python script.
import asyncio
import os.path
from argparse import Namespace, ArgumentParser
from typing import Sequence, Any

import aiohttp
from dateutil.parser import parser
from pandas import DataFrame

from Indicators import calculate_conversion_line, calculate_base_line, calculate_leading_span_a, \
    calculate_leading_span_b, calculate_lagging_span, calculate_macd, calculate_ao, calculate_ac, init_plot

from Parser import read_tickers_from_csv,write_candles_to_csv,get_market_data

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=False, help="Path to tickers table",
        type=str, default='data/tickers.csv')
    parser.add_argument("-o", "--output", dest="output", required=False, help="Path to output folder",
        type=str, default='data/')
    return parser.parse_args()

async def main(args):

    if not os.path.exists(args.input):
        print("You haven't tickers.csv file in data folder.\nCreate it and try again.")
        return

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if not os.path.exists(os.path.join(args.output, "data")):
        os.makedirs("data/stats")

    if not os.path.exists(os.path.join(args.output, "stats")):
        os.makedirs("data/charts")


    tickers = await read_tickers_from_csv(args.input)
    data : Sequence[Sequence[dict[str,Any]]]
    print("Fetching data...")
    async with aiohttp.ClientSession() as session:
        tasks = [get_market_data(session, ticker, 100) for ticker in tickers]
        data = await asyncio.gather(*tasks)
    print("Data fetched")
    dfs = [DataFrame(el) for el in data]

    for i in range(len(data)):
        print(f'Calculating indicators for {tickers[i]}')
        #ichimoku
        calculate_conversion_line(dfs[i])
        calculate_base_line(dfs[i])
        calculate_leading_span_a(dfs[i])
        calculate_leading_span_b(dfs[i])
        calculate_lagging_span(dfs[i])

        #others
        calculate_macd(dfs[i])
        calculate_ao(dfs[i])
        calculate_ac(dfs[i])
        print(f'Indicators calculated for {tickers[i]}')



    for i in range(len(data)):
        dfs[i].to_csv(os.path.join(args.output,f'stats/{tickers[i]}.csv'))


    for i in range(len(dfs)):
        print(f'Creating plots for {tickers[i]}')
        output = os.path.join(args.output, "charts",tickers[i])
        if not os.path.exists(output):
            os.makedirs(output)
        init_plot(dfs[i],tickers[i],output)
        print(f'Plots created for {tickers[i]}')


if __name__ == '__main__':
    args = parse_args()
    asyncio.run(main(args))



