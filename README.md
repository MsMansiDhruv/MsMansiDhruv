<div align="center">

<img src="./assets/architect-hero.svg" alt="Mansi Dhruv — Lead Data Engineer & Solution Architect" width="100%" />

<p align="center">
  <em><strong>"Less hype. More engineering."</strong></em>
</p>

<p align="center">
  <a href="https://portfolio-mansi-eight.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-mansidhruv.com-0EA5A4?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  &nbsp;
  <a href="https://portfolio-mansi-eight.vercel.app/projects"><img src="https://img.shields.io/badge/Case_Studies-Architecture-161B22?style=flat-square&logo=readthedocs&logoColor=0EA5A4" alt="Case Studies" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/"><img src="https://img.shields.io/badge/LinkedIn-mansidhruv-161B22?style=flat-square&logo=linkedin&logoColor=0EA5A4" alt="LinkedIn" /></a>
  &nbsp;
  <a href="https://glama.ai/mcp/servers/MsMansiDhruv/dlt-doctor"><img src="https://img.shields.io/badge/Glama_MCP-Grade_A_(100%25)-2EE6A7?style=flat-square&logo=anthropic&logoColor=white" alt="Glama MCP Grade A" /></a>
  &nbsp;
  <a href="https://pypi.org/project/dlt-doctor/"><img src="https://img.shields.io/badge/PyPI-dlt--doctor-0EA5A4?style=flat-square&logo=pypi&logoColor=white" alt="PyPI dlt-doctor" /></a>
  &nbsp;
  <a href="https://github.com/MsMansiDhruv?tab=achievements"><img src="https://img.shields.io/badge/GitHub-YOLO-FF4500?style=flat-square&logo=github&logoColor=white" alt="GitHub YOLO" /></a>
  &nbsp;
  <a href="mailto:mansi.p.dhruv@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-161B22?style=flat-square&logo=gmail&logoColor=0EA5A4" alt="Email" /></a>
</p>

</div>

---

### About Me

<img src="./assets/whoami.svg" alt="3D System Topography / Compute & Scale Surface wireframe" width="100%" />

I build and tune production data platforms across **Databricks, Apache Spark, Delta Lake, and AWS**.

Most data problems aren't solved by adding more tools—they're solved by understanding what the query engine is doing underneath the hood. Over 7+ years, my work has centered on the mechanics of scale: eliminating 100GB+ disk spills in Spark, catching silent data drops before they corrupt financial ledgers, pruning millions of unnecessary file scans with Liquid clustering, and cutting cloud compute waste.

When standard JVM runtimes hit their limits, I look at the execution primitives: vectorized execution, off-heap memory, and GPU kernel offload with **NVIDIA RAPIDS (cuDF)**. For the modern agentic tier, I build native **Model Context Protocol (MCP)** tools and semantic layers that give AI reasoning engines structured, reliable access to enterprise lakehouses without hallucinations.

---

### What I Focus On

<div align="center">

| Experience | Migration Scale | Open Source PRs | Ecosystem Rating |
| :---: | :---: | :---: | :---: |
| **7+ Years** Enterprise Platforms | **10+ TB** Financial Lakehouse | **7** Upstream Engine PRs | **Grade A (100%)** on Glama |

</div>

<br/>

| Engineering Focus | What I Solve in Production | Measured Result |
| :--- | :--- | :--- |
| **Spark & Memory Tuning** | Skew join resolution via AQE adaptive splitting, broadcast threshold tuning, off-heap allocation | Eliminated **100GB+ disk spills** and zero JVM GC pauses |
| **Lakehouse Architecture & I/O** | Medallion design (Bronze → Silver → Gold), Delta Lake Liquid clustering, Change Data Feed (CDF) | **24% I/O scan reduction** across high-cardinality analytical predicates |
| **Cloud Migrations & Streaming** | Automated metadata-driven AWS Glue & DMS pipelines from legacy SQL Server to Redshift, Terraform IaC | **10+ TB financial data** migrated with **40% lower OPEX** and zero loss |
| **Hardware Acceleration** | Columnar vectorized query execution, memory-mapped buffers, SIMD GPU offload with NVIDIA RAPIDS (cuDF) | Replaced heavy JVM iteration loops with parallel GPU kernel execution |
| **Agentic AI & Lakehouse MCP** | Offline AST static code analysis (`dlt-doctor`), Unity Catalog semantic harnesses, Model Context Protocol | Production AI agents querying lakehouse tables with zero hallucinations |

