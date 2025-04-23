import pandas as pd

#Leyendo los datos de asistencias
asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo informacion basica del dataframe
#print(asistenciaDataFrame.info())
#print(asistenciaDataFrame.head(20))
#print(asistenciaDataFrame.describe())
print(asistenciaDataFrame['estrato'].value_counts())

