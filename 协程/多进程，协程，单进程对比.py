import requests
import time
import asyncio
import aiohttp
start = time.time()


# def request():
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     result = requests.get(url).text
#     print('Get response from', url, 'Result:', result)
#
# 这个版本太慢了，
# for _ in range(100):
#     request()

async def get(url):
    session=aiohttp.ClientSession()
    response=await  session.get(url)
    result=await response.text()
    session.close()
    return result

async  def request():
    url = 'http://127.0.0.1:5000'
    print('Waiting for', url)
    result = await  get(url)
    print('Get response from', url, 'Result:', result)

tasks=[asyncio.ensure_future(request()) for _ in range(1000)]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

# 这个版本太慢了，
for _ in range(100):
    request()




end = time.time()
print('Cost time:', end - start)