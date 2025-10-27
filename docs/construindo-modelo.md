# Testando modelos

Antes realizamos um breve teste para ver qual modelo teria um melhor desempenho.

Testamos os modelos

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

```python3
# 1. Carregar o dataset
#df = pd.read_csv("student_depression.csv")

import kagglehub

path = kagglehub.dataset_download("adilshamim8/student-depression-dataset")

print("Path to dataset files:", path)

dataset_name = os.listdir(path)[0]

df = pd.read_csv(os.path.join(path, dataset_name))
```
```python3
# 2. Pré-processamento
# Remover colunas irrelevantes se houver (ex: IDs)
# Mapear "Sleep Duration" de texto para número
sleep_map = {
    "'Less than 5 hours'": 4,
    "'5-6 hours'": 5.5,
    "'7-8 hours'": 7.5,
    "'More than 8 hours'": 9
}
if 'Sleep Duration' in df.columns:
    df['Sleep Duration'] = df['Sleep Duration'].map(sleep_map)


# Tratar valores ausentes
df = df.dropna()

# Codificar variáveis categóricas
categorical = df.select_dtypes(include='object').columns
le = LabelEncoder()
for col in categorical:
    df[col] = le.fit_transform(df[col])

```

![Imagem do WhatsApp de 2025-10-26 à(s) 20 27 36_a7f51eb3](https://github.com/user-attachments/assets/1d0615a2-cc9f-465a-8be0-f0ea97d620a9)

![Imagem do WhatsApp de 2025-10-26 à(s) 20 22 54_d4c2526b](https://github.com/user-attachments/assets/f1676098-ff2a-4cfb-8da7-5d5823bc3c79)

Apos algumas variações no teste escolhemos utilizar o Random Forest

# Preparação dos dados

Pré-processamento e Tratamento de Dados

O pré-processamento do dataset student_depression foi conduzido com o objetivo de garantir a qualidade, integridade e consistência dos dados, preparando-os para análise exploratória e modelagem preditiva. Antes das etapas de limpeza e transformação, foi realizado um teste inicial do modelo (baseline), com o propósito de estabelecer uma referência de desempenho, avaliar rapidamente padrões nos dados e identificar possíveis ajustes necessários no pré-processamento.


1. Limpeza de Dados

Tratamento de Valores Ausentes: 	Inicialmente, linhas que continham o valor de preenchimento ('?') na coluna Financial Stress foram removidas do dataset. Em uma verificação posterior com isnull().sum(), confirmou-se a ausência de valores faltantes residuais, dispensando a necessidade de imputação.

2. Remoção de Duplicatas: 	O dataset foi inspecionado com duplicated(). Nenhuma linha duplicada foi identificada e, portanto, nenhuma remoção foi necessária.

3. Tratamento de Outliers: 	Os outliers foram identificados visualmente por meio de boxplots das variáveis numéricas. Contudo, não houve remoção ou transformação de outliers nesta fase, a fim de preservar a distribuição original dos dados.


2. Transformação de Dados

Padronização de variáveis textuais: A coluna Sleep Duration foi padronizada, removendo caracteres desnecessários (hours) e substituindo prefixos textuais (Less than → <, More than → >).

Codificação de variáveis categóricas:

- Gender: Male → 1, Female → 0

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

O gráfico demonstra que todos os modelos alcançaram um desempenho global alto e consistente, com as métricas Accuracy e F1 Score variando de aproximadamente $0.82$ a $0.86$, e o AUC sendo a métrica de maior valor, consistentemente acima de $0.85$ para todos os classificadores.


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

O modelo de Machine Learning construído para classificar a presença de depressão (Depression) foi avaliado utilizando um conjunto abrangente de métricas, cobrindo aspectos de desempenho global, balanceamento de classes e qualidade das probabilidades.

As principais métricas utilizadas e sua justificativa em um problema de classificação binária (Depressão = 1, Sem Depressão = 0) com classes moderadamente desbalanceadas são:

1. Métricas Baseadas em Desempenho (Threshold-Dependent)
   
1.1 Acurácia (Accuracy) : Proporção de previsões corretas (verdadeiros positivos + verdadeiros negativos) sobre o total de observações. Fornece uma visão rápida do desempenho geral. É útil, mas insuficiente sozinha, dada a distribuição das classes (58% vs. 42%).

1.2  Precisão (Precision): De todas as vezes que o modelo previu a classe positiva (Depressão), quantas vezes ele acertou (Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Positivos)).Importante para avaliar o custo de um Falso Positivo (dizer que há depressão quando não há). Garante que o modelo não está apenas superestimando a classe positiva.

1.3  Recall (Sensibilidade) : De todos os casos positivos reais (Depressão), quantos o modelo identificou corretamente (Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Negativos)). Crucial em problemas de saúde. Avalia o custo de um Falso Negativo (não detectar a depressão em um caso real). Um recall alto na classe 1 é vital.

1.4  Acurácia Balanceada (Balanced Accuracy): Essencial para avaliar se o modelo está performando bem em ambas as classes. Corrige o viés que a Acurácia simples teria em um dataset desbalanceado.

