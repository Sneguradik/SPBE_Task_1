import csv
from typing import Iterable, Sequence, Any

import aiofiles
from aiocsv import AsyncReader, AsyncDictWriter, AsyncDictReader


async def read_tickers_from_csv(path,csv_sep = ',') -> Sequence[str]:
    result = []

    async with aiofiles.open(path, 'r', newline='') as file:
        async for line in AsyncDictReader(file, delimiter=csv_sep):
            result.append(line['Tickers'])

    return result

async def write_candles_to_csv(path,data:Sequence[dict[str,Any]],csv_sep = ',') -> None:

    async with aiofiles.open(path, 'w', newline='') as file:
        writer = AsyncDictWriter(file, list(data[0].keys()),delimiter=csv_sep,restval="NULL", quoting=csv.QUOTE_ALL)
        await writer.writeheader()
        for elem in data:
            await writer.writerow(elem)
