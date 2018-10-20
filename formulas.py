import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
import assistance
import scipy as sp                                                         
import scipy.stats 
import os
from IPython.display import Image

dados_quick_1_a = assistance.carregar('quick-1-a/','quick-1-a', 0, 4)
dados_merge_1_a = assistance.carregar('merge-1-a/','merge-1-a', 0, 4)
dados_counting_1_a = assistance.carregar('counting-1-a/','counting-1-a', 0, 4)
dados_quick_1_b = assistance.carregar('quick-1-b/','quick-1-b', 0, 31)
dados_merge_1_b = assistance.carregar('merge-1-b/','merge-1-b', 0, 31)
dados_counting_1_b = assistance.carregar('counting-1-b/','counting-1-b', 0, 31)
dados_quick_2_a= assistance.carregar('quick/','quick', 0, 49)
dados_merge_2_a = assistance.carregar('merge/', 'merge', 0, 49)
dados_counting_2_a = assistance.carregar('counting/','counting', 0, 42)
dados_quick_2_b = assistance.carregar('quick-2-b/','quick-2-b', 0, 49)
dados_merge_2_b = assistance.carregar('merge-2-b/','merge-2-b/', 0, 49)
dados_counting_2_b = assistance.carregar('counting-2-b/','counting-2-b', 0, 42)
dados_quick_2_a.sort(key=assistance.chave1)
dados_merge_2_a.sort(key=assistance.chave1)
dados_counting_2_a.sort(key=assistance.chave1)
dados_quick_2_b.sort(key=assistance.chave2)
dados_merge_2_b.sort(key=assistance.chave2)
dados_counting_2_b.sort(key=assistance.chave2)
titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']

quick_1_a = assistance.gerar_listas_por_colunas(titulos, dados_quick_1_a)
merge_1_a = assistance.gerar_listas_por_colunas(titulos, dados_merge_1_a)
counting_1_a = assistance.gerar_listas_por_colunas(titulos, dados_counting_1_a)
quick_1_b = assistance.gerar_listas_por_colunas(titulos, dados_quick_1_b)
merge_1_b = assistance.gerar_listas_por_colunas(titulos, dados_merge_1_b)
counting_1_b = assistance.gerar_listas_por_colunas(titulos, dados_counting_1_b)
quick_2_a =  assistance.gerar_listas_por_colunas(titulos, dados_quick_2_a)
merge_2_a =  assistance.gerar_listas_por_colunas(titulos, dados_merge_2_a)
counting_2_a =  assistance.gerar_listas_por_colunas(titulos, dados_counting_2_a)
quick_2_b =  assistance.gerar_listas_por_colunas(titulos, dados_quick_2_b)
merge_2_b =  assistance.gerar_listas_por_colunas(titulos, dados_merge_2_b)
counting_2_b =  assistance.gerar_listas_por_colunas(titulos, dados_counting_2_b)

media_quick = statistics.mean(quick_1_a['TempoDeOrdenacao'])
media_merge = statistics.mean(merge_1_a['TempoDeOrdenacao'])
media_counting = statistics.mean(counting_1_a['TempoDeOrdenacao'])
media_quick_1_b = statistics.mean(quick_1_b['TempoDeOrdenacao'])
media_merge_1_b = statistics.mean(merge_1_b['TempoDeOrdenacao'])
media_counting_1_b = statistics.mean(counting_1_b['TempoDeOrdenacao'])

desvio_padrao_quick = np.std(quick_1_a['TempoDeOrdenacao'])
desvio_padrao_merge = np.std(merge_1_a['TempoDeOrdenacao'])
desvio_padrao_counting = np.std(counting_1_a['TempoDeOrdenacao'])
desvio_padrao_quick_1_b = np.std(quick_1_b['TempoDeOrdenacao'])
desvio_padrao_merge_1_b = np.std(merge_1_b['TempoDeOrdenacao'])
desvio_padrao_counting_1_b = np.std(counting_1_b['TempoDeOrdenacao'])

intervalo_de_conf_infe_and_supe_quick_1_b = scipy.stats.norm.interval(0.95, loc=media_quick_1_b, scale=desvio_padrao_quick_1_b)
intervalo_de_conf_infe_and_supe_merge_1_b = scipy.stats.norm.interval(0.95, loc=media_merge_1_b, scale=desvio_padrao_merge_1_b)
intervalo_de_conf_infe_and_supe_counting_1_b = scipy.stats.norm.interval(0.95, loc=media_counting_1_b, scale=desvio_padrao_counting_1_b)
intervalo_de_conf_quick_1_b = (intervalo_de_conf_infe_and_supe_quick_1_b[1]-intervalo_de_conf_infe_and_supe_quick_1_b[0])/2
intervalo_de_conf_merge_1_b = (intervalo_de_conf_infe_and_supe_merge_1_b[1]-intervalo_de_conf_infe_and_supe_merge_1_b[0])/2
intervalo_de_conf_counting_1_b = (intervalo_de_conf_infe_and_supe_counting_1_b[1]-intervalo_de_conf_infe_and_supe_counting_1_b[0])/2

minimo_quick = ((100* 1.96*desvio_padrao_quick)/(media_quick))**2
minimo_merge = ((100* 1.96*desvio_padrao_merge)/(media_merge))**2
minimo_counting = ((100* 1.96*desvio_padrao_counting)/(media_counting))**2
quest_1_a = pd.DataFrame([minimo_quick,minimo_merge,minimo_counting], index=['quick','merge','counting'],columns=['Número mínimo de observações'])
media_quest_1_b = pd.DataFrame([media_quick_1_b,media_merge_1_b,media_counting_1_b], index=['quick','merge','counting'],columns=['Media'])
interval_conf_quest_1_b = pd.DataFrame(data={'Intervalo de Confianca':[intervalo_de_conf_quick_1_b,intervalo_de_conf_merge_1_b,intervalo_de_conf_counting_1_b],
    'Intervalo inferior': [intervalo_de_conf_infe_and_supe_quick_1_b[0], intervalo_de_conf_infe_and_supe_merge_1_b[0], intervalo_de_conf_infe_and_supe_counting_1_b[0]],
    'Intervalo superior': [intervalo_de_conf_infe_and_supe_quick_1_b[1], intervalo_de_conf_infe_and_supe_merge_1_b[1], intervalo_de_conf_infe_and_supe_counting_1_b[1]]},
    index=['quick','merge','counting'])
