import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\parth\Desktop\Data_analyst\Project 2\DataSet\Superstore.csv")
print(df.shape)

engine = create_engine(
    "mysql+mysqlconnector://parth:PARTHS1148@localhost/SuperMarket"
)

df.to_sql(
    name="superstore",
    con=engine,
    if_exists="replace",
    index=False
)