---

### Production Benchmarks

<img src="./assets/benchmarks.svg" alt="Production Engineering Benchmarks and Measured Decisions" width="100%" />

- **I/O & Predictive File Pruning**: Liquid clustering reduced bytes scanned by **24%** across analytical predicates, measured against serverless cluster startup overheads.
- **Memory & Shuffle Optimization**: Mitigated high-cardinality skew via AQE dynamic partition splitting and adaptive broadcast switching, eliminating **100GB+ disk spills**.
- **Real-Time Stream Processing**: Engineered end-to-end streaming scoring with **40% latency acceleration** and **30% compute cost reduction** on Databricks Delta Live Tables.
- **Metadata-Driven Cloud Migration**: Automated migration of **10+ TB** financial data to AWS Redshift/Lakehouse with reproducible Terraform IaC and zero-loss observability.

---

### Under the Hood: Spark Internals & GPU Acceleration

<img src="./assets/systems-map.svg" alt="Distributed Spark Internals and Query Engine Execution Topology" width="100%" />

---

### Featured Projects

<table>
  <tr>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/dlt-doctor">dlt-doctor</a></h4>
      <p>
        <a href="https://pypi.org/project/dlt-doctor/"><img src="https://img.shields.io/pypi/v/dlt-doctor?color=0EA5A4&label=PyPI&style=flat-square" alt="PyPI" /></a>
        <a href="https://glama.ai/mcp/servers/MsMansiDhruv/dlt-doctor"><img src="https://img.shields.io/badge/Glama-Grade_A-2EE6A7?style=flat-square" alt="Glama MCP" /></a>
      </p>
      <p>Offline static AST analysis engine, optimizer, and native <strong>Model Context Protocol (MCP)</strong> server for Databricks Delta Live Tables, Lakeflow, and PySpark Catalyst plans.</p>
      <p><code>uvx dlt-doctor analyze .</code> · <code>MCP</code></p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/sentinel-lakehouse">Sentinel Lakehouse</a></h4>
      <p>
        <img src="https://img.shields.io/badge/Architecture-Medallion-0EA5A4?style=flat-square" alt="Medallion" />
        <img src="https://img.shields.io/badge/Databricks-Unity_Catalog-FF3621?style=flat-square" alt="Unity Catalog" />
      </p>
      <p>Production lakehouse featuring Auto Loader, Delta CDF, SCD1/SCD2, Great Expectations quarantine gates, offline SQLGlot AST eval, and <strong>AutoHeal-DE</strong> partition recovery.</p>
      <p><code>Databricks</code> · <code>Delta Lake</code> · <code>sqlglot</code></p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/gquery-engine-clone">GQuery Relational Engine</a></h4>
      <p>
        <img src="https://img.shields.io/badge/Execution-Vectorized-5EC8FF?style=flat-square" alt="Vectorized" />
        <img src="https://img.shields.io/badge/Memory-Columnar-2EE6A7?style=flat-square" alt="Columnar" />
      </p>
      <p>In-memory vectorized columnar query engine exploring contiguous <code>ColumnVector</code> chunks, <code>RecordBatch</code> iteration, bitmask filters, and pushdown optimizations.</p>
      <p><code>Columnar</code> · <code>Vectorized</code> · <code>C++ / Python</code></p>
    </td>
  </tr>
</table>

---

