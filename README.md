# AiohttpTest
Backend application with asyncio test

#Stack
- asyncio
- aiohttp
- postgresql
- docker-compose

#Local deployment

Clone the application, from root of the project run:
  docker-compose up
Containers will be initialized with table "api_response". 

Next create virtual env with:
  python -m venv venv
And activate it:
  source venv/bin/activate
Install requirements:
  pip install -r requirements.txt

change directory to "client" and run:
  python client.py 5000
5000 - number of requests to server

