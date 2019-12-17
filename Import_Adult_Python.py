# Load CSV (using python)
import os
import requests

url='https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
response = requests.get(url)
with open(os.path.join("python_adult_data", "adult.data"), 'wb') as f:
    f.write(response.content)