# Lab 04 · Formatted Sales Overview Page / หน้าภาพรวมยอดขายที่จัดรูปแบบแล้ว

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/04-charts-tables.md) | [TH](../../docs/th/04-charts-tables.md)

---

## 🇺🇸 English

**Objective:** Build a one-page sales overview with six chart types, a custom theme and consistent formatting.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Basic | Week 2 · Day 6 |

**Prerequisites:** Lab 03 data sources (`[LSG] sales_orders (BQ)` or the Sheets equivalent).

**Steps**
1. New report *Sales Overview – Lab 04*. Add `[LSG] sales_orders (BQ)`. **Theme and layout → Theme → Customize**: primary color `#1A73E8`, font *Google Sans* or *Roboto*, canvas 1200 × 900, grid 10 px.
2. **KPI strip** — 4 scorecards: `SUM(sales_amount)` *Net Sales*, `SUM(profit)` *Profit*, `COUNT_DISTINCT(order_id)` *Orders*, `AVG(discount)` *Avg Discount* (Percent). Compact numbers, comparison date range *Previous period*. Make them 220 × 100 px each, 20 px apart.
3. **Time series** — `order_date` (Month) × `sales_amount`, `profit` as second series on right axis. Style: line weight 2, points off, legend top.
4. **Bar chart** — `sales_channel` × `sales_amount`, sorted desc, data labels on, single color.
5. **Stacked column** — `order_date` (Quarter) × `sales_amount` with breakdown `payment_method` (max 5 + Other).
6. **Pie/donut** — `order_status` share of `Record Count`; donut hole 50%; ≤ 4 slices.
7. **Table with bars** — `payment_method` × `sales_amount` (bar), `profit` (heatmap), `Record Count`. Conditional formatting: `profit` < 0 → red text.
8. **Geo chart** — `province` (set type *Geo → Province/State*, country Thailand) × `sales_amount`. If Looker Studio cannot geocode a province, switch to a bar chart and note it.
9. Add a **Text** title and a **Rectangle** behind the KPI strip (light gray, no border). Align everything (right-click → Align).
10. Apply number formats: THB with 0 decimals for money, `#,##0` for counts.

**Expected result**
- One screen, no scrolling, 4 KPIs + 5 charts, a single palette, all charts titled with units.

**Checkpoint questions**
1. Which chart type best answers "which payment method is growing?" — pie, stacked column, or table? Why?
2. Why does the *Avg Discount* scorecard use AVG rather than SUM?
3. What does the comparison arrow compare against when the date range is *Auto*?

**Stretch goal:** Add **drill-down** on the bar chart: `sales_channel → payment_method`, and an **optional metric** toggle between sales and profit.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** สร้างหน้าภาพรวมยอดขายหน้าเดียวด้วย chart 6 ชนิด theme ที่กำหนดเอง และการจัดรูปแบบที่สม่ำเสมอ

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Basic | สัปดาห์ 2 · วันที่ 6 |

**สิ่งที่ต้องมี:** data source จาก Lab 03 (`[LSG] sales_orders (BQ)` หรือแบบ Sheets)

**ขั้นตอน**
1. รายงานใหม่ *Sales Overview – Lab 04* เพิ่ม `[LSG] sales_orders (BQ)` **Theme and layout → Theme → Customize**: สีหลัก `#1A73E8`, font *Google Sans* หรือ *Roboto*, canvas 1200 × 900, grid 10 px
2. **แถบ KPI** — scorecard 4 อัน: `SUM(sales_amount)` *Net Sales*, `SUM(profit)` *Profit*, `COUNT_DISTINCT(order_id)` *Orders*, `AVG(discount)` *Avg Discount* (Percent) เปิด compact number, comparison date range *Previous period* ขนาด 220 × 100 px ห่างกัน 20 px
3. **Time series** — `order_date` (Month) × `sales_amount` และ `profit` เป็น series ที่สองบนแกนขวา Style: เส้นหนา 2, ปิดจุด, legend ด้านบน
4. **Bar chart** — `sales_channel` × `sales_amount` เรียงมากไปน้อย เปิด data label สีเดียว
5. **Stacked column** — `order_date` (Quarter) × `sales_amount` breakdown ด้วย `payment_method` (สูงสุด 5 + Other)
6. **Pie/donut** — สัดส่วน `order_status` ของ `Record Count`; รูตรงกลาง 50%; ≤ 4 ชิ้น
7. **Table แบบมี bar** — `payment_method` × `sales_amount` (bar), `profit` (heatmap), `Record Count` Conditional formatting: `profit` < 0 → ตัวอักษรสีแดง
8. **Geo chart** — `province` (ตั้ง type *Geo → Province/State*, ประเทศ Thailand) × `sales_amount` ถ้า Looker Studio geocode จังหวัดไม่ได้ ให้เปลี่ยนเป็น bar chart แล้วจดไว้
9. เพิ่ม **Text** เป็นชื่อเรื่อง และ **Rectangle** หลังแถบ KPI (เทาอ่อน ไม่มีขอบ) จัดแนวทุกอย่าง (คลิกขวา → Align)
10. ใส่รูปแบบตัวเลข: THB ทศนิยม 0 สำหรับเงิน, `#,##0` สำหรับจำนวน

**ผลที่ควรได้**
- จอเดียว ไม่เลื่อน KPI 4 ตัว + chart 5 ตัว พาเลตเดียว ทุก chart มีชื่อพร้อมหน่วย

**คำถามตรวจสอบ**
1. Chart ชนิดไหนตอบ "วิธีจ่ายเงินแบบไหนกำลังโต?" ได้ดีที่สุด — pie, stacked column หรือ table? ทำไม?
2. ทำไม scorecard *Avg Discount* ใช้ AVG ไม่ใช่ SUM?
3. ลูกศรเปรียบเทียบเทียบกับอะไรเมื่อ date range เป็น *Auto*?

**Stretch goal:** เพิ่ม **drill-down** บน bar chart: `sales_channel → payment_method` และ **optional metric** สลับระหว่างยอดขายกับกำไร

---

← [ก่อนหน้า / Previous: Lab 03 — Data Sources](../lab03-data-sources/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/04-charts-tables.md) · [EN](../../docs/en/04-charts-tables.md) | [ถัดไป / Next: Lab 05 — Filters & Controls](../lab05-filters-controls/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
