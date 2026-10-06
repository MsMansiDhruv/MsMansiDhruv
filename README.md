# Mansi Dhruv

**Lead Data Engineer · Solution Architect**

I build and modernize data platforms, with a focus on **distributed processing, cloud architecture, performance, and reliable data systems**.

My day-to-day work spans AWS, Databricks, Apache Spark, PySpark, SQL, streaming, ETL/ELT, Terraform, CI/CD, and production ML integration.

I'm currently going deeper into **Spark internals, distributed systems, query execution, and performance engineering** — with a longer-term interest in GPU-accelerated data systems.

[Portfolio](https://portfolio-mansi-eight.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/mansidhruv/) · [Email](mailto:mansi.p.dhruv@gmail.com)

---

## What I work on

**Data platforms**  
Apache Spark · PySpark · Databricks · Delta Lake · SQL · ETL/ELT · Streaming

**Cloud & infrastructure**  
AWS · S3 · Glue · Redshift · Lambda · ECS · EC2 · API Gateway · DMS · Athena · Terraform · Docker · CI/CD

**Engineering**  
Python · Scala · FastAPI · GraphQL · Kafka · Kinesis · Airflow · GitHub Actions

**ML / analytics**  
MLflow · production ML pipeline integration · Power BI · Tableau

---

## Selected work

### [Sentinel Lakehouse](https://github.com/MsMansiDhruv/sentinel-lakehouse)

**Production-oriented Databricks lakehouse**

A deliberately imperfect commerce data platform designed to explore the problems that appear after a pipeline works: schema evolution, malformed records, data quality, quarantine, CDC, incremental processing, dimensional modeling, observability, CI/CD, governance, and performance.

The project includes reproducible engineering decisions and measured trade-offs rather than presenting one architecture as universally correct.

**Databricks · Apache Spark · Delta Lake · Lakeflow · Auto Loader · CDC · Unity Catalog · Python · pytest · GitHub Actions**

→ [Read the engineering work](https://github.com/MsMansiDhruv/sentinel-lakehouse)

---

### [Engineering Portfolio](https://portfolio-mansi-eight.vercel.app/)

My portfolio documents systems, architecture decisions, experiments, and technical work across data engineering and cloud infrastructure.

→ [View portfolio](https://portfolio-mansi-eight.vercel.app/) · [Source](https://github.com/MsMansiDhruv/portfolio_mansi)

---

## Engineering direction

I'm interested in the layer underneath data platforms:

```
Data Engineering
      ↓
Distributed Processing
      ↓
Query Execution
      ↓
Performance Engineering
      ↓
Parallel Computing
      ↓
Accelerated Data Systems
```

The questions I'm currently exploring:

- Where is a distributed workload actually spending its time?
- What causes unnecessary data movement and shuffle?
- How do partitioning and join strategies change execution?
- How do memory, storage, and serialization affect performance?
- When does scaling compute help — and when does it simply cost more?
- What changes when analytical workloads move toward heterogeneous CPU/GPU systems?

---

## What I'm building next

### Spark Performance Lab
Benchmark-driven experiments around partitioning, joins, shuffle, skew, AQE, caching, predicate pushdown, and execution plans.

### Query Engine Lab
A small query-processing engine to understand the path from:

`SQL → Logical Plan → Optimization → Physical Plan → Execution`

### Distributed Systems Experiments
Small, reproducible experiments around partitioning, replication, consistency, fault tolerance, and data movement.

### GPU Data Processing
Later-stage experiments comparing CPU and GPU execution for analytical workloads, including the cost of data transfer and the point at which acceleration becomes worthwhile.

These are intentionally **evidence-first projects**: experiments, measurements, code, failures, and conclusions — not certificate projects.

---

## Selected production outcomes

In professional work, I've worked on:

- modernizing legacy ETL into AWS lakehouse architecture
- reducing an end-to-end pipeline by ~40% while reducing infrastructure cost by ~30%
- productionizing ML-driven data workflows
- automating web-intelligence pipelines and reducing manual monitoring by ~50%
- reducing data-processing time by ~45% on an enterprise pipeline
- diagnosing and redesigning slow SQL paths with ~85% improvement on the affected workload

Client implementations are confidential, so the public repositories here use synthetic or independently reproducible systems to document the engineering principles.

---

## Open source

I'm building toward deeper contributions in the **Apache / CNCF / cloud-native / data systems** ecosystem.

Current areas of interest:

**Apache Spark · Airflow · MLflow · Delta Lake · Kubernetes · Kubeflow · RAPIDS**

The goal is not to accumulate contribution counts. I want to contribute where I can understand the problem, reproduce it, and add something maintainers can actually use.

---

## Current learning

- Spark internals
- Distributed query execution
- Performance profiling
- Data structures & algorithms
- System design
- Memory, storage & I/O
- C/C++
- Parallel computing
- CUDA fundamentals
- RAPIDS / cuDF

---

## Let's build things that can be measured.

If you're working on **data systems, distributed computing, cloud architecture, Spark performance, or accelerated data processing**, I'd be interested in comparing approaches and sharing experiments.

