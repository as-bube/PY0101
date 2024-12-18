import pandas as pd

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35]}
# df = pd.DataFrame(data)

# print("DataFrame:")
# print(df)

# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe

# print(df.head())


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
print(df.head())

# Access to the column Length

x = df[['Length']]
print(x)