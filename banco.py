import abc


class Banco(abc.ABC):
    def __init__(
        self, nome: str, conta: int = 0, saldo: float = 0.00
    ) -> None:
        super().__init__()
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def levantar(self, valor: float) -> None: ...

    def depositar(self, valor: float) -> None:
        deposito = self.saldo + valor
        self.saldo = deposito
        self._informacao(f"DEPÓSITO: MZN {valor:.2f} na conta {self.conta}\n")

    def _informacao(self, msg: str) -> str:
        print(msg)
        return msg


class Operacoes(Banco):
    def levantar(self, valor: float) -> None:
        saque = self.saldo - valor
        
        if saque >= 0:
            self.saldo -= valor
            self._informacao(f"LEVANTAMENTO: MZN {valor:.2f}\n")
            return
        
        self._informacao(f"OPERAÇÃO RECUSADA. Saldo MZN {self.saldo:.2f}\n")

    def consulta(self) -> str:
        return self._informacao(f"CONSULTA: saldo MZN {self.saldo:.2f}\n")

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attr = f"{class_name}{self.nome, self.conta, self.saldo}"
        return attr


class Cliente(Operacoes):
    ...


if __name__ == "__main__":
    joao = Cliente("Joao", 12345, 0)

    while True:
        instrucao = input("1. Depósitar\n2. Levantar\n3. Saldo\n0. Sair\n\t")
        
        if instrucao.isdigit():
            instrucao = int(instrucao)
        else:
            continue

        valor: float = 0
        pedido_valor = instrucao == 1 or instrucao == 2

        if pedido_valor:
            while True:

                try:
                    valor = float(input("Valor: "))
                    break
                except ValueError:
                    print("Verifique o valor digitado!\n")


        if instrucao == 1:
            joao.depositar(valor)

        elif instrucao == 2:
            joao.levantar(valor)

        elif instrucao == 3:
            saldo = joao.consulta()
        
        elif instrucao == 0:
            print(
                "\n=== Obrigado por usar os nossos serviços. Volte Sempe. ===\n"
            )
            break
        