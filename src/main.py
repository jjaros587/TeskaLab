import asyncio
import json


async def get_required_data(container):
    return {
        'name': container['name']
    }


if __name__ == "__main__":
    with open("../data/sample-data.json", 'r') as file:
        data = json.load(file)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_required_data(item)) for item in data]
    result = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    print(*result, sep='\n')
