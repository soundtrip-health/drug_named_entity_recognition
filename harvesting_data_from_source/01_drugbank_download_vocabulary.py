'''
MIT License

Copyright (c) 2023 Fast Data Science Ltd (https://fastdatascience.com)

Maintainer: Thomas Wood

Tutorial at https://fastdatascience.com/drug-named-entity-recognition-python-library/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import os
import re

import requests

response = requests.get("https://go.drugbank.com/releases/latest#open-data")

re_url = re.compile(r'\bhttps://go.drugbank.com/releases/[a-z0-9-/]+all-drugbank-vocabulary\b')

url = re_url.findall(response.text)[0]

tmpfile = "/tmp/tmp.zip"
print(f"Downloading Drugbank dump from {url} to {tmpfile}...")
response = requests.get(url)
response.raise_for_status()  # Raise an exception for bad status codes

with open(tmpfile, 'wb') as f:
    f.write(response.content)

print(f"Downloaded Drugbank dump from {url} to {tmpfile}.")

import zipfile
print(f"Unzipping Drugbank dump from {tmpfile} to current directory...")
with zipfile.ZipFile(tmpfile, 'r') as zip_ref:
    zip_ref.extractall(".")

print(f"Unzipped Drugbank dump from {tmpfile} to current directory.")
