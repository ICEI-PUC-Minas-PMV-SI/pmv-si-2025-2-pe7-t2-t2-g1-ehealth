# Introdução

## Problema

A depressão entre estudantes é um fenômeno crescente e preocupante em contextos educacionais, pois afeta diretamente o desempenho acadêmico, as relações sociais e o bem-estar geral. Apesar da relevância do tema, muitas instituições de ensino ainda encontram dificuldades em identificar precocemente os alunos em risco, já que os fatores associados à saúde mental são múltiplos, complexos e muitas vezes pouco visíveis no cotidiano escolar.

O conjunto de dados utilizado neste estudo reúne informações demográficas, acadêmicas, de estilo de vida e de histórico familiar que podem auxiliar na compreensão das condições que influenciam o desenvolvimento da depressão em estudantes. No entanto, a grande quantidade e a diversidade de variáveis tornam difícil para professores, psicólogos e gestores escolares interpretarem de forma clara quais fatores exercem maior impacto sobre a saúde mental.

Dessa forma, o problema central desta investigação é: como analisar, de forma sistemática, os fatores presentes nos dados para identificar tendências, padrões e preditores relacionados à depressão entre estudantes, possibilitando uma compreensão mais profunda desse fenômeno e contribuindo para estratégias de prevenção e intervenção precoce?

O contexto de aplicação envolve o uso deste dataset em pesquisas acadêmicas e projetos em ciência de dados, com potencial para apoiar tanto a formulação de políticas institucionais voltadas ao cuidado da saúde mental quanto o desenvolvimento de ferramentas que auxiliem profissionais da educação e da psicologia no acompanhamento de estudantes em risco.

## Questão de pesquisa

Quais fatores acadêmicos, demográficos, de estilo de vida e histórico familiar mais influenciam a ocorrência de depressão entre estudantes, e de que forma a análise desse conjunto de dados pode auxiliar na identificação precoce de alunos em risco?

## Objetivos preliminares

O objetivo geral deste trabalho é analisar e prever a presença de sintomas de depressão em estudantes universitários a partir do Student Depression Dataset, identificando fatores acadêmicos, demográficos e de estilo de vida que influenciam o problema. Essa formulação expressa de forma clara e delimitada a intenção central da pesquisa, que é compreender de maneira quantitativa e sistemática os elementos associados à saúde mental estudantil.

Para alcançar esse objetivo mais amplo, foram definidos alguns objetivos específicos que direcionam a investigação. Em primeiro lugar, pretende-se descrever o perfil dos estudantes, apresentando características demográficas, acadêmicas e de hábitos de vida disponíveis no conjunto de dados. Em seguida, busca-se investigar as correlações entre variáveis relevantes como duração do sono, pressão acadêmica e satisfação com os estudos e o status de depressão informado pelos participantes.

Além disso, será necessário aplicar algoritmos de aprendizado de máquina supervisionado, como Regressão Logística, Random Forest e XGBoost, de modo a avaliar a capacidade preditiva do conjunto de dados. Após essa etapa, pretende-se comparar o desempenho dos diferentes modelos, utilizando métricas apropriadas como acurácia, F1-Score e AUC-ROC, para verificar qual abordagem se mostra mais eficaz. Por fim, busca-se identificar e interpretar os fatores de maior relevância nas predições, valendo-se de técnicas de interpretabilidade como SHAP ou LIME, de modo a oferecer não apenas resultados numéricos, mas também explicações compreensíveis sobre os padrões encontrados.

<!-- Nesta seção, você deve apresentar os objetivos preliminares do trabalho, deixando claro que o objetivo geral é experimentar modelos de aprendizado de máquina adequados para solucionar o problema descrito anteriormente.

Além do objetivo geral, é importante definir pelo menos dois objetivos específicos, que direcionem a investigação de acordo com o foco que o grupo pretende adotar. Esses objetivos específicos podem envolver:
* Explorar um determinado tipo de modelagem ou técnica de aprendizado de máquina;
* Comparar diferentes abordagens para resolver o mesmo problema;
* Aplicar o modelo em um cenário real ou simulado;
* Otimizar parâmetros para melhorar métricas específicas de desempenho.

Exemplo:
Objetivo específico 1: Predizer a tendência de alta, estabilidade ou queda de uma determinada ação em uma janela de tempo definida.
Objetivo específico 2: Estimar o valor exato da ação ao final do período analisado.

