# Lab 06 · Build a Calculated-Field Library / สร้างคลัง Calculated Field

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/06-calculated-fields.md) | [TH](../../docs/th/06-calculated-fields.md)

---

## 🇺🇸 English

**Objective:** Create 10 reusable calculated fields at data-source level covering arithmetic, text, date, CASE and REGEXP, and clean the `hr_headcount` source.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Intermediate | Week 3 · Day 11 |

**Prerequisites:** `[LSG] sales_orders (BQ)`, `[LSG] marketing_campaigns`, `[LSG] hr_headcount` data sources.

**Steps** — open each data source editor → **Add a field**, name exactly as shown.
1. `Margin %` = `SUM(profit) / SUM(sales_amount)` → type Percent.
2. `AOV` = `SUM(sales_amount) / COUNT_DISTINCT(order_id)` → Currency THB.
3. `Order Size` = CASE on `sales_amount`: ≥ 10000 *Large*, ≥ 3000 *Medium*, else *Small*.
4. `Days to Ship` = `DATETIME_DIFF(ship_date, order_date, DAY)`; `Ship Bucket` = CASE 0–2 / 3–5 / 6+.
5. `Fiscal Year` = `CASE WHEN MONTH(order_date) >= 10 THEN YEAR(order_date)+1 ELSE YEAR(order_date) END` → type Number, aggregation None (use as dimension).
6. `Weekend?` = `CASE WHEN WEEKDAY(order_date) IN (0,6) THEN "Weekend" ELSE "Weekday" END`.
7. `Order Prefix` = `LEFT_TEXT(order_id, 2)`; `Order Seq` = `CAST(RIGHT_TEXT(order_id, 6) AS NUMBER)`.
8. In `marketing_campaigns`: `Channel Family` = REGEXP_CONTAINS CASE (Social & Video / Search / Owned / Other); `Campaign Month` = `REGEXP_EXTRACT(campaign_name, "(\\w{3} \\d{4})$")`; `ROAS` = `SUM(revenue)/SUM(spend)`.
9. In `hr_headcount`: `Headcount` = `IF(level != "_movement", headcount_or_hires, NULL)`; `Hires` and `Exits` for movement rows; `Weighted Avg Salary` as in chapter 06 §6.
10. Build a test page: table `Order Size` × `Record Count`, `Margin %`, `AOV`; bar `Ship Bucket`; table `Channel Family` × `ROAS`; scorecard `Headcount` filtered to the latest month.

**Expected result**
- All fields show a green check. `Margin %` in the table summary row equals the scorecard value (aggregated ratio works at both levels).
- `Headcount` scorecard for the latest month is a few hundred, not thousands (movement rows excluded).

**Checkpoint questions**
1. Why does `SUM(profit) / sales_amount` fail while `SUM(profit) / SUM(sales_amount)` works?
2. Why is `Fiscal Year` created with aggregation *None*?
3. What would happen to `Weighted Avg Salary` if you used `AVG(avg_salary_or_exits)` instead?

**Stretch goal:** Add `Sales Rank` using the chart-level **Running calculation → Rank** and a `% of Total` with *Percent of total*; explain why these cannot be data-source fields.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** สร้าง calculated field ที่ใช้ซ้ำได้ 10 ตัวที่ระดับ data source ครอบคลุมคำนวณ ข้อความ วันที่ CASE และ REGEXP และทำความสะอาด source `hr_headcount`

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Intermediate | สัปดาห์ 3 · วันที่ 11 |

**สิ่งที่ต้องมี:** data source `[LSG] sales_orders (BQ)`, `[LSG] marketing_campaigns`, `[LSG] hr_headcount`

**ขั้นตอน** — เปิด data source editor แต่ละตัว → **Add a field** ตั้งชื่อตามที่แสดง
1. `Margin %` = `SUM(profit) / SUM(sales_amount)` → type Percent
2. `AOV` = `SUM(sales_amount) / COUNT_DISTINCT(order_id)` → Currency THB
3. `Order Size` = CASE บน `sales_amount`: ≥ 10000 *Large*, ≥ 3000 *Medium*, อื่น ๆ *Small*
4. `Days to Ship` = `DATETIME_DIFF(ship_date, order_date, DAY)`; `Ship Bucket` = CASE 0–2 / 3–5 / 6+
5. `Fiscal Year` = `CASE WHEN MONTH(order_date) >= 10 THEN YEAR(order_date)+1 ELSE YEAR(order_date) END` → type Number, aggregation None (ใช้เป็น dimension)
6. `Weekend?` = `CASE WHEN WEEKDAY(order_date) IN (0,6) THEN "Weekend" ELSE "Weekday" END`
7. `Order Prefix` = `LEFT_TEXT(order_id, 2)`; `Order Seq` = `CAST(RIGHT_TEXT(order_id, 6) AS NUMBER)`
8. ใน `marketing_campaigns`: `Channel Family` = CASE ด้วย REGEXP_CONTAINS (Social & Video / Search / Owned / Other); `Campaign Month` = `REGEXP_EXTRACT(campaign_name, "(\\w{3} \\d{4})$")`; `ROAS` = `SUM(revenue)/SUM(spend)`
9. ใน `hr_headcount`: `Headcount` = `IF(level != "_movement", headcount_or_hires, NULL)`; `Hires` และ `Exits` สำหรับแถว movement; `Weighted Avg Salary` ตามบทที่ 06 §6
10. สร้างหน้าทดสอบ: ตาราง `Order Size` × `Record Count`, `Margin %`, `AOV`; bar `Ship Bucket`; ตาราง `Channel Family` × `ROAS`; scorecard `Headcount` กรองเดือนล่าสุด

**ผลที่ควรได้**
- ทุก field มีเครื่องหมายถูกสีเขียว `Margin %` ในแถวรวมของตารางเท่ากับค่าใน scorecard (aggregated ratio ทำงานถูกทั้งสองระดับ)
- scorecard `Headcount` เดือนล่าสุดอยู่ที่หลักร้อย ไม่ใช่หลักพัน (ตัดแถว movement แล้ว)

**คำถามตรวจสอบ**
1. ทำไม `SUM(profit) / sales_amount` ไม่ผ่านแต่ `SUM(profit) / SUM(sales_amount)` ผ่าน?
2. ทำไม `Fiscal Year` ต้องสร้างด้วย aggregation *None*?
3. `Weighted Avg Salary` จะเป็นอย่างไรถ้าใช้ `AVG(avg_salary_or_exits)` แทน?

**Stretch goal:** เพิ่ม `Sales Rank` ด้วย **Running calculation → Rank** ระดับ chart และ `% of Total` ด้วย *Percent of total*; อธิบายว่าทำไมสองตัวนี้เป็น field ระดับ data source ไม่ได้

---

← [ก่อนหน้า / Previous: Lab 05 — Filters & Controls](../lab05-filters-controls/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/06-calculated-fields.md) · [EN](../../docs/en/06-calculated-fields.md) | [ถัดไป / Next: Lab 07 — Blending](../lab07-blending/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
