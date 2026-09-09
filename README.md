# 🧪 Testes Automatizados em Python

Repositório desenvolvido para atividades práticas de **testes automatizados em Python**, utilizando as bibliotecas **Unittest** e **Pytest**.

O projeto contém duas atividades:

- **Atividade 1:** Criação de uma função com parâmetros e testes utilizando `Unittest`.
- **Atividade 2:** Criação de uma função para cálculo e classificação do IMC, com testes utilizando `Pytest`.

---

# 📌 Atividade 1 — Unittest

## 🎯 Objetivo

Criar uma função com parâmetros de entrada e desenvolver testes automatizados utilizando a biblioteca `Unittest`.

A atividade solicita testes para:

- Funcionamento correto da função;
- `ValueError`;
- `TypeError`.

## 💻 Função

Foi criada uma função para calcular a média de duas notas.

A função recebe:

```python
calcular_media(nota1, nota2)
```

As notas devem ser valores numéricos.

A função verifica:

- Se as notas são números;
- Se as notas não são negativas;
- Calcula a média das duas notas.

### Exemplo

```python
calcular_media(8, 6)
```

Resultado:

```text
7.0
```

## 🧪 Testes com Unittest

Foram criados três testes:

### Teste funcional

Verifica se a função calcula a média corretamente.

```python
def test_calcular_media(self):
    resultado = calcular_media(8, 6)
    self.assertEqual(resultado, 7)
```

### Teste de ValueError

Verifica se a função apresenta `ValueError` quando uma nota negativa é informada.

```python
def test_nota_negativa(self):
    with self.assertRaises(ValueError):
        calcular_media(-5, 8)
```

### Teste de TypeError

Verifica se a função apresenta `TypeError` quando uma nota que não é numérica é informada.

```python
def test_nota_invalida(self):
    with self.assertRaises(TypeError):
        calcular_media("8", 6)
```

---

# 🧮 Atividade 2 — Cálculo de IMC

## 🎯 Objetivo

Criar uma função para calcular o **Índice de Massa Corporal (IMC)** e classificar o resultado de acordo com os padrões definidos no exercício.

A função recebe três parâmetros:

```python
calcular_imc(altura, peso, nome)
```

### Parâmetros

- `altura` → deve ser `int` ou `float`;
- `peso` → deve ser `int` ou `float`;
- `nome` → nome da pessoa.

A função retorna o **nome e a classificação do IMC**.

## 📐 Fórmula

O cálculo utilizado é:

```text
IMC = peso / (altura²)
```

## 📊 Classificação do IMC

| IMC            | Classificação      |
| -------------- | ------------------ |
| Menor que 18.5 | Abaixo do peso     |
| 18.5 – 24.9    | Peso normal        |
| 25.0 – 29.9    | Sobrepeso          |
| 30.0 – 34.9    | Obesidade grau I   |
| 35.0 – 39.9    | Obesidade grau II  |
| 40.0 ou mais   | Obesidade grau III |

## 🧪 Testes com Pytest

Foram criados testes para verificar:

### Teste funcional

Testa a função utilizando nome, altura e peso.

Exemplo:

```python
def test_calcular_imc():
    resultado = calcular_imc(1.70, 65, "Julia")

    assert resultado == ("Julia", "Peso normal")
```

### Teste de TypeError para altura

Verifica se a função apresenta erro quando a altura não é um número.

```python
def test_altura_tipo_invalido():
    with pytest.raises(TypeError):
        calcular_imc("1.70", 65, "Julia")
```

### Teste de TypeError para peso

Verifica se a função apresenta erro quando o peso não é um número.

```python
def test_peso_tipo_invalido():
    with pytest.raises(TypeError):
        calcular_imc(1.70, "65", "Julia")
```

---

# 📂 Estrutura do projeto

Uma organização possível para o repositório é:

```text

Automacao-de-Testes-de-Software/
│
├── Ex_01_app1.py
├── Ex_02_app1.py
└── README.md

```

---

# 🛠️ Tecnologias utilizadas

- **Python**
- **Unittest**
- **Pytest**

---

# ▶️ Como executar os testes

## Atividade 1 — Unittest

Entre na pasta da atividade:

```bash
cd atividade_1
```

Execute:

```bash
python -m unittest
```

---

## Atividade 2 — Pytest

Entre na pasta:

```bash
cd atividade_2
```

Caso o Pytest ainda não esteja instalado:

```bash
pip install pytest
```

Depois execute:

```bash
pytest
```

---

# ✅ Requisitos atendidos

### Atividade 1

- [x] Criar uma função com parâmetros de entrada
- [x] Criar teste funcional
- [x] Testar `ValueError`
- [x] Testar `TypeError`
- [x] Utilizar `Unittest`

### Atividade 2

- [x] Criar função para cálculo do IMC
- [x] Utilizar os parâmetros `altura`, `peso` e `nome`
- [x] Aceitar altura como `int` ou `float`
- [x] Aceitar peso como `int` ou `float`
- [x] Retornar nome e classificação do IMC
- [x] Criar teste funcional
- [x] Testar `TypeError` para altura
- [x] Testar `TypeError` para peso
- [x] Utilizar `Pytest`

---

## 👩‍💻 Autora

**Julia**

Projeto desenvolvido como atividade prática de **testes automatizados em Python**.
