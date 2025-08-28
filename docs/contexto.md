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

Nesta seção, descreva quem poderá se beneficiar com a sua investigação, apresentando os diferentes perfis de pessoas ou grupos impactados.

O objetivo aqui não é definir clientes específicos ou papéis exatos dentro da aplicação, mas sim compreender o perfil dos usuários e partes interessadas. Para isso, considere:
* Conhecimentos prévios relacionados ao domínio do problema e ao uso de tecnologia;
* Nível de familiaridade com recursos digitais e possíveis barreiras de uso;
* Contexto profissional e hierárquico, quando aplicável (ex.: nível de decisão, responsabilidades, área de atuação);
* Necessidades e expectativas que podem ser atendidas pelo projeto.

**Dica:** Seja objetivo e baseie suas descrições em informações reais ou plausíveis para o contexto escolhido. Isso ajudará a manter o foco no desenvolvimento de soluções relevantes e aplicáveis.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

# Estado da arte

A aplicação de aprendizado de máquina (AM) à saúde mental de estudantes mostra desempenho prometedor em tarefas de triagem e previsão de risco. Uma revisão sistemática focada em universitários achou bons resultados com modelos como Random Forest, SVM, XGBoost e redes neurais, desde que haja validação adequada e atenção à generalização entre contextos institucionais e culturais [1]. Em estudo longitudinal com inquérito anual de saúde estudantil, modelos como gradient boosting e florestas aleatórias previram problemas de saúde mental em janelas de até 1 ano à frente [2].

Em universidades de países em desenvolvimento, abordagens de ensemble stacking com variáveis acadêmicas, de estresse/pressão, sono e satisfação alcançaram desempenho competitivo para detecção precoce de depressão [3]. Esses achados dialogam diretamente com os campos do nosso dataset (p. ex., *Academic Pressure*, *Financial Stress*, *Sleep Duration*, *Study Satisfaction*).

Por fim, a literatura recente enfatiza viés e equidade. Modelos de aprendizado de máquina podem ser úteis para prever depressão, principalmente em estágios iniciais desta. Revisões e estudos de caso mostram que modelos para depressão podem degradar desempenho em subgrupos se o treinamento não for representativo. Portanto, recomenda-se refinar os modelos e a alimentar com o máximo de variáveis e dados possíveis, mantendo uma melhora constante nas pesquisas e a mitigação de dados enviesados.

**Resumo:** há base empírica para empregar aprendizado de máquina na previsão/detecção de depressão em estudantes, sobretudo com atributos acadêmicos e de estilo de vida.

---

# Descrição do dataset selecionado

**Student Depression Dataset (Kaggle — por Adil Shamim)**

**Links de acesso ao dataset**
- Página oficial no Kaggle: <https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset>

**Descrição**
Conjunto de dados tabular, auto-reportado, voltado a analisar e prever depressão em estudantes a partir de demografia, variáveis acadêmicas/profissionais, hábitos de vida e estressores. Amostras incluem diversas cidades (muitas entradas da Índia, p. ex. Visakhapatnam, Pune, Jaipur, Varanasi). O alvo é um rótulo binário Depression (p. ex., *Yes/No* ou 0/1). Versões amplamente usadas em análises públicas reportam ~27,9 mil linhas e 18 colunas.

**Atributos (exemplos recorrentes)**
- `id` (inteiro)
- `Gender` (categoria)
- `Age` (inteiro)
- `City` (texto)
- `Working Professional or Student` / `Profession` (categoria)
- **Acadêmico/Trabalho:** `Academic Pressure` (escala), `Work Pressure` (escala), `CGPA` (numérico), `Study Satisfaction` (escala), `Job Satisfaction` (escala), `Work/Study Hours` (inteiro)
- **Hábitos/Histórico:** `Sleep Duration` (categorias como “Less than 5h”, “6–7h”, “7–8h”), `Dietary Habits` (Healthy/Moderate/Unhealthy), `Degree` (curso), `Financial Stress` (escala), `Family History of Mental Illness` (Sim/Não), **`Have you ever had suicidal thoughts?`** (Sim/Não)
- **Alvo:** `Depression` (binário)

**Tamanho e período**
- Tamanho: **≈ 27.901 amostras, 18 atributos** (algumas versões “limpas” variam levemente).
- Caráter **transversal** (sem carimbo de data por registro). Trate como *cross-sectional*.

**Valores faltantes e qualidade dos dados**
Relatos comunitários indicam CSV com **todas as colunas presentes** e, em várias cargas, **contagens *non-null* completas**; outras versões “limpas” variam levemente em linhas/tipos. Boas práticas recomendadas:
1. Padronizar categorias (p. ex., `Sleep Duration`, `Dietary Habits`);
2. Converter escalas para numérico coerente;
3. Verificar desbalanceamento do alvo e aplicar *class weights* ou *resampling* quando necessário.

