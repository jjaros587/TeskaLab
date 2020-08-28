import asyncio
import json
from src.container import Container


async def get_required_data(data):
    container = Container(data)
    return {
        'name': container.get_name(),
        'status': container.get_status(),
        'created_at': container.get_creation(),
        'memory': container.get_memory(),
        'cpu': container.get_cpu()
    }


if __name__ == "__main__":
    with open("../data/sample-data.json", 'r') as file:
        data = json.load(file)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_required_data(item)) for item in data]
    result = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    print(*result, sep='\n')
