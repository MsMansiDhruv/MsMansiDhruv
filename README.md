<div align="center">

<img src="./assets/profile-field.svg" alt="Mansi Dhruv custom GitHub profile visual" width="100%" />

<p><a href="https://portfolio-mansi-eight.vercel.app/">Portfolio</a> · <a href="https://www.linkedin.com/in/mansidhruv/">LinkedIn</a> · <a href="mailto:mansi.p.dhruv@gmail.com">Email</a></p>

</div>

---

## Who Am I

<img src="./assets/whoami.svg" alt="3D animated terrain surface plot of Mansi Dhruv's engineering focus" width="100%" />

I build production data systems across **AWS, Databricks, Spark, and PySpark**. My work sits between **platform engineering, distributed processing, and performance engineering** — from designing scalable pipelines to understanding what the engine is doing underneath them.

The longer arc is deliberate: **Data Platforms → Distributed Systems → Performance → Accelerated Data Systems**, with **semantic data and GenAI systems** becoming integral layers of the stack.

---

## Open Source & Engine Internals Contributions

Active contributions to core data engines, table formats, and query frameworks:

| Engine / Framework | Pull Request | Technical Focus & Scope | CI / Review Status |
| :--- | :--- | :--- | :--- |
| **NVIDIA cuDF Spark** | [#16688](https://github.com/NVIDIA/cudf-spark/pull/16688) | Spark Catalyst multi-digit patch versioning across build tooling, CI, and test matrices | Blossom CI Passed (30+ checks green), Greptile 5/5 |
| **NVIDIA cuDF Spark** | [#16715](https://github.com/NVIDIA/cudf-spark/pull/16715) | `GpuCreateDataSourceTableAsSelectCommand` table drop on `saveAsTable` overwrite (SPARK-60387) | Greptile 5/5, Signoff Passed, Upstream Synced |
| **Apache Iceberg** | [#4265](https://github.com/apache/iceberg-python/pull/4265) | Reference snapshot ID invariant validation during branch snapshot expiration (#4200) | 20/20 CI checks passed, in maintainer queue |
| **Ibis Project** | [#12211](https://github.com/ibis-project/ibis/pull/12211) | Decimal mean type promotion (`float64`) and product precision/scale calculation (#12209) | Semantic Release passed, DCO signed |
| **Databricks dbt** | [#1758](https://github.com/databricks/dbt-databricks/pull/1758) | Relation string literal escaping for metadata queries against catalogs and schemas (#1747) | 100% PR Test Coverage, 8/8 CI checks passed |

---

## Space-Time Trajectory Flux

<img src="./assets/space-time-network.svg" alt="Space-Time Trajectory Continuum and Execution Flux Network" width="100%" />

A live visual representation of **7+ years of production systems evolution**:
- **Foundations & Academic Core**: Master in Computer Applications (MCA), GEM Award for technical leadership, Python & SQL modeling.
- **Enterprise Cloud Migration**: Architected AWS framework (Glue, Redshift, DMS, S3) for financial datasets (Tata AMC) handling 10+ TB with 40% automation efficiency.
- **High-Throughput Streaming**: Databricks, PySpark, Delta Live Tables & Kafka/Kinesis real-time scoring (Acorns) delivering 40% pipeline time reduction and 30% compute cost savings.
- **Accelerated Frontier**: Advancing into Spark Catalyst optimization, off-heap Tungsten memory, and GPU kernel acceleration (NVIDIA CUDA & RAPIDS cuDF).

---

## Measured Systems Benchmarks & Trade-Offs

<img src="./assets/benchmarks.svg" alt="Production Engineering Benchmarks and Measured Decisions" width="100%" />

- **I/O & File Pruning**: Liquid clustering reduced bytes scanned by **24%** across analytical predicates, measured against serverless cluster startup overheads.
- **Memory & Shuffle Optimization**: Mitigated high-cardinality skew via AQE dynamic split and adaptive broadcast switching, eliminating **100GB+ disk spills**.
- **Real-Time Stream Processing**: Engineered end-to-end streaming scoring with **40% latency acceleration** and **30% compute cost reduction**.
- **Metadata-Driven Cloud Migration**: Automated migration of **10+ TB** financial data to Redshift with reproducible Terraform IaC and zero-loss observability.

---

## Distributed Engine & Query Execution Topology

<img src="./assets/systems-map.svg" alt="Distributed Spark Internals and Query Engine Execution Topology" width="100%" />

---

## Flagship Engineering: Sentinel Lakehouse & Compound GenAI Engine

<img src="./assets/sentinel-architecture.svg" alt="Animated Sentinel Lakehouse architecture" width="100%" />

**Incremental Ingestion · Data Quality · CDC · SCD1/SCD2 · Observability · Governance**

<a href="https://github.com/MsMansiDhruv/sentinel-lakehouse">Explore Sentinel Lakehouse Repository →</a>

---

## GenAI & AI/BI Architecture: Sentinel-GenAI Studio

<img src="./assets/genai-compound-ui.svg" alt="Sentinel-GenAI Studio: Databricks Genie Semantic Harness and Lakehouse Observability UI" width="100%" />

**Databricks Genie AI/BI · Mosaic AI Vector Search · Incident RCA · Compound Query Routing**

### Core Production Pillars:
- **Genie-Bench (Semantic Layer & Evaluation Harness)**: Semantic metadata compiler generating Unity Catalog table annotations, join graphs, and trusted SQL definitions with SQLGlot AST equivalence matching.
- **AutoHeal-DE (Pipeline Incident RCA & Healing)**: Live Delta commit log analyzer detecting late-arriving partitions, bounding historical window blast radii, and generating surgical partition-pruned Delta `MERGE` statements without expensive full-table backfills.
- **Hybrid Compound Router**: Fuses structured Databricks SQL aggregations with unstructured Mosaic AI Vector Search chunks via Reciprocal Rank Fusion (RRF k=60) with numerical consistency guardrails.

<a href="https://github.com/MsMansiDhruv/sentinel-lakehouse/blob/main/notebooks/14_sentinel_genai_hybrid_rag.ipynb">Explore Interactive Hybrid RAG & Genie Demo Notebook →</a>

---

## Systems Laboratories & Codebases

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/MsMansiDhruv/sentinel-lakehouse">Sentinel Lakehouse &amp; Sentinel-GenAI</a></h3>
      <p><strong>Flagship Production Architecture</strong></p>
      <p>Full Medallion Lakehouse engine on Databricks with Auto Loader incremental ingestion, Delta Change Data Feed (CDF), SCD Type 1 &amp; Type 2 dimensional models, automated Great Expectations quarantine dead-letter gates, Unity Catalog lineage, and the Sentinel-GenAI hybrid RAG engine.</p>
      <p><code>Databricks</code> · <code>Delta Lake</code> · <code>PySpark</code> · <code>Unity Catalog</code> · <code>Mosaic AI</code> · <code>pytest</code> · <code>CI/CD</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/MsMansiDhruv/dlt-doctor">dlt-doctor</a></h3>
      <p>
        <a href="https://pypi.org/project/dlt-doctor/"><img src="https://img.shields.io/pypi/v/dlt-doctor?color=3776AB&label=PyPI&logo=pypi&logoColor=white" alt="PyPI version" /></a>
        <a href="https://github.com/MsMansiDhruv/dlt-doctor/releases/tag/v0.4.0"><img src="https://img.shields.io/badge/Release-v0.4.0-10B981?logo=github&logoColor=white" alt="GitHub release" /></a>
        <a href="https://github.com/marketplace/actions/dlt-doctor"><img src="https://img.shields.io/badge/Action-Marketplace-blue?logo=githubactions&logoColor=white" alt="Marketplace" /></a>
      </p>
      <p><strong>Databricks DLT &amp; PySpark Optimization Engine</strong></p>
      <p>Open-source static AST optimizer and quality engine for Databricks. Features 11 diagnostic engines: Catalyst plan bloat auditing, zero-loss quarantine streams, bounded late-partition MERGE restatement, Unity Catalog migration, Liquid Clustering advisory, and DBU cost forecasting.</p>
      <p><code>pip install dlt-doctor</code> · <code>PySpark Catalyst</code> · <code>Delta Live Tables</code> · <code>Auto Loader</code> · <code>GitHub Action</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/MsMansiDhruv/gquery-engine-clone">Query Engine Laboratory</a></h3>
      <p><strong>Systems Internals &amp; Execution Exploration</strong></p>
      <p>A specialized technical laboratory exploring SQL query parsing, relational execution trees, vectorized columnar batch processing, predicate pushdown algorithms, and in-memory operator performance.</p>
      <p><code>Query Execution</code> · <code>Columnar Layout</code> · <code>Vectorized Kernels</code> · <code>Memory Planning</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/MsMansiDhruv/sentinel-lakehouse#autoheal-de">AutoHeal-DE: Lakehouse Pipeline Self-Healing</a></h3>
      <p><strong>Self-Healing Pipelines &amp; Incident RCA</strong></p>
      <p>Zero-scan Delta commit log monitor detecting late-arriving partitions, bounding rolling-window blast radii, and executing surgical partition-pruned Delta MERGE reconciliations without costly full-table restatements.</p>
      <p><code>Delta Lake CDF</code> · <code>Commit Log Inspection</code> · <code>AST Query Rewriter</code> · <code>Surgical Reconciler</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/MsMansiDhruv/sentinel-lakehouse#genie-bench">Genie-Bench: Semantic Layer &amp; Eval Harness</a></h3>
      <p><strong>Databricks AI/BI &amp; Genie Space Quality Gate</strong></p>
      <p>Automated semantic metadata compiler translating Unity Catalog tables, column metrics, and join graphs into Databricks Genie spaces with verified golden queries, SQLGlot AST validation, and automated scorecards.</p>
      <p><code>Databricks Genie</code> · <code>AI/BI Spaces</code> · <code>SQLGlot AST</code> · <code>Unity Catalog DDL</code> · <code>Scorecards</code></p>
    </td>
  </tr>
</table>

---

## Verified Credentials & Mastery

<img src="./assets/certifications.svg" alt="Verified Credentials and Certifications Radar" width="100%" />

---

## Systems Stack

<img src="./assets/stack.svg" alt="Simplified Core Production Toolchain" width="100%" />

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

---

## Vision / Let's Collaborate

I am interested in problems where **data, systems, performance, and intelligence** meet — especially **data platforms, Spark and query execution, performance experiments, semantic data, GenAI workflows, and GPU-accelerated data systems**.

<a href="mailto:mansi.p.dhruv@gmail.com">Let's build something worth measuring →</a>
