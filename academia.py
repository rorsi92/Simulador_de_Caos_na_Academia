import random

# Este código define uma classe chamada Academia, que simula o funcionamento de uma academia com halteres:

# 1: self.halteres é uma lista de halteres disponíveis na academia. São números de 10 a 36 (inclusive) que são múltiplos de 2.
# - self.porta_halteres é um dicionário que mapeia cada halter disponível para a sua posição na academia.
# - self.reiniciar_o_dia() é chamado para inicializar o estado dos halteres no início do dia.

# 2: O método reiniciar_o_dia redefine o dicionário self.porta_halteres para mapear cada halter disponível para sua posição na academia.

# 3: O método listar_halteres retorna uma lista dos halteres disponíveis na academia, excluindo aqueles que estão atualmente sendo usados (representados por 0).

# 4: O método pega_haltere recebe um peso de halter como parâmetro e simula alguém pegando um halter da academia com o peso especificado.
# - halt_pos é a posição do halter na academia, obtida a partir do valor fornecido.
# - key_halt é a chave (posição) no dicionário self.porta_halteres correspondente ao halter selecionado.
# - O valor do dicionário self.porta_halteres para a chave key_halt é alterado para 0 para indicar que o halter está em uso.
# - O peso do halter é retornado.

# 5: O método devolver_halter recebe a posição e o peso do halter e atualiza o dicionário self.porta_halteres para indicar que o halter foi devolvido à academia.

# 6: O método calcular_caos calcula a quantidade de "caos" na academia, que é definido como o número de halteres colocados em posições diferentes da sua posição original, dividido pelo total de halteres disponíveis na academia.

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10,36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pega_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt= list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos)/len(self.porta_halteres)

# Este código define uma classe chamada Usuario, que representa os usuários da academia e suas interações com os halteres durante o treino:

# 1: self.tipo representa o tipo de usuário: 1 para normal e 2 para bagunçeiro.
# - self.academia é uma referência à instância da academia em que o usuário está treinando.
# - self.peso armazena o peso do halter que o usuário está usando.  

# 2: O método iniciar_treino é chamado quando o usuário inicia o treino. Ele escolhe aleatoriamente um peso de halter disponível 
# na academia usando o método listar_halteres da academia e então pega esse halter chamando o método pega_haltere.     

# 3: O método finalizar_treino é chamado quando o usuário finaliza o treino.
# - Ele verifica se há espaços vazios na academia para devolver o halter.
# - Se o usuário for do tipo 1 (normal), ele verifica se o peso do halter está em um espaço vazio. Se estiver, o halter é devolvido à sua posição original na academia. Caso contrário, um espaço vazio é escolhido aleatoriamente e o halter é devolvido lá.
# - Se o usuário for do tipo 2 (bagunçeiro), ele simplesmente escolhe aleatoriamente um espaço vazio e devolve o halter lá.
# - O atributo self.peso é redefinido como 0 após o término do treino.

# Esse código simula o comportamento dos usuários em uma academia, onde usuários normais tentam devolver os halteres aos seus lugares originais, 
# enquanto usuários bagunçeiros os devolvem aleatoriamente em espaços vazios.

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 - normal / 2 - bagunçeiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pega_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0

# Este código simula o funcionamento de uma academia ao longo de 50 dias, 
# com uma série de usuários realizando treinos durante cada dia. Abaixo está uma explicação do que cada parte do código faz:

# 1: Inicialização da Academia e dos Usuários:
# - academia = Academia(): Cria uma instância da classe Academia.
# - usuarios = [Usuario(1,academia) for i in range(10)]: Cria uma lista de 10 usuários normais.
# - usuarios += [Usuario(2,academia) for i in range(1)]: Adiciona um usuário bagunçeiro à lista de usuários.
# - random.shuffle(usuarios): Embaralha a ordem dos usuários na lista.

# 2: Simulação dos Dias de Treino:
# - for k in range(50): Para cada um dos 50 dias de simulação:
#    academia.reiniciar_o_dia(): Reinicia o estado da academia para o início do dia.
# - for i in range(10): Para cada um dos 10 treinos realizados durante o dia:
#    random.shuffle(usuarios): Embaralha a ordem dos usuários para variar quem inicia o treino primeiro.
#    for user in usuarios: user.iniciar_treino(): Cada usuário inicia seu treino, pegando um halter disponível na academia.
#    for user in usuarios: user.finalizar_treino(): Cada usuário finaliza seu treino, devolvendo o halter à academia.
# - list_chaos += [academia.calcular_caos()]: Calcula e armazena o nível de "caos" na academia após cada dia de treino na lista list_chaos.

# 3: Plotagem do Gráfico:
# - import matplotlib.pyplot as plt: Importa o módulo Matplotlib para a plotagem.
# - import seaborn as sns: Importa o módulo Seaborn para aprimorar a visualização.
# - sns.displot(list_chaos): Cria um histograma para visualizar a distribuição dos níveis de "caos" ao longo dos 50 dias.
# - plt.show(): Exibe o gráfico na interface do usuário.


academia = Academia()

usuarios = [Usuario(1,academia) for i in range(10)]
usuarios += [Usuario(2,academia) for i in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia.calcular_caos()]

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(list_chaos)
plt.show()
