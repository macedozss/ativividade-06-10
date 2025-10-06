class Saldo:
    # Atributos de classe
    desconto = 20

    def __init__(self, nome, saldo_atual):
        # Atributos de instancia
        self.nome = nome
        self.saldo_atual = saldo_atual

    def resultado(self):
        # Caulcula o saldo final aplicando o desconto
        saldo_final = self.saldo_atual - Saldo.desconto
        print(f"Cliente: {self.nome}| saldo final apósdesconto: R${saldo_final:.2f}")

# Execução
cliente1 = Saldo("maria", 150.00)
cliente1.resultado()