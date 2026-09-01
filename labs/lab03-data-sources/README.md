# Lab 03 · Three Data Sources: Sheets, CSV Upload, BigQuery / สาม data source

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/03-data-sources.md) | [TH](../../docs/th/03-data-sources.md)

---

## 🇺🇸 English

**Objective:** Connect the same data through three connectors, fix field types and aggregations, and create **reusable** data sources for the rest of the course.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Basic | Week 1 · Day 4 |

**Prerequisites**
- Lab 02 done. A Google Cloud project with **BigQuery sandbox** enabled (no credit card needed).
- All six CSVs from `datasets/`.

**Steps**
1. **Sheets** — import `customers.csv` and `products.csv` into one Google Sheet as two tabs. In Looker Studio: **Create → Data source → Google Sheets** → pick the sheet, tab `customers` → **Connect**. Repeat for `products`. Name them `[LSG] customers`, `[LSG] products`.
2. In each data source editor: check **Type** — `customer_id`/`product_id` = Text (not Number), `signup_date` = Date, `unit_price`/`unit_cost` = Number with **Default aggregation → Average** (summing a unit price is meaningless). Set `loyalty_member` = Boolean.
3. **File upload** — **Create → Data source → File Upload** → drop `web_traffic.csv`. Set `bounce_rate` type **Percent**, `date` = Date. Name `[LSG] web_traffic (upload)`.
4. **BigQuery** — in the Cloud console: create dataset `looker_guide` (location `asia-southeast1`). **Create table → Upload** `sales_orders.csv`, table name `sales_orders`, *Auto detect* schema ✔. Repeat for `marketing_campaigns` and `hr_headcount`.
5. In Looker Studio: **Create → Data source → BigQuery → My projects → your project → looker_guide → sales_orders → Connect**. Name `[LSG] sales_orders (BQ)`.
6. Set **Data credentials → Owner's credentials** (top bar) and **Data freshness → 12 hours**.
7. Add fields: `discount` type → Percent; `order_date` = Date (check it is not Date & Time); `order_id` = Text.
8. Create a **Custom query** data source on BigQuery:
   ```sql
   SELECT * FROM `looker_guide.sales_orders` WHERE order_status != 'Cancelled'
   ```
   Tick *Enable date range parameters*. Name `[LSG] sales_orders (BQ, not cancelled)`.
9. Open your Lab 02 report → **Resource → Manage added data sources → Add a data source** → add all `[LSG]` sources. Switch the scorecard's data source from the Sheets copy to `[LSG] sales_orders (BQ)` and confirm the number does not change.

**Expected result**
- Six reusable data sources with `[LSG]` prefix visible on the Looker Studio home page under *Data sources*.
- `sales_amount` total identical from Sheets and BigQuery (except for the "not cancelled" query).

**Checkpoint questions**
1. Why must `customer_id` be Text even though it looks numeric in some datasets?
2. What breaks if `unit_price` keeps default aggregation Sum?
3. Which of your six sources refreshes fastest when the underlying data changes, and why?

**Stretch goal:** Query the public dataset `bigquery-public-data.google_trends.top_terms` for Thailand via a custom query and connect it as a seventh source.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** เชื่อมข้อมูลชุดเดียวกันผ่าน connector 3 แบบ แก้ชนิดข้อมูลและ aggregation และสร้าง data source **แบบใช้ซ้ำได้** สำหรับใช้ตลอดคอร์ส

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Basic | สัปดาห์ 1 · วันที่ 4 |

**สิ่งที่ต้องมี**
- ทำ Lab 02 แล้ว Google Cloud project ที่เปิด **BigQuery sandbox** (ไม่ต้องใช้บัตรเครดิต)
- CSV ทั้ง 6 ไฟล์จาก `datasets/`

**ขั้นตอน**
1. **Sheets** — import `customers.csv` และ `products.csv` เป็น 2 แท็บใน Google Sheet เดียว ใน Looker Studio: **Create → Data source → Google Sheets** → เลือก sheet แท็บ `customers` → **Connect** ทำซ้ำกับ `products` ตั้งชื่อ `[LSG] customers`, `[LSG] products`
2. ใน data source editor แต่ละตัว: ตรวจ **Type** — `customer_id`/`product_id` = Text (ไม่ใช่ Number), `signup_date` = Date, `unit_price`/`unit_cost` เป็น Number และตั้ง **Default aggregation → Average** (ราคาไม่ควร Sum) ตั้ง `loyalty_member` = Boolean
3. **File upload** — **Create → Data source → File Upload** → วาง `web_traffic.csv` ตั้ง `bounce_rate` เป็น **Percent**, `date` = Date ตั้งชื่อ `[LSG] web_traffic (upload)`
4. **BigQuery** — ใน Cloud console: สร้าง dataset `looker_guide` (location `asia-southeast1`) **Create table → Upload** `sales_orders.csv` ชื่อตาราง `sales_orders` ติ๊ก *Auto detect* schema ✔ ทำซ้ำกับ `marketing_campaigns` และ `hr_headcount`
5. ใน Looker Studio: **Create → Data source → BigQuery → My projects → project ของคุณ → looker_guide → sales_orders → Connect** ตั้งชื่อ `[LSG] sales_orders (BQ)`
6. ตั้ง **Data credentials → Owner's credentials** (แถบบน) และ **Data freshness → 12 hours**
7. แก้ field: `discount` → Percent; `order_date` = Date (ตรวจว่าไม่ใช่ Date & Time); `order_id` = Text
8. สร้าง data source แบบ **Custom query** บน BigQuery
   ```sql
   SELECT * FROM `looker_guide.sales_orders` WHERE order_status != 'Cancelled'
   ```
   ติ๊ก *Enable date range parameters* ตั้งชื่อ `[LSG] sales_orders (BQ, not cancelled)`
9. เปิดรายงาน Lab 02 → **Resource → Manage added data sources → Add a data source** → เพิ่มทุก source ที่มี `[LSG]` สลับ data source ของ scorecard จากสำเนา Sheets เป็น `[LSG] sales_orders (BQ)` แล้วยืนยันว่าตัวเลขไม่เปลี่ยน

**ผลที่ควรได้**
- Data source แบบใช้ซ้ำ 6 ตัวที่มี prefix `[LSG]` เห็นในหน้า Home ของ Looker Studio ใต้ *Data sources*
- ยอดรวม `sales_amount` จาก Sheets และ BigQuery เท่ากัน (ยกเว้น query "not cancelled")

**คำถามตรวจสอบ**
1. ทำไม `customer_id` ต้องเป็น Text แม้บาง dataset จะดูเหมือนตัวเลข?
2. อะไรจะพังถ้า `unit_price` ยังใช้ default aggregation เป็น Sum?
3. source ไหนใน 6 ตัว refresh เร็วที่สุดเมื่อข้อมูลต้นทางเปลี่ยน และทำไม?

**Stretch goal:** Query dataset สาธารณะ `bigquery-public-data.google_trends.top_terms` สำหรับประเทศไทยด้วย custom query แล้วเชื่อมเป็น source ที่ 7

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
