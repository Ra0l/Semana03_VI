import pymysql
from sqlalchemy import create_engine
import pandas as pd

conex=create_engine('mysql+pymysql://root:''@localhost:3306/sakila').connect()
codigo = "select * from film"
data=pd.read_sql(codigo,conex)

#Imprimir toodo
#print(data)

#imprimiendo lista con data frame
lista=pd.DataFrame(data)
#print("Imprimiendo lista")
#print(lista)
print("Columna replacement_cost")
print(lista['replacement_cost'])

media=lista['replacement_cost'].mean()
print("Media aritmetica de la columna replacement_cost")
print(media)

mediana = lista['replacement_cost'].median()
print("Mediana aritmetica de la columna replacement_cost")
print(mediana)

moda = lista['replacement_cost'].mode()
print("Moda de la columna replacement_cost")
print(moda)

#media = lista.mean()
#mediana=lista.median()
#moda = lista.mode()

#print("Media Aritemetica")
#print(media)
#print("Mediana")
#print(mediana)
#print("Moda")
#print(moda)

#print("Estadictica")
#print(lista.describe())
