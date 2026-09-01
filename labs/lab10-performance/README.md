# Lab 10 · Benchmark Sheets vs Extract vs BigQuery / Benchmark ประสิทธิภาพ

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/10-performance.md) | [TH](../../docs/th/10-performance.md)

---

## 🇺🇸 English

**Objective:** Measure the same chart on four back-ends, cut BigQuery bytes scanned with partitioning and an aggregate table, and set a sensible caching policy.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Advanced | Week 4 · Day 19 |

**Prerequisites:** `sales_orders` in Sheets and BigQuery (Lab 03).

**Steps**
1. New report *Performance – Lab 10*. Page **A**: time series `order_date` (Month) × `SUM(sales_amount)` breakdown `sales_channel`, plus a table `payment_method` × 3 metrics — on the **Sheets** source. Reload the page 3 times and note load time (browser dev tools → Network, or a stopwatch).
2. **Add data → Extract Data** from the Sheets source: dims `order_date`, `sales_channel`, `payment_method`; metrics `sales_amount`, `profit`, `Record Count`; auto-update daily. Page **B**: same charts on the extract. Time it.
3. Page **C**: same charts on `[LSG] sales_orders (BQ)` (raw table). Time it and open **BigQuery → Job history**; record *bytes billed* for one query.
4. In BigQuery create a partitioned + clustered copy and an aggregate table:
   ```sql
   CREATE OR REPLACE TABLE looker_guide.sales_orders_p
   PARTITION BY order_date CLUSTER BY sales_channel, payment_method
   AS SELECT * FROM looker_guide.sales_orders;

   CREATE OR REPLACE TABLE looker_guide.sales_daily_channel
   PARTITION BY order_date AS
   SELECT order_date, sales_channel, payment_method,
          SUM(sales_amount) sales_amount, SUM(profit) profit, COUNT(*) orders
   FROM looker_guide.sales_orders GROUP BY 1,2,3;
   ```
5. Page **D**: same charts on `sales_daily_channel` (date range dimension `order_date`). Set the date range control to *Last 90 days* and compare *bytes billed* against page C.
6. Set **Data freshness** on every BigQuery source to 12 hours; reload twice and confirm the second load hits the cache (job history shows no new job).
7. Fill the benchmark table in a Text box:

| Back-end | Load 1 | Load 2 (cached) | Bytes billed | Freshness |
|---|---|---|---|---|
| Sheets | | | n/a | |
| Extract | | | n/a | |
| BQ raw | | | | |
| BQ rollup | | | | |

8. Run the chapter 10 **performance checklist** against your Lab 09 report and fix two items.

**Expected result**
- Extract and BQ rollup are fastest; rollup with a 90-day filter scans a fraction of the raw table; cached reloads issue no BigQuery job.

**Checkpoint questions**
1. Why does the extract have no *bytes billed* and what is its trade-off?
2. Why did partition pruning not help much on the raw table with date range *Auto* and no control?
3. When would you choose BI Engine over an aggregate table?

**Stretch goal:** Schedule the rollup with a BigQuery scheduled query (daily 06:00 Asia/Bangkok) and switch the Lab 09 overview page to it.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** วัด chart เดียวกันบน back-end 4 แบบ ลด byte ที่ BigQuery สแกนด้วย partition และตาราง aggregate และตั้งนโยบาย cache ที่เหมาะสม

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Advanced | สัปดาห์ 4 · วันที่ 19 |

**สิ่งที่ต้องมี:** `sales_orders` ใน Sheets และ BigQuery (Lab 03)

**ขั้นตอน**
1. รายงานใหม่ *Performance – Lab 10* หน้า **A**: time series `order_date` (Month) × `SUM(sales_amount)` breakdown `sales_channel` และตาราง `payment_method` × 3 metric — บน source **Sheets** โหลดหน้า 3 ครั้งแล้วจดเวลา (dev tools → Network หรือนาฬิกาจับเวลา)
2. **Add data → Extract Data** จาก source Sheets: dim `order_date`, `sales_channel`, `payment_method`; metric `sales_amount`, `profit`, `Record Count`; auto-update รายวัน หน้า **B**: chart เดิมบน extract จับเวลา
3. หน้า **C**: chart เดิมบน `[LSG] sales_orders (BQ)` (ตารางดิบ) จับเวลาและเปิด **BigQuery → Job history**; จด *bytes billed* ของ query หนึ่งตัว
4. ใน BigQuery สร้างสำเนาที่ partition + cluster และตาราง aggregate
   ```sql
   CREATE OR REPLACE TABLE looker_guide.sales_orders_p
   PARTITION BY order_date CLUSTER BY sales_channel, payment_method
   AS SELECT * FROM looker_guide.sales_orders;

   CREATE OR REPLACE TABLE looker_guide.sales_daily_channel
   PARTITION BY order_date AS
   SELECT order_date, sales_channel, payment_method,
          SUM(sales_amount) sales_amount, SUM(profit) profit, COUNT(*) orders
   FROM looker_guide.sales_orders GROUP BY 1,2,3;
   ```
5. หน้า **D**: chart เดิมบน `sales_daily_channel` (date range dimension `order_date`) ตั้ง date range control เป็น *Last 90 days* แล้วเทียบ *bytes billed* กับหน้า C
6. ตั้ง **Data freshness** ของทุก source BigQuery เป็น 12 ชั่วโมง; โหลดซ้ำ 2 ครั้งและยืนยันว่าครั้งที่สองใช้ cache (job history ไม่มี job ใหม่)
7. กรอกตาราง benchmark ใน Text box

| Back-end | โหลด 1 | โหลด 2 (cache) | Bytes billed | Freshness |
|---|---|---|---|---|
| Sheets | | | n/a | |
| Extract | | | n/a | |
| BQ ดิบ | | | | |
| BQ rollup | | | | |

8. รัน **checklist ประสิทธิภาพ** บทที่ 10 กับรายงาน Lab 09 แล้วแก้ 2 ข้อ

**ผลที่ควรได้**
- Extract และ BQ rollup เร็วที่สุด; rollup ที่กรอง 90 วันสแกนเพียงเสี้ยวของตารางดิบ; การโหลดซ้ำจาก cache ไม่สร้าง job ใน BigQuery

**คำถามตรวจสอบ**
1. ทำไม extract ไม่มี *bytes billed* และข้อแลกเปลี่ยนคืออะไร?
2. ทำไม partition pruning ช่วยตารางดิบไม่มากเมื่อ date range เป็น *Auto* และไม่มี control?
3. เมื่อไรจะเลือก BI Engine แทนตาราง aggregate?

**Stretch goal:** ตั้งเวลา rollup ด้วย BigQuery scheduled query (รายวัน 06:00 Asia/Bangkok) แล้วสลับหน้า overview ของ Lab 09 ไปใช้มัน

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
