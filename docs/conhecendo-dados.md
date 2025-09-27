# Conhecendo os dados
Nesta etapa, realizou-se uma análise detalhada para compreender a estrutura da base de dados, identificar outliers, e avaliar relações entre variáveis.

1.1 Importação das Bibliotecas

<img width="610" height="328" alt="image" src="https://github.com/user-attachments/assets/338b988f-bbd5-478d-8c29-60f9ee68f7bb" />

As bibliotecas escolhidas permitem: manipular dados (pandas, numpy), gerar visualizações (matplotlib, seaborn) e preparar a base para modelos de machine learning (sklearn, shap).

1.2 Coleta e Criação do DataFrame

<img width="766" height="318" alt="image" src="https://github.com/user-attachments/assets/27163acb-b36b-42ff-80d0-d3788608aa8e" />

Total de registros: 27.901

1.3 Estrutura dos Dados
<img width="339" height="36" alt="image" src="https://github.com/user-attachments/assets/9168f605-fea6-4a80-9317-69c04107b6d8" />
<img width="646" height="402" alt="image" src="https://github.com/user-attachments/assets/957acce0-d08f-4181-9048-fe4c6723d809" />

Observa-se que a maioria das variáveis numéricas estão no tipo float64 e várias informações categóricas (Gender, City, Dietary Habits, Degree, etc.) estão no tipo object.

1.4 Estatísticas Descritivas

<img width="309" height="38" alt="image" src="https://github.com/user-attachments/assets/b60ca23d-b3d3-40c8-be22-9c31723beddb" />

Medidas de tendência central e dispersão foram calculadas: média, mediana, desvio padrão, quartis.
Exemplo de insight:

Age: distribuição concentrada entre 18 e 25 anos.

CGPA: média próxima de 7, indicando nota acadêmica moderada.

Academic Pressure e Work Pressure: dispersão significativa → diferentes níveis de pressão percebida.

1.5 Distribuição da Variável Alvo

<img width="663" height="264" alt="image" src="https://github.com/user-attachments/assets/1d0f7187-be99-4846-a87f-e6649fe8dd05" />

<img width="851" height="144" alt="image" src="https://github.com/user-attachments/assets/5804114d-d635-4adf-b9b5-490e53f72d58" />

1.6 Engenharia de Dados

Não há valores nulos (df_dataset.isnull().sum())

Nenhuma linha duplicada (df_dataset.duplicated().sum() = 0)

Coluna Sleep Duration formatada: <7, >9, etc., para facilitar análise numérica/categórica

<img width="964" height="234" alt="image" src="https://github.com/user-attachments/assets/953fd254-8046-4371-a5c7-ad14caad8400" />

Histogramas mostram concentração, assimetria e possíveis outliers. Exemplo: Academic Pressure possui pico próximo de 5 (média de pressão percebida) e cauda à direita (valores extremos).


1.7.2 Boxplots (Identificação de Outliers)

<img width="960" height="182" alt="image" src="https://github.com/user-attachments/assets/3afc211c-b988-4eda-9598-e3f10b3769d1" />

CGPA tende a ser levemente menor em alunos com depressão.
Work/Study Hours apresenta outliers para ambas classes.

1.7.3 Contagem de Variáveis Categóricas

<img width="950" height="213" alt="image" src="https://github.com/user-attachments/assets/7b4661af-5a01-438a-b75f-544336ff5366" />

Permite observar distribuição e possíveis associações entre categorias e depressão. Exemplo: maior proporção de depressão em estudantes com histórico familiar de doença mental.

1.8 Matriz de Correlação

<img width="686" height="170" alt="image" src="https://github.com/user-attachments/assets/7697fda0-530c-43ac-9ed9-535fbd9cd271" />

Principais relações lineares:

Academic Pressure ↔ Study Satisfaction: moderada negativa

Age ↔ Work/Study Hours: pequena positiva


1.9 Pares de Variáveis com Maior Correlação
<img width="971" height="138" alt="image" src="https://github.com/user-attachments/assets/bb2708aa-7559-413b-b826-c7760d66901c" />

1.10 Conclusões da Análise Exploratória

Distribuição da variável alvo: ligeira predominância de casos com depressão.

Variáveis numéricas: algumas apresentam outliers e dispersão significativa.

Variáveis categóricas: histórico familiar, gênero e hábitos alimentares podem influenciar a depressão.

Correlação entre variáveis: algumas relações lineares moderadas, mas a maior parte é fraca → interações não lineares podem ser relevantes para modelos.

Próximo passo: preparação de dados para modelagem preditiva, incluindo codificação de variáveis categóricas e possíveis transformações de outliers.
## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a atenção? Foi possível identificar correlação entre os atributos? Que tipo de correlação (forte, fraca, moderada)? 

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação. Vale destacar que, preferencialmente, as análises deverão ser realizadas utilizando a linguagem de programação Python.


