import os

class handler:
    def dados_arquivos(self, dir_):
        dados = []
        arquivos = os.listdir(dir_)
        for i in range(len(arquivos)):
            nome = dir_+"/"+arquivos[i]
            txt = open(nome,'r')
            linha = txt.readlines()
            linha[1] = linha[1].replace("\n,","")
            lista_linhas = linha[1].split()
            i=1
            while i < len(lista_linhas):
                lista_linhas[i] = int(lista_linhas[i])
                i+=1
            dados.append(lista_linhas)

        txt.close()
        return dados

    def dictonary(self,titles, dados):
        i = 0
        dic={}
        for coluna in titles:
            dic[coluna] = []
        for i in dados:
            dic[titles[0]].append(i[0])
            dic[titles[1]].append(i[1])
            dic[titles[2]].append(i[2])
            dic[titles[3]].append(i[3])
        return dic
