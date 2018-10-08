


import pandas as pd
from sqlalchemy import create_engine

df =pd.read_csv(r'csv_dir/lostAnimal_20180101_20181231_vol3.csv', encoding='CP949')
engine = create_engine("mysql+pymysql://root:"+"qwer1234!"+"@localhost:3306/animaldb?charset=utf8", encoding='utf-8')

conn =engine.connect()
df.to_sql(name='animal_2018', con=engine, if_exists='append', index=False)



conn.close()