**Importante:** À medida que a pesquisa/experimentação avança, os objetivos podem ser ajustados ou refinados. Mantenha essa seção atualizada no repositório para refletir o andamento e as novas decisões do projeto.

> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/) -->

## Justificativa

O presente projeto busca analisar o Student Depression Dataset, que reúne informações demográficas, acadêmicas, de estilo de vida e de saúde mental autorrelatada, para identificar padrões e fatores de risco associados à depressão. A escolha dos objetivos específicos está alinhada a esse propósito: descrever o perfil dos estudantes, investigar correlações entre variáveis críticas (como sono, pressão acadêmica e satisfação pessoal) e aplicar algoritmos de aprendizado de máquina para avaliar a viabilidade de prever o status de depressão. A justificativa para aprofundar a investigação nesses pontos é que tais variáveis foram apontadas em estudos recentes como preditores consistentes de sintomas depressivos (ZHANG et al., 2024; JISHA et al., 2024). Assim, compreender como esses fatores interagem no dataset é um passo essencial para propor soluções mais assertivas.

A relevância do estudo vai além do contexto acadêmico. Do ponto de vista profissional, os resultados podem subsidiar equipes pedagógicas e psicopedagógicas na formulação de programas de prevenção, campanhas de conscientização e estratégias de acolhimento estudantil. Do ponto de vista científico, contribui para a literatura sobre uso de inteligência artificial aplicada à saúde mental, em uma área onde ainda há lacunas relacionadas à generalização de modelos e à explicabilidade das previsões.

O impacto social também é significativo. Estimativas da Organização Mundial da Saúde (OMS, 2020) mostram que a depressão é uma das principais causas de incapacidade em jovens de 15 a 29 anos, e que estudantes com sintomas depressivos apresentam até duas vezes mais risco de evasão acadêmica. Além disso, problemas de saúde mental têm reflexos econômicos: a OMS calcula que transtornos como depressão e ansiedade custam à economia mundial cerca de 1 trilhão de dólares por ano em perda de produtividade. No ambiente universitário, esse impacto se traduz em queda de desempenho, desistências e sobrecarga nos serviços de saúde estudantil.

Por fim, a base do trabalho está sustentada em um dataset público disponível no Kaggle, o Student Depression Dataset, que oferece dados anonimizados de centenas de estudantes. Aliado à literatura científica recente, esse material fornece subsídios concretos para investigar o problema, garantindo que o estudo seja conduzido com robustez metodológica, relevância prática e impacto social.
<!--
Nesta seção, apresente a importância e a motivação para trabalhar com o conjunto de dados escolhido. Explique por que esse dataset é relevante e como ele se conecta ao problema identificado anteriormente.

Indique:
* Razões para a escolha dos objetivos específicos – Justifique por que decidiu aprofundar sua investigação nessas metas, relacionando-as ao potencial de solução ou melhoria para o problema.
* Relevância do estudo do problema – Mostre a importância de compreender e tratar a questão apresentada, tanto no contexto acadêmico quanto no profissional.
* Impacto social, econômico ou ambiental – Descreva como o problema afeta a sociedade ou um setor específico, buscando sempre quantificar o impacto por meio de dados reais.

**Importante:**
* Apresente números, estatísticas e informações concretas, citando as fontes (relatórios, artigos científicos, portais oficiais etc.).
* Mantenha a objetividade e a clareza, evitando argumentos genéricos.
* Construa um texto coeso que conecte o problema, os objetivos e a relevância do trabalho.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/) -->

## Público-Alvo

O projeto tem como público alvo, inicialmente, instituições de ensino que enfrentam diariamente o desafio de lidar com estudantes em diferentes contextos pessoais e emocionais. 
Instituições que contam com profissionais que visam dar suporte psicológico e pedagógico a seus alunos, apesar de terem domínio técnico sobre a atuação profissional para diagnóstico e tratamento, muitas vezes não dispõem de ferramentas para coletar dados e identificar alunos que podem se beneficiar de atendimento psicológico. Ao terem acesso a análises baseadas em dados, poderão ser planejadas atuações visando identificar e tratar de forma mais eficaz alunos em situação de risco.

Também são público-alvo os pesquisadores e acadêmicos das áreas de Ciência de Dados, Psicologia e Educação. Um grupo que possui mais familiaridade com métodos quantitativos e qualitativo, tecnologias e dados, podendo se beneficiar do projeto como material para estudo e desenvolvimento de metodologias sobre o tema. 

