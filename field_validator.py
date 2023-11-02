import pydantic
from typing import Optional, Dict
import requests
import pandas as pd


class Nutritions(pydantic.BaseModel):
    carbohydrates: float
    protein: float
    fat: float
    calories: float
    sugar: float


class Fruits(pydantic.BaseModel):
    name: str
    id: int
    family: str
    genus: str
    order: str
    nutritions: Nutritions
    

    @pydantic.field_validator('id')
    @classmethod
    def id_check(cls, value):
        if len(str(value)) > 2:
            raise Exception('aaaa')
    



# fruit1 = Fruits(name='Mango', id=1, family='mangofamily', genus='asda', order='342', nutritions={'carbohydrates': 2, 'protein': 3, 'fat': 5, 'calories': 5, 'sugar': 4})

URL = f'https://www.fruityvice.com/api/fruit/all'

def get_data(url):
    resp = requests.get(url)
    return resp.json()

def main():
    all_fruits = get_data(URL)
    print(all_fruits)
    # print(type(all_fruits))

    for fruit in all_fruits:
        item = Fruits(**fruit)
        # print(item)

    df = pd.json_normalize(all_fruits, sep='_')

    print(df.shape)
    print(df.head(5))



if __name__ == '__main__':
    main()