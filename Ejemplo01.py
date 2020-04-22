import pymysql
from sqlalchemy import create_engine
import pandas as pd

conex=create_engine('mysql+pymysql://root:''@localhost:3306/sakila').connect()
codigo = "select * from payment"
data=pd.read_sql(codigo,conex)
#print(data)

#imprimiendo lista
lista=pd.DataFrame(data)
print(lista)

#numero de regusros
regs= len(lista.index)
print("Registros: ",regs)

#numero de columnas
cols= len(lista.count())
print("Columnas: ",cols)

print(lista.describe())

#calcular la mediana
media= lista.mean()
print("Media aritmetica: ", media)

#calcular moda
moda= lista.mode()
print("Moda: ", moda)

#imprimri por campo 
med2=lista['amount'].mean()
mod2 = lista['amount'].mode()
print("Media aritmetica (2)", med2)
print("Moda (2)",mod2)

