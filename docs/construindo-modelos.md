 # Etapa 4 — Construção de Modelos  (parte 2)

A quarta etapa do projeto consistiu na implementação e avaliação de novos algoritmos de aprendizado de máquina, visando melhorar a capacidade preditiva em relação à Etapa 3 e promover a generalização do pipeline de análise.

## 1. Ajustes e Pré-Processamento de Dados 

Não foram necessários ajustes adicionais significativos ou novo pré-processamento dos dados em função da implementação dos novos algoritmos. Os modelos escolhidos, nomeadamente LGBMClassifier e RandomForestClassifier, são algoritmos de ensemble baseados em árvores de decisão. Esses modelos são robustos a diferentes distribuições de dados, não requerem normalização ou padronização de features e lidam bem com dados categóricos (One-Hot Encoding) e desbalanceamento, conforme já tratado na etapa de pré-processamento.

•	Diferença em Relação à Etapa Anterior: O pré-processamento se manteve, utilizando codificação One-Hot para variáveis nominais e mantendo a escala original das variáveis numéricas, o que foi adequado para a natureza dos novos modelos.

## 2. Implementação e Justificativa dos Algoritmos 

Foram implementados dois novos algoritmos de aprendizado de máquina: o Light Gradient Boosting Machine (LGBMClassifier) e o Random Forest (RandomForestClassifier).

a. Light Gradient Boosting Machine (LGBMClassifier)

- Implementação: O modelo LGBMClassifier foi instanciado, treinado e avaliado. 


<img width="886" height="248" alt="image" src="https://github.com/user-attachments/assets/af7b5bd2-e6d5-4b9b-81cc-766ccb27667f" />

 
- Justificativa da Escolha:

- 	Performance e Velocidade: LGBM é um algoritmo de gradient boosting conhecido por sua alta eficiência e velocidade de treinamento, especialmente em grandes conjuntos de dados, devido ao uso de técnicas como o Histogram-based Algorithm.
- 	Precisão: Ferequentemente alcança o estado da arte em problemas tabulares, superando outros algoritmos de boosting como o XGBoost em muitas situações.
-  ratamento de Features: Por ser baseado em árvores, naturalmente lida com a não-linearidade e as interações complexas entre as variáveis, características comuns em dados de saúde mental.


b. Random Forest (RandomForestClassifier)

•	Implementação: O RandomForestClassifier é um modelo de ensemble que utiliza Bagging (Bootstrap Aggregating) de múltiplas árvores de decisão.

•	Justificativa da Escolha:

o	Robustez e Estabilidade: É um modelo extremamente robusto e menos propenso ao overfitting do que uma única árvore de decisão ou modelos de boosting não regularizados, pois a variância é reduzida ao agregar as previsões de diversas árvores treinadas em subconjuntos aleatórios dos dados.
o	Interpretabilidade: Embora menos interpretável que uma única árvore, oferece uma medida de importância de features confiável.
o	Linha de Base Sólida: Serve como um modelo de referência forte e estável para comparação com algoritmos mais complexos (boosting).

## 3. Avaliação de Desempenho dos Modelos
   
O problema em questão é de classificação binária, onde o objetivo é prever a ocorrência de um determinado desfecho (Classe 1) ou sua ausência (Classe 0).

a. Escolha e Justificativa da Métrica Principal

-	Métrica Principal: F1-Score.

- Justificativa: O F1-Score é a média harmônica entre a Precisão (Proporção de positivos corretos dentre todas as previsões positivas) e o Recall (Proporção de positivos corretos dentre todos os positivos reais).

F1 = 2 .Precisão.Recall
             Precisão + Recall  
             
•	A escolha do F1-Score é crucial porque o conjunto de dados pode apresentar algum desbalanceamento (2313 vs. 3267 ).

•	Em um contexto de saúde, é vital que o modelo tenha tanto alta Precisão (para evitar alarmes falsos, prevenindo intervenções desnecessárias) quanto alto Recall (para garantir que a maioria dos casos positivos reais seja identificada, minimizando a negligência de casos). O F1-Score penaliza modelos que performam mal em uma dessas duas métricas, oferecendo um balanço mais realista do desempenho geral do classificador.


b. Desempenho do LGBMClassifier

Os resultados a seguir foram extraídos das imagens fornecidas: 

<img width="613" height="266" alt="image" src="https://github.com/user-attachments/assets/7e09c62f-d726-4b59-9975-3fb4d1b251d5" />



Matriz de Confusão (Dados Brutos) :
 
 <img width="886" height="628" alt="image" src="https://github.com/user-attachments/assets/87695c2d-ddf2-4cad-a6b1-74667a462cbc" />
 

