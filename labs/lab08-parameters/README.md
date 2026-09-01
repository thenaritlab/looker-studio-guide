# Lab 08 · What-if Simulator & Parameterised BigQuery Query / What-if simulator และ query แบบมี parameter

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/08-parameters.md) | [TH](../../docs/th/08-parameters.md)

---

## 🇺🇸 English

**Objective:** Drive calculations and a BigQuery query from viewer-controlled parameters: a growth target slider, a dimension switcher and a multi-select channel parameter.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Intermediate | Week 3 · Day 15 |

**Prerequisites:** BigQuery table `looker_guide.sales_orders`; Lab 07 report.

**Steps**
1. In `[LSG] sales_orders (BQ)` → **Add a parameter** `growth_rate`: Number, range 0–1 step 0.01, default 0.15.
2. Field `Target` = `SUM(sales_amount) * (1 + growth_rate)`. Time series by `order_date` (Month): `SUM(sales_amount)` and `Target`. Add a **Slider** control bound to `growth_rate`.
3. Parameter `dim_selector`: Text, list `Region`, `Channel`, `Payment`, default `Channel`. Field `Selected Dim` = CASE → `sales_channel` / `payment_method` / (for Region use Blend A from Lab 07 or add region via BigQuery view). Bar chart with `Selected Dim`; **Drop-down** bound to `dim_selector`, single select.
4. Dynamic title: add a Scorecard with metric `dim_selector` and hide the metric label, or a field `CONCAT("Sales by ", dim_selector)`; place it as the chart heading (a static Text component cannot read parameters).
5. **Custom query** data source with parameters: tick *Enable date range parameters* and *Enable parameters*; create list parameter `channels` (Text, multi-select, values from `sales_channel`) and number parameter `max_discount` default 0.3.
   ```sql
   SELECT DATE_TRUNC(order_date, MONTH) AS month, sales_channel,
          SUM(sales_amount) AS sales, SUM(profit) AS profit
   FROM `looker_guide.sales_orders`
   WHERE order_date BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) AND PARSE_DATE('%Y%m%d', @DS_END_DATE)
     AND sales_channel IN UNNEST(@channels)
     AND discount <= @max_discount
   GROUP BY 1, 2
   ```
6. Table on this source; **Fixed-size list** control → `channels`; **Input box** → `max_discount`. Change both and watch BigQuery **Job history** — a new query per change.
7. Boolean parameter `show_profit` + **Checkbox**; scorecard `IF(show_profit, SUM(profit), SUM(sales_amount))` with label field `IF(show_profit, "Profit", "Sales")`.
8. **Share → Get report link → Link to current report state** with slider at 0.25; decode the `params` JSON and change 0.25 to 0.10 in the URL; open it.

**Expected result**
- Target line moves with the slider; bar chart re-groups on drop-down change; custom query table respects channel and discount parameters; URL parameter overrides the default.

**Checkpoint questions**
1. Why is a parameter not a filter, even though the custom query uses it in `WHERE`?
2. Why do list parameters need `IN UNNEST(@channels)` rather than `= @channels`?
3. Two viewers open the report at the same time with different slider values — do they interfere?

**Stretch goal:** Add `@DS_USER_EMAIL` to the custom query joined to a small `rep_email → sales_rep` mapping table you upload, so each viewer sees only their own rows.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** ขับการคำนวณและ BigQuery query ด้วย parameter ที่ผู้อ่านควบคุม: slider เป้าการเติบโต, ตัวสลับ dimension และ parameter ช่องทางแบบเลือกหลายค่า

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Intermediate | สัปดาห์ 3 · วันที่ 15 |

**สิ่งที่ต้องมี:** ตาราง BigQuery `looker_guide.sales_orders`; รายงาน Lab 07

**ขั้นตอน**
1. ใน `[LSG] sales_orders (BQ)` → **Add a parameter** `growth_rate`: Number, ช่วง 0–1 step 0.01, ค่าเริ่มต้น 0.15
2. Field `Target` = `SUM(sales_amount) * (1 + growth_rate)` Time series ตาม `order_date` (Month): `SUM(sales_amount)` และ `Target` เพิ่ม **Slider** ผูกกับ `growth_rate`
3. Parameter `dim_selector`: Text, list `Region`, `Channel`, `Payment`, ค่าเริ่มต้น `Channel` Field `Selected Dim` = CASE → `sales_channel` / `payment_method` / (Region ใช้ Blend A จาก Lab 07 หรือเพิ่ม region ผ่าน BigQuery view) Bar chart ด้วย `Selected Dim`; **Drop-down** ผูกกับ `dim_selector` เลือกเดียว
4. ชื่อเรื่อง dynamic: Scorecard ที่ metric เป็น `dim_selector` ซ่อน label หรือ field `CONCAT("Sales by ", dim_selector)`; วางเป็นหัวเรื่องของ chart
5. Data source แบบ **Custom query** พร้อม parameter: ติ๊ก *Enable date range parameters* และ *Enable parameters*; สร้าง list parameter `channels` (Text, เลือกหลายค่า, ค่าจาก `sales_channel`) และ number parameter `max_discount` ค่าเริ่มต้น 0.3
   ```sql
   SELECT DATE_TRUNC(order_date, MONTH) AS month, sales_channel,
          SUM(sales_amount) AS sales, SUM(profit) AS profit
   FROM `looker_guide.sales_orders`
   WHERE order_date BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) AND PARSE_DATE('%Y%m%d', @DS_END_DATE)
     AND sales_channel IN UNNEST(@channels)
     AND discount <= @max_discount
   GROUP BY 1, 2
   ```
6. ตารางบน source นี้; **Fixed-size list** control → `channels`; **Input box** → `max_discount` เปลี่ยนทั้งสองแล้วดู BigQuery **Job history** — query ใหม่ทุกครั้งที่เปลี่ยน
7. Boolean parameter `show_profit` + **Checkbox**; scorecard `IF(show_profit, SUM(profit), SUM(sales_amount))` พร้อม field label `IF(show_profit, "Profit", "Sales")`
8. **Share → Get report link → Link to current report state** ขณะ slider อยู่ที่ 0.25; ถอดรหัส JSON ใน `params` แล้วเปลี่ยน 0.25 เป็น 0.10 ใน URL; เปิดดู

**ผลที่ควรได้**
- เส้นเป้าขยับตาม slider; bar chart จัดกลุ่มใหม่เมื่อเปลี่ยน drop-down; ตาราง custom query เคารพ parameter ช่องทางและส่วนลด; parameter ใน URL ทับค่าเริ่มต้น

**คำถามตรวจสอบ**
1. ทำไม parameter ไม่ใช่ filter แม้ custom query จะใช้มันใน `WHERE`?
2. ทำไม list parameter ต้องใช้ `IN UNNEST(@channels)` ไม่ใช่ `= @channels`?
3. ผู้อ่านสองคนเปิดรายงานพร้อมกันด้วยค่า slider ต่างกัน — รบกวนกันไหม?

**Stretch goal:** เพิ่ม `@DS_USER_EMAIL` ใน custom query โดย join กับตาราง mapping เล็ก ๆ `rep_email → sales_rep` ที่คุณอัปโหลด เพื่อให้ผู้อ่านแต่ละคนเห็นเฉพาะแถวของตัวเอง

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
