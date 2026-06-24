import pandas as pd
import mysql.connector

# pd.set_option("display.max_columns", None)
df = pd.read_csv("Project 2/dataSet/train.csv")
# print(df)

""" Understanding the data """
# print(df.shape)                                     # (9800, 18)
# print(df.describe())
# print(df.info())                                    # Convert 2,3,4 into datetime
# print(df.isnull().sum())                          # There are 11 null values in Postal Code

# print(df["Postal Code"].isnull().sum() * 100 / 9799)
# print(df["Postal Code"].duplicated().sum())                   




""" Cleaning the Data """

df["Postal Code"] = df["Postal Code"].fillna(df["Postal Code"].mode()[0])                   # Here we replaced null values with Maximum Counts...


# print(df["Order Date"])
df["Order Date"] = df["Order Date"].astype(str).str.strip()                                 # Here we Remove the blank spaces...
df["Order Date"] = df["Order Date"].replace(["", "nan", "NaN"], pd.NA)
df["Order Date"] = pd.to_datetime(df["Order Date"],format="%d/%m/%Y", errors="coerce")      # Converting into datetime...

# print(df["Order Date"].dtype)
# print(df["Order Date"].isna().sum())
# print(df["Order Date"])


# print(df["Ship Date"])
df["Ship Date"] = df["Ship Date"].astype(str).str.strip()                                       # Removes the blank spaces
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y", errors="coerce")           # Converting into datetime

# print(df["Ship Date"].isna().sum())
# print(df["Ship Date"].dtype)

df.to_csv(r"C:\Users\parth\Desktop\Data_analyst\Project 2\DataSet\Superstore.csv")



conn = mysql.connector.connect(
    host = "localhost",
    user = "parth",
    password = "PARTHS1148",
    database = "SuperMarket"

)
print("Connected to MySQL successfully!")

conn.close()