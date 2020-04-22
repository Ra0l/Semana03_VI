import pymysql
from sqlalchemy import create_engine
import pandas as pd

conex=create_engine('mysql+pymysql://root:''@localhost:3306/sakila').connect()
codigo = "select * from payment"
data=pd.read_sql(codigo,conex)

#imprimiendo lista con data frame
lista=pd.DataFrame(data)

amount=lista['amount']
print("Amount")
print(amount)

print("Media aritmetica Amount")
media=amount.mean()
print(media)
print("Mediana Amount")
mediana=amount.median()
print(mediana)
print("Moda Amount")
moda=amount.mode()
print(moda)

