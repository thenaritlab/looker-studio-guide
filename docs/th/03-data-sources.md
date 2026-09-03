🌐 [ภาษาไทย](../th/03-data-sources.md) | [English](../en/03-data-sources.md)

# 03 · Data Source และ Connector (Sheets, CSV, BigQuery)

> ⏱ **เวลาโดยประมาณ:** 60 นาที · 📅 **วันตาม Roadmap:** สัปดาห์ 1 · วันที่ 3–4 · 🎯 **ระดับ:** Basic

**ในบทนี้**
- [ประเภทของ connector](#1-ประเภทของ-connector)
- [องค์ประกอบของ data source](#2-องค์ประกอบของ-data-source)
- [Google Sheets connector](#3-google-sheets-connector)
- [File upload (CSV)](#4-file-upload-csv)
- [BigQuery connector](#5-bigquery-connector)
- [ชนิด field และ aggregation — สำคัญกว่าที่คิด](#6-ชนิด-field-และ-aggregation--สำคัญกว่าที่คิด)
- [Credential: Owner กับ Viewer](#7-credential-owner-กับ-viewer)
- [Data freshness และ cache](#8-data-freshness-และ-cache)
- [Reusable กับ embedded และการสลับ data source](#9-reusable-กับ-embedded-และการสลับ-data-source)

## 1. ประเภทของ connector

**Add data** จะเปิดแกลเลอรี connector ซึ่งมี 2 แท็บ

| แท็บ | ตัวอย่าง | ผู้ดูแล |
|---|---|---|
| **Google connectors** | Google Sheets, BigQuery, File upload, Google Analytics (GA4), Google Ads, Search Console, YouTube Analytics, Cloud SQL for MySQL/PostgreSQL, MySQL, PostgreSQL, Microsoft SQL Server, Extract Data, Looker, Google Cloud Storage | Google สร้างและซัพพอร์ตเอง |
| **Partner connectors** | Supermetrics, Funnel, Windsor.ai, Power My Analytics และอีกหลายร้อยตัวสำหรับ Meta Ads, TikTok, Shopify, HubSpot, LINE Ads ฯลฯ | บริษัทภายนอก หลายตัวมีค่าใช้จ่าย |

> **💡 Tip** ก่อนจ่ายเงินซื้อ partner connector ให้เช็กก่อนว่าแพลตฟอร์มนั้น export ไป BigQuery หรือ Google Sheets ได้เองไหม (Meta, Shopify, HubSpot ทำได้หมด) แล้วใช้ Google connector ฟรีแทน

## 2. องค์ประกอบของ data source

Data source = **การเชื่อมต่อ** + **schema** เปิดดูได้จากรายการ Data sources → คลิกชื่อ จะเห็น

- **Field name** — เปลี่ยนชื่อได้อิสระ และมีผลกับทุกรายงานที่ใช้ data source นี้
- **Type** — Number, Text, Date & Time (มีรูปแบบย่อยมาก), Boolean, Geo (Country, City, Latitude/Longitude…), URL, Image, Currency
- **Default aggregation** — Sum, Average, Count, Count Distinct, Min, Max, None (dimension จะเป็น None)
- **Description** — แสดงเป็น tooltip ให้ผู้แก้ไข
- **Add a field** / **Add a parameter** — calculated field ระดับ data source (บทที่ 06)
- **Data credentials**, **Data freshness**, **Community visualizations access** (แถบด้านบน)

## 3. Google Sheets connector

เหมาะกับ: ตารางอ้างอิงเล็ก ๆ ข้อมูลที่กรอกมือ (เป้าหมาย, ตาราง mapping), งานต้นแบบ

1. **Add data → Google Sheets** → เลือก spreadsheet → เลือกแท็บ
2. ตัวเลือก: **Use first row as headers**, **Include hidden and filtered cells**, **Optional range** (เช่น `A1:N`)
3. คลิก **Add**

กติกาของแท็บที่เป็นมิตรกับ Looker Studio
- หัวตาราง 1 แถว ไม่มี merged cell ไม่มีแถว/คอลัมน์ว่างคั่นกลางข้อมูล
- 1 คอลัมน์ 1 ชนิดข้อมูล (คอลัมน์ที่ปนตัวอักษรกับตัวเลขจะกลายเป็น Text)
- วันที่ต้องเป็นวันที่จริง ไม่ใช่ข้อความอย่าง `1/9/26` ถ้าไม่แน่ใจใช้ `YYYY-MM-DD`
- ไม่ควรเกิน ~100k เซลล์ถ้าอยากให้รายงานลื่น เกินกว่านั้นให้ย้ายไป BigQuery

> **⚠️ Warning** connector ของ Sheets ดึง **ทั้งชีต** ทุกครั้งที่ refresh ชีต 200k แถวจะทำให้ chart ช้าและอาจ timeout

## 4. File upload (CSV)

เหมาะกับ: การวิเคราะห์ครั้งเดียว หรือข้อมูลที่เอาไปไว้ใน Sheets ไม่ได้

1. **Add data → File upload** → ลากไฟล์ CSV มาวาง ขีดจำกัด 100 MB ต่อไฟล์ รวม 2 GB ต่อผู้ใช้ ต้องเป็น UTF-8
2. ไฟล์ที่อัปโหลดจะกลายเป็น **data set** ที่เก็บใน Looker Studio อัปโหลดไฟล์เพิ่มที่มี schema เดียวกันเพื่อ append ได้
3. แก้ไขข้อมูลในที่ไม่ได้ ต้องอัปโหลดใหม่

## 5. BigQuery connector

เหมาะกับ: ข้อมูลมากกว่า ~100k แถว, ข้อมูล production แบบ live, การ join ที่ทำใน SQL

เชื่อมต่อได้ 4 แบบ

| โหมด | ใช้เมื่อ |
|---|---|
| **My projects** → dataset → table/view | เป็นเจ้าของข้อมูลเอง ง่ายและเร็วที่สุด |
| **Shared projects** | มีคนแชร์ project ID มาให้ |
| **Custom query** | อยากเขียน SQL (aggregate, join, parameter) รองรับ `@parameter` (บทที่ 08) |
| **Public datasets** | ใช้เรียนและเดโม เช่น `bigquery-public-data.thelook_ecommerce` |

ตั้งค่า sandbox ฟรี
1. ไปที่ **https://console.cloud.google.com** → สร้างโปรเจกต์ (เช่น `looker-guide-2026`)
2. เปิด **BigQuery** โหมด sandbox ให้พื้นที่ 10 GB และ query 1 TB ต่อเดือน ไม่ต้องผูกบัตร
3. สร้าง dataset ชื่อ `looker_guide` ที่ region `asia-southeast1` แล้วโหลด CSV ทั้ง 6 ไฟล์ (คำสั่งอยู่ใน [datasets/README.md](../../datasets/README.md))

> **💡 Tip** ตารางที่ partition ตามวันที่ connector จะมีตัวเลือก **Use `_PARTITIONTIME` as date range dimension** เปิดไว้จะทำให้ date range control ตัด partition ได้ ประหยัดค่าใช้จ่าย

## 6. ชนิด field และ aggregation — สำคัญกว่าที่คิด

ชนิดข้อมูลผิดคือสาเหตุอันดับ 1 ของคำถาม "ทำไม chart ว่างเปล่า"

| อาการ | สาเหตุ | วิธีแก้ |
|---|---|---|
| `order_date` เป็น text, สร้าง time series ไม่ได้ | ตรวจจับเป็น Text | เปลี่ยน type เป็น **Date** (หรือ Date & Time แล้วระบุรูปแบบ) |
| `discount` รวมแล้วได้ 4,391 | aggregation เริ่มต้นเป็น Sum ทั้งที่เป็นอัตรา | เปลี่ยนเป็น **Average** หรือสร้าง field ถ่วงน้ำหนักให้ถูกต้อง |
| `customer_id` แสดงเป็นตัวเลขมีลูกน้ำ | type เป็น Number | เปลี่ยนเป็น **Text** |
| แผนที่ไม่ขึ้นอะไรเลย | type เป็น Text | เปลี่ยนเป็น **Geo → Country / Region / City** |
| `unit_price` × `quantity` ในตารางผิด | คูณกันหลัง aggregate | สร้าง calculated field ระดับแถว `unit_price * quantity` |

ใน data source editor คลิก dropdown ของ type ข้าง field เพื่อเปลี่ยน มีผลทุกที่ที่ใช้ data source นี้

## 7. Credential: Owner กับ Viewer

ที่ **Data credentials**

- **Owner's credentials** (ค่าเริ่มต้น): ผู้อ่านเห็นข้อมูลผ่านสิทธิ์ของ*เจ้าของ* ง่าย และเป็นมาตรฐานของ dashboard ทั่วไป
- **Viewer's credentials**: ผู้อ่านแต่ละคนต้องมีสิทธิ์เข้าถึง Sheet / ตาราง BigQuery เอง ใช้เมื่อบังคับ row-level security ไว้ที่ BigQuery (authorized view, RLS policy) และต้องการให้รายงานเคารพสิทธิ์นั้น
- **Service account** (เฉพาะ BigQuery): ตัวตนเฉพาะสำหรับรายงาน จะได้ไม่พังเมื่อพนักงานลาออก แนะนำสำหรับ production

> **🔁 มาจาก Tableau/Power BI?** Owner's credentials ≈ embedded credential ของ published data source ส่วน Viewer's credentials ≈ "prompt user" / SSO passthrough

## 8. Data freshness และ cache

Looker Studio cache ผลลัพธ์ของ query **Data freshness** (แถบบนของ data source) กำหนดว่าจะเชื่อ cache นานแค่ไหน

| Connector | ตัวเลือก |
|---|---|
| Google Sheets และ partner connector ส่วนใหญ่ | 15 นาที · 1 ชม. · 4 ชม. · 12 ชม. |
| BigQuery | 1 นาที · 15 นาที · 1 ชม. · 4 ชม. · 12 ชม. |
| File upload | คงที่จนกว่าจะอัปโหลดใหม่ |

ผู้อ่านสั่ง refresh เองได้ด้วยปุ่ม **↻ Refresh data** (มุมขวาบนใน view mode) ทุกครั้งที่ refresh คือรัน query ใหม่ ดังนั้น freshness 1 นาทีบน BigQuery กับรายงานที่คนเปิดเยอะอาจมีค่าใช้จ่ายจริง

## 9. Reusable กับ embedded และการสลับ data source

- **Embedded** อยู่ในรายงานเดียว สร้างจาก **Add data** ภายในรายงาน
- **Reusable** ปรากฏที่หน้า Home → **Data sources** แชร์แยกได้ และใช้กับหลายรายงาน สร้างจาก **Create → Data source** หรือแปลงจาก embedded ที่ **Resource → Manage added data sources → Make reusable**

การชี้ทั้งรายงานไปตารางใหม่ (เช่น ชีต dev → ตาราง BigQuery prod)
1. **File → Report settings → Data source → Select data source** หรือ
2. เลือกหลาย chart → Properties → **Data source** → เปลี่ยน หรือ
3. **File → Make a copy** แล้วเลือก data source ใหม่ในหน้าต่างทำสำเนา — นี่คือวิธีทำ template

ชื่อ field ต้องตรงกัน ไม่เช่นนั้น chart จะขึ้น *Invalid dimension/metric* ให้ไปแก้ใน properties panel

---
**Lab:** [Lab 03 — เชื่อมต่อ Sheets, CSV และ BigQuery](../../labs/lab03-data-sources/README.md)

← [ก่อนหน้า: 02 · เริ่มต้นใช้งาน](02-getting-started.md) | [ถัดไป: 04 · Chart และ Table พื้นฐาน →](04-charts-tables.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](00-toc.md)</sub>
