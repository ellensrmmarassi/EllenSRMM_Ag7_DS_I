<div align="center">

# 💧 Consumo de Água

### Sistema simples para avaliar o consumo mensal de água em diferentes tipos de imóveis.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white)
![Energia consciente](https://img.shields.io/badge/%E2%9A%A1_Energia-Consumo_consciente-2E7D32?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluido-F2C94C?style=for-the-badge&logo=progress&logoColor=black)

</div>

## 🎯 Objetivo

O **Consumo de Água** é um programa de linha de comando desenvolvido para analisar o consumo mensal de água de um imóvel. A aplicação identifica o tipo de imóvel informado, aplica regras simples de consumo e apresenta uma mensagem de orientação ao usuário.

O sistema contempla:

- 🏠 Imóveis residenciais, como casas e apartamentos;
- 🏢 Imóveis comerciais, com indicação para consulta de plano corporativo;
- ✅ Validação do tipo de imóvel;
- 💡 Alertas para consumo econômico, moderado ou excessivo.

## 🛠️ Tecnologia utilizada

![Python](https://img.shields.io/badge/Linguagem-Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white)

O projeto foi escrito em **Python**, utilizando apenas recursos nativos da linguagem e entradas pelo terminal. Não é necessário instalar bibliotecas externas.

## ▶️ Como executar

### Pré-requisitos

- 🐍 Python 3.x instalado;
- 💻 Terminal ou prompt de comando.

### Passo a passo

1. Abra o terminal na pasta do projeto:

	```bash
	cd consumo-agua
	```

2. Execute o programa:

	```bash
	python app.py
	```

	No Windows, também é possível usar:

	```bash
	py app.py
	```

3. Informe o tipo do imóvel usando uma das opções aceitas: `casa`, `comercial` ou `apartamento`.

4. Para imóveis residenciais, informe o consumo mensal em **m³ como número inteiro**.

## 📊 Regras de classificação

| Situação | Resultado apresentado |
| --- | --- |
| Tipo de imóvel diferente de `casa`, `comercial` ou `apartamento` | Opção informada inválida |
| Imóvel comercial | Tarifa comercial aplicada |
| Apartamento com consumo abaixo de 10 m³ | Consumo econômico |
| Casa ou apartamento com consumo de até 25 m³ | Consumo moderado |
| Qualquer imóvel com consumo acima de 25 m³ | Consumo excessivo e recomendação para verificar vazamentos |

## 📁 Estrutura do projeto

```text
consumo-agua/
├── app.py       # Código principal do sistema
└── README.md    # Documentação do projeto
```

## 🌱 Consumo consciente

Use os resultados como um alerta para acompanhar o uso de água, identificar possíveis vazamentos e adotar hábitos mais sustentáveis. Cada economia ajuda a preservar esse recurso essencial. 💧⚡
