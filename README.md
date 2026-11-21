<div align="center">

<img src="./assets/architect-hero.svg" alt="Mansi Dhruv — Lead Data Engineer & Solution Architect" width="100%" />

<br/>

<p align="center">
  <a href="https://portfolio-mansi-eight.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-mansidhruv.com-0EA5A4?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  &nbsp;
  <a href="https://portfolio-mansi-eight.vercel.app/projects"><img src="https://img.shields.io/badge/Case_Studies-Architecture-161B22?style=flat-square&logo=readthedocs&logoColor=0EA5A4" alt="Case Studies" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/mansidhruv/"><img src="https://img.shields.io/badge/LinkedIn-mansidhruv-161B22?style=flat-square&logo=linkedin&logoColor=0EA5A4" alt="LinkedIn" /></a>
  &nbsp;
  <a href="mailto:mansi.p.dhruv@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-161B22?style=flat-square&logo=gmail&logoColor=0EA5A4" alt="Email" /></a>
</p>

</div>

---

### Upstream Open Source & Engine Internals

<!-- OSS_PRS:START -->
| Engine / Repository | Pull Request | Technical Scope | Status |
| :--- | :---: | :--- | :--- |
| **databricks/dbt-databricks** | [#1787](https://github.com/databricks/dbt-databricks/pull/1787) | feat: support databricks_tags and liquid clustering for seeds (#1783) | Open (In Review) · 2026-11-21 |
| **databricks/dbt-databricks** | [#1786](https://github.com/databricks/dbt-databricks/pull/1786) | fix: preserve unconfigured row filters during table creation (#1782) | Closed · 2026-11-21 |
| **NVIDIA/cudf-spark** | [#16881](https://github.com/NVIDIA/cudf-spark/pull/16881) | Fix multithreaded read when maxNumFilesParallel is below task file count [r... | Open (In Review) · 2026-11-21 |
| **apache/iceberg-python** | [#4265](https://github.com/apache/iceberg-python/pull/4265) | Fix: assert ref snapshot id requirements during snapshot expiration (#4200) | Open (In Review) · 2026-11-21 |
| **NVIDIA/cudf-spark** | [#16938](https://github.com/NVIDIA/cudf-spark/pull/16938) | Implement TaskContext.addTaskPreCompletionListener in MockTaskContext [redu... | Open (In Review) · 2026-11-20 |
| **ibis-project/ibis** | [#12214](https://github.com/ibis-project/ibis/pull/12214) | fix(postgres): read query schema without temporary view DDL for read-only s... | Open (In Review) · 2026-11-16 |
| **delta-io/delta-rs** | [#5028](https://github.com/delta-io/delta-rs/pull/5028) | feat(python): support tuple filters in write, update, and delete predicates... | Open (In Review) · 2026-11-08 |
| **ibis-project/ibis** | [#12211](https://github.com/ibis-project/ibis/pull/12211) | fix(expr): type decimal mean as float64 and decimal product with combined s... | Open (In Review) · 2026-11-03 |
<!-- OSS_PRS:END -->

---

### Flagship Systems

<table>
  <tr>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/sentinel-lakehouse">Sentinel Lakehouse</a></h4>
      <p>Medallion Lakehouse on Databricks featuring Auto Loader, Delta CDF, SCD1/SCD2, Great Expectations quarantine gates, offline SQLGlot AST eval (~85ms), and AutoHeal-DE partition recovery.</p>
      <p><code>Databricks</code> · <code>Delta Lake</code> · <code>sqlglot</code></p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/gquery-engine-clone">GQuery Relational Engine</a></h4>
      <p>In-memory vectorized columnar query execution engine exploring contiguous <code>ColumnVector</code> chunks, <code>RecordBatch</code> iteration, bitmask filters, and rule-based pushdown.</p>
      <p><code>Columnar</code> · <code>Vectorized</code> · <code>Optimizer</code></p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/MsMansiDhruv/dlt-doctor">dlt-doctor</a></h4>
      <p>
        <a href="https://pypi.org/project/dlt-doctor/"><img src="https://img.shields.io/pypi/v/dlt-doctor?color=0EA5A4&label=PyPI&style=flat-square" alt="PyPI" /></a>
        <a href="https://pypi.org/project/dlt-doctor/"><img src="https://img.shields.io/pypi/dm/dlt-doctor?color=161B22&label=Downloads&style=flat-square" alt="PyPI Downloads" /></a>
      </p>
      <p>Open-source static AST optimizer, diagnostic engine, and built-in <strong>MCP server</strong> (<code>dlt-doctor mcp</code>) for Databricks DLT and PySpark Catalyst plans.</p>
      <p><code>pip install dlt-doctor</code> · <code>MCP</code></p>
    </td>
  </tr>
</table>

---

### Reference Lakehouse & AI Architecture

```mermaid
flowchart LR
    Ingest[Auto Loader / Kafka] --> Compute[Spark / RAPIDS GPU]
    Compute --> Gates{Quality & AST Gates}
    Gates -->|Valid| Storage[(Delta / Iceberg · Unity Catalog)]
    Gates -->|Quarantine| AutoHeal[AutoHeal-DE Partition Merge]
    Storage --> Serve[Databricks Genie / MCP Server]
```

---

### Recent Architecture Notes & Case Studies

<!-- ARCH_NOTES:START -->
- **[Legacy Data Modernization](https://portfolio-mansi-eight.vercel.app/projects/project-amc-datalake-solution)** (`2025-03`) — Cloud-native lake, Glue ETL, and Redshift analytics
- **[Productionizing an ML-Driven Allocation Engine](https://portfolio-mansi-eight.vercel.app/projects/brain-mvp)** (`2025-02`) — End-to-end ML allocation — eligibility, classification, and production serving on AWS
- **[Automated Web Intelligence Pipeline](https://portfolio-mansi-eight.vercel.app/projects/automated-intelligence-pipeline)** (`2025-01`) — Crawlers, extraction, deduplication, and DS model integration on AWS
- **[From OLAP to Workload-Specific Architecture](https://portfolio-mansi-eight.vercel.app/projects/olap-workload-architecture)** (`2024-12`) — Production migration — Redshift cost signal, engine benchmarks, workload separation
<!-- ARCH_NOTES:END -->

---

### Certifications, Credentials & Honors

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

<p align="center">
  <img src="https://cdn.simpleicons.org/python/2EE6A7" height="26" alt="Python" />
  &nbsp;&nbsp;
  <img src="./assets/aws.svg" height="26" alt="AWS" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/databricks/2EE6A7" height="26" alt="Databricks" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apachespark/FF9B4A" height="26" alt="Apache Spark" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/terraform/2EE6A7" height="26" alt="Terraform" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/docker/FF9B4A" height="26" alt="Docker" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apacheairflow/2EE6A7" height="26" alt="Apache Airflow" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/apachekafka/FF9B4A" height="26" alt="Apache Kafka" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/postgresql/2EE6A7" height="26" alt="PostgreSQL" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/cplusplus/2EE6A7" height="26" alt="C++" />
  &nbsp;&nbsp;
  <img src="https://cdn.simpleicons.org/nvidia/FF9B4A" height="26" alt="NVIDIA" />
</p>

<div align="center">
  <sub>Complexity → operability &nbsp;·&nbsp; <a href="https://portfolio-mansi-eight.vercel.app/">portfolio-mansi-eight.vercel.app</a></sub>
</div>