**Observações de modelagem**
Em tarefas binárias com esse CSV, **GBM/XGBoost e Random Forest** tendem a performar bem; *feature importance* costuma destacar **ideação suicida, pressão acadêmica e estresse financeiro** como preditores de alto ganho — compatível com a literatura sobre sono, estresse e desempenho. Use validação estratificada e explique o modelo (SHAP/LIME) para suporte à decisão.

---

## Referências (seleção)

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

# Canvas analítico

Nesta seção, você deverá estruturar e preencher o seu Canvas Analítico, que tem como objetivo registrar a organização das ideias e apresentar o modelo de negócio do projeto.

O Canvas deve ser preenchido integralmente, mesmo que algumas informações ainda não estejam totalmente definidas. Nessa etapa inicial, é aceitável trabalhar com hipóteses ou estimativas, desde que sejam coerentes com o problema e o contexto definidos.

**Dica:** O Canvas Analítico serve como guia visual para alinhar expectativas e direcionar o desenvolvimento. Ele poderá (e deverá) ser revisitado e atualizado ao longo do projeto.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Vídeo de apresentação da Etapa 01

Nesta etapa, o grupo deverá produzir um vídeo de 5 a 8 minutos apresentando o trabalho realizado, no qual cada integrante deve dizer seu nome e apresentar uma parte do conteúdo desenvolvido, garantindo que todos participem ativamente da gravação. A ausência de participação de qualquer membro resultará em penalização na nota final desta etapa. Recomenda-se que o grupo elabore previamente um roteiro para organizar a ordem das falas, distribuir o tempo de forma equilibrada e assegurar que todos os tópicos relevantes sejam apresentados de maneira clara e objetiva.

# Referências

ICEI-PUC-MINAS. Modelo do Canvas Analítico. Disponível em: https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf
. Acesso em: 10 ago. 2025.

ZHANG, Z.; CAI, Z.; MENG, Q. Negative life events, sleep quality and depression in university students. Sci Rep 15, 21193 (2025). Disponível em: https://doi.org/10.1038/s41598-025-08635-6
. Acesso em: 23 ago. 2025.

TERRELL, K. R.; STANTON, B. R.; HAMADI, H. Y.; MERTEN, J. W.; QUINN, N. Exploring life stressors, depression, and coping strategies in college students. J Am Coll Health, 72(3):923-932, abr. 2024. Disponível em: https://pubmed.ncbi.nlm.nih.gov/35427463/
. Acesso em: 22 ago. 2025.

NIU, C.; JIANG, Y.; LI, Y. et al. A network analysis of the heterogeneity and associated risk and protective factors of depression and anxiety among college students. Sci Rep 15, 6699 (2025). Disponível em: https://doi.org/10.1038/s41598-025-91025-9
. Acesso em: 22 ago. 2025.

LI, L.; WANG, P.; LI, S.; LIU, Q.; YU, F.; GUO, Z.; JIA, S.; WANG, X. Canonical correlation analysis of depression and anxiety symptoms among college students and their relationship with physical activity. Sci Rep, 13(1):11516, 17 jul. 2023. Disponível em: https://pubmed.ncbi.nlm.nih.gov/37460562/
. Acesso em: 23 ago. 2025.

ELBARAZI, A.; TIKAMDAS, R. Association between university student junk food consumption and mental health. Nutr Health, 30(4):861-867, dez. 2024. Disponível em: https://pubmed.ncbi.nlm.nih.gov/36691314/
. Acesso em: 21 ago. 2025.

ROLDÁN-ESPÍNOLA, L.; RIERA-SERRA, P.; ROCA, M.; GARCÍA-TORO, M.; CORONADO-SIMSIC, V.; CASTRO, A.; NAVARRA-VENTURA, G.; VILAGUT, G.; ALAYO, I.; BALLESTER, L.; BLASCO, M. J.; ALMENARA, J.; CEBRIÀ, A. I.; ECHEBURÚA, E.; GABILONDO, A.; LAGARES, C.; PIQUERAS, J. A.; SOTO-SANZ, V.; MORTIER, P.; KESSLER, R. C.; ALONSO, J.; FORTEZA-REY, I.; GILI, M. Depression and lifestyle among university students: A one-year follow-up study. The European Journal of Psychiatry, 38(3):100250, 2024. Disponível em: https://doi.org/10.1016/j.ejpsy.2024.100250
. Acesso em: 21 ago. 2025.


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
