# Introdução

## Problema

A depressão entre estudantes é um fenômeno crescente e preocupante em contextos educacionais, pois afeta diretamente o desempenho acadêmico, as relações sociais e o bem-estar geral. Apesar da relevância do tema, muitas instituições de ensino ainda encontram dificuldades em identificar precocemente os alunos em risco, já que os fatores associados à saúde mental são múltiplos, complexos e muitas vezes pouco visíveis no cotidiano escolar.

O conjunto de dados utilizado neste estudo reúne informações demográficas, acadêmicas, de estilo de vida e de histórico familiar que podem auxiliar na compreensão das condições que influenciam o desenvolvimento da depressão em estudantes. No entanto, a grande quantidade e a diversidade de variáveis tornam difícil para professores, psicólogos e gestores escolares interpretarem de forma clara quais fatores exercem maior impacto sobre a saúde mental.

Dessa forma, o problema central desta investigação é: como analisar, de forma sistemática, os fatores presentes nos dados para identificar tendências, padrões e preditores relacionados à depressão entre estudantes, possibilitando uma compreensão mais profunda desse fenômeno e contribuindo para estratégias de prevenção e intervenção precoce? 

O contexto de aplicação envolve o uso deste dataset em pesquisas acadêmicas e projetos em ciência de dados, com potencial para apoiar tanto a formulação de políticas institucionais voltadas ao cuidado da saúde mental quanto o desenvolvimento de ferramentas que auxiliem profissionais da educação e da psicologia no acompanhamento de estudantes em risco.

## Questão de pesquisa

Quais fatores acadêmicos, demográficos, de estilo de vida e histórico familiar mais influenciam a ocorrência de depressão entre estudantes, e de que forma a análise desse conjunto de dados pode auxiliar na identificação precoce de alunos em risco? 

## Objetivos preliminares

Nesta seção, você deve apresentar os objetivos preliminares do trabalho, deixando claro que o objetivo geral é experimentar modelos de aprendizado de máquina adequados para solucionar o problema descrito anteriormente.

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
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)

## Justificativa

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
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)

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

Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
