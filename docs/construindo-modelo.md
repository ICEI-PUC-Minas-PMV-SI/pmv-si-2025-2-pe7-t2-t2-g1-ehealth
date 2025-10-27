# Preparação dos dados

Pré-processamento e Tratamento de Dados

O pré-processamento do dataset student_depression foi conduzido com o objetivo de garantir a qualidade, integridade e consistência dos dados, preparando-os para análise exploratória e modelagem preditiva. As etapas realizadas foram:
Pré-processamento e Tratamento de DadosO pré-processamento do dataset foi realizado para garantir a qualidade, consistência e adequação dos dados à análise exploratória e à modelagem preditiva. As etapas concluídas até o momento são detalhadas abaixo:

1. Limpeza de Dados

Tratamento de Valores Ausentes: 	Inicialmente, linhas que continham o valor de preenchimento ('?') na coluna Financial Stress foram removidas do dataset. Em uma verificação posterior com isnull().sum(), confirmou-se a ausência de valores faltantes residuais, dispensando a necessidade de imputação.

2. Remoção de Duplicatas: 	O dataset foi inspecionado com duplicated(). Nenhuma linha duplicada foi identificada e, portanto, nenhuma remoção foi necessária.

3. Tratamento de Outliers: 	Os outliers foram identificados visualmente por meio de boxplots das variáveis numéricas. Contudo, não houve remoção ou transformação de outliers nesta fase, a fim de preservar a distribuição original dos dados.


2. Transformação de Dados

Padronização de variáveis textuais: A coluna Sleep Duration foi padronizada, removendo caracteres desnecessários (hours) e substituindo prefixos textuais (Less than → <, More than → >).

Codificação de variáveis categóricas: Na fase de preparação para a modelagem, as variáveis categóricas foram convertidas para o formato numérico:Dietary Habits: Mapeada de forma ordinal (ex: 'Healthy' $\rightarrow 3$, 'Moderate' $\rightarrow 2$, 'Unhealthy' $\rightarrow 1$, 'Others' $\rightarrow 0$).Gender: Mapeada de forma binária ('Male' $\rightarrow 1$, 'Female' $\rightarrow 0$).Have you ever had suicidal thoughts ? e Family History of Mental Illness: Mapeadas de forma binária ('Yes' $\rightarrow 1$, 'No' $\rightarrow 0$).

Normalização/padronização numérica: Não aplicada nesta fase.

3. Feature Engineering

Nenhuma nova feature foi criada neste estágio.

Foi realizada seleção inicial de variáveis para análise exploratória, distinguindo variáveis numéricas (Age, Academic Pressure, CGPA, etc.) e categóricas (Gender, City, Dietary Habits, etc.).

4. Tratamento de dados desbalanceados

A variável alvo Depression apresentou desbalanceamento (~58% com depressão, ~42% sem depressão).

Nenhuma técnica de oversampling, undersampling ou ajuste de peso foi aplicada nesta fase; a identificação do desbalanceamento serve para decisões futuras na modelagem.

5. Separação de dados

Até esta etapa, os dados ainda não foram divididos em conjuntos de treino, validação e teste.

6. Manuseio de Dados Temporais

Não aplicável ao dataset atual, pois não há variáveis temporais.

7. Redução de Dimensionalidade

Não foi realizada, pois a dimensionalidade do dataset não apresenta alta complexidade.

8. Validação Cruzada

Ainda não aplicada nesta etapa de pré-processamento; será implementada na fase de modelagem para avaliar a robustez do modelo e evitar overfitting.

9. Monitoramento Contínuo

Não aplicável neste estágio, mas recomenda-se atualização do pré-processamento caso novas versões do dataset sejam utilizadas ou alterações no contexto do problema ocorram.


# Descrição do modelo

O algoritmo selecionado para classificação binária da variável Depression foi o Support Vector Classifier (SVC), baseado em Support Vector Machines. O SVC busca encontrar o hiperplano ótimo que separa as classes com máxima margem, utilizando vetores de suporte. Para dados não linearmente separáveis, o algoritmo aplica o kernel trick, projetando as features em espaços de maior dimensão.

As principais vantagens do SVC incluem capacidade de lidar com alta dimensionalidade, modelagem de fronteiras complexas e robustez frente a pequenos outliers. Suas limitações envolvem sensibilidade à escolha de kernel e parâmetros (C, gamma) e maior custo computacional em grandes volumes de dados.

No contexto deste projeto, o SVC foi selecionado devido à sua adequação a problemas de classificação binária, à presença de variáveis numéricas e categóricas e à necessidade de capturar relações possivelmente não lineares. A configuração padrão do modelo (kernel='rbf', C=1.0, gamma='scale') foi utilizada para treino inicial, sendo planejada a exploração de hiperparâmetros em etapas subsequentes para otimização da performance.

# Avaliação do modelo criado

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar o modelo desenvolvido deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelo modelo construído, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade dele. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecer relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 

## Observações importantes

Todas as tarefas realizadas nesta etapa deverão ser registradas em formato de texto junto com suas explicações de forma a apresentar os códigos desenvolvidos e também, o código deverá ser incluído, na íntegra, na pasta "src".
