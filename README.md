<div align="center">

# MANSI DHRUV

### DATA SYSTEMS · DISTRIBUTED COMPUTING · PERFORMANCE

**Lead Data Engineer · Solutions Architect · Assistant Project Manager**

I build data systems — and I'm increasingly interested in what happens **underneath** them.

[![Portfolio](https://img.shields.io/badge/Portfolio-Explore_my_work-111111?style=flat-square&logo=vercel&logoColor=white)](https://portfolio-mansi-eight.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-MsMansiDhruv-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MsMansiDhruv)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mansidhruv/)
[![Email](https://img.shields.io/badge/Email-mansi.p.dhruv%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mansi.p.dhruv@gmail.com)

</div>

---

## Engineering Focus

```text
Data Engineering
      │
      ▼
Distributed Systems
      │
      ▼
Performance Engineering
      │
      ▼
Parallel Computing
      │
      ▼
GPU-Accelerated Data Systems
```

My work today spans **data engineering, solution architecture, cloud platforms, distributed processing, and technical delivery**. I'm particularly interested in the problems that appear when systems get bigger: **execution, data movement, memory, parallelism, reliability, performance, and cost**.

I'm currently going deeper into **distributed systems and performance engineering**, with a long-term focus on **GPU-accelerated data processing and high-performance data systems**.

> I don't want to just know how to run Spark. I want to understand **why it behaves the way it does — and how to make it faster.**

---

## Core Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Apache Spark" />
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks" />
  <img src="https://img.shields.io/badge/Delta%20Lake-003366?style=flat-square" alt="Delta Lake" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
</p>

**Data Engineering**  
Apache Spark · PySpark · Databricks · Delta Lake · SQL · Python · ETL/ELT · Streaming

**Architecture**  
Lakehouse Architecture · Medallion Architecture · Data Modeling · Data Quality · Schema Evolution · System Design

**Performance & Systems**  
Query Optimization · Partitioning · Shuffle Analysis · Distributed Processing · Performance Profiling

**Leadership**  
Solution Architecture · Technical Design · Project Delivery · Stakeholder Communication · Engineering Coordination

### Going deeper

`Spark Internals` · `Distributed Query Execution` · `Memory Management` · `Storage & I/O` · `Parallel Computing`

### Building toward

`C/C++` · `CUDA` · `RAPIDS` · `cuDF` · `GPU Architecture` · `GPU-Accelerated Spark`

---

## Featured Engineering

> ### 🛰️ [Sentinel Lakehouse](https://github.com/MsMansiDhruv/sentinel-lakehouse)
> **Production Lakehouse Engineering**  
> `Databricks` · `Apache Spark` · `Delta Lake` · `Auto Loader` · `Data Quality`  
> Resilient ingestion, schema evolution, quarantine patterns, failure handling, and trustworthy transformations.

> ### ⚡ [Data Engineering Portfolio](https://portfolio-mansi-eight.vercel.app/)
> **Systems · Architecture · Experiments**  
> `Distributed Data` · `Lakehouse` · `Spark` · `Performance` · `Data Platforms`  
> An interactive engineering portfolio documenting architectures, technical decisions, experiments, and trade-offs.  
> [Live portfolio →](https://portfolio-mansi-eight.vercel.app/) · [Source →](https://github.com/MsMansiDhruv/portfolio_mansi)

### Sentinel Lakehouse

![Status](https://img.shields.io/badge/status-active_development-2ea44f?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![Engine](https://img.shields.io/badge/engine-Apache_Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Architecture](https://img.shields.io/badge/architecture-Lakehouse-555555?style=flat-square)

**Production-oriented lakehouse engineering where failure is part of the design.**

I'm building Sentinel to explore what happens when real-world data refuses to behave. Instead of feeding the pipeline perfect inputs, the project deliberately introduces **schema drift, malformed types, rescued records, invalid business fields, duplicates, data-quality failures, and recovery scenarios**.

```text
Sources
   │
   ▼
Auto Loader
   │
   ▼
┌─────────┐
│ BRONZE  │ ─────► Rescued / Unexpected Data
└────┬────┘
     │
     ▼
DQ Validation ───► Quarantine
     │
     ▼
┌─────────┐
│ SILVER  │
└────┬────┘
     │
     ▼
┌─────────┐
│  GOLD   │
└─────────┘
```

The question behind the project is simple:

> **How do you design a data platform that remains trustworthy when its inputs aren't?**

`Databricks` · `Apache Spark` · `Auto Loader` · `Delta Lake` · `Data Quality` · `Streaming`

**[Explore Sentinel Lakehouse →](https://github.com/MsMansiDhruv/sentinel-lakehouse)**

### Data Engineering Portfolio

My interactive engineering portfolio documents the systems, architectures, experiments, and engineering decisions behind my work — from **distributed data pipelines and lakehouse architecture to Spark performance, retrieval systems, cloud architecture, and engineering trade-offs**.

**[Explore the portfolio →](https://portfolio-mansi-eight.vercel.app/)** · **[View source →](https://github.com/MsMansiDhruv/portfolio_mansi)**

---

## Currently Working On

### Production-grade Spark & Databricks

I'm currently working through the parts of data engineering that become important after a pipeline works:

`Resilient Ingestion` · `Schema Evolution` · `Data Quality` · `Streaming` · `Partitioning` · `Join Strategies` · `Shuffle Behavior` · `Query Execution` · `Observability` · `Failure Recovery`

The objective is to move from:

> **“The pipeline works.”**

to:

> **“I understand why it works, how it fails, and where the time and resources are going.”**

### Performance Engineering

The questions I'm increasingly interested in are:

- Where is the actual bottleneck?
- Why did this stage shuffle so much data?
- When should computation move instead of data?
- What does the execution engine actually do with this query?
- How do memory layout and data representation affect performance?
- What changes when a workload scales from one machine to a cluster?

---

## Engineering Labs

These aren't badge-collection projects. Each lab is intended to produce **experiments, measurements, execution evidence, and documented trade-offs**.

### ⚡ Spark Performance Lab · `PLANNED`

A benchmark-driven investigation of Spark execution.

`Partitioning` · `Shuffle` · `Join Strategies` · `Data Skew` · `AQE` · `Caching` · `Predicate Pushdown`

**Goal:** compare execution plans and measurable behavior instead of simply showing working Spark code.

### 🧠 Query Engine Lab · `PLANNED`

A small query-processing engine built to understand the path between:

```sql
SELECT ...
```

and the result returned to the user.

`Parsing → Logical Plan → Optimization → Physical Plan → Execution`

### 🌐 Distributed Systems Lab · `PLANNED`

Experiments around the fundamentals behind large-scale data infrastructure.

`Partitioning` · `Replication` · `Consistency` · `Fault Tolerance` · `Distributed Execution` · `Data Movement`

### GPU Data Processing Lab · `FUTURE`

CPU vs GPU experiments for analytical workloads.

`Pandas vs cuDF` · `CPU vs GPU Aggregations` · `Join Performance` · `Memory Transfer Overhead` · `Break-even Dataset Sizes` · `GPU-Accelerated Spark`

The goal won't be to prove that GPUs are always faster. It will be to understand **when acceleration helps, when it doesn't, and why**.

---

## Engineering Direction

```text
TODAY
│
├── Data Engineering
│   ├── Spark / PySpark
│   ├── Databricks / Delta Lake
│   ├── Lakehouse Architecture
│   └── Production Data Pipelines
│
├── NEXT DEPTH
│   ├── Spark Internals
│   ├── Distributed Systems
│   ├── Query Execution
│   ├── Performance Profiling
│   └── Memory / Storage / I/O
│
└── LONG-TERM SPECIALIZATION
    ├── C / C++
    ├── Parallel Algorithms
    ├── GPU Architecture
    ├── CUDA
    ├── RAPIDS / cuDF
    └── GPU-Accelerated Data Systems
```

My long-term engineering focus sits at the intersection of:

### **Data Systems × Distributed Computing × Hardware Acceleration**

I want to understand how joins, aggregations, sorting, filtering, compression, and large-scale ETL can be redesigned or accelerated for heterogeneous CPU/GPU systems.

Not just:

> How do I use a GPU?

But:

> **What makes a data workload worth accelerating in the first place?**

---

## How I Think About Engineering

I like systems where the interesting question isn't:

> “Which tool should we use?”

but:

> **“What is the system actually doing?”**

Tools change. Understanding **execution, memory, networks, storage, parallelism, failure, and trade-offs** lasts much longer.

<details>
<summary><b>What I'm currently studying</b></summary>

<br>

- Apache Spark internals
- Distributed query execution
- Query and performance profiling
- Data structures & algorithms
- System design
- Memory, storage, and I/O behavior
- C/C++ foundations
- Parallel computing
- GPU architecture
- CUDA fundamentals
- RAPIDS / cuDF

</details>

---

## GitHub Activity

<div align="center">

![Mansi's Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=MsMansiDhruv&theme=github-compact&hide_border=true&area=true)

</div>

> GitHub activity is only one signal. The projects above are where I document the architecture, experiments, failures, and engineering decisions behind the work.

---

## Let's Talk

I'm interested in conversations around **Data Engineering · Distributed Systems · Apache Spark · Performance Engineering · Data Infrastructure · Accelerated Computing**.

If you're building difficult data systems — especially systems where **scale and performance actually matter** — I'd love to talk.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mansidhruv/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Explore-111111?style=flat-square&logo=vercel&logoColor=white)](https://portfolio-mansi-eight.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MsMansiDhruv)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mansi.p.dhruv@gmail.com)

</div>

---

<div align="center">

**Building toward the intersection of data engineering, distributed systems, performance, and accelerated computing.**

</div>
