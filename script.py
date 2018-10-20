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

def segundo_a(tamanho, algoritmo):
    for i in range(14000000,tamanho,200000):
        with open(os.path.join('command.bat'), 'w') as OPATH:
            OPATH.writelines([
                'java -cp bin MedidorDeOrdenacao '+str(algoritmo)+' '+
                str(i)+' 1400000 > 2a/'+str(algoritmo)+'/'+
                str(algoritmo)+'_teste_'+str(i)+'.txt'])

        p=Popen("command.bat", cwd=r"C:\Users\evinh\Desktop\ADS-Lab5", encoding='utf8')
        stdout, stderr = p.communicate()

def segundo_b(tamanho, algoritmo):
    for i in range(14000000,tamanho,200000):
        with open(os.path.join('command.bat'), 'w') as OPATH:
            OPATH.writelines([
                'java -cp bin MedidorDeOrdenacao '+str(algoritmo)+
                ' 1400000 '+str(i)+'> 2b/'+str(algoritmo)+'/'+
                str(algoritmo)+'_teste_'+str(i)+'.txt'])

        p=Popen("command.bat", cwd=r"C:\Users\evinh\Desktop\ADS-Lab5", encoding='utf8')
        stdout, stderr = p.communicate()

for i in ['counting']:
    varia_tam_amostra(5,i)
    letra_b(277,i)
    segundo_a(40000000,i)
    segundo_b(40000000,i)