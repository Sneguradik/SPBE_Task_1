import urllib.parse
from datetime import datetime
from typing import Any

import aiohttp


def convert_from_binance(data:list)->dict:
    return {
        'open_time':datetime.fromtimestamp(data[0]/1000), # Open time
        'open':float(data[1]), # Open
        'high':float(data[2]), # High
        'low':float(data[3]), # Low
        'close':float(data[4]), # Close
        'volume':int(data[5]), # Volume
        'close_time':datetime.fromtimestamp(data[6]/1000), # Close time
        'base_asset_volume':float(data[7]), # Base asset volume
        'number_of_trades':data[8], # Number of trades
        'taker_by_volume':int(data[9]), # Taker by volume
        'taker_buy_asset_volume':float(data[10]), # Taker buy base asset volumes
    }

async def get_market_data(session : aiohttp.ClientSession,ticker:str, candles_limit:int = 100) -> list[dict[str,Any]]:

    base_url = "https://dapi.binance.com/dapi/v1/klines?"
    params = {
        "symbol": ticker+"_PERP",
        "interval": "15m",
        "limit": candles_limit,
    }
    url = base_url + urllib.parse.urlencode(params)

    async with session.get(url) as response:
        raw_candles : list = await response.json()

        return list(map(lambda a: convert_from_binance(a), raw_candles))
