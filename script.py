import os
from subprocess import Popen

def varia_tam_amostra(tamanho, algoritmo):
    for i in range(1,tamanho+1):
        with open(os.path.join('command.bat'), 'w') as OPATH:
            OPATH.writelines([
                'java -cp bin MedidorDeOrdenacao '+str(algoritmo)+
                ' 1400000 1400000 > 1a/'+str(algoritmo)+'/'+
                str(algoritmo)+'_teste_'+str(i)+'.txt'])

        p=Popen("command.bat", cwd=r"C:\Users\evinh\Desktop\ADS-Lab5", encoding='utf8')
        stdout, stderr = p.communicate()

def letra_b(tamanho, algoritmo):
    for i in range(1,tamanho+1):
        with open(os.path.join('command.bat'), 'w') as OPATH:
            OPATH.writelines([
                'java -cp bin MedidorDeOrdenacao '+str(algoritmo)+
                ' 1400000 1400000 > 1b/'+str(algoritmo)+'/'+
                str(algoritmo)+'_teste_'+str(i)+'.txt'])

        p=Popen("command.bat", cwd=r"C:\Users\evinh\Desktop\ADS-Lab5", encoding='utf8')
        stdout, stderr = p.communicate()

for i in ['quick','merge']:
    varia_tam_amostra(5,i)
    letra_b(277,i)