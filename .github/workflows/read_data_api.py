
import requests 
import pandas as pd
response=requests.get("https //jsonplaceholder.typicode.come/users")
data=response.json()
df=pd.DataFrame(data)
print(df)