""" 
Universiad del Valle de Guatemala
Mineria de datos

Kenneth Galvez
Andrea Lam
Mariano Reyes
Rebecca Smith
Jessica Ortiz

"""

import pyreadstat
import pandas as pd

# Leer el primer archivo .sav
df, meta = pyreadstat.read_sav('archivo1.sav')
df.columns = [x.upper() for x in df.columns] # poner titulos en mayúsculas

# Unir los datos de los archivos .sav restantes
for i in range(2, 11):
    file_name = 'archivo' + str(i) + '.sav'
    df_temp, meta_temp = pyreadstat.read_sav(file_name)
    df_temp.columns = [x.upper() for x in df_temp.columns] # poner titulos en mayúsculas
    df = pd.concat([df, df_temp], axis=0)

# Guardar el DataFrame unido en formato .csv
df.to_csv('archivo_final.csv', index=False)
