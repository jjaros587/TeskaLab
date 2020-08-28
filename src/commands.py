import asyncio
import json
from src.container import Container
from src.database import Database


async def get_required_data(data):
    container = Container(data)
    return {
        'name': container.get_name(),
        'status': container.get_status(),
        'created_at': container.get_creation(),
        'memory': container.get_memory(),
        'cpu': container.get_cpu()
    }


def save():
    with open("data/sample-data.json", 'r') as file:
        data = json.load(file)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_required_data(item)) for item in data]
    result = loop.run_until_complete(asyncio.gather(*tasks))

    Database().save_data(result)


def get():
    for item in Database().get_data():
        print(item)


def delete():
    Database().delete_data()
