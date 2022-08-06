tipo_carro = 'Carro'
tipo_moto = 'Moto'

class Estacionamento: 
    def __init__(self, limite_vagas_carro, limite_vagas_moto):
        self.__vagas = []
        self.__limite_vagas_carro = limite_vagas_carro
        self.__limite_vagas_moto = limite_vagas_moto
    
    def adicionar_vaga(self, vaga):
        if vaga.tipo_veiculo == tipo_moto:
            if self.total_vagas_moto >= self.limite_vagas_moto:
                return
            if self.total_vagas_moto < self.limite_vagas_moto:
                self.__vagas.append(vaga)

        if vaga.tipo_veiculo == tipo_carro:
            if self.total_vagas_carro >= self.limite_vagas_carro:
                return
            if self.total_vagas_carro < self.limite_vagas_carro:
                self.__vagas.append(vaga)


    @property
    def limite_vagas_carro(self):
        return self.__limite_vagas_carro

    @property
    def limite_vagas_moto(self):
        return self.__limite_vagas_moto   
          
    @property
    def vagas(self):
        return self.__vagas

    @property
    def total_vagas(self):
        return len(self.vagas)

    @property
    def total_limite_vagas(self):
        return self.limite_vagas_carro + self.limite_vagas_moto

    @property
    def vagas_carro(self):
        vagas_carros = []
        for vaga in self.vagas:
            if vaga.tipo_veiculo == tipo_carro:
                vagas_carros.append(vaga)
        return vagas_carros

    @property
    def vagas_carro_livre(self):
        vagas_carro_livre = []
        for vaga in self.vagas_carro:
            if vaga.esta_livre:
                vagas_carro_livre.append(vaga)
        return vagas_carro_livre

    @property
    def total_vagas_carro(self):
        return len(self.vagas_carro)

    @property
    def total_vagas_carro_livre(self):
        return len(self.vagas_carro_livre)
    
    @property
    def total_vagas_carro_ocupada(self):
        return self.total_vagas_carro - self.total_vagas_carro_livre

    @property
    def vagas_moto(self):
        vagas_motos = []
        for vaga in self.vagas:
            if vaga.tipo_veiculo == tipo_moto :
                vagas_motos.append(vaga)
        return vagas_motos

    @property
    def total_vagas_moto(self):
        return len(self.vagas_moto)
    
    @property
    def vagas_moto_livre(self):
        vagas_moto_livre = []
        for vaga in self.vagas_moto:
            if vaga.esta_livre:
                vagas_moto_livre.append(vaga)
        return vagas_moto_livre

    @property
    def total_vagas_moto(self):
        return len(self.vagas_moto)

    @property
    def total_vagas_moto_livre(self):
        return len(self.vagas_moto_livre)
    
    @property
    def total_vagas_moto_ocupada(self):
        return self.total_vagas_moto - self.total_vagas_moto_livre

    
    @property
    def id_vagas_disponiveis_carro(self):
        id_vagas_carro_livre = []
        print('A vaga que está disponível é:')
        for vaga in self.vagas_carro_livre:
            print(vaga.id)
            id_vagas_carro_livre.append(vaga.id)
        return id_vagas_carro_livre

    @property
    def id_vagas_disponiveis_moto(self):
        id_vagas_moto_livre = []
        print('A vaga que está disponível é:')
        for vaga in self.vagas_moto_livre:
            print(vaga.id)
            id_vagas_moto_livre.append(vaga.id)
        return id_vagas_moto_livre

    @property
    def id_primeira_vaga_carro_livre(self):
        print(self.vagas_carro_livre[0].id)
        return self.vagas_carro_livre[0].id

    @property
    def id_primeira_vaga_moto_livre(self):
        print(self.vagas_moto_livre[0].id)
        return self.vagas_moto_livre[0].id
    
    def posicao_vaga_por_id(self, id):
        posicao = 0
        for i in range(0, self.total_vagas):
            if self.vagas[i].id == id:
                posicao = i
        return posicao


    def estacionar_carro(self, veiculo):
        if self.total_vagas_carro_livre == 0:
            print('Não há vagas livres!')
            return 
        if self.total_vagas_carro_livre > 0:
            id = self.id_primeira_vaga_carro_livre
            posicao = self.posicao_vaga_por_id(id)
            self.__vagas[posicao].ocupar_vaga(veiculo)

    def estacionar_moto(self, veiculo):
        if self.total_vagas_moto_livre > 0:
            id = self.id_primeira_vaga_moto_livre
            posicao = self.posicao_vaga_por_id(id)
            self.__vagas[posicao].ocupar_vaga(veiculo)
        if self.total_vagas_moto_livre == 0:
            if self.total_vagas_carro_livre > 0:
                self.estacionar_carro(veiculo)
            if self.total_vagas_carro_livre == 0:
                print('Não há vagas livres!')
                return 
             

    def remover_veiculo(self, id_vaga):
        posicao = self.posicao_vaga_por_id(id_vaga)
        self.__vagas[posicao].desocupar_vaga()


    
    def estado_do_estacionamento(self):
        if self.total_vagas_carro_livre == 0:
            print('Não há vagas de carro!') 
        if self.total_vagas_moto_livre == 0:
            print('Não há vagas de moto!')
        if self.total_vagas_carro_livre >0:
            print(f'Há {self.total_vagas_carro_livre} vagas de carro disponíveis!')
        if self.total_vagas_moto_livre >0 or self.total_vagas_carro_livre>0:
            print(f'Há {self.total_vagas_moto_livre + self.total_vagas_carro_livre} vagas de moto disponíveis!')



