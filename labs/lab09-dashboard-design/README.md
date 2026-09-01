# Lab 09 · Redesign the Executive Page / ออกแบบหน้าผู้บริหารใหม่

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/09-dashboard-design.md) | [TH](../../docs/th/09-dashboard-design.md)

---

## 🇺🇸 English

**Objective:** Take a deliberately bad "before" page, critique it against the chapter 09 checklist, and rebuild it as a one-screen executive summary.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Intermediate | Week 4 · Day 17 |

**Prerequisites:** Lab 04–07 sources and Blend A.

**Steps**
1. **Build the "before" page (10 min)** on a new report: 12 charts of mixed types on `sales_orders` — 4 pies (channel, payment, status, weekend), 3 time series (daily granularity), 2 tables with 15 columns, a treemap, a scatter, a bullet — random sizes, default rainbow theme, filters in three corners, no titles.
2. **Critique (10 min)**: in a Text box list ≥ 8 problems using the chapter 09 checklist (hierarchy, color, chart choice, cardinality, titles, alignment, filter placement, missing context).
3. **Define the audience**: write the sentence *"This page helps the leadership team decide where to focus this week, every Monday."*
4. **Rebuild on a new page (35 min)**: canvas 1200 × 900, grid 10 px, theme with one accent color.
   - Row 1: title, date range (last 12 months), region drop-down (Blend A), logo placeholder.
   - Row 2: 5 identical KPI tiles (Net Sales, Profit, Margin %, Orders, AOV) with previous-period comparison.
   - Row 3: wide monthly combo (sales bars + margin line) and a sorted bar by channel (≤ 5 + Other).
   - Row 4: sorted bar by category (Blend A) and a top-10 products table with bars; one Text insight under the combo chart.
   - Footer: source, refresh, owner.
5. Apply **Dimension value colors** so channels keep the same color across charts. Turn off borders/shadows, light gridlines.
6. Screenshot both pages into `assets/images/` (your own copies) and put them side by side in an *About* page.

**Expected result**
- "After" page fits one screen, 5 KPIs + 4 charts + 1 insight, consistent palette, aligned to grid.

**Checkpoint questions**
1. Which three "before" charts carried no decision value? Why?
2. Why does a single trend chart beat three?
3. Where would you put a 40-column detail table, and how do users get there?

**Stretch goal:** Create a 400 × 1400 mobile page with stacked KPIs and one chart per row; link to it with a Button visible only on the main page.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** เอาหน้า "ก่อน" ที่ตั้งใจทำให้แย่ มาวิจารณ์ตาม checklist ในบทที่ 09 แล้วสร้างใหม่เป็นสรุปผู้บริหารจอเดียว

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Intermediate | สัปดาห์ 4 · วันที่ 17 |

**สิ่งที่ต้องมี:** source จาก Lab 04–07 และ Blend A

**ขั้นตอน**
1. **สร้างหน้า "ก่อน" (10 นาที)** ในรายงานใหม่: chart 12 ตัวหลายชนิดบน `sales_orders` — pie 4 อัน (channel, payment, status, weekend), time series 3 อัน (granularity รายวัน), ตาราง 2 ตารางที่มี 15 คอลัมน์, treemap, scatter, bullet — ขนาดสุ่ม theme สายรุ้งเริ่มต้น filter อยู่ 3 มุม ไม่มีชื่อ
2. **วิจารณ์ (10 นาที)**: ใน Text box ระบุปัญหา ≥ 8 ข้อตาม checklist บทที่ 09 (ลำดับ สี การเลือก chart cardinality ชื่อ การจัดแนว ตำแหน่ง filter ขาดบริบท)
3. **นิยามผู้ใช้**: เขียนประโยค *"หน้านี้ช่วยให้ทีมผู้บริหารตัดสินใจว่าจะโฟกัสอะไรในสัปดาห์นี้ ทุกวันจันทร์"*
4. **สร้างใหม่ในหน้าใหม่ (35 นาที)**: canvas 1200 × 900, grid 10 px, theme ที่มีสี accent เดียว
   - แถว 1: ชื่อเรื่อง, date range (12 เดือนล่าสุด), drop-down region (Blend A), ที่วาง logo
   - แถว 2: KPI tile เหมือนกัน 5 อัน (Net Sales, Profit, Margin %, Orders, AOV) พร้อมเปรียบเทียบช่วงก่อนหน้า
   - แถว 3: combo รายเดือนแบบกว้าง (bar ยอดขาย + line margin) และ sorted bar ตามช่องทาง (≤ 5 + Other)
   - แถว 4: sorted bar ตาม category (Blend A) และตาราง top-10 สินค้าพร้อม bar; Text insight หนึ่งบรรทัดใต้ combo chart
   - Footer: แหล่งข้อมูล การ refresh เจ้าของ
5. ใช้ **Dimension value colors** ให้ช่องทางเป็นสีเดิมทุก chart ปิดขอบ/เงา gridline อ่อน
6. บันทึกภาพทั้งสองหน้าไว้ที่ `assets/images/` (สำเนาของคุณ) แล้ววางเทียบกันในหน้า *About*

**ผลที่ควรได้**
- หน้า "หลัง" อยู่ในจอเดียว KPI 5 ตัว + chart 4 ตัว + insight 1 ข้อ พาเลตสม่ำเสมอ จัดตาม grid

**คำถามตรวจสอบ**
1. Chart "ก่อน" 3 ตัวไหนที่ไม่มีค่าต่อการตัดสินใจ? ทำไม?
2. ทำไม trend chart ตัวเดียวดีกว่า 3 ตัว?
3. ตารางรายละเอียด 40 คอลัมน์ควรวางที่ไหน และผู้ใช้ไปถึงได้อย่างไร?

**Stretch goal:** สร้างหน้ามือถือ 400 × 1400 ที่มี KPI ซ้อนกันและหนึ่ง chart ต่อแถว; ลิงก์ด้วย Button ที่เห็นเฉพาะหน้าหลัก

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