Por fim, os próprios estudantes são beneficiados, pois são públicos que esperamos ajudar socialmente. As informações extraídas dos dados podem orientar ações que promovam melhor qualidade de vida e amparo profissional. 


# Estado da arte

A aplicação de aprendizado de máquina (AM) à saúde mental de estudantes mostra desempenho prometedor em tarefas de triagem e previsão de risco. Uma revisão sistemática focada em universitários achou bons resultados com modelos como Random Forest, SVM, XGBoost e redes neurais, desde que haja validação adequada e atenção à generalização entre contextos institucionais e culturais [1]. Em estudo longitudinal com inquérito anual de saúde estudantil, modelos como gradient boosting e florestas aleatórias previram problemas de saúde mental em janelas de até 1 ano à frente [2].

Em universidades de países em desenvolvimento, abordagens de ensemble stacking com variáveis acadêmicas, de estresse/pressão, sono e satisfação alcançaram desempenho competitivo para detecção da depressão em estágios iniciais [3]. Esses achados dialogam diretamente com os campos do dataset (p. ex., Academic Pressure, Financial Stress, Sleep Duration, Study Satisfaction).

Por fim, a literatura recente enfatiza viés e equidade. Modelos de aprendizado de máquina podem ser úteis para prever depressão, principalmente em estágios iniciais desta.  Portanto, recomenda-se refinar os modelos e a alimentá-los com o máximo de variáveis e dados possíveis, mantendo uma melhora constante nas pesquisas e uma mitigação de dados enviesados.

**Resumo:** há base empírica para empregar aprendizado de máquina na previsão/detecção de depressão em estudantes, sobretudo com atributos acadêmicos e de estilo de vida.

---

# Descrição do _dataset_ selecionado

## Conjunto de dados sobre depressão estudantil

Arquivo de tabela no formato CSV contendo 18 colunas e 27.901 registros

Tamanho do arquivo: 2,9MB

Disponível em: https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset

Este conjunto de dados contém informações abrangentes sobre a saúde mental dos estudantes e fatores relacionados. Ele foi desenvolvido para analisar tendências e preditores de depressão entre estudantes. Os dados incluem detalhes demográficos, pressões acadêmicas e profissionais, hábitos de vida e indicadores específicos de saúde mental. 

### Atributos e descrições dos campos

*  id

    * Tipo: Inteiro

    * Descrição: Um identificador em numero inteiro exclusivo atribuído a cada registro de aluno no conjunto de dados.

* Gender

    * Nosso idioma: Gênero

    * Tipo: String

    * Descrição: O gênero do aluno (ex.: masculino, feminino, outro). Isso ajuda a analisar tendências específicas de gênero na saúde mental.

* Age

    * Nosso idioma: Idade

    * Tipo: Inteiro

    * Descrição: Idade do aluno em anos.

* City

    * Nosso idioma: Cidade

    * Tipo: String

    * Descrição: Nome da cidade ou região onde o aluno reside, fornecendo contexto geográfico para a análise.

* Profission

    * Nosso idioma: Profissão

    * Tipo: String

    * Descrição: Área de trabalho ou estudo do aluno, que pode oferecer insights sobre fatores de estresse ocupacional ou acadêmico.

* Academic Pressure

    * Nosso idioma: Pressão Acadêmica

    * Tipo: Inteiro

    * Escala: 0 a 5

    * Descrição: Uma medida que indica o nível de pressão que o aluno enfrenta em ambientes acadêmicos. Isso pode incluir estresse causado por provas, trabalhos e expectativas acadêmicas gerais.

* Work Pressure

    * Nosso idioma: Pressão no trabalho

    * Tipo: Inteiro

    * Escala: 0 a 5

    * Descrição: Uma medida da pressão relacionada ao trabalho ou às responsabilidades do cargo, relevante para estudantes que trabalham paralelamente aos estudos.

* CGPA

    * Tipo: Decimal

    * Escala: 0 a 10

    * Descrição: Média cumulativa de notas do aluno, refletindo o desempenho acadêmico geral.

* Study Satisfaction

    * Nosso idioma: Satisfação com os estudos

    * Tipo: Inteiro

    * Escala: 0 a 5

    * Descrição: Um indicador de quão satisfeito o aluno está com seus estudos, o que pode estar relacionado ao bem-estar mental.

* Job Satisfaction

    * Nosso idioma: Satisfação no trabalho

    * Tipo: Inteiro

    * Escala: 0 a 5

    * Descrição: Uma medida da satisfação do aluno com seu trabalho ou ambiente de trabalho, se aplicável.