## Discussão dos resultados obtidos

Os modelos Random Forest e LightGBM apresentaram alto poder preditivo, com Acurácia e F1-Score superiores a 0,84 e AUC acima de 0,85. Esse desempenho demonstra a capacidade dos modelos em identificar padrões significativos no dataset, alinhando-se aos objetivos de detectar estudantes com risco de depressão.

1. Relação com o Problema e Objetivos

Alcance da meta: O elevado F1-Score e AUC indicam que o modelo distingue eficazmente alunos com e sem depressão.

Aplicação prática: Um F1-Score de 0,84 sugere que o modelo pode ser utilizado como ferramenta de triagem inicial, identificando rapidamente alunos que necessitam de avaliação profissional.

2. Métricas e Impacto do Desbalanceamento

O dataset apresenta desbalanceamento moderado (58% positivos), tornando métricas como F1-Score e Balanced Accuracy mais relevantes que Acurácia simples.

Recall elevado (~0,86 no Random Forest): Minimiza falsos negativos, crucial para problemas de saúde.

F1-Score Macro: Confirma bom equilíbrio entre Precisão e Recall, evitando viés para a classe majoritária.

3. Insights das Variáveis Relevantes

“Have you ever had suicidal thoughts?”: variável mais informativa, essencial para alta performance e priorização de risco.

“Academic Pressure” e “Financial Stress”: destacam fatores externos associados à depressão em estudantes, reforçando a validade prática do modelo.

4. Avaliação da Calibração

Log Loss e Brier Score: utilizados para verificar a confiabilidade das probabilidades previstas.

Probabilidades bem calibradas permitem priorizar intervenções, por exemplo, atribuindo alta prioridade a alunos com probabilidade prevista ≥90%.

Conclusão: Os resultados indicam que os modelos são consistentes, robustos e diretamente aplicáveis para identificar fatores de risco de depressão em estudantes, oferecendo suporte confiável para intervenções em ambientes educacionais.

# Pipeline de pesquisa e análise de dados

Com base em todas as etapas de coleta, pré-processamento, análise e modelagem descritas, o Pipeline de Pesquisa e Análise de Dados do projeto pode ser estruturado e resumido da seguinte forma:


<img width="1172" height="697" alt="image" src="https://github.com/user-attachments/assets/67ac5898-64c4-484d-8ef5-21d1ad57af18" />



## Métricas utilizadas

O modelo de Machine Learning construído para classificar a presença de depressão (Depression) foi avaliado utilizando um conjunto abrangente de métricas, cobrindo aspectos de desempenho global, balanceamento de classes e qualidade das probabilidades.

As principais métricas utilizadas e sua justificativa em um problema de classificação binária (Depressão = 1, Sem Depressão = 0) com classes moderadamente desbalanceadas são:

1. Métricas Baseadas em Desempenho (Threshold-Dependent)
   
1.1 Acurácia (Accuracy) : Proporção de previsões corretas (verdadeiros positivos + verdadeiros negativos) sobre o total de observações. Fornece uma visão rápida do desempenho geral. É útil, mas insuficiente sozinha, dada a distribuição das classes (58% vs. 42%).

1.2  Precisão (Precision): De todas as vezes que o modelo previu a classe positiva (Depressão), quantas vezes ele acertou (Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Positivos)).Importante para avaliar o custo de um Falso Positivo (dizer que há depressão quando não há). Garante que o modelo não está apenas superestimando a classe positiva.

1.3  Recall (Sensibilidade) : De todos os casos positivos reais (Depressão), quantos o modelo identificou corretamente (Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Negativos)). Crucial em problemas de saúde. Avalia o custo de um Falso Negativo (não detectar a depressão em um caso real). Um recall alto na classe 1 é vital.

1.4  Acurácia Balanceada (Balanced Accuracy): Essencial para avaliar se o modelo está performando bem em ambas as classes. Corrige o viés que a Acurácia simples teria em um dataset desbalanceado.

## Discussão dos resultados obtidos

Os modelos Random Forest e LightGBM apresentaram alto poder preditivo, com Acurácia e F1-Score superiores a 0,84 e AUC acima de 0,85. Esse desempenho demonstra a capacidade dos modelos em identificar padrões significativos no dataset, alinhando-se aos objetivos de detectar estudantes com risco de depressão.


1. Relação com o Problema e Objetivos

Alcance da meta: O elevado F1-Score e AUC indicam que o modelo distingue eficazmente alunos com e sem depressão.

Aplicação prática: Um F1-Score de 0,84 sugere que o modelo pode ser utilizado como ferramenta de triagem inicial, identificando rapidamente alunos que necessitam de avaliação profissional.

2. Métricas e Impacto do Desbalanceamento

O dataset apresenta desbalanceamento moderado (58% positivos), tornando métricas como F1-Score e Balanced Accuracy mais relevantes que Acurácia simples.

Recall elevado (~0,86 no Random Forest): Minimiza falsos negativos, crucial para problemas de saúde.

F1-Score Macro: Confirma bom equilíbrio entre Precisão e Recall, evitando viés para a classe majoritária.