### Lakehouse AI & Agentic Systems

<img src="./assets/genai-compound-ui.svg" alt="Sentinel-GenAI Studio: Databricks Genie Semantic Harness & Autonomous Agentic Lakehouse UI Screenshot" width="100%" />

**Databricks Genie AI/BI · Mosaic AI Vector Search · Autonomous Observability · Compound Query Routing**

- **Genie-Bench (Semantic Harness)**: Generates Unity Catalog annotations, join graphs, and a validated **Trusted SQL Catalog** to prevent metric hallucinations when business users query lakehouses.
- **AutoHeal-DE (Automated Observability & RCA)**: Scans live Delta transaction logs to detect late-arriving partitions, isolates affected date ranges, and writes surgical partition-pruned Delta `MERGE` statements without expensive full-table recomputations.
- **Hybrid Compound Router**: Blends structured Databricks SQL queries with unstructured Mosaic AI Vector Search using Reciprocal Rank Fusion (RRF k=60), backed by strict numerical consistency checks.

---

### Upstream Open Source PRs

<!-- OSS_PRS:START -->
| Engine / Repository | Pull Request | Technical Scope | Status |
| :--- | :---: | :--- | :--- |
| **punkpeye/awesome-mcp-servers** | [#20359](https://github.com/punkpeye/awesome-mcp-servers/pull/20359) | Add MsMansiDhruv/dlt-doctor to Data Platforms 🤖🤖🤖 | Open (In Review) · 2026-11-27 |
| **NVIDIA/cudf-spark** | [#16881](https://github.com/NVIDIA/cudf-spark/pull/16881) | Fix multithreaded read when maxNumFilesParallel is below task file count [r... | Open (In Review) · 2026-11-27 |
| **delta-io/delta-rs** | [#5126](https://github.com/delta-io/delta-rs/pull/5126) | feat(merge): use exact source keys to prune streamed MERGE scans (#5120) | Open (In Review) · 2026-11-27 |
| **NVIDIA/cudf-spark** | [#16939](https://github.com/NVIDIA/cudf-spark/pull/16939) | Support aggregate formatting in driverless broadcast metric assertion [redu... | Open (In Review) · 2026-11-26 |
| **databricks/dbt-databricks** | [#1758](https://github.com/databricks/dbt-databricks/pull/1758) | fix: escape relation string literals in metadata queries (#1747) | Open (In Review) · 2026-11-22 |
| **databricks/dbt-databricks** | [#1787](https://github.com/databricks/dbt-databricks/pull/1787) | feat: support databricks_tags and liquid clustering for seeds (#1783) | Open (In Review) · 2026-11-22 |
| **apache/iceberg-python** | [#4265](https://github.com/apache/iceberg-python/pull/4265) | Fix: assert ref snapshot id requirements during snapshot expiration (#4200) | Open (In Review) · 2026-11-21 |
| **ibis-project/ibis** | [#12214](https://github.com/ibis-project/ibis/pull/12214) | fix(postgres): read query schema without temporary view DDL for read-only s... | Open (In Review) · 2026-11-16 |
<!-- OSS_PRS:END -->

---

### Case Studies & Architecture Notes

<!-- ARCH_NOTES:START -->
- **[Legacy Data Modernization](https://portfolio-mansi-eight.vercel.app/projects/project-amc-datalake-solution)** (`2025-03`) — Cloud-native lake, Glue ETL, and Redshift analytics
- **[Productionizing an ML-Driven Allocation Engine](https://portfolio-mansi-eight.vercel.app/projects/brain-mvp)** (`2025-02`) — End-to-end ML allocation — eligibility, classification, and production serving on AWS
- **[Automated Web Intelligence Pipeline](https://portfolio-mansi-eight.vercel.app/projects/automated-intelligence-pipeline)** (`2025-01`) — Crawlers, extraction, deduplication, and DS model integration on AWS
- **[From OLAP to Workload-Specific Architecture](https://portfolio-mansi-eight.vercel.app/projects/olap-workload-architecture)** (`2024-12`) — Production migration — Redshift cost signal, engine benchmarks, workload separation
<!-- ARCH_NOTES:END -->

---

### Certifications & Awards

<p>
  <a href="https://academy.claude.com/verify/8322df364fb4d1f0609198a5e7823602"><img src="https://img.shields.io/badge/Anthropic-MCP:_Advanced_Topics_(Oct_2026)-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic MCP Advanced Topics" /></a>
  &nbsp;
  <a href="https://academy.claude.com/verify/0d63295bdb3096e5c2e1141d55d645cc"><img src="https://img.shields.io/badge/Anthropic-Intro_to_MCP_(Oct_2026)-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic Intro to MCP" /></a>
  &nbsp;
  <a href="https://credentials.databricks.com/f5bffd1a-99c8-4fd6-bb44-8f36255e6c39"><img src="https://img.shields.io/badge/Databricks-Genie_Code_Foundations_(Nov_2026)-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks Genie Code Foundations" /></a>
  &nbsp;
  <a href="https://credentials.databricks.com/0743a9e5-302b-4ba1-ba56-8b536f0957d8"><img src="https://img.shields.io/badge/Databricks-Genie_One_%26_Agents_(Nov_2026)-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks Genie One & Agents" /></a>
  &nbsp;
  <a href="https://credentials.databricks.com/e7b0c79e-fd02-452c-972f-c8e5a66b9fed"><img src="https://img.shields.io/badge/Databricks-Spark_Declarative_Pipeline_(Jun_2026)-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks Spark Declarative Pipeline" /></a>
  &nbsp;
  <a href="https://credentials.databricks.com/43bfffd4-8e37-4d58-afe1-0a79250a4906"><img src="https://img.shields.io/badge/Databricks-Performance_Optimization_(Jun_2026)-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks Performance Optimization" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/overlay/Certifications/1626116210/treasury/?profileId=ACoAABZywEoB0TXDu6A5bImQpa8-QAw0aa-GDMg"><img src="https://img.shields.io/badge/NASA-Open_Science_Essentials_(Nov_2026)-0B3D91?style=flat-square&logo=nasa&logoColor=white" alt="NASA Open Science Essentials" /></a>
  &nbsp;
  <a href="https://aw.certmetrics.com/amazon/en/public/verification.aspx"><img src="https://img.shields.io/badge/AWS_Certified-Cloud_Practitioner_(CLF)-FF9900?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS Certified" /></a>
</p>

<p>
  <a href="https://github.com/MsMansiDhruv?tab=achievements"><img src="https://img.shields.io/badge/GitHub_Achievement-YOLO-FF4500?style=flat-square&logo=github&logoColor=white" alt="GitHub YOLO" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/details/honors-awards/"><img src="https://img.shields.io/badge/SG_Analytics-Value--able_Award_(2024)-161B22?style=flat-square&logo=award&logoColor=FF9B4A" alt="Value-able Award" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/details/honors-awards/"><img src="https://img.shields.io/badge/SG_Analytics-GEM_Leadership_Award_(2023)-161B22?style=flat-square&logo=award&logoColor=2EE6A7" alt="GEM Award" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/details/honors-awards/"><img src="https://img.shields.io/badge/GHCI--18-Grace_Hopper_Scholar-161B22?style=flat-square&logo=star&logoColor=5EC8FF" alt="GHCI Scholar" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/details/honors-awards/"><img src="https://img.shields.io/badge/ACM--W-Innovative_Project_Mention-161B22?style=flat-square" alt="ACM-W Mention" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/details/honors-awards/"><img src="https://img.shields.io/badge/AESICS-MCA_Merit_Scholarship-161B22?style=flat-square&logo=graduationcap&logoColor=0EA5A4" alt="MCA Merit Scholar" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-a6a6cbcf-d2b6-4b93-925e-0bcf1e777205/"><img src="https://img.shields.io/badge/SQL_for_Data_Analysis_%26_Science-Udemy_2024-161B22?style=flat-square&logo=postgresql&logoColor=0EA5A4" alt="SQL for Data Analysis" /></a>
  &nbsp;
  <img src="https://img.shields.io/badge/Azure_Databricks_ETL-Pluralsight_2022-161B22?style=flat-square&logo=databricks&logoColor=2EE6A7" alt="Azure Databricks ETL" />
  &nbsp;
  <img src="https://img.shields.io/badge/PySpark_Data_Analysis-Pluralsight_2022-161B22?style=flat-square&logo=apachespark&logoColor=FF9B4A" alt="PySpark for Data Analysis" />
  &nbsp;
  <img src="https://img.shields.io/badge/Big_Data_Analytics_Spark-edX_2021-161B22?style=flat-square&logo=edx&logoColor=5EC8FF" alt="Big Data Analytics using Spark" />
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-d2d52e37-7982-400c-b78b-4a8833641cf9/"><img src="https://img.shields.io/badge/Data_Structures_Python-Udemy_2021-161B22?style=flat-square&logo=python&logoColor=2EE6A7" alt="Data Structures with Python" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-98742817-dfc1-415d-be88-c70c692ff871/"><img src="https://img.shields.io/badge/ML_Using_Python-Udemy_2020-161B22?style=flat-square&logo=scikitlearn&logoColor=2EE6A7" alt="Machine Learning Using Python" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-88749a3a-c8ea-4b5a-8b80-b0323a3dddc7/"><img src="https://img.shields.io/badge/Django_2.2-Udemy_2020-161B22?style=flat-square&logo=django&logoColor=8B949E" alt="Django 2.2" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-XNDH2JI1/"><img src="https://img.shields.io/badge/Docker_Essentials-Udemy_2019-161B22?style=flat-square&logo=docker&logoColor=5EC8FF" alt="Docker Essentials" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-SCQBZAAK/"><img src="https://img.shields.io/badge/Node.js-Udemy_2018-161B22?style=flat-square&logo=nodedotjs&logoColor=8B949E" alt="Node JS" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-X0AU2IFK/"><img src="https://img.shields.io/badge/Big_Data_Training-Udemy_2018-161B22?style=flat-square&logo=apachehadoop&logoColor=5EC8FF" alt="Big Data Training" /></a>
  &nbsp;
  <a href="https://www.udemy.com/certificate/UC-SWD4RAR8/"><img src="https://img.shields.io/badge/AI_Website_Creation-Udemy_2018-161B22?style=flat-square&logo=openai&logoColor=8B949E" alt="AI Website Creation" /></a>
</p>

---

### Tech Stack

<p align="center">
  <img src="https://cdn.simpleicons.org/python/2EE6A7" height="28" alt="Python" />
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/aws.svg" height="28" alt="AWS" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/databricks/2EE6A7" height="28" alt="Databricks" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apachespark/FF9B4A" height="28" alt="Apache Spark" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/terraform/2EE6A7" height="28" alt="Terraform" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/docker/FF9B4A" height="28" alt="Docker" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apacheairflow/2EE6A7" height="28" alt="Apache Airflow" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apachekafka/FF9B4A" height="28" alt="Apache Kafka" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/postgresql/2EE6A7" height="28" alt="PostgreSQL" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/duckdb/FFF000" height="28" alt="DuckDB" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/cplusplus/2EE6A7" height="28" alt="C++" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/nvidia/76B900" height="28" alt="NVIDIA RAPIDS" />
</p>

<div align="center">
  <sub>Data Platforms · Distributed Query Engines · Performance Architecture &nbsp;·&nbsp; <a href="https://portfolio-mansi-eight.vercel.app/">portfolio-mansi-eight.vercel.app</a></sub>
</div>
