from objetivo_a.culturas import CULTURA_1, CULTURA_2
from typing import List
import json
from time import sleep


class Area:
    # 1 = retângulo
    # 2 = triangulo
    tipo: str
    base: float
    altura: float

    def __init__(self, tipo: str, base: float, altura: float):
        self.tipo = tipo
        self.base = base
        self.altura = altura

    def to_json(self):
        return {
            "tipo": self.tipo,
            "base": self.base,
            "altura": self.altura
        }

    @classmethod
    def from_json(cls, json):
        return cls(json['tipo'], json['base'], json['altura'])

    def calcular_area(self):
        if self.tipo == '2':
            return self.base * self.altura / 2
        elif self.tipo == '1':
            return self.base * self.altura
        else:
            raise Exception('Tipo inválido')

    def __str__(self):
        if self.tipo == '1':
            return f'Tipo: Retângulo, Base: {self.base:.2f} m, Altura: {self.altura:.2f} m, Área: {self.calcular_area():.2f} m²'
        elif self.tipo == '2':
            return f'Tipo: Triângulo, Base: {self.base:.2f} m, Altura: {self.altura:.2f} m, Área: {self.calcular_area():.2f} m²'
        else:
            return f'Tipo: Inválido, Base: {self.base:.2f} m, Altura: {self.altura:.2f} m, Área: {self.calcular_area():.2f} m²'

class Culturas:

    cultura_1: List[Area] = []

    cultura_2: List[Area] = []

    def __getitem__(self, key):

        if key.lower() == 'cultura_1' or key.lower() == 'cultura1' or key.lower() == CULTURA_1.lower():
            return self.cultura_1

        elif key.lower() == 'cultura_2' or key.lower() == 'cultura2' or key.lower() == CULTURA_2.lower():
            return self.cultura_2

        else:
            raise KeyError(f'Key inválida {key}')

    def append_area_cultura_1(self, tipo:str, base:float, altura:float):
        self.cultura_1.append(Area(
            tipo=tipo,
            base=base,
            altura=altura
        ))
        self._write_to_file()

    def remove_area_cultura_1(self, index:int):
        self.cultura_1.pop(index)
        self._write_to_file()

    def replace_area_cultura_1(self, index:int, tipo:str, base:float, altura:float):
        self.cultura_1[index] = Area(
            tipo=tipo,
            base=base,
            altura=altura
        )
        self._write_to_file()

    def append_area_cultura_2(self, tipo:str, base:float, altura:float):
        self.cultura_2.append(Area(
            tipo=tipo,
            base=base,
            altura=altura
        ))
        self._write_to_file()

    def remove_area_cultura_2(self, index:int):
        self.cultura_2.pop(index)
        self._write_to_file()

    def replace_area_cultura_2(self, index:int, tipo:str, base:float, altura:float):
        self.cultura_2[index] = Area(
            tipo=tipo,
            base=base,
            altura=altura
        )
        self._write_to_file()

    def _write_to_file(self):
        print('Salvando...')
        retries = 0

        while retries < 3:
            try:
                with open('culturas.json', 'w') as f:
                    f.write(json.dumps(self.to_json()))
                    print('Dados Salvos com sucesso!')
                    return
            except Exception as e:
                retries += 1
                if retries >= 3:
                    raise e
                sleep(0.5)


    def to_json(self):
        return {
            "cultura_1": [area.to_json() for area in self.cultura_1],
            "cultura_2": [area.to_json() for area in self.cultura_2]
        }

    @classmethod
    def from_json(cls, json):
        culturas = cls()
        culturas.cultura_1 = [Area.from_json(area) for area in json['cultura_1']]
        culturas.cultura_2 = [Area.from_json(area) for area in json['cultura_2']]
        return culturas

    @classmethod
    def new_or_from_file(cls):
        try:
            with open('culturas.json', 'r') as f:

                classe = cls.from_json(json.loads(f.read()))

                print(f'Dados carregados com sucesso!\n{classe}')

                return classe
        except:
            return cls()

    def __str__(self):

        resp = 'CULTURAS'

        if len(self.cultura_1) > 0:
            resp += f'\n{CULTURA_1.capitalize()}:\n'
            resp += '\n'.join([str(area) for area in self.cultura_1])

        if len(self.cultura_2) > 0:
            resp += f'\n{CULTURA_2.capitalize()}:\n'
            resp += '\n'.join([str(area) for area in self.cultura_2])

        return  resp