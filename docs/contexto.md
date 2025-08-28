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

## Estado da arte

Nesta seção, descreva abordagens da literatura que tratam problemas semelhantes ao seu. Seu objetivo é documentar métodos, dados, métricas e resultados.

### O que levantar (mínimo 5 trabalhos)
Para **cada estudo encontrado** aderente à temática do grupo, registre de forma objetiva:
* Problema e contexto: que problema o trabalho buscou resolver e em qual domínio/cenário foi aplicado.
* Dados (dataset): origem, tamanho, período, variáveis/atributos, pré-processamentos relevantes (faltantes, balanceamento, normalização).
* Abordagem/algoritmos: algoritmos utilizados e parâmetros principais (quando informados).
* Métricas de avaliação: quais e por quê (ex.: Acurácia, F1, AUC, RMSE, MAE, etc.).
* Resultados: principais números, comparações internas, limitações citadas e conclusões.

* Texto-síntese crítico (2–4 parágrafos) respondendo:
- O que os estudos concordam? Onde divergem?
- Quais lacunas permanecem (dados, métricas, cenários, limitações técnicas/éticas)?
- Como seu projeto se alinha aos estudos identificados?

**Dica:** Prefira artigos dos últimos 5 anos ou referências clássicas indispensáveis.

### Ferramentas inteligentes permitidas
Você pode utilizar: Perplexity, SciSpace, Elicit, Research Rabbit, Litmaps.
Use-as para descoberta, organização e triagem de literatura. 

**Atenção:** 
* Sempre acesse a fonte original (PDF/artigo) antes de citar; verifique números e conclusões.
* Registre DOI/URL oficial e dados bibliográficos completos.
* Evite “alucinações” das ferramentas: desconfie de referências sem DOI ou que você não consiga localizar oficialmente.
* Use as ferramentas inteligentes para mapear redes de citação (Research Rabbit), mapas de tópicos (Litmaps), filtrar por período e gerar resumos iniciais (Perplexity/SciSpace/Elicit).
* Leia os trabalhos mais promissores e descarte estudos fora de escopo.

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do _dataset_ selecionado

Nesta seção, apresente uma visão clara e objetiva do dataset selecionado, incluindo:
* Identificação e origem – Nome, link de acesso, fonte (instituição, repositório, API etc.) e licença de uso.
* Visão geral – Total de registros e atributos, período coberto e breve contextualização.
* Atributos – Tabela com nome, descrição, tipo, unidade de medida (se aplicável) e exemplos de valores.
* Qualidade dos dados – Presença de valores faltantes, inconsistências, duplicatas ou outliers.

**Dica:** Seja objetivo, mas inclua detalhes suficientes para que outra pessoa possa entender e reutilizar o conjunto de dados sem buscar informações extras.

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
