import pandas as pd

# FIXME: TEST DATA
df = pd.DataFrame({
    'localid': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Bilbao', 'Alicante', 'Malaga', 'Murcia', 'Palma',
                'Las Palmas'],
    'coord_y': [40.4165, 41.3851, 39.4699, 37.3891, 43.2630, 38.3452, 36.7213, 37.9922, 39.5696, 28.1235],
    'coord_x': [-3.70256, 2.17340, -0.3763, -5.9845, -2.9350, -0.4815, -4.4214, -1.1300, 2.6502, -15.4134],
    'lat': [40.4165, 41.3851, 39.4699, 37.3891, 43.2630, 38.3452, 36.7213, 37.9922, 39.5696, 28.1235],
    'lon': [-3.70256, 2.17340, -0.3763, -5.9845, -2.9350, -0.4815, -4.4214, -1.1300, 2.6502, -15.4134],
    'random_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'number_assets': [34, 23, 12, 45, 67, 56, 78, 89, 90, 100],
    'value': [80, 20, 10, 80, 20, 60, 70, 80, 90, 30],
    'max': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    'label': ["Madrid: 80%", "Barcelona: 20%", "Valencia: 80%", "Seville: 80%", "Bilbao: 20%", "Alicante: 60%",
              "Malaga: 70%", "Murcia: 80%", "Palma: 90%", "Las Palmas: 100%"]
})

df_global = pd.DataFrame({
    'localid': ['Logroño', 'Oviedo', 'Santander', 'Vitoria', 'Zaragoza', 'Pamplona', 'Valladolid', 'Caceres',
                'Badajoz'],
    'coord_y': [42.4668, 43.3603, 43.4647, 42.8467, 41.6488, 42.8125, 41.6520, 39.4762, 38.8794],
    'coord_x': [-2.4500, -5.8448, -3.8044, -2.6716, -0.8891, -1.6483, -4.7280, -6.3703, -6.9707],
    'lat': [42.4668, 43.3603, 43.4647, 42.8467, 41.6488, 42.8125, 41.6520, 39.4762, 38.8794],
    'lon': [-2.4500, -5.8448, -3.8044, -2.6716, -0.8891, -1.6483, -4.7280, -6.3703, -6.9707],
    'random_number': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'number_assets': [34, 23, 12, 45, 67, 56, 78, 89, 90],
    'color': ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond'],
    'value': [80, 20, 10, 80, 20, 60, 70, 80, 90],
    'max': [100, 100, 100, 100, 100, 100, 100, 100, 100],
    'label': ["Logroño: 80%", "Oviedo: 20%", "Santander: 80%", "Vitoria: 80%", "Zaragoza: 20%", "Pamplona: 60%",
              "Valladolid: 70%", "Caceres: 80%", "Badajoz: 90%"]
})
