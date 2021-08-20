import asyncio
from bs4 import BeautifulSoup
import urllib.request
import csv

import GetData
import json


async def Main(data: GetData.Data):
    while True:
        data.Fetch()
        data.Export()
        print("Exported data.")
        print("Waiting 2 two hours")
        await asyncio.sleep(7200)  # 2h


if __name__ == "__main__":
    # query the website and return the html to the variable 'page'
    with open("secrets.json", 'r') as outfile:
        jsonLoad = json.load(outfile)
        data = GetData.Data(jsonLoad["user"], jsonLoad["collection"])

    asyncio.run(Main(data))




