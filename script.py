import os
from subprocess import Popen

def varia_tam_amostra(intervalo, tamanho, algoritmo):
    for i in range(1,tamanho+1):
        with open(os.path.join('command.bat'), 'w') as OPATH:
            OPATH.writelines([
                'java -cp bin MedidorDeOrdenacao '+str(algoritmo)+
                ' 1400000 1400000 > 1a/'+str(algoritmo)+'/'+
                str(algoritmo)+'_teste_'+str(i)+'.txt'])

        p=Popen("command.bat", cwd=r"C:\Users\evinh\Desktop\ADS-Lab5", encoding='utf8')
        stdout, stderr = p.communicate()

for i in ['quick','merge','counting']:
    varia_tam_amostra(1,5,i)