* Sleep Duration

    * Nosso idioma: Duração do sono

    * Tipo: String

    * Formato: Intervalos de sono

    * Descrição: Intervalo médio de horas que o aluno dorme por dia, o que é um fator importante para a saúde mental.

* Dietary Habits

    * Nosso idioma: Hábitos alimentares

    * Tipo: String

    * Formato: Intervalos de sono ex: 8 horas

    * Descrição: Uma avaliação dos padrões alimentares e hábitos nutricionais do aluno, que podem impactar a saúde geral e o humor.

* Degree

    * Nosso idioma: Grau

    * Tipo: String

    * Formato: Classificação de escolaridade americana

    * Descrição: O grau acadêmico ou programa que o aluno está cursando.

* Have you ever had suicidal thoughts?

    * Nosso idioma: Você já teve pensamentos suicidas?

    * Tipo: String

    * Formato: Sim ou Não

    * Descrição: Um indicador binário (Sim/Não) que reflete se o aluno já teve ideação suicida.

* Work/Study Hours

    * Nosso idioma: Horas de Trabalho/Estudo

    * Tipo: Inteiro

    * Formato: Sim ou Não

    * Descrição: Número médio de horas por dia que o aluno dedica ao trabalho ou estudo, o que pode influenciar os níveis de estresse.

* Financial Stress

    * Nosso idioma: Estresse financeiro

    * Tipo: Inteiro

    * Escala: 1 a 5

    * Descrição: Uma medida do estresse experimentado devido a preocupações financeiras, que podem afetar a saúde mental.

* Family History of Mental Illness

    * Nosso idioma: Histórico familiar de doença mental

    * Tipo: String

    * Formato: Sim ou Não

    * Descrição: Indica se há histórico familiar de doença mental (Sim/Não), o que pode ser um fator significativo nas predisposições à saúde mental.

* Depression

    * Nosso idioma: Depressão

    * Tipo: Binario

    * Descrição: Variável-alvo que indica se o aluno está sofrendo de depressão (Sim/Não). Este é o foco principal da análise.

# Vídeo de apresentação da Etapa 01

A seguir link do video publicado no Youtbe

https://youtu.be/C58-2ict588

# Referências

[1] Schaab, B. L., et al. (2024). *How do machine learning models perform in the detection and prediction of depression, anxiety, and stress among undergraduate university students?* Systematic Review. Disponível em: https://pmc.ncbi.nlm.nih.gov/articles/PMC11654111/

[2] Baba, A., et al. (2023). *Prediction of Mental Health Problem Using Annual Student Health Survey Data: Machine Learning Approach.* JMIR Mental Health. Disponível em: https://mental.jmir.org/2023/1/e42420

[3] Vergaray, A. D., et al. (2023). *Predicting the depression in university students using machine learning (Ensemble Stacking).* Data in Brief / Elsevier. Disponível em: https://www.sciencedirect.com/science/article/pii/S2352914823001417

[4] Kroenke, K., Spitzer, R. L., Williams, J. B. W. (2001). *The PHQ‑9: Validity of a Brief Depression Severity Measure.* J Gen Intern Med, 16(9), 606–613. Disponível em: https://pubmed.ncbi.nlm.nih.gov/11556941/

[5] Olawade, D. B., et al. (2024). *Enhancing mental health with Artificial Intelligence.* Journal of Medicine in AI. (Discussão sobre viés/fairness.) Disponível em: https://www.sciencedirect.com/science/article/pii/S2949916X24000525

[6] Dang, V. N., et al. (2024). *Fairness and bias correction in machine learning for depression: A systematic study.* Disponível em: https://pmc.ncbi.nlm.nih.gov/articles/PMC10991528/

[7] Jiang, Z., et al. (2024). *Evaluating and mitigating unfairness in multimodal remote mental health assessment.* Disponível em: https://pmc.ncbi.nlm.nih.gov/articles/PMC11268595/

[8] Choi, A., et al. (2024). *Digital Phenotyping for Stress, Anxiety, and Mild Depression Using Smartphones.* JMIR mHealth and uHealth. Disponível em: https://mhealth.jmir.org/2024/1/e40689

[9] Borelli, J. L., et al. (2025). *Detection of Depressive Symptoms in College Students Using Passive Sensing and LightGBM.* JMIR Formative Research. Disponível em: https://formative.jmir.org/2025/1/e67964

