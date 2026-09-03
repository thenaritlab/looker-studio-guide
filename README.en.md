<p align="center">
  <img src="assets/logo/thenaritlab-logo.svg" alt="The Narit Lab" width="420">
</p>

<h1 align="center">Google Looker Studio — From Basic to Advanced<br/><sub>A complete learning guide by The Narit Lab</sub></h1>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <img alt="Languages: TH / EN" src="https://img.shields.io/badge/Languages-TH%20%7C%20EN-blue.svg">
  <img alt="Chapters" src="https://img.shields.io/badge/Chapters-16-informational.svg">
  <img alt="Labs" src="https://img.shields.io/badge/Labs-13-informational.svg">
  <img alt="Made by The Narit Lab" src="https://img.shields.io/badge/Made%20by-The%20Narit%20Lab-0F5AA6.svg">
</p>

<p align="center">🌐 <a href="README.md"><b>← ฉบับภาษาไทย</b></a> | English</p>

---

A bilingual (Thai / US English) learning guide for **Google Looker Studio**, from first report to enterprise-grade practices, with **13 hands-on labs**, **6 synthetic datasets**, and a **6-week, ~30-hour learning roadmap** you can start any day — the plan is numbered Week 1–6 / Day 1–30 and is not tied to calendar dates. It opens with a self-service BI comparison (Tableau · Power BI · Looker Studio · Looker) and closes with an overview of **Looker** (LookML, semantic layer) and a step-by-step guide to publishing your own work on GitHub.

**Who it is for:** analysts, business users and consultants coming from Excel or another BI tool.

**What you need:** a free Google account, a Google Cloud project with the BigQuery sandbox (no credit card), and about one hour per day.

### Quick start

1. Read [docs/en/00-toc.md](docs/en/00-toc.md) (15 min).
2. Follow [ROADMAP.md](ROADMAP.md) — one chapter or lab per day.
3. Load the datasets from [`datasets/`](datasets/README.md) into Google Sheets / BigQuery in [Lab 03](labs/lab03-data-sources/README.md).
4. Finish with the [Capstone](docs/en/14-capstone.md) and publish it using [chapter 99](docs/en/99-publish-to-github.md).

<details open>
<summary><b>📚 Table of contents (English)</b></summary>

| # | Chapter | Level | Lab |
|---|---|---|---|
| 00 | [Table of Contents & How to Use This Guide](docs/en/00-toc.md) | — | — |
| 01 | [Self-Service BI Landscape: Tableau · Power BI · Looker Studio · Looker](docs/en/01-bi-landscape.md) | Intro | — |
| 02 | [Getting Started: account, UI tour, first report in 15 minutes](docs/en/02-getting-started.md) | Basic | [Lab 02](labs/lab02-getting-started/README.md) |
| 03 | [Data Sources & Connectors (Sheets, CSV, BigQuery)](docs/en/03-data-sources.md) | Basic | [Lab 03](labs/lab03-data-sources/README.md) |
| 04 | [Core Charts & Tables, Formatting, Themes](docs/en/04-charts-tables.md) | Basic | [Lab 04](labs/lab04-charts-tables/README.md) |
| 05 | [Filters, Controls, Date Ranges, Interactions](docs/en/05-filters-controls.md) | Basic | [Lab 05](labs/lab05-filters-controls/README.md) |
| 06 | [Calculated Fields & Functions](docs/en/06-calculated-fields.md) | Intermediate | [Lab 06](labs/lab06-calculated-fields/README.md) |
| 07 | [Data Blending & Joins](docs/en/07-blending.md) | Intermediate | [Lab 07](labs/lab07-blending/README.md) |
| 08 | [Parameters & Dynamic Reports](docs/en/08-parameters.md) | Intermediate | [Lab 08](labs/lab08-parameters/README.md) |
| 09 | [Dashboard Design Principles](docs/en/09-dashboard-design.md) | Intermediate | [Lab 09](labs/lab09-dashboard-design/README.md) |
| 10 | [Performance, Extract Data, BigQuery Best Practices](docs/en/10-performance.md) | Advanced | [Lab 10](labs/lab10-performance/README.md) |
| 11 | [Sharing, Scheduling, Embedding, Access Control, Looker Studio Pro](docs/en/11-sharing-pro.md) | Advanced | [Lab 11](labs/lab11-sharing-pro/README.md) |
| 12 | [Community Visualizations & Advanced Customization](docs/en/12-community-viz.md) | Advanced | [Lab 12](labs/lab12-community-viz/README.md) |
| 13 | [Looker (Enterprise) Overview: LookML, Semantic Layer, Migration](docs/en/13-looker-overview.md) | Advanced | [Lab 13](labs/lab13-looker-overview/README.md) |
| 14 | [Capstone: End-to-End Sales & Marketing Dashboard](docs/en/14-capstone.md) | Capstone | [Lab 14](labs/lab14-capstone/README.md) |
| 99 | [Publishing This Repo to GitHub](docs/en/99-publish-to-github.md) | Appendix | — |

**Datasets:** [sales_orders](datasets/sales_orders.csv) · [customers](datasets/customers.csv) · [products](datasets/products.csv) · [marketing_campaigns](datasets/marketing_campaigns.csv) · [web_traffic](datasets/web_traffic.csv) · [hr_headcount](datasets/hr_headcount.csv) · [Data dictionary](datasets/README.md)

</details>

### Repository layout

```
looker-studio-guide/
├── README.md (TH) · README.en.md (EN) · LICENSE · CREDITS.md · ROADMAP.md · CONTRIBUTING.md
├── assets/logo/        The Narit Lab logo (SVG) + icon
├── assets/images/      screenshot placeholders + README listing each one
├── docs/STYLE-GUIDE.md
├── docs/th/            00-toc … 99-publish-to-github  (ภาษาไทย)
├── docs/en/            00-toc … 99-publish-to-github  (English)
├── labs/               lab02 … lab14, bilingual README per lab
├── datasets/           6 synthetic CSVs + generate_datasets.py + data dictionary
└── scripts/            check_links.py
```

---

## License

Content, code and synthetic datasets: **MIT License** © 2026 The Narit Lab — see [LICENSE](LICENSE) and [CREDITS.md](CREDITS.md). Public datasets referenced in labs keep their original licenses.

Google Looker Studio, Looker and BigQuery are trademarks of Google LLC. This is an independent educational project.

<p align="center"><sub>Made by <b>The Narit Lab</b> · MIT License · <a href="docs/en/00-toc.md">Back to TOC</a> · <a href="README.md">Thai README</a></sub></p>
