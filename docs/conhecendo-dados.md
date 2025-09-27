# Conhecendo os dados
Nesta etapa, realizou-se uma análise detalhada para compreender a estrutura da base de dados, identificar outliers, e avaliar relações entre variáveis.

1. Importação das Bibliotecas

<img width="563" height="180" alt="image" src="https://github.com/user-attachments/assets/9a6a1e02-fdfb-410b-973b-2cdbc9712a03" />


As bibliotecas escolhidas permitem: manipular dados (pandas, numpy), gerar visualizações (matplotlib, seaborn) e preparar a base para modelos de machine learning (sklearn, shap).

2. Coleta  de Dados e criação do dataframe

<img width="811" height="403" alt="image" src="https://github.com/user-attachments/assets/6ab53a4f-1436-49df-b523-1a0fa0550063" />

O dataset utilizado neste trabalho foi obtido da plataforma Kaggle por meio da biblioteca kagglehub, que permite baixar e acessar datasets diretamente em ambientes como Google Colab.

Tipo de Dados

<img width="523" height="473" alt="image" src="https://github.com/user-attachments/assets/dea6034d-6e52-47bd-966c-d1d80efc4aa6" />

1.4 Estatísticas Descritivas

A análise descritiva foi aplicada ao dataset com o objetivo de resumir, organizar e compreender as principais características dos dados antes de prosseguir para análises mais complexas. Essa etapa é fundamental para verificar distribuições, dispersão, valores atípicos e proporção das classes.

Principais medidas utilizadas:

count: número de valores válidos (não nulos).

mean: média aritmética dos valores.

std: desvio-padrão, que expressa a variabilidade.

min: menor valor observado.

25% (Q1): primeiro quartil (25% dos dados estão abaixo desse valor).

50% (Mediana/Q2): valor central da distribuição.

75% (Q3): terceiro quartil (75% dos dados estão abaixo desse valor).

max: maior valor observado.

O método df_dataset.describe() foi utilizado para gerar essas estatísticas de forma automatizada para todas as variáveis numéricas do dataset.

O dataset contém 27.901 registros, dos quais 58,55% apresentam sintomas de depressão, enquanto 41,45% não apresentam. Essa diferença indica um leve desbalanceamento das classes, aspecto relevante para as etapas posteriores de modelagem e aprendizado de máquina.

<img width="779" height="586" alt="image" src="https://github.com/user-attachments/assets/2026c4ce-201e-41a8-ae92-b86c3ae2565e" />

<img width="965" height="597" alt="image" src="https://github.com/user-attachments/assets/a0a336ca-a99a-495e-ad10-22e6721ff818" />



## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.


