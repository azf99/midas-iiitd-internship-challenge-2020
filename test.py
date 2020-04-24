''''
A script for sending a JSON in the POST request
'''

import requests
import json
import time


path = "http://127.0.0.1:5000/automated_testing"


path1 = "https://reddit-flair-azf99.herokuapp.com/automated_testing"

file = open("test.txt", "rb")
folder = {"upload_file": file}

st = time.time()

r = requests.post(path1, files = folder)
print(r.text)
print("Time taken:", time.time()- st)
