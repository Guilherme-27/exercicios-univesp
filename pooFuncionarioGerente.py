# Exercício
#
# Considere uma entidade Funcionário, que possui nome, data de admissão e salário.
# Implemente sua classe, definindo também alguns métodos para manipulação dos atributos.
#
# Em seguida, considere a entidade Gerente, que também é um funcionário.
# Além dos atributos de funcionário, um gerente também contém um bônus,
# que é uma porcentagem adicional aplicada no seu salário.
#
# Implemente a classe Gerente como uma extensão de Funcionário.

class Funcionario:
    def __init__(self, nome, admissao, salario):
        self.nome = nome
        self.admissao = admissao
        self.salario = float(salario)

    def __str__(self):
        return f'Nome: {self.nome}, Admissão: {self.admissao}, Salário: {self.salario}'

    def promover(self):
        print(f"O funcionário {self.nome} foi promovido a Gerente")
        return Gerente(self.nome, self.admissao, self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, admissao, salario_base):
        self.salario_base = salario_base
        self.bonus = 2000.00
        self.salario_total = salario_base + self.bonus
        super().__init__(nome, admissao, self.salario_total)

    def __str__(self):
        return (f'Nome: {self.nome}, Admissão: {self.admissao}, '
                f'Salário Base: {self.salario_base}, Bônus: {self.bonus}, '
                f'Salário Total: {self.salario}, Cargo: Gerente')


f1 = Funcionario("João", "2023-01-01", 3000)
print(f1)
f1 = f1.promover()
print(f1)