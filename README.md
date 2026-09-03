<p align="center">
  <img src="assets/logo/thenaritlab-logo.svg" alt="The Narit Lab" width="420">
</p>

<h1 align="center">Google Looker Studio — จากพื้นฐานสู่ขั้นสูง<br/><sub>คู่มือเรียนรู้ฉบับสมบูรณ์ โดย The Narit Lab</sub></h1>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <img alt="Languages: TH / EN" src="https://img.shields.io/badge/Languages-TH%20%7C%20EN-blue.svg">
  <img alt="Chapters" src="https://img.shields.io/badge/Chapters-16-informational.svg">
  <img alt="Labs" src="https://img.shields.io/badge/Labs-13-informational.svg">
  <img alt="Made by The Narit Lab" src="https://img.shields.io/badge/Made%20by-The%20Narit%20Lab-0F5AA6.svg">
</p>

<p align="center">🌐 ภาษาไทย | <a href="README.en.md"><b>English version →</b></a></p>

---

คู่มือเรียนรู้ **Google Looker Studio** สองภาษา (ไทย / อังกฤษ) ตั้งแต่สร้างรายงานแรกจนถึงแนวปฏิบัติระดับองค์กร พร้อม **Lab ปฏิบัติ 13 บท**, **dataset สังเคราะห์ 6 ชุด** และ **แผนการเรียน 6 สัปดาห์ (~30 ชั่วโมง)** ที่เริ่มวันไหนก็ได้ — แผนนับเป็น Week 1–6 / Day 1–30 ไม่ผูกกับปฏิทิน เปิดด้วยการเปรียบเทียบเครื่องมือ self-service BI (Tableau · Power BI · Looker Studio · Looker) และปิดด้วยภาพรวม **Looker** (LookML, semantic layer) รวมถึงขั้นตอนการเผยแพร่ผลงานของคุณขึ้น GitHub

**เหมาะกับ:** นักวิเคราะห์ ผู้ใช้ธุรกิจ และที่ปรึกษาที่มาจาก Excel หรือเครื่องมือ BI อื่น

**สิ่งที่ต้องมี:** Google account ฟรี, Google Cloud project ที่เปิด BigQuery sandbox (ไม่ต้องใช้บัตรเครดิต) และเวลาประมาณ 1 ชั่วโมงต่อวัน

### เริ่มต้นอย่างรวดเร็ว

1. อ่าน [docs/th/00-toc.md](docs/th/00-toc.md) (15 นาที)
2. ทำตาม [ROADMAP.md](ROADMAP.md) — วันละ 1 บทหรือ 1 lab
3. โหลด dataset จาก [`datasets/`](datasets/README.md) เข้า Google Sheets / BigQuery ใน [Lab 03](labs/lab03-data-sources/README.md)
4. จบด้วย [Capstone](docs/th/14-capstone.md) และเผยแพร่ตาม [บทที่ 99](docs/th/99-publish-to-github.md)

<details open>
<summary><b>📚 สารบัญ (ภาษาไทย)</b></summary>

