🌐 [ภาษาไทย](../th/08-parameters.md) | [English](../en/08-parameters.md)

# 08 · Parameter และรายงานแบบ Dynamic

> ⏱ **เวลาโดยประมาณ:** 60 นาที · 📅 **วันตาม Roadmap:** สัปดาห์ 3 · วันที่ 14–15 · 🎯 **ระดับ:** Intermediate

**ในบทนี้**
- [Parameter คืออะไร](#1-parameter-คืออะไร)
- [การสร้าง parameter](#2-การสร้าง-parameter)
- [ผูก control เข้ากับ parameter](#3-ผูก-control-เข้ากับ-parameter)
- [Use case 1: what-if target simulator](#4-use-case-1-what-if-target-simulator)
- [Use case 2: สลับ dimension / metric แบบ dynamic](#5-use-case-2-สลับ-dimension--metric-แบบ-dynamic)
- [Use case 3: parameter ใน BigQuery custom query](#6-use-case-3-parameter-ใน-bigquery-custom-query)
- [Use case 4: ข้อความ dynamic, threshold และสกุลเงิน](#7-use-case-4-ข้อความ-dynamic-threshold-และสกุลเงิน)
- [Parameter ใน URL](#8-parameter-ใน-url)
- [ข้อจำกัดและเคล็ดลับ](#9-ข้อจำกัดและเคล็ดลับ)

## 1. Parameter คืออะไร

**Parameter** คือค่าที่มีชื่อ ซึ่งผู้อ่านเปลี่ยนได้และสูตรอ้างอิงได้ ต่างจาก filter ตรงที่ไม่ตัดแถวออก แต่ **เปลี่ยนวิธีคำนวณ field หรือเลือกว่าจะแสดง field ไหน**

| ชนิด | ตัวอย่างค่า |
|---|---|
| Text | `"THB"`, `"Sales"` |
| Number | `1.15`, `500000` |
| Boolean | `true / false` |
| List (text หรือ number, เลือกเดียวหรือหลายค่า) | `Region / Channel / Category` |

Parameter อยู่ได้ที่ **ระดับ data source** (ใช้ใน calculated field ของ source นั้นและ BigQuery query) หรือ **ระดับ report** (Resource → Manage parameters; ใช้ใน calculated field ระดับ report และ blend)

## 2. การสร้าง parameter

1. Data source editor → **Add a parameter** (หรือ Resource → Manage parameters → Add)
2. ตั้งชื่อ (`Target Growth`), ID (อัตโนมัติ เช่น `target_growth`), ชนิดข้อมูล, ค่าที่อนุญาต (any / list of values / range), ค่าเริ่มต้น
3. Save parameter จะแสดงในแผง Data เป็นสีม่วง

## 3. ผูก control เข้ากับ parameter

Control ที่ขับ parameter ได้: **Input box**, **Slider**, **Drop-down list**, **Fixed-size list**, **Checkbox**, **Button** เพิ่ม control แล้วใน Setup เลือก parameter เป็น **Control field** ตัวเลือกใน control จะมาจากค่าที่อนุญาตของ parameter

ตั้งค่า parameter ผ่าน **ลิงก์รายงาน** (URL) ได้ด้วย — ดู §8

## 4. Use case 1: what-if target simulator

คำถาม: "ถ้าปีหน้าโต 15% ต้องมีรายได้ต่อเดือนเท่าไร"

1. Parameter `growth_rate`: Number, ช่วง 0–1, step 0.01, ค่าเริ่มต้น 0.15 Control: **Slider**
2. Calculated field:
```sql
-- เป้ารายเดือนปีหน้า
SUM(sales_amount) * (1 + growth_rate)
```
3. Time series: `SUM(sales_amount)` และ field เป้าหมายเป็น 2 เส้น เลื่อน slider แล้วเส้นเป้าจะวาดใหม่ทันที

ต่อยอดด้วย `target_margin` และเน้นเดือนที่ `SUM(profit)/SUM(sales_amount) < target_margin` ด้วย conditional formatting

## 5. Use case 2: สลับ dimension / metric แบบ dynamic

คำถาม: "แสดงยอดขายตาม ___" ให้ผู้อ่านเลือก Region, Channel หรือ Category

1. Parameter `dim_selector`: Text, list of values `Region`, `Channel`, `Category`, ค่าเริ่มต้น `Region` Control: **Drop-down list** (single select)
2. Calculated dimension:
```sql
CASE dim_selector
  WHEN "Region"   THEN region
  WHEN "Channel"  THEN sales_channel
  WHEN "Category" THEN category
END
```
3. ใช้ field นี้เป็น dimension ของ bar chart; ตั้งชื่อ chart ด้วย parameter (ดู §7)

Metric ก็ทำแบบเดียวกัน
```sql
CASE metric_selector
  WHEN "Sales"  THEN SUM(sales_amount)
  WHEN "Profit" THEN SUM(profit)
  WHEN "Orders" THEN COUNT_DISTINCT(order_id)
END
```

> **💡 Tip** Looker Studio มี component **Dimension control** และ **Metric control** โดยเฉพาะที่ทำสิ่งนี้ได้โดยไม่ต้องเขียน CASE — ทำงานร่วมกับ **Optional metrics** และ drill-down ใช้สำหรับการสลับง่าย ๆ; ใช้ CASE เมื่อต้องการตรรกะเฉพาะ

## 6. Use case 3: parameter ใน BigQuery custom query

ใน data source แบบ BigQuery **Custom query** ติ๊ก **Enable date range parameters** และ **Enable parameters** แล้วอ้างอิงเป็น `@name`

```sql
SELECT
  DATE_TRUNC(order_date, MONTH) AS month,
  sales_channel,
  SUM(sales_amount) AS sales,
  SUM(profit) AS profit
FROM `your_project.looker_guide.sales_orders`
WHERE order_date BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE)
                     AND PARSE_DATE('%Y%m%d', @DS_END_DATE)
  AND sales_channel IN UNNEST(@channels)        -- list parameter แบบเลือกหลายค่า
  AND discount <= @max_discount                  -- number parameter
GROUP BY 1, 2
```

- `@DS_START_DATE`, `@DS_END_DATE` (สตริง `YYYYMMDD`) และ `@DS_USER_EMAIL` (อีเมลผู้อ่าน สำหรับ row-level security) มีให้ในตัว
- Parameter ของเราต้องสร้างใน data source และส่งเป็นค่าที่มีชนิดข้อมูล List parameter มาเป็น array — ใช้ `IN UNNEST(@param)`

รูปแบบนี้ผลักการกรองเข้า BigQuery **ก่อน** aggregate: สแกน byte น้อยลง chart เร็วขึ้น

> **⚠️ Warning** อย่าต่อ parameter เข้าไปในสตริง SQL (ไม่จำเป็น — BigQuery bind ค่าให้อย่างปลอดภัย) Custom query ที่มี parameter จะ cache ข้ามค่าที่ต่างกันไม่ได้ ทุกครั้งที่เปลี่ยนค่าคือ query ใหม่

## 7. Use case 4: ข้อความ dynamic, threshold และสกุลเงิน

- **ชื่อเรื่องแบบ dynamic**: Scorecard ที่ใช้ metric `dim_selector` (aggregation: none, เป็นข้อความ) วางเป็นหัวเรื่องจะแสดง "Region", "Channel"… หรือใช้ `CONCAT("Sales by ", dim_selector)`
- **Threshold**: parameter `sla_days`; field `IF(DATETIME_DIFF(ship_date, order_date, DAY) > sla_days, "Late", "On time")` ป้อนให้ pie และ filter
- **แปลงสกุลเงิน**: parameter `fx_rate` (ค่าเริ่มต้น 36.5); field `SUM(sales_amount) / fx_rate` ตั้งชื่อ "Sales (USD)"
- **สลับมุมมอง**: Boolean parameter `show_profit`; `IF(show_profit, SUM(profit), SUM(sales_amount))`

## 8. Parameter ใน URL

ลิงก์รายงานรับค่า parameter ผ่าน query string `params` (JSON ที่ URL-encode)

```
https://lookerstudio.google.com/reporting/REPORT_ID/page/PAGE_ID?params=%7B%22ds0.growth_rate%22%3A0.2%7D
```

ถอดรหัสแล้ว: `{"ds0.growth_rate":0.2}` โดย `ds0` คือ alias ของ data source ที่เห็นใน **Resource → Manage added data sources** (เอาเมาส์ชี้ที่ source) ส่ง filter แบบเดียวกันได้ด้วย key `df` ใช้ **Share → Get report link → Link to current report state** เพื่อได้ตัวอย่างที่ใช้งานได้แล้วแก้ต่อ

การใช้งาน: embed รายงานในพอร์ทัลแล้วส่ง region ของลูกค้ามาจาก URL ของพอร์ทัล

## 9. ข้อจำกัดและเคล็ดลับ

- Parameter เป็น **ต่อ session ของผู้อ่าน** — ผู้อ่านสองคนถือค่าต่างกันพร้อมกันได้
- Text parameter ที่ใช้ใน CASE ต้องตรงกับค่าทุกตัวอักษร (แยกตัวพิมพ์เล็ก-ใหญ่)
- บาง connector ใช้ parameter เป็น dimension ตรง ๆ ไม่ได้; ครอบด้วย calculated field
- ใช้ parameter ให้น้อยและติดป้าย control ให้ชัด ผู้อ่านมักสับสนว่า control ของ parameter คือ filter
- Version history กู้คืน parameter และ control ได้เหมือน component อื่น

---
**Lab:** [Lab 08 — What-if simulator และ BigQuery query แบบมี parameter](../../labs/lab08-parameters/README.md)

← [ก่อนหน้า: 07 · Data Blending](07-blending.md) | [ถัดไป: 09 · หลักการออกแบบ Dashboard →](09-dashboard-design.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](00-toc.md)</sub>
