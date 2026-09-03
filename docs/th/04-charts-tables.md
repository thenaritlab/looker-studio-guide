🌐 [ภาษาไทย](../th/04-charts-tables.md) | [English](../en/04-charts-tables.md)

# 04 · Chart และ Table พื้นฐาน การจัดรูปแบบ Theme

> ⏱ **เวลาโดยประมาณ:** 60 นาที · 📅 **วันตาม Roadmap:** สัปดาห์ 1 · วันที่ 5 + Lab สัปดาห์ 2 · วันที่ 6 · 🎯 **ระดับ:** Basic

**ในบทนี้**
- [Chart ประกอบด้วยอะไรบ้าง](#1-chart-ประกอบด้วยอะไรบ้าง)
- [คู่มือเลือกชนิด chart](#2-คู่มือเลือกชนิด-chart)
- [Table และ Pivot table เชิงลึก](#3-table-และ-pivot-table-เชิงลึก)
- [Scorecard และการเปรียบเทียบ](#4-scorecard-และการเปรียบเทียบ)
- [Time series, Bar, Line, Combo](#5-time-series-bar-line-combo)
- [การจัดรูปแบบตัวเลข วันที่ และ Conditional formatting](#6-การจัดรูปแบบตัวเลข-วันที่-และ-conditional-formatting)
- [Theme และ Layout](#7-theme-และ-layout)
- [Optional metric, Drill-down และ Metric slider](#8-optional-metric-drill-down-และ-metric-slider)

## 1. Chart ประกอบด้วยอะไรบ้าง

ทุก chart ใน Looker Studio คือ **data source + dimension + metric + date range + sort + filter + style** แท็บ **Setup** ดูแล 6 อย่างแรก แท็บ **Style** ดูแลอย่างสุดท้าย เวลา chart ดูผิดปกติให้เช็ก Setup ก่อน — 80% ของปัญหามาจาก aggregation หรือ date range

![เมนู Add a chart](../../assets/images/ch04-01.png)

## 2. คู่มือเลือกชนิด chart

| คำถามที่ต้องการตอบ | ใช้ | หลีกเลี่ยง |
|---|---|---|
| ตอนนี้ตัวเลขเท่าไร | **Scorecard** | Gauge (เว้นแต่มีเป้าหมายชัดเจน) |
| เปลี่ยนแปลงตามเวลาอย่างไร | **Time series** / Line | Pie |
| หมวดไหนใหญ่สุด | **Bar** (แนวนอน เรียงลำดับ) | Column ที่มี 20+ หมวด |
| สัดส่วนของทั้งหมด (≤5 ส่วน) | **Donut / Pie** หรือ 100% stacked bar | Pie 10 ชิ้น |
| 2 metric สัมพันธ์กันไหม | **Scatter** / Bubble | Dual-axis line ถ้าหน่วยเดียวกัน |
| รายละเอียดรายแถว | **Table** พร้อม heatmap / bar | Pivot ทั้งที่ dimension เดียวก็พอ |
| Cross-tab 2 dimension | **Pivot table** | Table 30 คอลัมน์ |
| อยู่ที่ไหนบนแผนที่ | **Google Maps** (bubble/filled) หรือ Geo chart | อะไรก็ตามที่เป็น 3D |
| ขั้นตอนของ funnel | **Funnel** (มีให้ในตัว) หรือ bar | Pie |
| การกระจายตามเวลาแยกหมวด | **Stacked bar** / Area | Pie หลายอัน |
| ข้อความเล่าเรื่อง / KPI | **Text** ประกอบ scorecard | — |

> **🔁 มาจาก Tableau?** chart ใน Looker Studio เป็นชนิดตายตัว ไม่ใช่ grammar แบบ "Show Me" กราฟ dual-axis เป็นชนิดของตัวเอง (**Combo chart**) ไม่ใช่การซ้อน mark 2 ชั้น

## 3. Table และ Pivot table เชิงลึก

**Table**
- ใส่ได้สูงสุด 10 dimension และ 20 metric, **Rows per page** 5–5000, **Show summary row** สำหรับผลรวม
- **Style → Metric** เลือกแสดงคอลัมน์เป็น **Number**, **Heatmap** หรือ **Bar** (แท่งในเซลล์เหมาะกับการจัดอันดับ)
- **Wrap text**, **Row numbers**, **Show pagination** อยู่ใน Style
- ปรับความกว้างคอลัมน์ได้โดยลากที่หัวตารางใน Edit mode หรือใช้ **Fit to data**

**Pivot table**
- มี row dimension, column dimension, metric; ขยาย/ยุบได้เมื่อมี row dimension หลายชั้น
- ผลรวมแยกแถว/คอลัมน์ได้ (**Show totals**)
- จำกัดที่ 500k เซลล์ที่แสดง; column dimension ควรมีค่าไม่มาก (เดือน ภูมิภาค) ไม่ใช่ order ID

![Table พร้อม heatmap และ bar](../../assets/images/ch04-02.png)

## 4. Scorecard และการเปรียบเทียบ

Scorecard แสดง metric ที่ aggregate แล้ว 1 ค่า ฟีเจอร์ 2 อย่างที่ทำให้กลายเป็น KPI tile

1. **Comparison date range** (Setup → Date range → Comparison): *Previous period*, *Previous year* หรือกำหนดเอง จะแสดงส่วนต่างเป็น % หรือค่าจริง สีเขียว/แดง
2. **Compact numbers** (Style): แสดง `1.23M` แทน `1,234,567` ตั้ง **Decimal precision** 1–2 ตำแหน่ง

รูปแบบที่ใช้บ่อย
- ยอดขายเดือนนี้เทียบเดือนก่อน: date range เริ่มต้น *This month*, comparison *Previous period*
- YTD เทียบ YTD ปีก่อน: *Year to date*, comparison *Previous year*
- อัตรากำไร: metric = calculated field `SUM(profit) / SUM(sales_amount)` จัดรูปแบบเป็น Percent (บทที่ 06)

![Scorecard พร้อม comparison](../../assets/images/ch04-04.png)

> **💡 Tip** วาง scorecard 3–5 ใบเรียงเป็นแถวบนสุดของหน้า — เรียกว่า *KPI strip* ผู้อ่านคาดหวังแบบนี้

## 5. Time series, Bar, Line, Combo

**Time series** ต้องใช้ dimension ชนิด Date ใน Setup ทำได้ดังนี้
- เปลี่ยนความละเอียด: คลิกไอคอนปฏิทินที่ dimension → *Year, Quarter, Month, Week, Day, Hour…*
- เพิ่ม **Breakdown dimension** (เช่น `sales_channel`) เพื่อให้มีหลายเส้น จำกัดจำนวนเส้นที่ **Number of series**
- **Trendline** (linear/exponential/polynomial) และ **Reference line** (ค่าคงที่, metric หรือ parameter) อยู่ใน Style
- **Missing data**: line to zero / line breaks / linear interpolation

**Bar/Column**: เปิด **Stacked** หรือ **100% stacked** ใน Setup; แท่งแนวนอนอ่านง่ายกว่าเมื่อป้ายชื่อยาว; เรียงตาม metric เสมอเว้นแต่ลำดับมีความหมาย (เดือน)

**Combo chart**: แท่ง + เส้น มี 2 แกน Y ใช้เมื่อหน่วยต่างกัน (รายได้กับ margin %) กำหนดแกนซ้าย/ขวาให้แต่ละ metric ใน Style

## 6. การจัดรูปแบบตัวเลข วันที่ และ Conditional formatting

**รูปแบบตัวเลข** (Style → ต่อ metric หรือตั้งที่ data source)
- ชนิด: Number, Percent, Currency (เลือก THB/USD…), Duration
- Compact numbers, decimal precision, prefix/suffix

**รูปแบบวันที่**: ตั้ง type เป็น Date ที่ data source แล้วเลือกรูปแบบแสดงผล (เช่น `MMM YYYY`) หรือตั้งระดับ chart ที่ Style

**Conditional formatting** (table, scorecard, pivot): Style → **Conditional formatting → Add** — สร้างกฎเช่น *ถ้า `profit` < 0 ให้ตัวหนังสือสีแดง* หรือไล่สีทั้งคอลัมน์ กฎอ้างอิง field อื่นได้ ตารางที่เรียงตามยอดขายจึงยังไฮไลต์ margin ต่ำได้

## 7. Theme และ Layout

**Theme and layout** (toolbar) มี 2 แท็บ

- **Theme**: เลือก theme สำเร็จรูป หรือ **Extract theme from image** (อัปโหลดโลโก้แล้วระบบสร้างชุดสีให้) กด **Customize** เพื่อตั้งฟอนต์ สีกราฟ พื้นหลัง มุมโค้ง theme มีผลทั้งรายงาน ส่วน Style ของแต่ละ chart จะ override
- **Layout**: ขนาด canvas (เริ่มต้น 1200 × 900; ใช้กว้าง 1600 สำหรับจอทีวี), **Has margin**, **Grid settings** (snap to grid, 10 px กำลังดี), **Display mode** (Fit to width กับ Actual size), ชนิด navigation (Left, Tab, Top)

![Theme และ layout](../../assets/images/ch04-03.png)

> **💡 Tip** ตั้ง theme *ก่อน* สร้าง chart 30 อัน เปลี่ยนทีหลังก็ได้ แต่ style ที่ override ไว้รายอันจะยังอยู่และดูไม่เข้ากัน

## 8. Optional metric, Drill-down และ Metric slider

- **Optional metrics** (สวิตช์ใน Setup): ผู้อ่านเลือกเองได้ว่าจะแสดง metric ไหนในตารางหรือ chart — 1 chart ตอบโจทย์หลายคน
- **Drill down** (สวิตช์ใน Setup สำหรับ chart ที่มีหลาย dimension): ผู้อ่านคลิกแท่งเพื่อไล่จาก Category → Sub-category → Product ตั้ง **Default drill-down level** ได้
- **Metric sliders** (Setup): ผู้อ่านกรองแถวตามช่วงของ metric ได้ใน chart เอง เช่น แสดงเฉพาะช่องทางที่ยอดขาย > 1M
- **Chart header** (Style): Show on hover / Always show / Do not show — header มีปุ่ม export, sort และ drill

---
**Lab:** [Lab 04 — สร้างหน้าภาพรวมยอดขายที่จัดรูปแบบครบ](../../labs/lab04-charts-tables/README.md)

← [ก่อนหน้า: 03 · Data Source](03-data-sources.md) | [ถัดไป: 05 · Filter, Control และ Interaction →](05-filters-controls.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](00-toc.md)</sub>
