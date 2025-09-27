# Conhecendo os dados
Nesta seção, realizamos uma análise descritiva e exploratória detalhada da base de dados selecionada. O objetivo é compreender a estrutura dos dados, identificar outliers e avaliar possíveis relações entre as variáveis.

Foram utilizados cálculos de medidas de tendência central (média, mediana, moda), medidas de dispersão (desvio padrão e intervalos interquartis), além de gráficos descritivos (histogramas, boxplots e mapas de calor) para compreender melhor o comportamento dos dados.

1. Importação das Bibliotecas

Foram carregadas as bibliotecas necessárias para manipulação dos dados, visualização gráfica e, futuramente, aplicação de algoritmos de machine learning. As bibliotecas escolhidas permitem: manipular  tratar dados (pandas, numpy), gerar visualizações (matplotlib, seaborn) e preparar a base para modelos de machine learning (sklearn, shap).


<img width="563" height="180" alt="image" src="https://github.com/user-attachments/assets/9a6a1e02-fdfb-410b-973b-2cdbc9712a03" />



2. Coleta  de Dados e criação do dataframe
O dataset foi obtido diretamente do KaggleHub, utilizando o recurso de cache do Google Colab para acesso mais rápido.

<img width="811" height="403" alt="image" src="https://github.com/user-attachments/assets/6ab53a4f-1436-49df-b523-1a0fa0550063" />

Em seguida, os dados foram carregados em um DataFrame pandas:

<img width="577" height="47" alt="image" src="https://github.com/user-attachments/assets/b575d89d-4440-4043-89ea-f75682cae521" />


3. Estrutura dos Dados

A verificação inicial do tipo de cada variável mostrou que o dataset contém tanto variáveis numéricas (idade, notas, pressão acadêmica, etc.) quanto categóricas (gênero, cidade, hábitos alimentares, histórico familiar)


<img width="523" height="473" alt="image" src="https://github.com/user-attachments/assets/dea6034d-6e52-47bd-966c-d1d80efc4aa6" />

3.  Estatísticas Descritivas

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





## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.