•	Verdadeiros Positivos (VP - Real 1, Previsto 1): 2873
•	Verdadeiros Negativos (VN - Real 0, Previsto 0): 1832
•	Falsos Positivos (FP - Real 0, Previsto 1): 481
•	Falsos Negativos (FN - Real 1, Previsto 0): 394

Calibração:

 <img width="886" height="392" alt="image" src="https://github.com/user-attachments/assets/dec72692-6d16-485e-8398-ce5a8086e3da" />
 

•	A Curva de Calibração (Base ou Classe 1) mostra que o modelo Base (sem calibração adicional) está bem calibrado para a Classe 1, seguindo de perto a linha pontilhada (Perfeita y=x). Isso indica que as probabilidades previstas são confiáveis (e.g., uma previsão de 0.80 corresponde a uma taxa observada de 0.80). A calibração isotônica aprimora ligeiramente a performance.


## 4. Comparação de Desempenho e Análise Crítica 
A comparação se concentra na métrica principal: F1-Score.

A análise crítica será baseada nos resultados fornecidos para o LGBMClassifier e no conhecimento teórico de ambos os modelos no contexto do problema.

<img width="756" height="370" alt="image" src="https://github.com/user-attachments/assets/2631f621-8e4a-4d93-a1d3-367d1ecb8093" />

Análise Crítica:
•	O LGBMClassifier demonstrou um excelente desempenho (F1-Score de 0.865 para a Classe 1), indicando um equilíbrio entre a correta identificação dos casos positivos (Recall = 0.870) e a confiança nessas identificações (Precisão = 0.861).

•	As visualizações de Importância de Features (LGBM e Relevância de Variáveis (Permutation Importance e Mutual Information ) concordam que as variáveis de maior impacto são: CGPA, Idade (Age), Horas de Estudo/Trabalho (Work/Study Hours), Estresse Financeiro, Pressão Acadêmica e Pensamentos Suicidas.

<img width="886" height="385" alt="image" src="https://github.com/user-attachments/assets/7e6e0c23-54b7-4856-893b-5b6b807a7cc4" />

<img width="886" height="649" alt="image" src="https://github.com/user-attachments/assets/8a370d8f-688b-408e-8ce6-dfb83fe85abb" />

<img width="886" height="735" alt="image" src="https://github.com/user-attachments/assets/5abc2779-83a7-4e4d-afd1-a392d709a01b" />



•	Teoricamente, o Random Forest seria crucial para confirmar a robustez do desempenho do LGBM e como uma opção de deployment mais segura em cenários de alta sensibilidade ao overfitting. A alta performance do LGBM, no entanto, sugere que as interações complexas entre as features foram capturadas de maneira eficaz pelo gradient boosting.

## 5. Refinamento e Generalização do Pipeline 

O pipeline de pesquisa e análise de dados foi refinado para se tornar modular e reutilizável, seguindo os princípios de boas práticas de machine learning.

a. Estrutura Modular
1.	Módulo de Pré-Processamento (preprocessing.py):
o	Contém a função para tratamento de valores faltantes, codificação One-Hot e engenharia de features.
o	Benefício: Isola as transformações de dados, garantindo que o mesmo tratamento seja aplicado consistentemente aos dados de treino, teste e novos dados.


2.	Módulo de Modelagem (modeling.py):
o	Contém as classes ou funções para instanciar diferentes modelos (LGBMClassifier, RandomForestClassifier etc.), treiná-los e realizar ajuste de hiperparâmetros (como GridSearchCV mencionado na imagem a seguir): 
 
o	Benefício: Permite a rápida substituição e comparação de algoritmos.
3.	Módulo de Avaliação (evaluation.py):
o	Contém funções padronizadas para cálculo de métricas (Precisão, Recall, F1-Score, etc.), geração de Matriz de Confusão e Curvas de Calibração.
o	Benefício: Assegura que todos os modelos sejam avaliados com as mesmas métricas e procedimentos, facilitando a comparação justa.
b. Reutilização e Documentação
•	Estrutura de Repositório: A organização do código em pastas (e.g., src/, data/, notebooks/) garante que a lógica esteja separada da execução (notebooks).
•	Flexibilidade: O uso de funções e classes no Python permite que o pipeline aceite qualquer modelo que siga a API do Scikit-learn (.fit(), .predict(), .predict_proba()), suportando o desenvolvimento de múltiplos modelos de forma estruturada.
•	Documentação: Cada módulo contém docstrings claras, detalhando as entradas, saídas e a lógica das funções, tornando o pipeline replicável em contextos distintos com mínima adaptação.


