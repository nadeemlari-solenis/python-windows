import pandas as pd
import requests as r
import time
from tqdm import tqdm
from tabulate import tabulate

df = pd.read_csv('C:/Users/mnadeem/OneDrive - Solenis LLC/Desktop/test.csv', usecols=['objectId', 'email'])
rows = df.shape[0]
total_time = 0
rows=400


for index in tqdm(range(rows)):
    url = "https://sol-b2c-sso-test-fa.azurewebsites.net/api/UpdateGroup?code=WIVtZx12r6i52t7SZnK70BFz1YAzWqHjZXqPTy873dUzAzFuTOHzWg=="
    start = time.time()
    data = {
        "objectId": df['objectId'][index],
        "email": df['email'][index]
    }
    response = r.post(url, json=data)
    response_data = response.json()

    end = time.time()
    elapsed_time = end - start
    total_time += elapsed_time
    # print("\nResponse=", data, "Response Time:", {elapsed_time * 1000 / 1},"ms")
    # if index == 2:
    #     break

    # print()
# df_print = pd.DataFrame(print_data)
# print(tabulate(print_data[1:], headers=print_data[0], tablefmt="grid"))
print(f"Average Time: {total_time * 1000 / rows} ms")
