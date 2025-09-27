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

4. Estatística Descritiva

A estatistica descritiva foi aplicada ao dataset com o objetivo de resumir, organizar e compreender as principais características dos dados antes de prosseguir para análises mais complexas. Essa etapa é fundamental para verificar distribuições, dispersão, valores atípicos e proporção das classes.A
count → número de valores não nulos. Foram aplicadas as seguintes medidas: 

mean → média aritmética dos valores

std → desvio padrão, quee expressa a variabilidade.

min / max → valores mínimo e máximo observados.

25%, 50%, 75% → quartis, que permitem identificar a mediana e intervalos interquartis.


O método df_dataset.describe() foi utilizado para gerar essas estatísticas de forma automatizada para todas as variáveis numéricas do dataset.

O dataset contém 27.901 registros, dos quais 58,55% apresentam sintomas de depressão, enquanto 41,45% não apresentam. Essa diferença indica um leve desbalanceamento das classes, aspecto relevante para as etapas posteriores de modelagem e aprendizado de máquina.


<img width="1375" height="440" alt="image" src="https://github.com/user-attachments/assets/7b5d608b-c120-467f-b4c3-f887fc73f2ef" />


Distribuição da Variável-Alvo (Depression)

A variável Depression indica a presença (1) ou ausência (0) de sintomas depressivos.

<img width="632" height="80" alt="image" src="https://github.com/user-attachments/assets/dd33b113-448c-4650-aa6b-4ff6e7d609d9" />

 Tabela de Frequências: 
 
<img width="368" height="83" alt="image" src="https://github.com/user-attachments/assets/ce80e2a9-8135-4a9e-a746-9947ae503357" />

Foi gerado um gráfico de barras para ilustrar a distribuição:


<img width="914" height="573" alt="image" src="https://github.com/user-attachments/assets/b2f1a922-b48b-4800-a4a3-ef0a13b6184d" />


Resultado:

58,55% dos registros apresentam sintomas de depressão.

41,45% dos registros não apresentam sintomas.

Total de registros: 27.901.

ENGENHARIA DE DADOS

Nesta etapa, foram realizados procedimentos de limpeza, padronização e preparação dos dados para análises mais aprofundadas.

1. Eliminação de Valores Nulos

<img width="446" height="700" alt="image" src="https://github.com/user-attachments/assets/1db24df3-c97b-4ad1-b56f-61512b3eb39e" />

Não há dados nulos. 

2. Remoção de Duplicatas

Foi verificado que não há registros duplicados.


3. Padronização de Colunas

Exemplo: a coluna Sleep Duration apresentava valores com descrições textuais como "Less than 5 hours" e "More than 8 hours".

Foram aplicadas transformações para substituir "Less than" por "<" e "More than" por ">".

Também foi retirado o sufixo "hours".


| Sleep Duration Raw | Sleep Duration |
| ------------------ | -------------- |
| Less than 5 hours  | <5             |
| 5 - 6 hours        | 5 - 6          |
| 6 - 7 hours        | 6 - 7          |
| More than 8 hours  | >8             |
| 7 - 8 hours        | 7 - 8          |


| Sleep Duration Raw | Sleep Duration |
| ------------------ | -------------- |
| 6 - 7 hours        | 6 - 7          |
| More than 8 hours  | >8             |
| Less than 5 hours  | <5             |
| 7 - 8 hours        | 7 - 8          |
| 5 - 6 hours        | 5 - 6          |


4. Análises Gráficas Iniciais

Distribuição por tipo de graduação (Degree):

<img width="824" height="605" alt="image" src="https://github.com/user-attachments/assets/0cdc930d-0da9-4cee-aec9-444516f43bb3" />


Histogramas de variáveis numéricas:

<img width="960" height="486" alt="image" src="https://github.com/user-attachments/assets/43b2d6d7-1bb6-4894-9788-a78502699a8e" />


<img width="897" height="514" alt="image" src="https://github.com/user-attachments/assets/e0f59121-1b13-40e4-b0db-bb18fb38bc8e" />



Boxplots segmentados por Depressão (0/1):


<img width="1059" height="587" alt="image" src="https://github.com/user-attachments/assets/e9be0ad1-0ce9-4a1b-a77f-d7b4e037b28c" />


<img width="1059" height="584" alt="image" src="https://github.com/user-attachments/assets/fbff18b6-5f0b-4be3-813c-98bd922ca417" />

Countplots de variáveis categóricas (com vs. sem depressão):


