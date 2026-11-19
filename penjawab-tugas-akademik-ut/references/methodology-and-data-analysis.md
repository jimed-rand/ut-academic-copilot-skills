# Research Methodology, Literature Synthesis, Data Analysis & Ethics Reference Guide

Consolidated reference manual integrating **Research Methodology**, **Literature Review**, **Data Analysis**, **Results Interpreter**, **Ethics Checker**, and **Abstract Writer**, tailored for Universitas Terbuka (`STSI4310`, `ISIP4216`, `ADPU4441`, `EKMA4313`, `IDIK4007`, `TAP`, and `Karil`) and international academic research.

---

## Contents

1. [Research Paradigms & FINER Question Design](#1-research-paradigms--finer-question-design)
2. [Literature Review Synthesis & 5-Type Research Gap Matrix](#2-literature-review-synthesis--5-type-research-gap-matrix)
3. [Quantitative, Qualitative & Mixed-Methods Research Designs](#3-quantitative-qualitative--mixed-methods-research-designs)
4. [Population, Sampling Strategies & Sample Size Justification](#4-population-sampling-strategies--sample-size-justification)
5. [Data Analysis Decision Tree, Effect Sizes & APA Statistical Reporting](#5-data-analysis-decision-tree-effect-sizes--apa-statistical-reporting)
6. [Qualitative Analysis Frameworks & Lincoln-Guba Trustworthiness](#6-qualitative-analysis-frameworks--lincoln-guba-trustworthiness)
7. [Results Interpretation & Discussion Architecture (8-Part Reverse Funnel)](#7-results-interpretation--discussion-architecture-8-part-reverse-funnel)
8. [Research Ethics, Informed Consent & UU PDP No. 27 Tahun 2022 Compliance](#8-research-ethics-informed-consent--uu-pdp-no-27-tahun-2022-compliance)
9. [IMRAD Abstract & Keyword Construction Guide](#9-imrad-abstract--keyword-construction-guide)

---

## 1. Research Paradigms & FINER Question Design

### A. Paradigm Alignment Matrix
| Paradigm | Ontological & Epistemological Stance | Primary Approach | Typical Designs & Canonical References |
|---|---|---|---|
| **Positivism / Post-Positivism** | Objective reality measurable via operational indicators; probabilistic falsification | Quantitative | True/Quasi-Experiment (Shadish et al., 2002), Survey & Correlational (Creswell & Creswell, 2018) |
| **Interpretivism / Constructivism** | Socially & technically constructed meaning within bounded institutional contexts | Qualitative | Case Study (Robert K. Yin, 2018), Phenomenology (Moustakas, 1994), Ethnography (Geertz, 1973), Grounded Theory (Charmaz, 2014) |
| **Pragmatism** | Problem-centered integration of objective metrics and contextual meanings | Mixed Methods | Convergent Parallel, Explanatory Sequential, Exploratory Sequential (Creswell & Plano Clark, 2018) |
| **Critical / Transformative** | Structural power asymmetries, digital sovereignty, emancipation, action | Qualitative / PAR | Participatory Action Research (Kemmis & McTaggart, 2014), Critical Discourse Analysis (Fairclough, 2013) |

### B. FINER Criteria for Research Questions (*Rumusan Masalah*)
Every research question in **Bab I (Subbab 1.2)** must satisfy:
- **F**easible: Achievable with observable empirical units, accessible informants/datasets, and realistic timeframe.
- **I**nteresting: Probes a non-trivial mechanism or institutional paradox.
- **N**ovel: Addresses an explicit empirical, methodological, or regulatory gap in prior literature.
- **E**thical: Complies with institutional ethics, informed consent, and UU No. 27 Tahun 2022 (UU PDP).
- **R**elevant: Generates actionable theoretical and policy/architectural contributions.

> **1-to-1 Alignment Rule (Mandatory in UT Rubrics)**: If **1.2 Rumusan Masalah** has $k$ numbered questions (`1..k`), then **1.3 Tujuan Penelitian** MUST have $k$ matching numbered objectives (`1..k`), and **Bab III (Instrumen & Teknik Analisis Data)** must operationalize every single question.

---

## 2. Literature Review Synthesis & 5-Type Research Gap Matrix

### A. Universitas Terbuka Minimum Reference Quota (Bab II — Tinjauan Pustaka)
Unless a specific Tuton prompt specifies otherwise, always satisfy or exceed the standard UT benchmark:
- **$\ge 5$ International Peer-Reviewed Journal Articles** (indexed in Scopus / Web of Science / IEEE / ACM / DOAJ, with verifiable DOIs).
- **$\ge 5$ National Accredited Journal Articles (SINTA 1–4)** published within the **last 10 years** (e.g., 2016–2026).
- **$\ge 5$ Academic Reference Books / Textbooks / Standards** published within the **last 10 years** (plus foundational theoretical classics such as W. B. Arthur, 1989 or Robert K. Yin, 2018 when theoretically required).

### B. Thematic Synthesis vs. Annotated-Bibliography Trap
Never write Bab II as a disconnected laundry list where each paragraph begins with *"Penelitian pertama dilakukan oleh X (2021)..."*, *"Penelitian kedua oleh Y (2022)..."*. Instead, synthesize by **theme, mechanism, or methodological tension**, and complement the prose with a **Tabel Matriks Penelitian Terdahulu** (`No. | Peneliti (Tahun) & Judul | Metode & Unit Analisis | Temuan Utama | Celah Penelitian / Posisi Studi Ini`).

### C. The 5-Type Research Gap Taxonomy
Explicitly identify at least two of the following five gap dimensions at the close of **Bab II**:
1. **Population / Unit-of-Analysis Gap**: Prior studies examined commercial cloud or Western enterprise settings, leaving Indonesian public agencies or decentralized technical communities unexamined.
2. **Geographical / Regulatory Gap**: Prior literature precedes or omits Indonesia's statutory framework (`UU No. 27 Tahun 2022`, `PP No. 71 Tahun 2019`, `Perpres No. 95 Tahun 2018`).
3. **Methodological / Architectural Gap**: Prior studies evaluated only a single protocol in laboratory isolation rather than a comparative, multi-unit embedded case study (*embedded multiple-case study*) combining protocol telemetry and operator interviews.
4. **Theoretical Gap**: Prior engineering studies focused purely on throughput/cryptography without integrating institutional *path dependence* (W. B. Arthur, 1989) and *digital sovereignty* (Couture & Toupin, 2019).
5. **Temporal Gap**: Recent protocol specifications (e.g., `XEP No. 0384` OMEMO v2, `RFC No. 7194` TLS on IRC) and post-2022 data protection enforcement have altered the empirical landscape.

---

## 3. Quantitative, Qualitative & Mixed-Methods Research Designs

### A. Quantitative Designs
| Design | Core Structure | When to Use | Key Validity Controls |
|---|---|---|---|
| **True Experimental** | Random assignment + manipulation + control group ($R \rightarrow O_1 \rightarrow X \rightarrow O_2$) | Testing direct causal effects of an intervention | Randomization, blinding, baseline equivalence |
| **Quasi-Experimental** | Non-random comparison groups with pre-test & post-test ($O_1 \rightarrow X \rightarrow O_2$ vs. $O_1 \rightarrow O_2$) | Field settings (classes, agencies) where random assignment is impossible | Pre-test covariate adjustment (ANCOVA), matching (Shadish et al., 2002) |
| **Cross-Sectional Survey / Correlational** | Single-timepoint structured measurement across $N$ respondents | Testing multivariable associations, SEM-PLS, or regression models | Validated scales, Cronbach's $\alpha \ge .70$, common-method bias control |
| **Longitudinal / Panel** | Repeated measurements across $T$ time periods | Tracking dynamic trajectories, policy impacts, or panel econometrics | Fixed/random effects, attrition diagnostics |

### B. Qualitative Designs
| Design | Core Focus | Sample / Unit Guideline | Canonical Methodological Reference |
|---|---|---|---|
| **Case Study (*Studi Kasus*)** | Deep investigation of a contemporary phenomenon within its real-world bounded context (*single/multiple, holistic/embedded*) | 1–4 cases with embedded sub-units + 4–10 key informants (*purposive*) | Robert K. Yin (2018); Stake (1995) |
| **Phenomenology (*Fenomenologi*)** | Lived subjective experiences (*lived experience*) of actors facing a phenomenon | 5–15 informants with direct experience | Moustakas (1994); Creswell & Poth (2018) |
| **Grounded Theory** | Inductive construction of an explanatory process theory from field data | 20–30 informants via theoretical sampling until saturation | Charmaz (2014); Corbin & Strauss (2015) |
| **Ethnography (*Etnografi*)** | Cultural norms, practices, and socio-technical rituals through prolonged immersion | Long-term field observation + informant interviews | Geertz (1973); Hammersley & Atkinson (2019) |

### C. Mixed-Methods Designs (Creswell & Plano Clark, 2018)
- **Convergent Parallel (`QUAN + QUAL`)**: Collect quantitative telemetry/survey and qualitative interview data simultaneously; merge and compare for triangulation.
- **Explanatory Sequential (`QUAN → qual`)**: Run quantitative phase first to identify statistically significant patterns or outliers, followed by qualitative interviews to explain the underlying mechanisms.
- **Exploratory Sequential (`QUAL → quan`)**: Conduct qualitative fieldwork first to build constructs/instruments, then validate them quantitatively on a larger sample.

---

## 4. Population, Sampling Strategies & Sample Size Justification

| Approach | Sampling Strategy | Selection Logic & Mandatory Bab III Justification |
|---|---|---|
| **Quantitative (Probability)** | *Simple Random, Stratified Random, Cluster Sampling* | Every population unit has a known non-zero probability; required for statistical generalization. Justify sample size via **G\*Power** power analysis ($1-\beta = .80, \alpha = .05$), **Krejcie & Morgan (1970)**, **Slovin formula** ($n = N / (1 + Ne^2)$), or **Hair et al. (2019)** ($10\times$ maximum arrowheads/indicators for SEM-PLS). |
| **Qualitative (Non-Probability)** | *Purposive (Judgmental), Maximum Variation, Snowball, Theoretical Sampling* | Informants are selected intentionally based on explicit **inclusion criteria** (e.g., $\ge 3$ years operating production servers, direct authority over infrastructure policy, active user representation). Specify exact informant codes (`IK-01` s.d. `IK-05`), roles, and data saturation (*kejenuhan data*) criteria. |

---

## 5. Data Analysis Decision Tree, Effect Sizes & APA Statistical Reporting

### A. Quantitative Statistical Test Selection Matrix
| Research Goal | Variable Types | Parametric Test (Normal Distribution) | Non-Parametric Equivalent (Skewed / Ordinal) |
|---|---|---|---|
| Compare 2 independent groups | IV: 2 groups; DV: Continuous | **Independent Samples $t$-test** | **Mann-Whitney $U$ test** |
| Compare 2 paired/pre-post measurements | IV: Time/Condition (2); DV: Continuous | **Paired Samples $t$-test** | **Wilcoxon Signed-Rank test** |
| Compare $\ge 3$ independent groups | IV: $\ge 3$ groups; DV: Continuous | **One-Way ANOVA** (+ Tukey HSD post-hoc) | **Kruskal-Wallis $H$ test** |
| Compare $\ge 3$ repeated measures | IV: $\ge 3$ timepoints; DV: Continuous | **Repeated Measures ANOVA** | **Friedman test** |
| Association between 2 continuous vars | 2 Continuous variables | **Pearson Correlation ($r$)** | **Spearman's Rho ($\rho$)** |
| Association between 2 categorical vars | 2 Categorical variables | — | **Chi-Square Test of Independence ($\chi^2$)** / Fisher's Exact |
| Predict continuous DV from multiple IVs | Continuous DV; $\ge 2$ IVs | **Multiple Linear Regression (OLS)** | **Quantile / Robust Regression** |
| Predict binary DV ($0/1$) | Binary DV; $\ge 1$ IVs | **Binary Logistic Regression** (Odds Ratio) | — |

### B. Effect Size & Reliability Threshold Benchmarks
| Metric | Small / Acceptable | Medium / Good | Large / Excellent | Application |
|---|---|---|---|---|
| **Cohen's $d$** | $0.20$ | $0.50$ | $0.80$ | Mean difference between two groups ($t$-test) |
| **Pearson $r$ / Spearman $\rho$** | $\pm 0.10$ | $\pm 0.30$ | $\pm 0.50$ | Bivariate linear/monotonic correlation |
| **Eta-squared ($\eta^2$)** | $0.01$ | $0.06$ | $0.14$ | Proportion of variance explained in ANOVA |
| **$R^2$ (Regression)** | $0.02$ (Weak) | $0.13$ (Moderate) | $0.26$ (Substantial) | Variance explained in linear regression (Cohen, 1988) |
| **Cronbach's $\alpha$ / Composite Reliability** | $\ge .70$ (Acceptable) | $\ge .80$ (Good) | $\ge .90$ (Excellent) | Internal consistency reliability of multi-item scales |

### C. APA 7th Statistical Reporting Templates
- **$t$-test**: *"Kelompok eksperimen memperoleh skor pascates yang lebih tinggi ($M = 78.50, SD = 5.20$) dibandingkan kelompok kontrol ($M = 72.10, SD = 6.80$), $t(118) = 5.79, p < .001, d = 1.06$."*
- **ANOVA**: *"Terdapat perbedaan signifikan antar ketiga topologi peladen, $F(2, 87) = 8.45, p < .001, \eta^2 = .16$."*
- **Correlation**: *"Konsumsi memori berbanding lurus dengan jumlah koneksi konkurensi, $r(98) = .64, p < .001$."*
- **Regression**: *"Model regresi memprediksi 42% varians kepatuhan keamanan data, $R^2 = .42, F(3, 96) = 23.15, p < .001$; otonomi infrastruktur berpengaruh positif signifikan ($\beta = .38, t = 4.12, p < .001$)."*

---

## 6. Qualitative Analysis Frameworks & Lincoln-Guba Trustworthiness

### A. Three Canonical Qualitative Analysis Procedures
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
| **1. Credibility (*Kredibilitas*)** | Internal Validity | **Triangulasi Sumber** (comparing system admins, security auditors, and end-users), **Triangulasi Teknik** (cross-checking interviews against live configuration logs/RFC audits and observation), **Triangulasi Waktu**, and **Member Checking** (having informants verify their interview transcripts). |
| **2. Transferability (*Transferabilitas*)** | External Validity | **Thick Description (*Uraian Rinci*)** of the organizational architecture, hardware/network constraints, and socio-technical setting so readers can assess applicability to analogous institutions. |
| **3. Dependability (*Dependabilitas*)** | Reliability | Maintaining a complete **Audit Trail (*Jejak Audit*)** of interview protocols, raw anonymized transcripts, coding books, and timestamped observation logs for independent methodological audit. |
| **4. Confirmability (*Konfirmabilitas*)** | Objectivity | Explicit researcher reflexivity and linking every conclusion directly to verifiable informant quote codes (`[IK-01]`, `[IK-02]`) and archival/technical artifacts. |

---

## 7. Results Interpretation & Discussion Architecture (8-Part Reverse Funnel)

When interpreting findings for Bab IV / Discussion sections (adapted from `results-interpreter`):
1. **Summary of Core Findings**: Restate the primary empirical results directly corresponding to each research question (`1..k`) without introducing new raw statistics.
2. **Mechanistic Interpretation**: Explain *why* the observed pattern emerged (e.g., why IRC's plaintext frame structure consumes $< 15\%$ of the RAM required by XML-stanza parsing in XMPP, whereas XMPP's `XEP No. 0384` provides native multi-device cryptographic federation).
3. **Dialogue with Prior Literature**: Explicitly contrast findings that corroborate (`sejalan dengan Ermoshina et al., 2016`), extend (`memperluas temuan Yokotani et al., 2025 ke konteks instansi daerah`), or diverge from prior studies.
4. **Theoretical Implications**: Specify how the findings validate, refine, or establish boundary conditions for the core theory (e.g., *path dependence* [W. B. Arthur, 1989] and *digital sovereignty* [Couture & Toupin, 2019]).
5. **Practical & Policy Implications**: Formulate concrete, actionable recommendations for system architects, public-sector IT leaders, or regulators enforcing `UU No. 27 Tahun 2022` and `Perpres No. 95 Tahun 2018`.
6. **Methodological & Scope Limitations**: State empirical boundaries honestly and without self-deprecation.
7. **Future Research Directions**: Propose specific longitudinal, experimental, or multi-site extensions grounded directly in the study's limitations.
8. **Conclusion**: Deliver a concise synthesis answering every research question.

---

## 8. Research Ethics, Informed Consent & UU PDP No. 27 Tahun 2022 Compliance

Every research proposal (**Bab III**) and empirical manuscript must explicitly document:
1. **Informed Consent (*Persetujuan Setelah Penjelasan*)**: Informants receive a written explanation of the research objective, voluntary participation, right to withdraw at any stage without penalty, and permission for audio/log recording prior to data collection.
2. **Anonymization & Confidentiality (*Anonimisasi dan Kerahasiaan*)**: Replace all personal names, private IP addresses, cryptographic keys, and sensitive organizational identifiers with pseudonymous codes (`IK-01` s.d. `IK-05`, `Peladen-A`, `Peladen-B`).
3. **Statutory Data Protection Compliance**: Store raw transcripts and system logs in encrypted local storage compliant with **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (Pasal 16 dan Pasal 35)**.
4. **Ethical Academic Integrity & AI Transparency**: Verify 100% of citations against primary sources (zero fabricated DOIs), declare original authorship on the signed **Surat Pernyataan Kejujuran Akademik**, and comply with COPE/ICMJE authorship standards.

---

## 9. IMRAD Abstract & Keyword Construction Guide

When an assignment, Karil (`Karya Ilmiah`), or journal submission requires an **Abstrak / Abstract** (`150–250 words`):
- **Sentence 1–2 (Background & Problem)**: State the empirical/regulatory problem and research gap concisely.
- **Sentence 3–4 (Purpose & Method)**: Name the exact research design (e.g., *studi kasus terpancang ganda / embedded multiple-case study* or *kuasi-eksperimen*), sample/informant size ($N$), data collection instruments, and analysis method (`Miles et al., 2014` or statistical test).
- **Sentence 5–7 (Key Findings / Expected Output)**: Report the specific empirical findings (with exact statistics $M, SD, t, p, d$ for completed quantitative studies, or core thematic/architectural findings for qualitative/proposal studies).
- **Sentence 8 (Implications)**: State the theoretical and practical contribution.
- **Keywords (*Kata Kunci*)**: Provide **3–5 specific terms** separated by commas or semicolons, combining the core phenomenon, technical/policy object, methodology, and regulatory context (e.g., *kedaulatan digital, protokol IRC, protokol XMPP, studi kasus terpancang, UU Pelindungan Data Pribadi*).
