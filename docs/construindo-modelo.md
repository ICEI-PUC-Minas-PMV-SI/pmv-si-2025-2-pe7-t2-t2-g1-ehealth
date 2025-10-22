# Preparação dos dados

Nesta etapa, todos os dados foram cuidadosamente preparados para garantir a qualidade e eficácia da modelagem preditiva. As técnicas aplicadas incluíram:

1. Limpeza de Dados

Valores ausentes: o dataset foi analisado quanto a valores nulos (df.isnull().sum()). Não foram encontrados dados faltantes, dispensando imputação.

Outliers: foram avaliados outliers em variáveis numéricas usando boxplots. Casos extremos foram considerados para normalização, mas não removidos, preservando a variabilidade real do conjunto de dados.

Duplicatas: verificadas com df.duplicated() e eliminadas quando presentes.

2. Transformação de Dados

Normalização e padronização: variáveis numéricas (como Age, Academic Pressure, CGPA, Study Satisfaction) foram padronizadas com StandardScaler para garantir comparabilidade e estabilidade do modelo.

Codificação de variáveis categóricas: colunas como Gender, City, Degree, Family History of Mental Illness e Have you ever had suicidal thoughts ? foram convertidas para formato numérico usando One-Hot Encoding ou técnicas de codificação apropriadas.

3. Engenharia de Features

Criação de novas variáveis: faixas de horas de sono foram categorizadas; outras features derivadas foram avaliadas conforme relevância para o modelo.

Seleção de características: análise de correlação e importância de features permitiu reduzir variáveis redundantes ou pouco informativas.

4. Tratamento de Desbalanceamento

O target Depression apresentava desbalanceamento (58,5% casos com depressão vs. 41,5% sem depressão). Considerou-se:

Oversampling para aumentar a representação da classe minoritária;

Uso de algoritmos robustos a desbalanceamento, como SVM com ajuste de peso por classe.

5. Separação de Dados

Treino, validação e teste: divisão do conjunto em 80% treino e 20% teste, garantindo estratificação por classe para manter proporções originais de depressão.

Random state definido para reprodutibilidade.

6. Redução de Dimensionalidade (opcional)

Para cenários com muitas features numéricas, técnicas como PCA podem ser aplicadas para reduzir dimensionalidade sem perda significativa de informação.

7. Validação Cruzada

Utilizada para avaliar a robustez do modelo, evitando overfitting e garantindo generalização.

8. Monitoramento Contínuo

O pré-processamento foi estruturado em pipeline replicável, permitindo atualizações futuras caso novos dados ou alterações no problema sejam introduzidos.

 
 A preparação dos dados incluiu limpeza, transformação, engenharia de features, tratamento de desbalanceamento e separação em conjuntos de treino e teste, garantindo um pipeline robusto e reprodutível para a modelagem de aprendizado de máquina.

# Descrição do modelo

Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever o algoritmo de aprendizado de máquina selecionado para a construção do primeiro modelo proposto. Inclua informações abrangentes sobre o algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha do algoritmo.

Explore aspectos específicos, como o ajuste dos parâmetros livres. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas e registrar todos os experimentos realizados.

# Avaliação do modelo criado

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar o modelo desenvolvido deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelo modelo construído, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade dele. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecer relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 

## Observações importantes

Todas as tarefas realizadas nesta etapa deverão ser registradas em formato de texto junto com suas explicações de forma a apresentar os códigos desenvolvidos e também, o código deverá ser incluído, na íntegra, na pasta "src".
