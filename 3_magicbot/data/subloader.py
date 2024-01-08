import os
from ujson import loads # pip install ujson
import aiofiles # pip install aiofiles


# def get_json(filename: str) -> list:
#     path = f"data/{filename}"
#     if os.path.exists(path):
#         print("file exists")
#         with open(path, 'r', encoding='utf-8') as file:
#             return loads(file.read())
#     return []


async def get_json(filename: str = None) -> list:
    smiles = [
        ["🥑", "menga avakado yoqadi"],
        ["🍎", "menga olma yoqadi"],
        ["🍐", "menga olcha yoqadi"],
        ["🍊", "menga apelsin yoqadi"],
        ["☁️", "ob havo ancha yaxshi"]
    ]
    return smiles
