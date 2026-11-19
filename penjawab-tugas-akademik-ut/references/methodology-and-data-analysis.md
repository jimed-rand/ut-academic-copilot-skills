# Research Methodology, Literature Synthesis, Measurement, Data Analysis & Ethics Reference Guide

Consolidated reference manual integrating **Research Methodology**, **Literature Review**, **Measurement & Instrument Design**, **Data Analysis**, **Results & Discussion Architecture**, **Ethics Checker**, and **Abstract Writer**, aligned with Universitas Terbuka's *Metodologi Penelitian* curriculum (`STSI4310` / `MSIM4312`, `ISIP4216`, `ADPU4441`, `EKMA4313`, `IDIK4007`, `TAP`, and `Karil`) as well as cross-faculty and international academic standards.

---

## Contents

1. [Research Foundations, Problem Formulation, Research Questions & Hypotheses](#1-research-foundations-problem-formulation-research-questions--hypotheses)
2. [Originality (Novelty), Literature Synthesis, Research Gaps & Theoretical Framework](#2-originality-novelty-literature-synthesis-research-gaps--theoretical-framework)
3. [Quantitative, Qualitative & Mixed-Methods Research Designs](#3-quantitative-qualitative--mixed-methods-research-designs)
4. [Measurement Levels, Scaling, Questionnaire Design, Validity & Reliability](#4-measurement-levels-scaling-questionnaire-design-validity--reliability)
5. [Population, Sampling Strategies & Sample Size Justification](#5-population-sampling-strategies--sample-size-justification)
6. [Data Analysis Decision Tree, Parametric Assumptions, Effect Sizes & APA Reporting](#6-data-analysis-decision-tree-parametric-assumptions-effect-sizes--apa-reporting)
7. [Qualitative Analysis Frameworks & Lincoln-Guba Trustworthiness](#7-qualitative-analysis-frameworks--lincoln-guba-trustworthiness)
8. [Results, Discussion (Pyramid/Reverse Funnel), Limitations & Conclusions](#8-results-discussion-pyramidreverse-funnel-limitations--conclusions)
9. [Research Ethics, Informed Consent & UU PDP No. 27 Tahun 2022 Compliance](#9-research-ethics-informed-consent--uu-pdp-no-27-tahun-2022-compliance)
10. [IMRAD Abstract & Keyword Construction Guide](#10-imrad-abstract--keyword-construction-guide)

---

## 1. Research Foundations, Problem Formulation, Research Questions & Hypotheses

### A. Core Distinctions: Methodology vs. Method vs. Technique
- **Metodologi Penelitian (*Research Methodology*)**: The systematic science and logical framework explaining *how* and *why* research is conducted scientifically (steps + underlying rationale).
- **Metode Penelitian (*Research Method*)**: The overarching strategies/approaches selected to conduct research (e.g., survey, case study, experiment), grouped into three operational families: (1) data collection methods, (2) statistical/analytical techniques linking data to unknowns, and (3) methods for evaluating accuracy of results.
- **Teknik Penelitian (*Research Technique*)**: Concrete operational behaviors and instruments used to execute a method (e.g., online questionnaire, audio-recorded unstructured interview, packet capture).

### B. Paradigm Alignment Matrix
| Paradigm | Ontological & Epistemological Stance | Primary Approach | Typical Designs & Canonical References |
|---|---|---|---|
| **Positivism / Post-Positivism** | Objective reality measurable via operational indicators; probabilistic falsification | Quantitative | True/Quasi-Experiment (Shadish et al., 2002), Survey & Correlational (Creswell & Creswell, 2018) |
| **Interpretivism / Constructivism** | Socially & technically constructed meaning within bounded institutional contexts | Qualitative | Case Study (Robert K. Yin, 2018), Phenomenology (Moustakas, 1994), Ethnography (Geertz, 1973), Grounded Theory (Charmaz, 2014) |
| **Pragmatism** | Problem-centered (*problem-driven*) integration of objective metrics and contextual meanings | Mixed Methods | Convergent Parallel, Explanatory Sequential, Exploratory Sequential, Multilevel (Creswell & Plano Clark, 2018) |
| **Critical / Transformative** | Structural power asymmetries, digital sovereignty, emancipation, action | Qualitative / PAR | Participatory Action Research (Kemmis & McTaggart, 2014), Critical Discourse Analysis (Fairclough, 2013) |

### C. Research Purpose Taxonomy & Problem Distinction
- **Four Classical Research Purposes**: (1) **Exploratory / Formulative** (*eksploratif*) — gaining new insights into an under-studied phenomenon; (2) **Descriptive** (*deskriptif*) — accurately portraying characteristics of individuals, groups, or situations; (3) **Diagnostic** (*diagnostik*) — determining the frequency or association of an occurrence; (4) **Hypothesis-Testing** (*pengujian hipotesis*) — testing causal relationships between variables.
- **Never Conflate Three Terms**:
  - **Topik Penelitian (*Research Topic*)**: Broad subject area of interest.
  - **Masalah Penelitian (*Research Problem*)**: Specific empirical issue, contradiction, or knowledge gap — either **Practical** (improving operational processes/minimizing organizational risk) or **Theoretical** (expanding scientific knowledge and resolving literature gaps).
  - **Pertanyaan Penelitian (*Research Question*)**: Focused, operationalized interrogative statement narrowing the problem into answerable analytical units.
- **Four Problem-Formulation Pitfalls to AVOID (BMP UT)**:
  1. Purely for **self-enlightenment** (*pencerahan diri sendiri*) without broader scholarly or practical contribution.
  2. Merely **comparing two datasets** without a theoretical or empirical problem rationale.
  3. Merely **computing a correlation coefficient** between two sets of numbers without explanatory framing.
  4. Questions answerable with a **bare "yes" or "no"** (*ya/tidak*).

### D. FINER Criteria & Four Categories of Quantitative Research Questions
Every research question in **Bab I (Subbab 1.2)** must satisfy **FINER**: **F**easible, **I**nteresting, **N**ovel, **E**thical, **R**elevant, and avoid asking vague opinions or unanswerable "why" questions lacking empirical anchors.

| Category | Core Goal | Typical Indonesian / English Openers | Variable Structure |
|---|---|---|---|
| **1. Deskriptif** | Describe distribution, frequency, or level of data | *Berapa banyak/sering/persen/proporsi...?*, *Apa yang...?* | 1 variable + target subject group |
| **2. Komparatif** | Compare $\ge 2$ groups on 1+ dependent variable(s) | *Apa yang berbeda pada...?*, *Apakah terdapat perbedaan [Y] antara kelompok A dan B?* | $\ge 2$ subject groups + 1+ dependent variable (continuous or categorical) |
| **3. Relasional** | Assess strength and direction of association between variables | *Bagaimana relasi antara [X] dan [Y]?* | $\ge 2$ variables (no strict IV/DV distinction; dichotomous, ordinal, or continuous) |
| **4. Sebab-Akibat / Prediktif** | Test causal effect or predictive power of IV(s) on DV | *Bagaimana pengaruh [X] terhadap [Y]?*, *Apakah [X1, X2] memprediksi [Y]?* | Independent variable(s) (*peubah bebas*) $\rightarrow$ Dependent variable (*peubah tak bebas*) |

> **1-to-1 Alignment Rule (Mandatory in UT Rubrics)**: If **1.2 Rumusan Masalah** has $k$ numbered questions (`1..k`), then **1.3 Tujuan Penelitian** MUST have $k$ matching numbered objectives (`1..k`) — fulfilling the 5 functions of research objectives (setting study focus, identifying variables, guiding steps, bounding scope, and preventing unnecessary data collection) — and **Bab III** must operationalize every single question.

### E. Hypothesis Taxonomy & Quality Rules (Quantitative / Experimental)
- **Four Categories (1-to-1 with Research Questions)**:
  1. **Hipotesis Deskriptif**: Educated claim about the value of a single variable (no comparison/association).
  2. **Hipotesis Komparatif**: Compares the value of the same measure across two or more distinct sample groups.
  3. **Hipotesis Relasional**: States a correlation/association between two variables.
  4. **Hipotesis Sebab-Akibat / Prediktif**: States a directional/causal effect from independent variable (*peubah bebas*) to dependent variable (*peubah tak bebas*), often structured as an *"jika–maka"* (*if–then*) proposition.
- **Two Non-Negotiable Quality Tests**:
  1. **Testable (*Dapat Diuji*)**: Observable empirical evidence can be collected to test its validity within a realistic timeframe.
  2. **Falsifiable (*Dapat Disalahkan*)**: Empirical evidence can potentially refute/disprove the statement.
- **Six Drafting Rules**: Write as a **declarative statement** (*kalimat berita*, never a question); explicitly state the expected variable relationship; ground it directly in the literature review and theory; keep it concise and specific (split multi-variable hypotheses into focused pairs); ensure consistency with established facts; choose precise operational wording.

---

## 2. Originality (Novelty), Literature Synthesis, Research Gaps & Theoretical Framework

### A. Proving Research Originality (*Keaslian Penelitian / Novelty*)
Originality demonstrates (1) how the study differs from prior works, (2) its exact position in the literature, and (3) its specific contribution. Two primary strategies establish originality:
1. Investigating an **old/established problem** using a **new method/approach**, demonstrating methodological and theoretical implications.
2. Investigating a **new/emerging problem** using an **established method**, demonstrating methodological and theoretical implications.
- **Warning Against the "Object-Swap Trap"**: Merely moving an identical method from Organization A to Organization B (e.g., building the same type of information system at Hospital B instead of Hospital A using the same SDLC method) **does not automatically constitute novelty**. Conversely, studying the same object/domain with a rigorously justified alternative method or theoretical lens *does* establish genuine novelty.
- **Modified Fishbone (Ishikawa) Diagram for Originality**: Can be used to map prior studies and unresolved problem dimensions on the "bones" (*duri* = causes/existing gaps) converging toward the "head" (*kepala ikan* = the proposed study's novelty/core focus).

### B. Universitas Terbuka Minimum Reference Quota & 5-Criteria Source Evaluation
Unless a specific Tuton prompt specifies otherwise, satisfy or exceed the standard UT benchmark:
- **$\ge 5$ International Peer-Reviewed Journal Articles** (Scopus / WoS / IEEE / ACM / DOAJ, with verifiable DOIs).
- **$\ge 5$ National Accredited Journal Articles (SINTA 1–4)** published within the **last 5–10 years**.
- **$\ge 5$ Academic Reference Books / Textbooks / Standards** (plus foundational theoretical classics such as Leedy & Ormord, 2015; Robert K. Yin, 2018; W. B. Arthur, 1989 when theoretically required).

Evaluate every candidate source against **5 Credibility Criteria** (UT BMP / CRAAP):
1. **Kekinian (*Currency*)**: Up-to-date findings/editions relevant to current state of the art.
2. **Relevansi (*Relevance*)**: Direct topical and analytical alignment with the research problem.
3. **Otoritas (*Authority*)**: Credible author qualifications and peer-reviewed publisher/institution (prefer journals, proceedings, theses/dissertations, and official standards over newspapers/popular magazines).
4. **Akurasi (*Accuracy*)**: Verifiable origin of data and adequate empirical evidence.
5. **Tujuan (*Purpose*)**: Clear scholarly intent (objective inquiry rather than commercial or partisan bias).

### C. Literature Review Organization & Synthesis Architecture
Never write Bab II as a disconnected laundry list (*"Penelitian pertama dilakukan oleh X..."*). Structure it as an analytical essay (**Introduction** [topic, rationale, organizational order, inclusion/exclusion scope] $\rightarrow$ **Main Body** $\rightarrow$ **Synthesis Conclusion**) using one of three organizational approaches:
- **Kronologis**: Tracing the historical evolution of a concept, technology, or policy.
- **Tematik**: Grouping studies by recurring themes, variables, or mechanisms (recommended default).
- **Metodologis**: Comparing how different research designs or analytical techniques yield divergent findings.

During synthesis, explicitly extract **5 analytical elements**: *kecenderungan* (trends in theory/methods/results), *tema* (recurring concepts), *debat/konflik/kontradiksi* (disagreements across studies), *publikasi utama* (seminal works), and *kesenjangan* (gaps), complemented by a **Tabel Matriks Penelitian Terdahulu** (`No. | Peneliti (Tahun) & Judul | Metode & Unit Analisis | Temuan Utama | Celah Penelitian / Posisi Studi Ini`).

### D. The 5 Canonical Research Gap Categories (BMP UT + Domain Extensions)
Explicitly name at least two of the following gap types at the close of **Bab II**:
1. **Kesenjangan Bukti (*Evidence Gap*)**: Contradictory findings across prior studies or insufficient empirical proof for a widely assumed claim.
2. **Kesenjangan Metodologi (*Methodological Gap*)**: Limitations in prior research designs, instruments, or analytical techniques (e.g., relying solely on lab benchmarks without field interviews, or cross-sectional surveys without longitudinal validation).
3. **Kesenjangan Empiris (*Empirical Gap*)**: Theoretical claims, frameworks, or new technologies/regulations that have not yet been empirically tested or verified in real-world practice (including *geographical/regulatory* and *temporal* shifts such as post-2022 `UU No. 27 Tahun 2022` enforcement).
4. **Kesenjangan Teoretis (*Theoretical Gap*)**: Phenomenon examined purely descriptively or technically without integrating explanatory theoretical frameworks.
5. **Kesenjangan Populasi (*Population Gap*)**: Under-researched populations, organizational types, or demographic segments (e.g., Indonesian regional public agencies, SMEs, or decentralized communities).

### E. Theoretical Framework (*Landasan Teori*) — 5 Drafting Rules
A **theory** (Leedy & Ormord, 2015) is an organized set of concepts and principles extensively tested and broadly accepted to explain a phenomenon—distinct from a **hypothesis** (an untested educated guess). When writing *Landasan Teori*:
1. Clearly specify the exact framework, concept, model, or theory supporting the study.
2. Position the chosen theoretical framework within the broader landscape of related theories.
3. State enduring theoretical principles in the **present tense** (when writing in English) or general-truth declarative form (in Indonesian).
4. Articulate all **theoretical assumptions** as explicitly as possible and map them directly to research variables/indicators.
5. Acknowledge that any theory remains **tentative/falsifiable** and may be refined or refuted by new empirical evidence.

---

## 3. Quantitative, Qualitative & Mixed-Methods Research Designs

### A. Quantitative Designs (Non-Experimental vs. Experimental)
| Family & Design | Core Structure | When to Use | Key Validity Controls |
|---|---|---|---|
| **Non-Exp: Deskriptif** (*Survey / Observational*) | Structured measurement of current conditions without variable manipulation | Portraying profiles, frequencies, perceptions, or behaviors | Validated scales, representative sampling |
| **Non-Exp: Korelasional** (*Explanatory / Predictive*) | Measuring natural co-variation between $\ge 2$ variables across groups | Explaining natural associations (*eksplanatori*) or predicting outcomes from known predictors (*prediktif*) | Common-method bias control, Cronbach's $\alpha \ge .70$ |
| **Non-Exp: Kausal-Komparatif** (*Ex Post Facto*) | Comparing pre-existing groups after a condition has already occurred | Exploring plausible causes of group differences when manipulation is impossible (note: cannot prove strict causality) | Controlling confounding variables, careful causal hedging |
| **Exp: True Experimental** | **Random selection + Random assignment** to treatment vs. control groups ($R \rightarrow O_1 \rightarrow X \rightarrow O_2$) | Testing direct causal effects of an intervention | Randomization, blinding, baseline equivalence |
| **Exp: Quasi-Experimental** | Manipulation with comparison groups **without full random assignment** ($O_1 \rightarrow X \rightarrow O_2$ vs. $O_1 \rightarrow O_2$) | Field settings (classes, agencies) where random assignment is infeasible | Pre-test covariate adjustment (ANCOVA), matching (Shadish et al., 2002) |
| **Longitudinal / Panel** | Repeated measurements across $T$ time periods | Tracking dynamic trajectories, policy impacts, or panel econometrics | Fixed/random effects, attrition diagnostics |

### B. Qualitative Designs & Data Collection Techniques
Qualitative research pursues one or more of four goals: **Deskriptif**, **Interpretasi**, **Verifikasi**, and **Evaluasi**.

| Design | Core Focus | Sample / Unit Guideline | Canonical Reference |
|---|---|---|---|
| **Studi Kasus (*Case Study*)** | Deep empirical investigation of a contemporary phenomenon within its real-world bounded context (*single/multiple, holistic/embedded*) | 1–4 cases with embedded sub-units + 4–10 key informants (*purposive*) | Robert K. Yin (2018); Stake (1995) |
| **Penelitian Tindakan (*Action Research / PTK*)** | Iterative cycle of inquiry, intervention, and learning aimed at solving a practical/organizational change problem | 1–2 bounded sites/classes across $\ge 2$ action cycles | Kemmis & McTaggart (2014) |
| **Fenomenologi (*Phenomenology*)** | Lived subjective experiences (*lived experience*) of actors facing a phenomenon | 5–15 informants with direct experience | Moustakas (1994); Creswell & Poth (2018) |
| **Etnografi (*Ethnography*)** | Cultural norms, practices, and socio-technical routines via prolonged immersion | Long-term field immersion + participant observation + interviews | Geertz (1973); Hammersley & Atkinson (2019) |
| **Grounded Theory** | Inductive construction of a theoretical model derived systematically from field data | 20–30 informants via theoretical sampling until saturation | Charmaz (2014); Corbin & Strauss (2015) |
| **Analisis Konten (*Content Analysis*)** | Detailed, systematic examination of texts, documents, media, or digital artifacts to identify patterns/themes | Structured corpus of documents/logs/media with coding protocol | Krippendorff (2018) |

- **8 Qualitative Data Collection Techniques**: (1) Direct observation (*pengamatan langsung*, non-participant), (2) Open-ended survey (*survei terbuka*), (3) Focus group (*kelompok fokus*, typically **5–15 participants**), (4) In-depth interview (*wawancara mendalam*, 1-on-1 with structured guide), (5) Historical records/oral history (*catatan sejarah*), (6) Participant observation (*pengamatan partisipan*), (7) Ethnographic observation (*pengamatan etnografi*, long-term immersion), (8) Content analysis (*analisis konten* on documents, digital media, logs).

### C. Qualitative vs. Quantitative Quick Comparison (8 Dimensions)
| Dimension | Qualitative (*Kualitatif*) | Quantitative (*Kuantitatif*) |
|---|---|---|
| **Approach** | Inductive (*induktif*) | Deductive (*deduktif*) |
| **Goal** | Deep local meaning; hypothesis generation | Broad generalization; hypothesis testing |
| **Design** | Non-experimental | Non-experimental, true experimental, quasi-experimental |
| **Setting** | Naturalistic field (*lapangan/alam*) | Field or controlled laboratory |
| **Data Collection** | Narrative collection (documents, interviews, FGD, observation) | Structured instruments (questionnaires, closed-ended tests, sensors) |
| **Sampling** | Purposive / intentional (*non-probabilistik*) | Probabilistic / random |
| **Data Type** | Descriptive (words, notes, audio, video) — narrow but rich | Numeric (nominal, ordinal, interval, ratio) — broad but lean |
| **Analysis** | Iterative interpretation to uncover meaning | Statistical tests, mathematical/computational models |

### D. Mixed-Methods Designs (*Metode Campuran*)
- **Core Notation**: `KUAL` / `QUAL` (qualitative data/methods) and `KUAN` / `QUAN` (quantitative data/methods).
- **Four Designs**:
  1. **Convergent Parallel (`QUAN + QUAL`)**: Collect quantitative and qualitative data simultaneously; merge and compare for triangulation.
  2. **Explanatory Sequential (`QUAN → qual`)**: Run quantitative phase first to identify patterns/outliers, then qualitative interviews to explain mechanisms.
  3. **Exploratory Sequential (`QUAL → quan`)**: Run qualitative fieldwork first to build constructs/instruments, then test quantitatively on a larger sample.
  4. **Multilevel (`Banyak-Aras`)**: Apply `KUAL` and `KUAN` across nested institutional tiers (e.g., individual student experiences [`KUAL`] + class exam scores [`KUAN`] + faculty graduation rates [`KUAN`] + institutional history [`KUAL`]).
- **4 Core Benefits**: Higher accuracy via triangulation, fuller picture answering both *how/why* and *how many*, compensating methodological weaknesses, and aiding sample selection.
- **5 Risks to Mitigate in Bab III**: Escalated time/cost, need for dual methodological competence, oversimplifying the `KUAL`–`KUAN` divide, misinterpreting pragmatism as "anything goes / *pokoknya ada hasil*", and handling divergent/contradictory findings between strands.

---

## 4. Measurement Levels, Scaling, Questionnaire Design, Validity & Reliability

### A. Proxy Variables & Four Levels of Measurement (*Aras Pengukuran*)
Abstract constructs (e.g., satisfaction, trust, digital awareness) are measured via observable **manifest/proxy variables (*peubah proksi*)**. Every quantitative variable must specify its exact measurement level:

| Level (*Aras*) | Properties | Example | Permissible Statistics |
|---|---|---|---|
| **1. Nominal** | Pure categorization; **mutually exclusive** labels; no order or magnitude | Occupation (`1=Pegawai, 2=Wirausaha`), jersey numbers, gender | Mode, frequency, percentage, Chi-Square ($\chi^2$) |
| **2. Ordinal** | Ordered/ranked categories along a continuum; intervals between ranks are **not** guaranteed equal | Rank (`1st, 2nd, 3rd`), Likert ratings, weight category (`kurus/sedang/gemuk`) | Median, mode, Spearman $\rho$, Mann-Whitney $U$, Kruskal-Wallis $H$ |
| **3. Interval** | Ordered + **equal distances** between adjacent values; **no true/absolute zero** | Temperature in Celsius/Fahrenheit, calendar years, IQ scores | Mean, SD, Pearson $r$, $t$-test, ANOVA, OLS Regression |
| **4. Rasio** | Ordered + equal intervals + **absolute zero** (zero means complete absence; ratios are meaningful) | Income (Rp), age, latency (ms), throughput (Mbps), count of transactions | All parametric & geometric/ratio statistics |

### B. Scaling (*Penskalaan*) & Questionnaire Design
- **Skala Likert (*Summative Rating Scale*)**: Non-comparative, unidimensional psychometric scale (typically 5-point ordinal: `1 = Sangat Tidak Setuju` to `5 = Sangat Setuju`, with `3 = Netral`) capturing agreement or preference.
- **Skala Guttman (*Cumulative Scale*)**: Unidimensional cumulative scale where agreeing with a higher-intensity item implies agreement with all lower-intensity items on the continuum.
- **Kodifikasi (*Coding* & *Precoding*)**: Assigning numeric codes to response categories prior to deployment (*precoding*) so survey data maps cleanly into statistical software.
- **Questionnaire Item Architecture**:
  - **Structured (Closed-Ended)** vs. **Unstructured (Open-Ended)** items.
  - **Dichotomous / Binary Questions**: Strictly two mutually exclusive choices (`Ya/Tidak`, `Benar/Salah`, `Setuju/Tidak Setuju`).
  - **Filter / Contingency Questions (*Pertanyaan Saringan*)**: Conditional screening items ensuring respondents only answer subsequent items relevant to their actual experience (e.g., asking *"Pernahkah Anda berbelanja daring?"* before asking about payment methods).
- **7-Point Questionnaire Content Audit** (verify every draft item before deployment):
  1. Is this question genuinely necessary for answering the research questions?
  2. Should a compound question be split into separate items?
  3. Does the respondent actually possess the requested information?
  4. Does the item need to be more specific?
  5. Is the item sufficiently general/accessible without jargon?
  6. Is the wording free from leading/loaded bias?
  7. Will respondents be willing and able to answer honestly?

### C. Instrument Validity & Reliability (Quantitative)
- **4 Types of Validity** (*sejauh mana instrumen mengukur apa yang seharusnya diukur*):
  1. **Face Validity**: Subjective surface-level judgment that items appear to measure the intended construct.
  2. **Content Validity (*Validitas Konten*)**: Degree to which items form a representative sample of the target domain (often verified via expert judgment / *CVI*).
  3. **Criterion Validity (*Validitas Kriteria*)**: Correlation of instrument scores with an established external benchmark/criterion instrument (concurrent or predictive).
  4. **Construct Validity (*Validitas Konstruk*)**: Degree to which the instrument accurately measures an unobservable theoretical construct (verified via convergent/discriminant validity, factor analysis / AVE).
- **4 Ways to Assess Reliability** (*konsistensi hasil pengukuran ketika objek tidak berubah*):
  1. **Inter-Rater Reliability**: Consistency across $\ge 2$ independent evaluators/coders (e.g., Cohen's $\kappa$, ICC).
  2. **Test-Retest Reliability**: Stability of scores from the same respondents across two timepoints.
  3. **Equivalent Form Reliability**: Consistency between two parallel/equivalent versions of the same instrument.
  4. **Internal Consistency Reliability**: Homogeneity across items measuring the same construct (e.g., **Cronbach's $\alpha \ge .70$**, Composite Reliability).

---

## 5. Population, Sampling Strategies & Sample Size Justification

### A. Sampling Strategies
| Approach | Sampling Strategy | Selection Logic & Mandatory Bab III Justification |
|---|---|---|
| **Quantitative (Probability)** | **Simple Random**, **Stratified Random** (by strata), **Cluster Sampling** (geographic/institutional groups such as *kelurahan/sekolah*), **Systematic Sampling** (every $k$-th unit) | Every population unit has a known non-zero probability of selection; required for statistical generalization. |
| **Large-Population Multi-Stage Area Sampling** | **5-Stage Area Sampling**: (1) *Area utama* (kecamatan/metro) $\rightarrow$ (2) *Sampel lokasi* (kelurahan) $\rightarrow$ (3) *Chunk* (bounded geographic sub-area) $\rightarrow$ (4) *Segmen* (RT) $\rightarrow$ (5) *Rumah tinggal* | Used when a complete sampling frame of a massive national/regional population is unavailable; random selection is applied at each hierarchical stage. |
| **Non-Probability (Quantitative / Qualitative)** | **Convenience / Accidental** (readily available), **Quota** (non-random matching of population proportions), **Purposive / Judgmental** (explicit inclusion criteria), **Maximum Variation**, **Snowball**, **Theoretical Sampling** | For qualitative studies, specify explicit **inclusion criteria** (e.g., $\ge 3$ years operating production systems, policy authority), exact informant codes (`IK-01` s.d. `IK-05`), roles, and data saturation (*kejenuhan data*) criteria. |

### B. Sample Size Justification Benchmarks
Justify quantitative sample size using an explicit canonical rule:
1. **Gay, Mills, & Airasian (2012) Rule of Thumb** (cited in UT BMP):
   - Population $N \le 100$: **Census** (survey the entire population; sampling is unnecessary).
   - Population $N \approx 500$: Sample **50%** ($\approx 250$).
   - Population $N \approx 1{,}500$: Sample **20%** ($\approx 300$).
   - Population $N \ge 5{,}000$: Population size becomes largely irrelevant; a sample size of **$n = 400$** is adequate.
2. **Central Limit Theorem (CLT)**: Minimum sample size **$n \ge 30$** for sampling distribution of the mean to approximate normality.
3. **Slovin Formula**: $n = \frac{N}{1 + N e^2}$ (for known finite population $N$ and margin of error $e$, e.g., $0.05$).
4. **Statistical Power / SEM-PLS**: **G\*Power** ($1-\beta = .80, \alpha = .05$), **Krejcie & Morgan (1970)** table, or **Hair et al. (2019)** ($10\times$ maximum structural arrowheads/indicators for SEM-PLS).

---

## 6. Data Analysis Decision Tree, Parametric Assumptions, Effect Sizes & APA Reporting

### A. Descriptive vs. Inferential Statistics & Parametric Assumptions
- **Statistika Deskriptif** (focuses on summarizing raw data):
  - *Ukuran Pusat Kecenderungan (Central Tendency)*: **Mean** (*rerata*), **Median** (*nilai tengah* — requires ascending sort), **Mode** (*modus*).
  - *Ukuran Variabilitas*: **Simpang rerata** (mean absolute deviation) and **Simpang baku** (*standard deviation*, preferred for describing dispersion; identical means with different SDs require explicit interpretation).
  - *Nilai Standar (Standard Score / $Z$-score)*: Standardizes observations to compare across distributions with different scales/means.
- **Statistika Inferensial** (requires representative random sample): Two core functions — (1) **Estimating population parameters** from sample statistics, and (2) **Statistical hypothesis testing** (significance testing). Grounded in the **Central Limit Theorem**: (a) means of infinite random samples form a normal distribution, (b) the mean of sample means equals the population mean ($\mu$), and (c) the standard error of the mean relates directly to the population SD.
- **Two Mandatory Assumptions for Parametric Tests**:
  1. Data are measured at the **Interval or Ratio** level.
  2. Data follow a **Normal Distribution** (peaked in the center, with **skewness** and **kurtosis** within acceptable bounds). If violated (or data are ordinal/skewed), switch to the non-parametric equivalent below.

### B. Quantitative Statistical Test Selection Matrix
| Research Goal | Variable Types | Parametric Test (Normal, Interval/Ratio) | Non-Parametric Equivalent (Skewed / Ordinal) |
|---|---|---|---|
| Compare 2 independent groups | IV: 2 groups; DV: Continuous | **Independent Samples $t$-test** | **Mann-Whitney $U$ test** |
| Compare 2 paired/pre-post measurements | IV: Time/Condition (2); DV: Continuous | **Paired Samples $t$-test** | **Wilcoxon Signed-Rank test** |
| Compare $\ge 3$ independent groups | IV: $\ge 3$ groups; DV: Continuous | **One-Way ANOVA** (+ Tukey HSD post-hoc) | **Kruskal-Wallis $H$ test** |
| Compare $\ge 3$ repeated measures | IV: $\ge 3$ timepoints; DV: Continuous | **Repeated Measures ANOVA** | **Friedman test** |
| Association between 2 continuous vars | 2 Continuous variables | **Pearson Correlation ($r$)** | **Spearman's Rho ($\rho$)** |
| Association between 2 categorical vars | 2 Categorical variables | — | **Chi-Square Test of Independence ($\chi^2$)** / Fisher's Exact |
| Predict continuous DV from multiple IVs | Continuous DV; $\ge 2$ IVs | **Multiple Linear Regression (OLS)** | **Quantile / Robust Regression** |
| Predict binary DV ($0/1$) | Binary DV; $\ge 1$ IVs | **Binary Logistic Regression** (Odds Ratio) | — |

### C. Effect Size & Reliability Threshold Benchmarks
| Metric | Small / Acceptable | Medium / Good | Large / Excellent | Application |
|---|---|---|---|---|
| **Cohen's $d$** | $0.20$ | $0.50$ | $0.80$ | Mean difference between two groups ($t$-test) |
| **Pearson $r$ / Spearman $\rho$** | $\pm 0.10$ | $\pm 0.30$ | $\pm 0.50$ | Bivariate linear/monotonic correlation |
| **Eta-squared ($\eta^2$)** | $0.01$ | $0.06$ | $0.14$ | Proportion of variance explained in ANOVA |
| **$R^2$ (Regression)** | $0.02$ (Weak) | $0.13$ (Moderate) | $0.26$ (Substantial) | Variance explained in linear regression (Cohen, 1988) |
| **Cronbach's $\alpha$ / Composite Reliability** | $\ge .70$ (Acceptable) | $\ge .80$ (Good) | $\ge .90$ (Excellent) | Internal consistency reliability of multi-item scales |

### D. APA 7th Statistical Reporting Templates
- **$t$-test**: *"Kelompok eksperimen memperoleh skor pascates yang lebih tinggi ($M = 78.50, SD = 5.20$) dibandingkan kelompok kontrol ($M = 72.10, SD = 6.80$), $t(118) = 5.79, p < .001, d = 1.06$."*
- **ANOVA**: *"Terdapat perbedaan signifikan antar ketiga topologi peladen, $F(2, 87) = 8.45, p < .001, \eta^2 = .16$."*
- **Correlation**: *"Konsumsi memori berbanding lurus dengan jumlah koneksi konkurensi, $r(98) = .64, p < .001$."*
- **Regression**: *"Model regresi memprediksi 42% varians kepatuhan keamanan data, $R^2 = .42, F(3, 96) = 23.15, p < .001$; otonomi infrastruktur berpengaruh positif signifikan ($\beta = .38, t = 4.12, p < .001$)."*

---

## 7. Qualitative Analysis Frameworks & Lincoln-Guba Trustworthiness

### A. Core Nature & Three Canonical Qualitative Analysis Procedures
Qualitative data analysis is inherently **iterative** (collection and analysis co-evolve concurrently), **inductive** (moving from specific field observations to broader patterns/themes), and **researcher-centered** (requiring explicit reflexivity regarding researcher subjectivity).

1. **Miles, Huberman, & Saldaña (2014) Interactive Model**:
   - **Data Condensation (*Kondensasi Data*)**: Selecting, focusing, simplifying, abstracting, and transforming raw field transcripts, server logs, and archival documents using structured open/axial/selective coding (replacing the older term "data reduction").
   - **Data Display (*Penyajian Data*)**: Organizing compressed data into cross-case comparison matrices, architectural topology diagrams, and thematic networks.
   - **Conclusion Drawing & Verification (*Penarikan dan Verifikasi Simpulan*)**: Testing patterns against rival explanations (*pattern matching* and *explanation building*; Robert K. Yin, 2018) and verifying through triangulation.
2. **Braun & Clarke (2006, 2022) 6-Phase Thematic Analysis**:
   - (1) Familiarization with data $\rightarrow$ (2) Generating initial codes $\rightarrow$ (3) Searching for themes $\rightarrow$ (4) Reviewing themes $\rightarrow$ (5) Defining and naming themes $\rightarrow$ (6) Producing the scholarly report.
3. **Krippendorff (2018) Content & Archival Analysis**:
   - Unitizing, sampling, recording/coding legal statutes (`UU No. 27 Tahun 2022`, `PP No. 71 Tahun 2019`) and technical specifications (`IETF RFC`, `XEP`), assessing inter-coder reliability (Cohen's $\kappa \ge .80$ or Krippendorff's $\alpha \ge .80$).

### B. Lincoln & Guba (1985) Four Trustworthiness Criteria (*Keabsahan Data*)
| Criterion | Quantitative Analog | Concrete Operational Procedure Required in Bab III |
|---|---|---|
| **1. Credibility (*Kredibilitas*)** | Internal Validity | **Triangulasi Sumber** (comparing distinct informant groups), **Triangulasi Teknik** (cross-checking interviews against live logs/documents and observation), **Triangulasi Waktu**, and **Member Checking** (having informants verify their interview transcripts). |
| **2. Transferability (*Transferabilitas*)** | External Validity | **Thick Description (*Uraian Rinci*)** of the organizational architecture, operational constraints, and socio-technical setting so readers can assess applicability to analogous contexts. |
| **3. Dependability (*Dependabilitas*)** | Reliability | Maintaining a complete **Audit Trail (*Jejak Audit*)** of interview protocols, raw anonymized transcripts, coding books, and timestamped observation logs for independent methodological audit. |
| **4. Confirmability (*Konfirmabilitas*)** | Objectivity | Explicit researcher reflexivity and linking every conclusion directly to verifiable informant quote codes (`[IK-01]`, `[IK-02]`) and archival/technical artifacts. |

---

## 8. Results, Discussion (Pyramid/Reverse Funnel), Limitations & Conclusions

### A. Bagian Hasil Penelitian (BHP / Results Section)
- **Two Presentation Patterns**: (a) Present all findings objectively first with brief factual statements (e.g., stating which hypotheses were rejected), deferring explanations to the Discussion section; OR (b) Alternate each finding subsection with brief contextual explanation (common in longer reports/theses).
- **5 Mandatory Elements of BHP**:
  1. Brief opening restating the research problem to orient the reader.
  2. Logical sequence of core findings aligned with the method (for surveys, **report instrument validity & reliability first**, followed by descriptive and inferential results).
  3. Non-textual visuals (tables, charts, diagrams, maps) strictly illustrating relevant findings.
  4. Focus exclusively on findings relevant to the research questions—omit extraneous raw dumps.
  5. Length proportional to data complexity, never padded.

### B. Bagian Diskusi (Discussion — Pyramid / 8-Part Reverse Funnel)
Organize the Discussion using a **pyramid / reverse-funnel flow** (specific findings $\rightarrow$ broader literature/theory $\rightarrow$ limitations $\rightarrow$ overarching implications), maintaining consistent terminology throughout:
1. **Summary of Core Findings**: Restate the research problem and directly answer every research question (`1..k`) without introducing new raw data.
2. **Explanation of Expected AND Unexpected Results**: Explain *why* patterns emerged—especially **unexpected findings, outliers, or rejected hypotheses** (*hipotesis yang ditolak*).
3. **Dialogue with Prior Literature**: Explicitly contrast findings against the key studies reviewed in Bab II (*Keaslian Penelitian / Kajian Pustaka*) to show corroboration, extension, or divergence.
4. **Theoretical Implications**: Specify how findings validate, refine, or bound the core theory, and propose testable claims for future studies.
5. **Practical Utilization (*Pemanfaatan Hasil*)**: Deliver actionable *lesson learned*, best practices, or policy/architectural recommendations.
6. **Methodological & Scope Limitations** (placed before the closing summary).
7. **Future Research Directions**: Concrete extensions directly addressing the stated limitations.
8. **Closing Takeaway**: Concise summary of the principal implications **regardless of statistical significance**.

### C. Research Limitations Taxonomy (3 Types & 7 Specific Sources)
Every proposal (Bab IV: *Batasan Penelitian*) and final report must honestly disclose procedural limitations and estimate their impact:
- **3 Macro Types**:
  1. **Keterbatasan Rancangan Penelitian**: Constrained accessible population or procedural limits (e.g., scarce specialist respondents).
  2. **Keterbatasan Dampak**: Narrow generalizability due to an overly specialized population or single-site focus.
  3. **Keterbatasan Data / Prosedur Statistika**: Small sample size or methodological constraints in statistical modeling (e.g., reliance on non-parametric tests).
- **7 Specific Limitation Sources**: (1) Ukuran sampel, (2) Profil sampel, (3) Pemilihan metode penelitian, (4) Proses pengumpulan data, (5) Akses ke sumber pustaka, (6) Umur data, (7) Perangkat pengambil data.

### D. Conclusions (*Kesimpulan*) & Recommendations (*Saran*)
- **Synthesis, Not Mere Repetition**: Conclusions synthesize key takeaways to show *why* the study matters—never merely copy-paste earlier results or restate the problem verbatim.
- **Two Standard Formats**: (1) **Bullet/numbered list** where each item directly answers one research question; OR (2) **Cohesive essay** (1–3 paragraphs) answering all research questions (including unexpected/rejected outcomes) backed by key statistics/facts.
- **Future Works / Saran**: Explicitly point to future research opportunities (either integrated into the closing conclusion if no separate *Saran* section exists, or in a dedicated *Saran* section linked directly to the study's limitations).

---

## 9. Research Ethics, Informed Consent & UU PDP No. 27 Tahun 2022 Compliance

Every research proposal (**Bab III**) and empirical manuscript must explicitly document:
1. **Informed Consent (*Persetujuan Setelah Penjelasan*)**: Informants receive a written explanation of the research objective, voluntary participation, right to withdraw at any stage without penalty, and permission for audio/log recording prior to data collection.
2. **Anonymization & Confidentiality (*Anonimisasi dan Kerahasiaan*)**: Replace all personal names, private IP addresses, cryptographic keys, and sensitive organizational identifiers with pseudonymous codes (`IK-01` s.d. `IK-05`, `Peladen-A`, `Peladen-B`).
3. **Statutory Data Protection Compliance**: Store raw transcripts and system logs in encrypted local storage compliant with **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (Pasal 16 dan Pasal 35)**.
4. **Ethical Academic Integrity & Citation Ethics**: Cite all borrowed ideas, theories, non-textual visuals/tables (with permission where required), non-common-knowledge facts, direct quotes (in quotation marks **with page numbers**), paraphrases (no quotation marks, page number optional), and personal communications (with permission). Verify 100% of citations against primary sources, declare original authorship on the signed **Surat Pernyataan Kejujuran Akademik**, and comply with Pertor UT No. 436/2025 & COPE/ICMJE standards.

---

## 10. IMRAD Abstract & Keyword Construction Guide

When an assignment, Karil (`Karya Ilmiah`), or journal submission requires an **Abstrak / Abstract** (`150–250 words`):
- **Sentence 1–2 (Background & Problem)**: State the empirical/regulatory problem and research gap concisely.
- **Sentence 3–4 (Purpose & Method)**: Name the exact research design (e.g., *studi kasus terpancang ganda* or *kuasi-eksperimen*), sample/informant size ($N$), data collection instruments, and analysis method (`Miles et al., 2014` or statistical test).
- **Sentence 5–7 (Key Findings / Expected Output)**: Report the specific empirical findings (with exact statistics $M, SD, t, p, d$ for completed quantitative studies, or core thematic/architectural findings for qualitative/proposal studies).
- **Sentence 8 (Implications)**: State the theoretical and practical contribution.
- **Keywords (*Kata Kunci*)**: Provide **3–5 specific terms** separated by commas or semicolons, combining the core phenomenon, technical/policy object, methodology, and regulatory context.
