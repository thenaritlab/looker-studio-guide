# Lab 05 · Make the Sales Page Interactive / ทำหน้ายอดขายให้โต้ตอบได้

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/05-filters-controls.md) | [TH](../../docs/th/05-filters-controls.md)

---

## 🇺🇸 English

**Objective:** Add four controls, an editor filter, cross-filtering and a reset button to the Lab 04 page; understand filter scope.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Basic | Week 2 · Day 8 |

**Prerequisites:** Lab 04 report.

**Steps**
1. Open the Lab 04 report. Top-right: **Add a control → Date range control**, default *Advanced: Today minus 12 months → Today*. Right-click → **Make report-level**.
2. **Drop-down list** on `sales_channel` (multi-select, show metric `sales_amount`, search box on). Make report-level.
3. **Drop-down list** on `payment_method`, **Slider** on `discount` (0–30%), and an **Input box** on `customer_id` (operator *contains*).
4. Chart-level **editor filter**: on all KPI scorecards add filter `Completed only`: Include `order_status` Equal to `Completed`. Verify the Net Sales number drops.
5. Enable **Cross-filtering** (Setup → Chart interactions) on the channel bar, payment table and donut. Click *Marketplace* on the bar → observe every chart.
6. Group test: select the stacked column + payment table → right-click → **Group**. Add a drop-down on `order_status` *inside* the group. Confirm it filters only those two charts.
7. **Add a control → Button → Reset**: label *Clear filters*, place top-right.
8. Enable the **Filter bar** (File → Report settings) and compare it with your controls.
9. **Share → Get report link → Link to current report state** after selecting *Marketplace* + *Credit Card*; open the link in a new tab.

**Expected result**
- Date range and channel controls affect every page; the status drop-down affects only the grouped charts; clicking a bar cross-filters the page; the button resets everything.

**Checkpoint questions**
1. A colleague adds a table from `[LSG] customers` to this page. Why does the channel drop-down not filter it? Two ways to fix?
2. What is the difference between the editor filter `Completed only` and a drop-down on `order_status` set to *Completed*?
3. When is the *Filter bar* a better choice than controls?

**Stretch goal:** Add a second page with the same KPI strip and confirm report-level controls carry across; then make one KPI *not* respond to the date control (Custom date range) and explain when that is useful.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** เพิ่ม control 4 ตัว editor filter cross-filtering และปุ่ม reset ให้หน้า Lab 04; เข้าใจขอบเขตของ filter

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Basic | สัปดาห์ 2 · วันที่ 8 |

**สิ่งที่ต้องมี:** รายงาน Lab 04

**ขั้นตอน**
1. เปิดรายงาน Lab 04 มุมขวาบน: **Add a control → Date range control** ค่าเริ่มต้น *Advanced: Today minus 12 months → Today* คลิกขวา → **Make report-level**
2. **Drop-down list** บน `sales_channel` (เลือกหลายค่า แสดง metric `sales_amount` เปิดช่องค้นหา) ทำเป็น report-level
3. **Drop-down list** บน `payment_method`, **Slider** บน `discount` (0–30%) และ **Input box** บน `customer_id` (operator *contains*)
4. **Editor filter** ระดับ chart: ที่ scorecard KPI ทุกอันเพิ่ม filter `Completed only`: Include `order_status` Equal to `Completed` ตรวจว่า Net Sales ลดลง
5. เปิด **Cross-filtering** (Setup → Chart interactions) ที่ bar ช่องทาง ตาราง payment และ donut คลิก *Marketplace* บน bar → สังเกตทุก chart
6. ทดสอบ group: เลือก stacked column + ตาราง payment → คลิกขวา → **Group** เพิ่ม drop-down บน `order_status` *ภายใน* group ยืนยันว่ากรองเฉพาะ 2 chart นั้น
7. **Add a control → Button → Reset**: label *Clear filters* วางมุมขวาบน
8. เปิด **Filter bar** (File → Report settings) แล้วเปรียบเทียบกับ control ของคุณ
9. **Share → Get report link → Link to current report state** หลังเลือก *Marketplace* + *Credit Card*; เปิดลิงก์ในแท็บใหม่

**ผลที่ควรได้**
- Date range และ control ช่องทางมีผลทุกหน้า; drop-down สถานะมีผลเฉพาะ chart ใน group; คลิก bar แล้ว cross-filter ทั้งหน้า; ปุ่ม reset ล้างทุกอย่าง

**คำถามตรวจสอบ**
1. เพื่อนร่วมงานเพิ่มตารางจาก `[LSG] customers` ในหน้านี้ ทำไม drop-down ช่องทางไม่กรองมัน? แก้ได้ 2 วิธีอย่างไร?
2. editor filter `Completed only` ต่างจาก drop-down บน `order_status` ที่เลือก *Completed* อย่างไร?
3. เมื่อไร *Filter bar* เป็นทางเลือกที่ดีกว่า control?

**Stretch goal:** เพิ่มหน้าที่สองที่มีแถบ KPI เดียวกันแล้วยืนยันว่า control ระดับ report ติดไปด้วย; จากนั้นทำให้ KPI หนึ่งตัว *ไม่* ตอบสนอง date control (Custom date range) และอธิบายว่ามีประโยชน์เมื่อไร

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
