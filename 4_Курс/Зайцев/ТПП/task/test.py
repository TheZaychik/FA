import requests
from datetime import datetime

start = datetime.now()
for i in range(1000):
    requests.post(
        "http://localhost:8080/",
        json={
            "data": i
        }
        )
for i in range(100):
    requests.get(f"http://localhost:8080/{i}")

for i in range(100):
    requests.get(f"http://localhost:8080/")

print(datetime.now() - start) # 0:00:04.661237
    