"""
Grafica de contagiados por covid en {pais}
"""

import requests
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':

    URL = "https://corona.lmao.ninja/v2/countries?yesterday&sort"

    payload={}
    headers = {}

    response = requests.request("GET", URL, headers=headers, data=payload)

    print(response.text)
