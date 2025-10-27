# Preparação dos dados

Pré-processamento e Tratamento de Dados

O pré-processamento do dataset student_depression foi conduzido com o objetivo de garantir a qualidade, integridade e consistência dos dados, preparando-os para análise exploratória e modelagem preditiva. As etapas realizadas foram:


1. Limpeza de Dados

Tratamento de Valores Ausentes: 	Inicialmente, linhas que continham o valor de preenchimento ('?') na coluna Financial Stress foram removidas do dataset. Em uma verificação posterior com isnull().sum(), confirmou-se a ausência de valores faltantes residuais, dispensando a necessidade de imputação.

2. Remoção de Duplicatas: 	O dataset foi inspecionado com duplicated(). Nenhuma linha duplicada foi identificada e, portanto, nenhuma remoção foi necessária.

3. Tratamento de Outliers: 	Os outliers foram identificados visualmente por meio de boxplots das variáveis numéricas. Contudo, não houve remoção ou transformação de outliers nesta fase, a fim de preservar a distribuição original dos dados.


2. Transformação de Dados

Padronização de variáveis textuais: A coluna Sleep Duration foi padronizada, removendo caracteres desnecessários (hours) e substituindo prefixos textuais (Less than → <, More than → >).

Codificação de variáveis categóricas:

- ender: Male → 1, Female → 0

 - Dietary Habits: Healthy=3, Moderate=2, Unhealthy=1

 - Variáveis binárias (Yes/No) → 1/0

Conversão de Sleep Duration em valores numéricos aproximados.


3. Feature Engineering

3.1 Variáveis selecionadas como features:

- Age, Academic Pressure, Study Satisfaction, Sleep Duration, Dietary Habits, Have you ever had suicidal thoughts?, Work/Study Hours, Financial Stress, Family History of Mental Illness.

- Variável alvo: Depression.

- # Preparação dos dados

Pré-processamento e Tratamento de Dados

O pré-processamento do dataset student_depression foi conduzido com o objetivo de garantir a qualidade, integridade e consistência dos dados, preparando-os para análise exploratória e modelagem preditiva. As etapas realizadas foram:


1. Limpeza de Dados

Tratamento de Valores Ausentes: 	Inicialmente, linhas que continham o valor de preenchimento ('?') na coluna Financial Stress foram removidas do dataset. Em uma verificação posterior com isnull().sum(), confirmou-se a ausência de valores faltantes residuais, dispensando a necessidade de imputação.

2. Remoção de Duplicatas: 	O dataset foi inspecionado com duplicated(). Nenhuma linha duplicada foi identificada e, portanto, nenhuma remoção foi necessária.

3. Tratamento de Outliers: 	Os outliers foram identificados visualmente por meio de boxplots das variáveis numéricas. Contudo, não houve remoção ou transformação de outliers nesta fase, a fim de preservar a distribuição original dos dados.


2. Transformação de Dados

Padronização de variáveis textuais: A coluna Sleep Duration foi padronizada, removendo caracteres desnecessários (hours) e substituindo prefixos textuais (Less than → <, More than → >).

Codificação de variáveis categóricas:

- ender: Male → 1, Female → 0

 - Dietary Habits: Healthy=3, Moderate=2, Unhealthy=1

 - Variáveis binárias (Yes/No) → 1/0

Conversão de Sleep Duration em valores numéricos aproximados.


3. Feature Engineering

Variáveis selecionadas como features:

Age, Academic Pressure, Study Satisfaction, Sleep Duration, Dietary Habits, Have you ever had suicidal thoughts?, Work/Study Hours, Financial Stress, Family History of Mental Illness.

Variável alvo: Depression.

3.2 Análise de Relevância de Features

- Cálculo de Mutual Information para verificar importância de cada feature em relação à classe alvo. O ojetivo é garantir que os dados estejam limpos, consistentes e adequados para modelagem, além de priorizar variáveis mais relevantes.

![Imagem do WhatsApp de 2025-10-26 à(s) 20 45 56_83f96c5f](https://github.com/user-attachments/assets/2d9855e2-e472-4991-99aa-c3cd306bf78c)

![Imagem do WhatsApp de 2025-10-26 à(s) 20 46 48_af607313](https://github.com/user-attachments/assets/75b9eec6-8489-4de1-9c97-7b86994c5d8c)

![Imagem do WhatsApp de 2025-10-26 à(s) 20 47 33_80507d50](https://github.com/user-attachments/assets/596ef468-dcf9-4421-88d3-18192e3ddcfa)



4. Tratamento de dados desbalanceados

A variável alvo Depression apresentou desbalanceamento (~58% com depressão, ~42% sem depressão).

Técnicas como SMOTE serão aplicadas posteriormente na fase de modelagem para balancear as classes.

5. Separação de dados

Quatro modelos de Machine Learning foram testados para classificar a variável alvo (Depression): Regressão Logística, Random Forest, XGBoost e LightGBM. O desempenho de cada um foi avaliado usando métricas-chave: Accuracy (Acurácia), F1 Score e AUC (Area Under the Curve).

![Imagem do WhatsApp de 2025-10-26 à(s) 20 22 54_d4c2526b](https://github.com/user-attachments/assets/f1676098-ff2a-4cfb-8da7-5d5823bc3c79)

O gráfico demonstra que todos os modelos alcançaram um desempenho global alto e consistente, com as métricas Accuracy e F1 Score variando de aproximadamente $0.82$ a $0.86$, e o AUC sendo a métrica de maior valor, consistentemente acima de $0.85$ para todos os classificadores.

![Imagem do WhatsApp de 2025-10-26 à(s) 20 27 36_a7f51eb3](https://github.com/user-attachments/assets/1d0615a2-cc9f-465a-8be0-f0ea97d620a9)

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
