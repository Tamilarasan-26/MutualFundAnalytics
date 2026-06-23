import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        df = pd.read_csv(
            os.path.join(folder_path, file)
        )

        print("\n" + "="*50)
        print("FILE:", file)

        print("Duplicate Rows:")
        print(df.duplicated().sum())
        
        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())