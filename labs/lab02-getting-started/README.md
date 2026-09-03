# Lab 02 · Your First Report / รายงานแรกของคุณ

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/02-getting-started.md) | [TH](../../docs/th/02-getting-started.md)

---

## 🇺🇸 English

**Objective:** Build a two-page Looker Studio report from `sales_orders.csv` in Google Sheets with a scorecard, a time series and a table, then share it.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 45 min | Basic | Week 1 · Day 2 |

**Prerequisites**
- Google account; `datasets/sales_orders.csv` downloaded.
- Chapter 02 read.

**Steps**
1. Open Google Sheets → **File → Import → Upload** `sales_orders.csv` → *Replace spreadsheet* → *Detect automatically*. Rename the file `LS Guide – Sales Orders`.
2. Go to https://lookerstudio.google.com → **Create → Report**.
3. In *Add data to report* choose **Google Sheets** → pick the file and tab → keep *Use first row as headers* ✔ → **Add**.
4. Delete the default table. **Add a chart → Scorecard**: Metric `sales_amount` (SUM). Rename label to *Total Sales*. Style → Compact numbers ✔, Currency THB.
5. **Add a chart → Time series**: Dimension `order_date`, Metric `sales_amount`. Set date granularity to **Month** (click the pencil next to the dimension).
6. **Add a chart → Table**: Dimension `sales_channel`, Metrics `sales_amount`, `profit`, `Record Count`. Sort by `sales_amount` desc. Style → show summary row ✔.
7. **Add a control → Date range control**; default *Last 12 months* — wait, the data ends Aug 2026: use **Advanced → Fixed** 1 Jan 2025 – 31 Aug 2026 instead.
8. Add a **Text** title: "Siam Goods · Sales Overview". Rename the page *Overview*.
9. **Page → New page** → name it *Detail*. Add a **Table** with `order_id`, `order_date`, `customer_id`, `sales_amount` (rows per page 50).
10. **View** mode → check both pages. **Share → Get report link** → *Anyone in your organisation / anyone with the link (viewer)* and open in an incognito window.

**Expected result**
- Scorecard shows total sales in the tens of millions THB; time series shows Nov–Dec peaks; table lists 4–5 channels with a summary row.
- The date range control changes all three charts.

**Checkpoint questions**
1. Which channel has the highest total sales? Which has the highest profit — the same one?
2. What happens to the time series when you change granularity to *Week*?
3. Why does the scorecard *not* change when you sort the table?

**Stretch goal:** Add a second scorecard for `profit`, then a **Comparison date range → Previous period** to both scorecards and explain the arrows.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** สร้างรายงาน Looker Studio 2 หน้าจาก `sales_orders.csv` ใน Google Sheets ด้วย scorecard, time series และ table แล้วแชร์

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 45 นาที | Basic | สัปดาห์ 1 · วันที่ 2 |

**สิ่งที่ต้องมี**
- Google account; ดาวน์โหลด `datasets/sales_orders.csv` แล้ว
- อ่านบทที่ 02 แล้ว

**ขั้นตอน**
1. เปิด Google Sheets → **File → Import → Upload** `sales_orders.csv` → *Replace spreadsheet* → *Detect automatically* ตั้งชื่อไฟล์ `LS Guide – Sales Orders`
2. ไปที่ https://lookerstudio.google.com → **Create → Report**
3. ใน *Add data to report* เลือก **Google Sheets** → เลือกไฟล์และแท็บ → คง *Use first row as headers* ✔ → **Add**
4. ลบตารางเริ่มต้น **Add a chart → Scorecard**: Metric `sales_amount` (SUM) เปลี่ยน label เป็น *Total Sales* Style → Compact numbers ✔, Currency THB
5. **Add a chart → Time series**: Dimension `order_date`, Metric `sales_amount` ตั้ง granularity เป็น **Month** (คลิกดินสอข้าง dimension)
6. **Add a chart → Table**: Dimension `sales_channel`, Metric `sales_amount`, `profit`, `Record Count` เรียงตาม `sales_amount` มากไปน้อย Style → show summary row ✔
7. **Add a control → Date range control** ข้อมูลจบที่ ส.ค. 2569 ดังนั้นใช้ **Advanced → Fixed** 1 ม.ค. 2568 – 31 ส.ค. 2569
8. เพิ่ม **Text** เป็นชื่อเรื่อง: "Siam Goods · Sales Overview" เปลี่ยนชื่อหน้าเป็น *Overview*
9. **Page → New page** → ชื่อ *Detail* เพิ่ม **Table** ที่มี `order_id`, `order_date`, `customer_id`, `sales_amount` (50 แถวต่อหน้า)
10. โหมด **View** → ตรวจทั้งสองหน้า **Share → Get report link** → *Anyone in your organisation / anyone with the link (viewer)* แล้วเปิดใน incognito

**ผลที่ควรได้**
- Scorecard แสดงยอดขายรวมหลายสิบล้านบาท; time series มียอดพุ่งช่วง พ.ย.–ธ.ค.; ตารางมี 4–5 ช่องทางพร้อมแถวรวม
- Date range control เปลี่ยน chart ทั้งสามพร้อมกัน

**คำถามตรวจสอบ**
1. ช่องทางไหนยอดขายรวมสูงสุด? กำไรสูงสุดคือช่องทางเดียวกันไหม?
2. เกิดอะไรขึ้นกับ time series เมื่อเปลี่ยน granularity เป็น *Week*?
3. ทำไม scorecard *ไม่* เปลี่ยนเมื่อคุณเรียงตาราง?

**Stretch goal:** เพิ่ม scorecard ที่สองสำหรับ `profit` แล้วใส่ **Comparison date range → Previous period** ให้ทั้งสอง scorecard และอธิบายความหมายของลูกศร

---

← [ก่อนหน้า / Previous: บท 02 / Chapter 02](../../docs/th/02-getting-started.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/02-getting-started.md) · [EN](../../docs/en/02-getting-started.md) | [ถัดไป / Next: Lab 03 — Data Sources](../lab03-data-sources/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
