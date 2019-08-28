import pandas as pd
url = 'https://data.gov.ru/opendata/7017069388-gostta/data-20161213T0100-structure-20161213T0100.csv'


dataFrame = pd.read_csv(url)
print(dataFrame)
result = dataFrame[dataFrame['name'] == 'Siberian Motel System']
print(result)