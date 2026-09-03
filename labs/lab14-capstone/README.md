# Lab 14 · Capstone Build Guide / คู่มือสร้าง Capstone

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/14-capstone.md) | [TH](../../docs/th/14-capstone.md)

---

## 🇺🇸 English

**Objective:** Build the 3-page *Siam Goods Weekly Business Review* with checkpoints per session, meeting the chapter 14 acceptance checklist.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 4 × 60 min | Capstone | Week 6 · Day 26–29 |

**Prerequisites:** All previous labs; BigQuery dataset `looker_guide` with the six tables (or Sheets equivalents).

### Session 1 — Foundations (Mon 12 Oct)
1. Run the `v_sales_enriched` view SQL (chapter 14 §3). Connect it as `[SG] sales_enriched`. Connect `[SG] marketing`, `[SG] web_traffic`.
2. In `[SG] sales_enriched` create every KPI field from the chapter 14 §2 table plus parameter `growth_rate` (default 0.15) and `Target` = `SUM(IF(order_status="Completed", sales_amount, 0)) * (1 + growth_rate)`, used against a *previous year* comparison series.
3. New report *Siam Goods · Weekly Business Review*. Theme: one accent (`#0F5AA6`), canvas 1200 × 900, grid 10. Create 4 pages: Executive, Marketing, Customers & Products, About.
4. Report-level: title, date range control (default *Last 12 months*), region drop-down, logo image, footer text.
   ✅ **Checkpoint:** KPIs render on a blank Executive page with non-zero values.

### Session 2 — Executive page (Tue 13 Oct)
5. KPI strip: Net Sales, Gross Profit, Margin %, Orders, AOV, Return Rate — previous-period comparison, identical tiles.
6. Combo chart: bars `Net Sales` by `order_month`, line `Target`; second series `Net Sales` with comparison *Previous year* for context.
7. Sorted bar by `sales_channel`; geo or bar by `region`; top-10 `product_name` table with bars; insight Text.
8. Cross-filtering on channel bar and region chart.
   ✅ **Checkpoint:** moving the `growth_rate` slider moves the target line; region drop-down filters every chart.

### Session 3 — Marketing page (Wed 14 Oct)
9. Blend `sales_enriched` × `marketing` on month (full outer) → combo Spend vs Net Sales.
10. KPI strip: Spend, Attributed Revenue, ROAS, Leads, CPL, Conversion Rate.
11. ROAS by channel sorted bar with conditional color (< 1.0 red). Funnel (community viz or 4 scorecards) Impressions → Clicks → Leads → Conversions.
12. Web sessions stacked bar `channel × device` from `web_traffic`; campaign table with optional metrics.
   ✅ **Checkpoint:** ROAS in the bar matches `SUM(revenue)/SUM(spend)` in a BigQuery query for the same period.

### Session 4 — Customers, About, polish (Thu 15 Oct)
13. Customers & Products page: KPIs; pivot `segment × category` heatmap; return rate by category; `age_group × sales_channel` 100% stacked; product table with drill-down.
14. About page: KPI definitions table (copy from chapter 14 §2), sources, refresh, owner, how to use.
15. Performance pass: data freshness 12 h; check job history; ≤ 10 charts per page.
16. Share with a reviewer (Viewer), schedule Monday 08:00 Asia/Bangkok, name version "v1.0".
17. Write one insight paragraph per page; record a 3-minute walkthrough.
   ✅ **Checkpoint:** every box in the chapter 14 §6 acceptance checklist is ticked.

**Expected result** — a portfolio-ready 4-page report scoring ≥ 80% on the chapter 14 rubric.

**Checkpoint questions**
1. Which KPI was hardest to define precisely, and what did you decide?
2. Where did you choose SQL over a blend, and why?
3. What would you change first if the CEO asked for a mobile version?

**Stretch goal:** Replace the month blend with a BigQuery view `v_monthly_kpi` and compare load time; add a Gemini-generated summary (Pro) or a manual "This week in 3 bullets" text.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** สร้าง *Siam Goods Weekly Business Review* 3 หน้า พร้อม checkpoint ต่อ session ให้ผ่าน checklist ตรวจรับในบทที่ 14

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 4 × 60 นาที | Capstone | สัปดาห์ 6 · วันที่ 26–29 |

**สิ่งที่ต้องมี:** ทุก lab ก่อนหน้า; dataset BigQuery `looker_guide` ที่มี 6 ตาราง (หรือแบบ Sheets)

