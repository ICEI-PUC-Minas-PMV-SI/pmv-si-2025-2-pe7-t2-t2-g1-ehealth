 # Etapa 4 — Construção de Modelos  (parte 2)

A quarta etapa do projeto consistiu na implementação e avaliação de novos algoritmos de aprendizado de máquina, visando melhorar a capacidade preditiva em relação à Etapa 3 e promover a generalização do pipeline de análise.

## 1. Ajustes e Pré-Processamento de Dados 

Não foram necessários ajustes adicionais significativos ou novo pré-processamento dos dados em função da implementação dos novos algoritmos. Os modelos escolhidos, nomeadamente LGBMClassifier e CatBoostClassifier, são algoritmos de ensemble baseados em árvores de decisão. Esses modelos são robustos a diferentes distribuições de dados, não requerem normalização ou padronização de features e lidam bem com dados categóricos (One-Hot Encoding) e desbalanceamento, conforme já tratado na etapa de pré-processamento.

•	Diferença em Relação à Etapa Anterior: O pré-processamento se manteve, utilizando codificação One-Hot para variáveis nominais e mantendo a escala original das variáveis numéricas, o que foi adequado para a natureza dos novos modelos.

## 2. Implementação e Justificativa dos Algoritmos 

Foram implementados formalmente dois novos algoritmos (LGBM e Random Forest), com a subsequente inclusão do CatBoost para otimização da performance.

a. Light Gradient Boosting Machine (LGBMClassifier)

- Implementação: O modelo LGBMClassifier foi instanciado, treinado e avaliado. Utilizado com GridSearchCV para otimizar seus hiperparâmetros:


<img width="944" height="220" alt="image" src="https://github.com/user-attachments/assets/29355cd6-ed3f-4e5d-bd79-dfeaaab49923" />


 
- Justificativa da Escolha:

- 	Performance e Velocidade: LGBM é um algoritmo de gradient boosting conhecido por sua alta eficiência e velocidade de treinamento, especialmente em grandes conjuntos de dados, devido ao uso de técnicas como o Histogram-based Algorithm.
- 	Precisão: Ferequentemente alcança o estado da arte em problemas tabulares, superando outros algoritmos de boosting como o XGBoost em muitas situações.
-  Tratamento de Features: Por ser baseado em árvores, naturalmente lida com a não-linearidade e as interações complexas entre as variáveis, características comuns em dados de saúde mental. Algoritmo de Gradient Boosting conhecido por sua velocidade e precisão superior em grandes conjuntos de dados tabulares. 

b.  CatBoostClassifier 

Justificativa: Introduzido como um segundo ensemble (também baseado em Gradient Boosting) conhecido por seu tratamento eficiente de variáveis categóricas e sua robustez, buscando refinar a performance. Otimizado com auto_class_weights="Balanced" para lidar com o desbalanceamento de classes.

<img width="303" height="42" alt="image" src="https://github.com/user-attachments/assets/046e81ad-6a94-4bcb-81c4-7b6b1c4e5615" />

  
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

Os resultados extraídos das imagens indicam que o LGBMClassifier apresentou desempenho consistente nas duas classes. A Classe 1, foco principal do problema, obteve Precisão = 0.861, Recall = 0.870 e F1-Score = 0.865, demonstrando excelente capacidade de identificar corretamente os casos positivos e manter baixo o número de falsos alarmes. Para a Classe 0, o modelo também apresentou bom desempenho (F1-Score = 0.807), reforçando equilíbrio entre as classes.

A média ponderada das métricas manteve-se estável (F1-Score = 0.841), mesmo diante do leve desbalanceamento entre as classes. A acurácia geral foi de 0.842, indicando que 84,2% das previsões totais foram corretas. O support foi de 2313 amostras para a Classe 0 e 3267 para a Classe 1 (total = 5580), garantindo representatividade adequada para o cálculo das métricas.

| Métrica          | Classe 0 (Negativo) | Classe 1 (Positivo) | Média Ponderada |
|------------------|---------------------|-----------------------|------------------|
| Precisão         | 0.814               | 0.861                 | 0.841            |
| Recall           | 0.801               | 0.870                 | 0.842            |
| F1-Score         | 0.807               | 0.865                 | 0.841            |
| Acurácia Geral   | \multicolumn{3}{c}{0.842} |
| Support          | 2313                | 3267                  | 5580             |



c. Desempenho do CatBoostClassifier

O modelo demonstra um bom desempenho geral, com a acurácia de 84.71%. A Classe 1 (support=3267) tem métricas ligeiramente superiores (f1-score $\approx 0.87) em comparação com a Classe 0 (support=2313, f1-score $\approx 0.81).O f1-score ponderado de 0.84646 é uma métrica robusta para a performance geral do classificador.


<img width="449" height="195" alt="image" src="https://github.com/user-attachments/assets/223d1add-649b-4f70-b676-7da09b322c0e" />






-  Matriz de Confusão do LGBMClassifier 

A matriz do LGBMClassifier mostra a distribuição de acertos e erros no conjunto de teste (Total de 5580 amostras).

Análise do LGBM:

•	Verdadeiros Positivos (VP - Real 1, Previsto 1): 2873
•	Verdadeiros Negativos (VN - Real 0, Previsto 0): 1832
•	Falsos Positivos (FP - Real 0, Previsto 1): 481
•	Falsos Negativos (FN - Real 1, Previsto 0): 394
 
 - O modelo acertou a maioria dos casos positivos.
 -  O modelo deixou de identificar 394 casos positivos reais (risco de negligência). Este valor representa $12.06\%$ da Classe 1 real ($\frac{394}{3267}$).
 -  O modelo classificou 481 casos como positivos quando eram negativos (intervenção desnecessária). Este valor representa $20.80\%$ da Classe 0 real ($\frac{481}{2313}$. O LGBM é um modelo mais sensível, pois tem um Recall (0.870) mais alto, resultando em um número menor de Falsos Negativos.


 
 <img width="886" height="628" alt="image" src="https://github.com/user-attachments/assets/87695c2d-ddf2-4cad-a6b1-74667a462cbc" />
 

-   Matriz de Confusão do Random Forest 


A matriz do Random Forest mostra sua distribuição de acertos e erros no conjunto de teste.

 - Verdadeiros Positivos (VP): 2770. Acertou um número ligeiramente menor de positivos que o LGBM.
 - Falsos Negativos (FN): 497. O modelo deixou de identificar 497 casos positivos reais (risco de negligência). Este valor representa $15.21\%$ da Classe 1 real ($\frac{497}{3267}$).
 - Falsos Positivos (FP): 370. O modelo classificou 370 casos como positivos quando eram negativos (intervenção desnecessária). Este valor representa $16.00\%$ da Classe 0 real ($\frac{370}{2313}$).
 - O Random Forest é um modelo mais conservador, obtendo um número maior de Falsos Negativos, mas um número significativamente menor de Falsos Positivos.



<img width="522" height="397" alt="image" src="https://github.com/user-attachments/assets/43c5ae01-9d2d-4b01-bc2b-e53bcef38d49" />



 a. Calibração do LGBMClassifier

 <img width="886" height="392" alt="image" src="https://github.com/user-attachments/assets/dec72692-6d16-485e-8398-ce5a8086e3da" />
 

•	A Curva de Calibração (Base ou Classe 1) mostra que o modelo Base (sem calibração adicional) está bem calibrado para a Classe 1, seguindo de perto a linha pontilhada (Perfeita y=x). Isso indica que as probabilidades previstas são confiáveis (e.g., uma previsão de 0.80 corresponde a uma taxa observada de 0.80). A calibração isotônica aprimora ligeiramente a performance.

b. Calibração do  Random Forest 



 <img width="794" height="392" alt="image" src="https://github.com/user-attachments/assets/d08571c2-756e-4126-8aa4-df229f1f1944" />

## 4. Comparação de Desempenho e Análise Crítica 
A comparação se concentra na métrica principal: F1-Score.

A análise crítica será baseada nos resultados fornecidos para o LGBMClassifier e no conhecimento teórico de ambos os modelos no contexto do problema.

| Modelo                | F1-Score (Classe 1) | Vantagens Percebidas                                                                                      | Limitações Percebidas                                                                                                          |
|-----------------------|----------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **LGBMClassifier**    | 0.865                | Alta precisão (0.861) e recall (0.870) para a classe positiva. Velocidade de treinamento. Lida bem com desbalanceamento através da métrica de *boosting*. | Maior propensão a *overfitting* se não for bem parametrizado (necessitando de *early stopping* e regularização).               |
| **RandomForestClassifier** | *(Não disponível)* | Mais estável, robusto e menos propenso a *overfitting*. Paralelizável. Fornece uma boa linha de base de interpretabilidade de *features*. | Geralmente alcança performance ligeiramente inferior a modelos de *boosting* finamente ajustados.                               |


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
   
- Contém as classes ou funções para instanciar diferentes modelos (LGBMClassifier, RandomForestClassifier etc.), treiná-los e realizar ajuste de hiperparâmetros (como GridSearchCV mencionado na imagem a seguir): 
 
- 	Benefício: Permite a rápida substituição e comparação de algoritmos.
  
3.	Módulo de Avaliação (evaluation.py):
   
- 	Contém funções padronizadas para cálculo de métricas (Precisão, Recall, F1-Score, etc.), geração de Matriz de Confusão e Curvas de Calibração.
- Benefício: Assegura que todos os modelos sejam avaliados com as mesmas métricas e procedimentos, facilitando a comparação justa.
  
b. Reutilização e Documentação

- 	Estrutura de Repositório: A organização do código em pastas (e.g., src/, data/, notebooks/) garante que a lógica esteja separada da execução (notebooks).
- Flexibilidade: O uso de funções e classes no Python permite que o pipeline aceite qualquer modelo que siga a API do Scikit-learn (.fit(), .predict(), .predict_proba()), suportando o desenvolvimento de múltiplos modelos de forma estruturada.
- Documentação: Cada módulo contém docstrings claras, detalhando as entradas, saídas e a lógica das funções, tornando o pipeline replicável em contextos distintos com mínima adaptação.