class Vaga:
    def __init__(self, id, tipo_veiculo):
        self.__id = id 
        self.__tipo_veiculo = tipo_veiculo
        self.__veiculo = False
        
    @property
    def id(self):
        return self.__id
    @property
    def tipo_veiculo(self):
        return self.__tipo_veiculo
    @property
    def veiculo(self):
        return self.__veiculo
    @property
    def placa(self):
        if self.esta_livre:
            return
        if not self.esta_livre:
            return self.veiculo.placa
    @property
    def esta_livre(self):
        return self.veiculo == False

    def ocupar_vaga(self, veiculo):
        if not self.esta_livre:
            return
        if self.esta_livre:
            self.__veiculo = veiculo

    def desocupar_vaga(self):
        if not self.esta_livre:
            self.__veiculo = False

class Veiculo:
    def __init__(self, placa):
        self.__placa = placa
    @property
    def placa(self):
        return self.__placa

class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
    @property
    def tipo():
        return tipo_carro

class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
    @property
    def tipo():
        return tipo_moto



meu_estacionamento = Estacionamento(5,5)
carros = []
motos = []

for i in range(1,6):
    meu_estacionamento.adicionar_vaga(Vaga(f'C{i}', tipo_carro))
    meu_estacionamento.adicionar_vaga(Vaga(f'M{i}', tipo_moto))
    carros.append(Carro(f'CARRO-000{i}'))
    motos.append(Moto(f'MOTO-000{i}'))

# meu_estacionamento.id_vagas_disponiveis_carro
# meu_estacionamento.id_vagas_disponiveis_moto
meu_estacionamento.estacionar_carro(carros[0])
meu_estacionamento.estacionar_carro(carros[2])
meu_estacionamento.estacionar_moto(motos[0])
meu_estacionamento.estacionar_moto(motos[1])
meu_estacionamento.estacionar_moto(motos[2])

for i in range(0, meu_estacionamento.total_vagas):
    print(f'{i} - {meu_estacionamento.vagas[i].esta_livre} - {meu_estacionamento.vagas[i].id}')
    if not meu_estacionamento.vagas[i].esta_livre:
        print(f'{meu_estacionamento.vagas[i].veiculo.placa}')

meu_estacionamento.estado_do_estacionamento()

meu_estacionamento.remover_veiculo('C2')
meu_estacionamento.estado_do_estacionamento()



