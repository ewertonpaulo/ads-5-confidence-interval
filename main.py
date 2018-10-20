from txt_handler import handler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
import scipy as sp                                                         
import scipy.stats 
import os
from IPython.display import Image

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

def segundo_a():
    hl = handler()
    for i in ['quick','counting','merge']:
        data = hl.dados_arquivos('2a/'+i)
        titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']
        dic = hl.dictonary(titulos, data)
        plt.plot(dic['TamanhoDaEntrada'], dic['TempoDeOrdenacao'])
        plt.show()

def segundo_b():
    hl = handler()
    for i in ['quick','counting','merge']:
        data = hl.dados_arquivos('2b/'+i)
        titulos = ['algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao']
        dic = hl.dictonary(titulos, data)
        plt.plot(dic['ValorMaximo'], dic['TempoDeOrdenacao'])
        plt.show()

def minimo(desvio,media):
    return ((100* 1.96*desvio)/(1*media))**2

primeiro_a()
primeiro_b()
segundo_a()
segundo_b()