<img width="1065" height="610" alt="image" src="https://github.com/user-attachments/assets/3af3d372-7dd1-4963-a1a1-04fd5170a392" />

Após os processos de estatística descritiva, limpeza e engenharia de dados, a base está consistente, sem valores nulos ou duplicados, com variáveis padronizadas e pronta para análises mais avançadas e modelagem preditiva.


## Descrição dos achados

A análise descritiva e exploratória da base de dados trouxe informações importantes para compreender o perfil dos estudantes e os fatores associados à presença de sintomas depressivos.

1. Distribuição da variável-alvo (Depression)

Observou-se um desequilíbrio de classes: aproximadamente 58,6% dos estudantes apresentam sintomas de depressão, contra 41,4% sem depressão.

Esse desbalanceamento deve ser considerado nas próximas etapas de modelagem, pois pode impactar o desempenho de classificadores.

2. Medidas de tendência central e dispersão

Em variáveis contínuas, como idade, notas acadêmicas e duração do sono, verificou-se que a média e a mediana estavam próximas, sugerindo distribuições relativamente simétricas.

Entretanto, alguns atributos apresentaram amplitude elevada entre o mínimo e o máximo, indicando a presença de outliers.

Em especial, a variável Sleep Duration mostrou concentrações nas faixas intermediárias (6–8 horas), mas também casos extremos (<5h ou >8h), que podem estar relacionados a padrões de saúde ou estilo de vida.

3. Análise gráfica (histogramas e boxplots)

Boxplots mostraram diferenças entre grupos com e sem depressão, especialmente em variáveis relacionadas a pressão acadêmica, qualidade do sono e hábitos alimentares.

Em histogramas, algumas distribuições exibiram assimetria, reforçando a necessidade de padronização ou transformação para análises estatísticas mais robustas.

4. Relações entre variáveis (correlações)

A matriz de correlação de Pearson revelou, de modo geral, correlações fracas a moderadas entre os atributos. Destacaram-se:


 - Correlação moderada negativa entre qualidade do sono e nível de depressão: menor qualidade do sono associou-se a maiores índices de depressão.

- Correlação moderada positiva entre pressão acadêmica e nível de depressão: estudantes com maior percepção de sobrecarga acadêmica tendem a relatar mais sintomas depressivos.

- Outras variáveis, como hábitos alimentares e histórico familiar, apresentaram correlações fracas, mas consistentes, sugerindo contribuição secundária ao risco de depressão.

5. Aspectos gerais

O dataset apresentou boa qualidade: sem valores nulos ou duplicados, e com variáveis categóricas padronizadas. Apesar disso, a distribuição desigual da variável-alvo e a presença de alguns outliers demandam atenção em etapas futuras (balanceamento de classes, normalização e tratamento de valores extremos).


## Ferramentas utilizadas

A análise dos dados foi conduzida utilizando principalmente a linguagem de programação Python, escolhida por sua ampla adoção em ciência de dados, robustez e grande ecossistema de bibliotecas. As principais ferramentas e tecnologias empregadas foram:

🔹 Linguagem de Programação

Python: linguagem de código aberto, versátil e com bibliotecas especializadas para manipulação de dados, análise estatística e aprendizado de máquina.

🔹 Bibliotecas de Manipulação e Análise de Dados

pandas: utilizada para leitura dos arquivos, estruturação dos dados em DataFrames, limpeza, filtragem, cálculos estatísticos e agregações.

numpy: empregada para operações matemáticas e manipulação de arrays, auxiliando na vetorização e no desempenho computacional.

🔹 Visualização Gráfica

matplotlib: responsável pela geração de gráficos básicos (histogramas, boxplots, gráficos de dispersão, barras, entre outros).

seaborn: utilizada para visualizações estatísticas mais elaboradas, como mapas de calor (heatmaps), pairplots e gráficos estilizados com maior clareza interpretativa.

🔹 Modelagem e Pré-processamento

scikit-learn (sklearn): empregada na divisão dos dados em treino e teste, na normalização, no balanceamento de classes e na implementação de algoritmos de classificação e predição.

🔹 Interpretação de Modelos

shap (SHapley Additive exPlanations): biblioteca utilizada para explicar as predições dos modelos de aprendizado de máquina, atribuindo pesos de importância às variáveis.

🔹 Ambiente de Desenvolvimento

Google Colab: plataforma em nuvem utilizada para a execução dos notebooks Python, por oferecer praticidade, acesso a recursos de GPU e integração com bibliotecas como o KaggleHub, que foi utilizado para importar diretamente o dataset.