**Dataset de interesse:** Kaggle — *Student Depression Dataset* (Adil Shamim). https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset

BABA, A.; et al. Prediction of mental health problem using annual student health survey data: machine learning approach. *JMIR Mental Health*, 2023. Disponível em: [https://mental.jmir.org/2023/1/e42420](https://mental.jmir.org/2023/1/e42420). Acesso em: 29 ago. 2025.
 
BORELLI, J. L.; et al. Detection of depressive symptoms in college students using passive sensing and LightGBM. *JMIR Formative Research*, 2025. Disponível em: [https://formative.jmir.org/2025/1/e67964](https://formative.jmir.org/2025/1/e67964). Acesso em: 29 ago. 2025.
 
CHOI, A.; et al. Digital phenotyping for stress, anxiety, and mild depression using smartphones. *JMIR mHealth and uHealth*, 2024. Disponível em: [https://mhealth.jmir.org/2024/1/e40689](https://mhealth.jmir.org/2024/1/e40689). Acesso em: 29 ago. 2025.
 
DANG, V. N.; et al. Fairness and bias correction in machine learning for depression: a systematic study. 2024. Disponível em: [https://pmc.ncbi.nlm.nih.gov/articles/PMC10991528/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10991528/). Acesso em: 29 ago. 2025.
 
FACELI, Katti; LORENA, Ana Carolina; GAMA, João; CARVALHO, André Carlos Ponce de Leon Ferreira de. *Inteligência artificial: uma abordagem de aprendizado de máquina*. 2. ed. Rio de Janeiro: LTC, 2021. ISBN 978-85-216-3749-3.
 
ICEI-PUC-MINAS. Modelo do Canvas Analítico. Disponível em: [https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf). Acesso em: 10 ago. 2025.
 
JIANG, Z.; et al. Evaluating and mitigating unfairness in multimodal remote mental health assessment. 2024. Disponível em: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11268595/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268595/). Acesso em: 29 ago. 2025.
 
KROENKE, K.; SPITZER, R. L.; WILLIAMS, J. B. W. The PHQ-9: validity of a brief depression severity measure. *Journal of General Internal Medicine*, v. 16, n. 9, p. 606–613, 2001. Disponível em: [https://pubmed.ncbi.nlm.nih.gov/11556941/](https://pubmed.ncbi.nlm.nih.gov/11556941/). Acesso em: 29 ago. 2025.
 
LARSON, Ron; FARBER, Elizabeth. *Estatística aplicada*. 6. ed. São Paulo: Pearson Education do Brasil, 2016. ISBN 9788543004778.
 
OLAWADE, D. B.; et al. Enhancing mental health with artificial intelligence. *Journal of Medicine in AI*, 2024. Disponível em: [https://www.sciencedirect.com/science/article/pii/S2949916X24000525](https://www.sciencedirect.com/science/article/pii/S2949916X24000525). Acesso em: 29 ago. 2025.
 
SCHAAB, B. L.; et al. How do machine learning models perform in the detection and prediction of depression, anxiety, and stress among undergraduate university students? *Systematic Review*, 2024. Disponível em: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11654111/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11654111/). Acesso em: 29 ago. 2025.
 
SGRECCIA, Elio. *Manual de bioética: volume 1: fundamentos e ética biomédica*. São Paulo: Edições Loyola, 1996. 686 p. ISBN 8515012855.
 
SHAMIM, A. *Student Depression Dataset*. Kaggle, 2023. Disponível em: [https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset). Acesso em: 29 ago. 2025.
 
VERGARAY, A. D.; et al. Predicting the depression in university students using machine learning (Ensemble Stacking). *Data in Brief*, 2023. Disponível em: [https://www.sciencedirect.com/science/article/pii/S2352914823001417](https://www.sciencedirect.com/science/article/pii/S2352914823001417). Acesso em: 29 ago. 2025.


<!--

> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)
> - [Matriz Certezas, Suposições e Dúvidas](https://medium.com/educa%C3%A7%C3%A3o-fora-da-caixa/matriz-certezas-suposi%C3%A7%C3%B5es-e-d%C3%BAvidas-fa2263633655)
> - [Brainstorming](https://www.euax.com.br/2018/09/brainstorming/)
> - [Questão de pesquisa](https://www.enago.com.br/academy/how-to-develop-good-research-question-types-examples/)
> - [Problema de pesquisa](https://blog.even3.com.br/problema-de-pesquisa/)
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)


Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886) -->
