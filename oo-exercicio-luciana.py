class CidadeNatal:
    def __init__(self, nome, ddd, pop):
        self.nome_cidade = nome
        self.ddd = ddd
        self.populacao = pop

class Setor:
    def __init__(self, nome_setor):
        self.nome_setor = nome_setor
        

class Pessoa:
    def __init__(self, nome, cidade_natal):
        self.nome = nome
        self.cidade_natal = cidade_natal
             

class Chefe(Pessoa):
    def __init__(self, nome, cidade_natal, setor):
        super().__init__(nome, cidade_natal)
        self.setor = setor

    def delegar_servico(self, empregado, servico):
        print(f"Chefe {self.nome} delega o serviço '{servico}' a {empregado.nome}")


class Empregado(Pessoa):
    def __init__(self, nome, cidade_natal, chefe):
        super().__init__(nome, cidade_natal)
        self.chefe = chefe

    def executar_servico(self, servico):
        print(f"Empregado {self.nome} executa o serviço '{servico}'")
  
        
class Cliente(Pessoa):
    def __init__(self, nome, cidade_natal):
        super().__init__(nome, cidade_natal)

    def solicitar_servico(self, servico):
        print(f"Cliente {self.nome} solicita o serviço '{servico}'")
        
    def fazer_pagamento(self, valor):
        print(f"Cliente {self.nome} fez um pagamento de R${valor}")




macae = CidadeNatal("Macaé")
riodasostras = CidadeNatal("Rio das Ostras")

manutencao = Setor("Manutenção")

maria = Chefe("Maria", riodasostras, manutencao)
joao = Empregado("João", macae, maria)

luciana = Cliente("Luciana", macae)


luciana.solicitar_servico("Limpeza")
maria.delegar_servico(joao, "Limpeza")
joao.executar_servico("Limpeza")
luciana.fazer_pagamento(100)


print(luciana.nome)
print(luciana.cidade_natal.nome_cidade)



print(maria.nome)
print(maria.cidade_natal.nome_cidade)
print(maria.setor.nome_setor)




print(joao.nome)
print(joao.cidade_natal.nome_cidade)
print(joao.chefe.nome)
print(joao.chefe.setor.nome_setor)