| # | บท | ระดับ | Lab |
|---|---|---|---|
| 00 | [สารบัญและวิธีใช้คู่มือนี้](docs/th/00-toc.md) | — | — |
| 01 | [ภาพรวม Self-Service BI: Tableau · Power BI · Looker Studio · Looker](docs/th/01-bi-landscape.md) | Intro | — |
| 02 | [เริ่มต้นใช้งาน: บัญชี ทัวร์ UI รายงานแรกใน 15 นาที](docs/th/02-getting-started.md) | Basic | [Lab 02](labs/lab02-getting-started/README.md) |
| 03 | [Data Source และ Connector (Sheets, CSV, BigQuery)](docs/th/03-data-sources.md) | Basic | [Lab 03](labs/lab03-data-sources/README.md) |
| 04 | [Chart และ Table หลัก การจัดรูปแบบ Theme](docs/th/04-charts-tables.md) | Basic | [Lab 04](labs/lab04-charts-tables/README.md) |
| 05 | [Filter, Control, Date Range และ Interaction](docs/th/05-filters-controls.md) | Basic | [Lab 05](labs/lab05-filters-controls/README.md) |
| 06 | [Calculated Field และฟังก์ชัน](docs/th/06-calculated-fields.md) | Intermediate | [Lab 06](labs/lab06-calculated-fields/README.md) |
| 07 | [Data Blending และ Join](docs/th/07-blending.md) | Intermediate | [Lab 07](labs/lab07-blending/README.md) |
| 08 | [Parameter และรายงานแบบ Dynamic](docs/th/08-parameters.md) | Intermediate | [Lab 08](labs/lab08-parameters/README.md) |
| 09 | [หลักการออกแบบ Dashboard](docs/th/09-dashboard-design.md) | Intermediate | [Lab 09](labs/lab09-dashboard-design/README.md) |
| 10 | [ประสิทธิภาพ, Extract Data และ Best Practice ของ BigQuery](docs/th/10-performance.md) | Advanced | [Lab 10](labs/lab10-performance/README.md) |
| 11 | [การแชร์, ตั้งเวลาส่ง, Embed, การควบคุมสิทธิ์, Looker Studio Pro](docs/th/11-sharing-pro.md) | Advanced | [Lab 11](labs/lab11-sharing-pro/README.md) |
| 12 | [Community Visualization และการปรับแต่งขั้นสูง](docs/th/12-community-viz.md) | Advanced | [Lab 12](labs/lab12-community-viz/README.md) |
| 13 | [ภาพรวม Looker (Enterprise): LookML, Semantic Layer, Migration](docs/th/13-looker-overview.md) | Advanced | [Lab 13](labs/lab13-looker-overview/README.md) |
| 14 | [Capstone: Dashboard ยอดขายและการตลาดครบวงจร](docs/th/14-capstone.md) | Capstone | [Lab 14](labs/lab14-capstone/README.md) |
| 99 | [เผยแพร่ repo นี้ขึ้น GitHub](docs/th/99-publish-to-github.md) | ภาคผนวก | — |

**Dataset:** [sales_orders](datasets/sales_orders.csv) · [customers](datasets/customers.csv) · [products](datasets/products.csv) · [marketing_campaigns](datasets/marketing_campaigns.csv) · [web_traffic](datasets/web_traffic.csv) · [hr_headcount](datasets/hr_headcount.csv) · [Data dictionary](datasets/README.md)

</details>

### โครงสร้าง repository

```
looker-studio-guide/
├── README.md (ไทย) · README.en.md (English) · LICENSE · CREDITS.md · ROADMAP.md · CONTRIBUTING.md
├── assets/logo/        โลโก้ The Narit Lab (SVG) + icon
├── assets/images/      screenshot placeholder + README อธิบายแต่ละรูป
├── docs/STYLE-GUIDE.md
├── docs/th/            00-toc … 99-publish-to-github  (ภาษาไทย)
├── docs/en/            00-toc … 99-publish-to-github  (English)
├── labs/               lab02 … lab14, README สองภาษาต่อ lab
├── datasets/           CSV สังเคราะห์ 6 ชุด + generate_datasets.py + data dictionary
└── scripts/            check_links.py
```

---

## สัญญาอนุญาต

เนื้อหา โค้ด และ dataset สังเคราะห์: **MIT License** © 2026 The Narit Lab — ดู [LICENSE](LICENSE) และ [CREDITS.md](CREDITS.md) ส่วน public dataset ที่อ้างถึงใน lab ใช้สัญญาอนุญาตต้นทางของแต่ละชุด

Google Looker Studio, Looker และ BigQuery เป็นเครื่องหมายการค้าของ Google LLC — โปรเจกต์นี้เป็นสื่อการเรียนรู้อิสระ ไม่มีส่วนเกี่ยวข้องกับ Google

<p align="center"><sub>Made by <b>The Narit Lab</b> · MIT License · <a href="docs/th/00-toc.md">กลับสารบัญ</a> · <a href="README.en.md">English README</a></sub></p>
