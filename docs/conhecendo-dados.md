# Conhecendo os dados

Nesta etapa, foi realizada uma análise descritiva e exploratória detalhada da base de dados student-depression-dataset, com o objetivo de compreender a estrutura dos dados, identificar outliers e explorar relações entre variáveis.

1. Importação e carregamento dos dados

Foram carregadas bibliotecas essenciais para manipulação de dados (pandas e numpy), visualização (matplotlib e seaborn) e modelagem (sklearn e shap). A base de dados foi baixada do Kaggle e importada para um DataFrame do pandas, permitindo inspeção inicial das colunas e seus tipos de dados. As variáveis incluíam informações demográficas, acadêmicas, hábitos de vida e o diagnóstico de depressão, sendo classificadas como numéricas ou categóricas.

<img width="742" height="186" alt="image" src="https://github.com/user-attachments/assets/c82d4147-7e1c-49a1-858e-ad5befc1e372" />


2. Análise descritiva

Variáveis numéricas: Foram calculadas medidas de tendência central (média, mediana e moda) e dispersão (desvio padrão, intervalos interquartis, mínimo e máximo).

Variáveis categóricas: Foram avaliadas frequências absolutas e percentuais para identificar distribuição das categorias e verificar o equilíbrio da variável alvo “Depression”.

Observou-se que a base contém 27.901 registros, sendo que 58,55% correspondem a estudantes com depressão e 41,45% a estudantes sem depressão.

3. Engenharia de dados

Valores nulos: Nenhum valor nulo foi identificado.

Duplicatas: Não foram encontradas linhas duplicadas.

Formatação de colunas: A coluna Sleep Duration foi padronizada, removendo textos redundantes e substituindo termos descritivos por símbolos (< e >).

4. Visualização dos dados

Histogramas: Foram gerados para variáveis numéricas, permitindo observar a distribuição dos dados, detectar assimetrias e identificar possíveis outliers.

Boxplots: Compararam variáveis numéricas em função da depressão, evidenciando diferenças de distribuição entre os grupos e possíveis valores extremos.

Countplots: Foram aplicados em variáveis categóricas para examinar a distribuição de categorias entre estudantes com e sem depressão.

Pairplots: Permitiram explorar visualmente relações entre variáveis numéricas e identificar agrupamentos ou padrões diferenciados entre os grupos.

5. Análise de correlação

Foi gerada uma matriz de correlação de Pearson entre as variáveis numéricas, revelando relações lineares entre pares de variáveis.

Um gráfico de barras horizontais destacou a correlação entre variáveis e a depressão, mostrando que algumas variáveis, como Academic Pressure e Study Satisfaction, apresentaram associações mais relevantes, enquanto outras apresentaram correlações baixas, sugerindo que relações não lineares podem ser exploradas por modelos preditivos.

6. Principais insights

A variável alvo está desbalanceada, com maior número de estudantes diagnosticados com depressão.

Algumas variáveis numéricas mostraram diferenças significativas entre grupos, o que indica relevância potencial para modelagem preditiva.

Outliers foram identificados em certas variáveis, justificando análises futuras de tratamento de dados.

Correlações lineares foram em geral baixas, indicando que interações complexas entre variáveis podem ser importantes para capturar padrões associados à depressão.

7. Organização do código

Todo o código utilizado foi estruturado de forma reprodutível e será disponibilizado na pasta src, garantindo que toda a análise possa ser replicada.

## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.