### Session 1 — พื้นฐาน (จ. 12 ต.ค.)
1. รัน SQL สร้าง view `v_sales_enriched` (บทที่ 14 §3) เชื่อมเป็น `[SG] sales_enriched` เชื่อม `[SG] marketing`, `[SG] web_traffic`
2. ใน `[SG] sales_enriched` สร้าง KPI field ทุกตัวจากตารางบทที่ 14 §2 บวก parameter `growth_rate` (ค่าเริ่มต้น 0.15) และ `Target` = `SUM(IF(order_status="Completed", sales_amount, 0)) * (1 + growth_rate)` ใช้กับ series เปรียบเทียบ *ปีก่อน*
3. รายงานใหม่ *Siam Goods · Weekly Business Review* Theme: accent เดียว (`#0F5AA6`), canvas 1200 × 900, grid 10 สร้าง 4 หน้า: Executive, Marketing, Customers & Products, About
4. ระดับ report: ชื่อเรื่อง, date range control (ค่าเริ่มต้น *Last 12 months*), drop-down region, รูป logo, ข้อความ footer
   ✅ **Checkpoint:** KPI แสดงค่าไม่เป็นศูนย์บนหน้า Executive ที่ยังว่าง

### Session 2 — หน้า Executive (อ. 13 ต.ค.)
5. แถบ KPI: Net Sales, Gross Profit, Margin %, Orders, AOV, Return Rate — เปรียบเทียบช่วงก่อน tile เหมือนกันทุกอัน
6. Combo chart: bar `Net Sales` ตาม `order_month`, line `Target`; series ที่สอง `Net Sales` แบบเปรียบเทียบ *Previous year* เพื่อบริบท
7. Sorted bar ตาม `sales_channel`; geo หรือ bar ตาม `region`; ตาราง top-10 `product_name` พร้อม bar; Text insight
8. Cross-filtering บน bar ช่องทางและ chart region
   ✅ **Checkpoint:** เลื่อน slider `growth_rate` แล้วเส้นเป้าขยับ; drop-down region กรองทุก chart

### Session 3 — หน้า Marketing (พ. 14 ต.ค.)
9. Blend `sales_enriched` × `marketing` ด้วย month (full outer) → combo Spend vs Net Sales
10. แถบ KPI: Spend, Attributed Revenue, ROAS, Leads, CPL, Conversion Rate
11. ROAS ตามช่องทาง sorted bar สีเงื่อนไข (< 1.0 แดง) Funnel (community viz หรือ scorecard 4 อัน) Impressions → Clicks → Leads → Conversions
12. Stacked bar session เว็บ `channel × device` จาก `web_traffic`; ตาราง campaign แบบ optional metrics
   ✅ **Checkpoint:** ROAS ใน bar ตรงกับ `SUM(revenue)/SUM(spend)` จาก query BigQuery ช่วงเดียวกัน

### Session 4 — Customers, About, ขัดเกลา (พฤ. 15 ต.ค.)
13. หน้า Customers & Products: KPI; pivot heatmap `segment × category`; return rate ตาม category; `age_group × sales_channel` 100% stacked; ตารางสินค้าพร้อม drill-down
14. หน้า About: ตารางคำนิยาม KPI (copy จากบทที่ 14 §2) แหล่งข้อมูล การ refresh เจ้าของ วิธีใช้
15. รอบประสิทธิภาพ: data freshness 12 ชม.; ตรวจ job history; ≤ 10 chart ต่อหน้า
16. แชร์ให้ผู้ตรวจ (Viewer) ตั้งเวลาจันทร์ 08:00 Asia/Bangkok ตั้งชื่อ version "v1.0"
17. เขียน insight หนึ่งย่อหน้าต่อหน้า; บันทึกวิดีโอเดินชม 3 นาที
   ✅ **Checkpoint:** ทุกช่องใน checklist ตรวจรับบทที่ 14 §6 ถูกติ๊กครบ

**ผลที่ควรได้** — รายงาน 4 หน้าระดับ portfolio ได้ ≥ 80% ตามเกณฑ์บทที่ 14

**คำถามตรวจสอบ**
1. KPI ไหนนิยามให้แม่นยากที่สุด และคุณตัดสินใจอย่างไร?
2. ตรงไหนที่คุณเลือก SQL แทน blend และทำไม?
3. ถ้า CEO ขอเวอร์ชันมือถือ คุณจะเปลี่ยนอะไรก่อน?

**Stretch goal:** แทน blend รายเดือนด้วย BigQuery view `v_monthly_kpi` แล้วเทียบเวลาโหลด; เพิ่มสรุปจาก Gemini (Pro) หรือข้อความ "สัปดาห์นี้ใน 3 ข้อ" ที่เขียนเอง

---

← [ก่อนหน้า / Previous: Lab 13 — Looker Overview](../lab13-looker-overview/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/14-capstone.md) · [EN](../../docs/en/14-capstone.md) | [ถัดไป / Next: บท 99 เผยแพร่ขึ้น GitHub / Ch 99 Publish](../../docs/th/99-publish-to-github.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
