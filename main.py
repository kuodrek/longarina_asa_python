import itertools
import calcula_longarina

# 2.Dimensões de tubo disponíveis e propriedades
#       De          Di           E      Densidade     Xt           G
M = [
    [08.225E-03, 07.3400E-03, 44.93e9, 0.03274, 430e6, 46.950e9],
    [11.430E-03, 10.5156E-03, 44.93e9, 0.04762, 430e6, 46.950e9],
    [12.573E-03, 11.0490E-03, 44.93e9, 0.08482, 500e6, 46.950e9],
    [14.605E-03, 13.6906E-03, 44.93e9, 0.062503, 430e6, 46.950e9],  # 5 camadas
    [17.780E-03, 16.8656E-03, 44.93e9, 0.077384, 430e6, 46.950e9],  # 5 camadas
    [20.955E-03, 20.0406E-03, 44.93e9, 0.092266, 430e6, 46.950e9],  # 5 camadas
    [15.748E-03, 14.2240E-03, 44.93e9, 0.110125, 500e6, 46.950e9],  # 9 camadas
    [18.923E-03, 17.3990E-03, 44.93e9, 0.13393, 500e6, 46.950e9],  # 9 camadas
    [22.098E-03, 20.574E-03, 44.93e9, 0.148816, 500e6, 46.950e9],  # 9 camadas
    [22.098E-03, 20.574E-03, 44.93e9, 0.148816, 500e6, 46.950e9],  # 9 camadas
]

n_particoes = 3

# Atencao: o numero de particoes e tubos afeta a performance muito rapidamente

# Todas as possiveis longarinas a serem calculadas
lista_longarinas = itertools.combinations_with_replacement(range(len(M)), n_particoes)

longarina_dict = {
    'deu_boa': False,
    'index': (1, 2, 3),
    'de': (1, 2, 3),
    'di': (0.5, 1.5, 2.5),
    'massa': 100,
    'deflexao': 20e-3,
    'torcao': 30e-3,
    'FS': (1.6, 1.5, 2.0),
    }

for longarina in list(lista_longarinas):
    longarina_dict = calcula_longarina(longarina)
    longarina_massa = longarina_dict['massa']
    if longarina_dict['deu_boa'] is True and menor_massa > longarina_dict['massa']:
        melhor_longarina = longarina_dict
        menor_massa = melhor_longarina['massa']




