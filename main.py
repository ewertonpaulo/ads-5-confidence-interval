from txt_handler import handler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
import scipy as sp                                                         
import scipy.stats 
import os
from IPython.display import Image

dados = []
dic = {}

hl = handler()
data_quick_1a = hl.dados_arquivos('1a/quick')
data_couting_1a = hl.dados_arquivos('1a/counting')
data_merge_1a = hl.dados_arquivos('1a/merge')


titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']

quick_1a = hl.dictonary(titulos, data_quick_1a)
counting_1a = hl.dictonary(titulos, data_couting_1a)
merge_1a = hl.dictonary(titulos, data_merge_1a)

mean_quick = statistics.mean(quick_1a['TempoDeOrdenacao'])
mean_counting = statistics.mean(quick_1a['TempoDeOrdenacao'])
mean_merge = statistics.mean(quick_1a['TempoDeOrdenacao'])

desvio_padrao_quick = np.std(quick_1a['TempoDeOrdenacao'])
desvio_padrao_merge = np.std(merge_1a['TempoDeOrdenacao'])
desvio_padrao_counting = np.std(counting_1a['TempoDeOrdenacao'])

def primeiro_a():
    hl = handler()
    for i in ['1a/quick','1a/counting','1a/merge']:
        data = hl.dados_arquivos(i)
        titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']

        dic = hl.dictonary(titulos, data)

        media = statistics.mean(dic['TempoDeOrdenacao'])
        desvio = statistics.pstdev(dic['TempoDeOrdenacao'])

        min = minimo(desvio,media)
        print(min)

def minimo(desvio,media):
    return ((100* 1.96*desvio)/(1*media))**2

primeiro_a()




