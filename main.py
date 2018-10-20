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
    for i in ['quick','counting','merge']:
        data = hl.dados_arquivos('1a/'+i)
        titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']
        dic = hl.dictonary(titulos, data)
        media = statistics.mean(dic['TempoDeOrdenacao'])
        desvio = statistics.pstdev(dic['TempoDeOrdenacao'])
        min = minimo(desvio,media)
        print(i +' ==> %s' %min)
        input()
    os.system('cls')

def primeiro_b():
    hl = handler()
    for i in ['quick','counting','merge']:
        data = hl.dados_arquivos('1b/'+i)
        titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']
        dic = hl.dictonary(titulos, data)
        media = statistics.mean(dic['TempoDeOrdenacao'])
        desvio = statistics.pstdev(dic['TempoDeOrdenacao'])
        inter = scipy.stats.norm.interval(0.95, loc=media, scale=desvio)
        intervalo_1b = (inter[1]-inter[0])/2
        print(i +' media ==> %s' %media)
        print('Intervalo de Confianca ==> %s' %intervalo_1b)
        print('Intervalo inferior ==> %s' %inter[0])
        print('Intervalo superior ==> %s' %inter[1])
        input()
       

def minimo(desvio,media):
    return ((100* 1.96*desvio)/(1*media))**2

primeiro_a()




