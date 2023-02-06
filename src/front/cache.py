import numpy as np

from src.front.get import * 

BACK_PORT = 8080
BACK_URL = "http://127.0.0.1"
BACK_OPTION = "None"


BASE_URL = f"{BACK_URL}:{BACK_PORT}/"

# cache
id_list = get_ids(BASE_URL)["id_list"]
print(id_list)
np.random.shuffle(id_list)
print(id_list)
model_dec = get_model_decision(BASE_URL)