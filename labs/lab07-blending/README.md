# Lab 07 · Enrich Sales and Build a Marketing ROI Blend / เติมยอดขายและสร้าง blend Marketing ROI

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/07-blending.md) | [TH](../../docs/th/07-blending.md)

---

## 🇺🇸 English

**Objective:** Build three blends — lookup enrichment, two facts at month grain, and a self-blend share-of-total — and learn how filters behave on blends.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Intermediate | Week 3 · Day 13 |

**Prerequisites:** Lab 03 sources; `month` field = `DATETIME_TRUNC(order_date, MONTH)` on sales and `DATETIME_TRUNC(start_date, MONTH)` on marketing (create if missing).

**Steps**
1. New report *Blends – Lab 07*. **Resource → Manage blends → Add a blend**.
2. **Blend A – Sales Enriched**: Table 1 `sales_orders` (dims `customer_id`, `product_id`, `order_date`; metrics `sales_amount`, `profit`, `Record Count`; date range dimension `order_date`). Join `customers` **left outer** on `customer_id` (dims `segment`, `region`). Join `products` **left outer** on `product_id` (dims `category`, `brand`). Save.
3. Chart: stacked bar `segment` × `SUM(sales_amount)`, breakdown `category`. Add a drop-down on `region` with data source = **Blend A**.
4. **Blend B – Marketing ROI**: Table 1 `sales_orders` (dim `month`; metric `sales_amount`; date range `order_date`). Table 2 `marketing_campaigns` (dim `month`; metrics `spend`, `leads`, `conversions`, `revenue`; date range `start_date`). Join **full outer** on `month`.
5. Add blend field `Month` = `COALESCE(month, month)` — note the editor prefixes table names; pick both. Combo chart: bars `SUM(spend)`, line `SUM(sales_amount)` on right axis. Add metric `Revenue per Baht` = `SUM(sales_amount)/SUM(spend)`.
6. **Blend C – Share of Total**: Table 1 `sales_orders` (dim `sales_channel`, metric `sales_amount`). Table 2 `sales_orders` (no dims, metric `sales_amount`). Join **cross**. Field `Share` = `SUM(t1.sales_amount)/SUM(t2.sales_amount)` → Percent. Table `sales_channel` × `Share` — verify the summary row = 100%.
7. Add a **date range control**. Confirm all three blended charts respond. Remove the date range dimension from Table 2 of Blend B and observe the "sales for period vs spend for all time" bug; put it back.
8. Compare: time the enriched chart, then create a BigQuery view `v_sales_enriched` (chapter 14 §3) and rebuild the same chart on it. Note the difference.

**Expected result**
- Segment × category bar with region filter working; combo chart with months on both sides; share table summing to 100%.

**Checkpoint questions**
1. Why must `customer_id` be in Table 1's dimensions even though it is not displayed?
2. What changes if Blend B uses *left outer* instead of *full outer*?
3. Why can the share-of-total field not be built in a single data source?

**Stretch goal:** Add `web_traffic` as a fourth table to Blend B on `month` and compute `Sessions per Conversion`.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** สร้าง blend 3 ตัว — เติม lookup, fact สองตารางที่ grain รายเดือน, และ self-blend สัดส่วนของยอดรวม — และเรียนรู้ว่า filter ทำงานกับ blend อย่างไร

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Intermediate | สัปดาห์ 3 · วันที่ 13 |

**สิ่งที่ต้องมี:** source จาก Lab 03; field `month` = `DATETIME_TRUNC(order_date, MONTH)` ที่ sales และ `DATETIME_TRUNC(start_date, MONTH)` ที่ marketing (สร้างถ้ายังไม่มี)

**ขั้นตอน**
1. รายงานใหม่ *Blends – Lab 07* **Resource → Manage blends → Add a blend**
2. **Blend A – Sales Enriched**: ตาราง 1 `sales_orders` (dim `customer_id`, `product_id`, `order_date`; metric `sales_amount`, `profit`, `Record Count`; date range dimension `order_date`) join `customers` **left outer** ด้วย `customer_id` (dim `segment`, `region`) join `products` **left outer** ด้วย `product_id` (dim `category`, `brand`) Save
3. Chart: stacked bar `segment` × `SUM(sales_amount)` breakdown `category` เพิ่ม drop-down บน `region` ที่ data source = **Blend A**
4. **Blend B – Marketing ROI**: ตาราง 1 `sales_orders` (dim `month`; metric `sales_amount`; date range `order_date`) ตาราง 2 `marketing_campaigns` (dim `month`; metric `spend`, `leads`, `conversions`, `revenue`; date range `start_date`) join **full outer** ด้วย `month`
5. เพิ่ม blend field `Month` = `COALESCE(month, month)` — editor จะเติม prefix ชื่อตาราง เลือกทั้งสอง Combo chart: bar `SUM(spend)`, line `SUM(sales_amount)` แกนขวา เพิ่ม metric `Revenue per Baht` = `SUM(sales_amount)/SUM(spend)`
6. **Blend C – Share of Total**: ตาราง 1 `sales_orders` (dim `sales_channel`, metric `sales_amount`) ตาราง 2 `sales_orders` (ไม่มี dim, metric `sales_amount`) join **cross** Field `Share` = `SUM(t1.sales_amount)/SUM(t2.sales_amount)` → Percent ตาราง `sales_channel` × `Share` — ตรวจว่าแถวรวม = 100%
7. เพิ่ม **date range control** ยืนยันว่า chart ที่เป็น blend ทั้งสามตอบสนอง ลอง date range dimension ของตาราง 2 ใน Blend B ออกแล้วดูบั๊ก "ยอดขายตามช่วง vs งบตลอดกาล"; ใส่กลับ
8. เปรียบเทียบ: จับเวลา chart ที่เติมข้อมูล แล้วสร้าง BigQuery view `v_sales_enriched` (บทที่ 14 §3) สร้าง chart เดิมบน view จดความต่าง

**ผลที่ควรได้**
- Bar segment × category ที่ filter region ทำงาน; combo chart ที่มีเดือนครบทั้งสองฝั่ง; ตารางสัดส่วนรวม 100%

**คำถามตรวจสอบ**
1. ทำไม `customer_id` ต้องอยู่ใน dimension ของตาราง 1 ทั้งที่ไม่ได้แสดง?
2. อะไรเปลี่ยนถ้า Blend B ใช้ *left outer* แทน *full outer*?
3. ทำไม field สัดส่วนของยอดรวมสร้างใน data source เดียวไม่ได้?

**Stretch goal:** เพิ่ม `web_traffic` เป็นตารางที่ 4 ใน Blend B ด้วย `month` แล้วคำนวณ `Sessions per Conversion`

---

← [ก่อนหน้า / Previous: Lab 06 — Calculated Fields](../lab06-calculated-fields/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/07-blending.md) · [EN](../../docs/en/07-blending.md) | [ถัดไป / Next: Lab 08 — Parameters](../lab08-parameters/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
