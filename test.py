# import pycountry_convert as pc

# def get_continent(country_name):
#     try:
#         # Convertir le nom du pays en code ISO 3166-1 alpha-2
#         country_alpha2 = pc.country_name_to_country_alpha2(country_name, cn_name_format="default")
        
#         # Obtenir le continent à partir du code alpha-2
#         continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
#         continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        
#         return continent_name
#     except (ValueError, KeyError):
#         return None

# # Exemple d'utilisation pour le Brésil
# country_name = "UK"
# country_name = country_name.title()
# print(country_name.title())
# continent = get_continent(country_name)

# if continent:
#     print(f"Le continent de {country_name} est {continent}.")
# else:
#     print(f"Impossible de déterminer le continent pour {country_name}.")

import pandas as pd

# Créer un DataFrame exemple
df = pd.DataFrame({'A': [1, 'a', None, 4],
                   'B': [None, 5, 6, 'b'],
                   'C': [8, 9, 'c', None]})

# Colonne pour laquelle vous souhaitez afficher les valeurs non numériques
column_name = 'A'

# Sélectionner les lignes où les valeurs ne sont pas numériques
non_numeric_values = df.loc[df[column_name].apply(lambda x: not isinstance(x, (int, float)))]

print(non_numeric_values)
