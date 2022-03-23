import sys
import random
import json

import asyncio
from aiohttp.client import ClientSession

import psycopg2


connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="admin",
        password="adm1n0ut")
cursor = connection.cursor()


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.json()


async def run(r):

    url = f'http://localhost:8080/?json_nested_depth={random.randint(1, 500)}'
    tasks = []

    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        unpacked_responses = [(item['request_uuid'], item['date_start_request'], item['description'], \
                               json.dumps(item['attachment'])) for sublist in responses for item in sublist]
        args_str = ','.join(['%s'] * len(unpacked_responses))
        sql = "INSERT INTO api_response (request_uuid, date_start_request, description, attachment) VALUES {}".format(args_str)
        cursor.execute(sql, unpacked_responses)
        connection.commit()
        cursor.close()
        connection.close()


try:
    requests_num = int(sys.argv[1])
except Exception as error:
    print(f"Input is missing (number of requests)")
    raise error

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(requests_num))
loop.run_until_complete(future)
