# Lab 13 · Write LookML for the Sales Model / เขียน LookML สำหรับ sales model

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/13-looker-overview.md) | [TH](../../docs/th/13-looker-overview.md)

---

## 🇺🇸 English

**Objective:** Translate the guide's data model and KPI definitions into LookML views and an explore — on paper (any text editor) or in a Looker trial — and write a one-page Looker vs Looker Studio recommendation.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Advanced | Week 5 · Day 25 |

**Prerequisites:** Chapter 13 read; `datasets/README.md` data dictionary; optional Looker trial (https://cloud.google.com/looker).

**Steps**
1. Create a folder `lookml/` with `sales_orders.view.lkml` from chapter 13 §3. Add measures `net_sales` (completed only, using `sql: CASE WHEN ${order_status} = 'Completed' THEN ${sales_amount} END ;;`), `return_rate`, `aov`.
2. Write `customers.view.lkml`: dimensions `customer_id` (primary key), `segment`, `region`, `province`, `age_group`, `loyalty_member` (yesno), `signup_date` dimension_group; measure `customer_count` (count).
3. Write `products.view.lkml`: `product_id` pk, `category`, `sub_category`, `brand`, `unit_price`, `status`; measure `avg_unit_price`.
4. Write `marketing_campaigns.view.lkml` with a `start` dimension_group and measures `total_spend`, `total_leads`, `roas`, `cpl`.
5. Write `sales.model.lkml`: connection, includes, explore `sales_orders` joining customers and products (`many_to_one`, `left_outer`); a second explore `marketing_campaigns`.
6. Add `access_filter` on `customers.region` with user attribute `region`, and a `datagroup` `daily_etl` with `sql_trigger: SELECT MAX(order_date) FROM looker_guide.sales_orders ;;` used by `persist_with`.
7. Validate mentally (or with the LookML Validator in a trial): every `${}` reference exists; every join has `relationship`; measures use only fields in the same view or `${view.field}`.
8. If you have a trial: create a project, paste the files, **Validate LookML**, open Explore *Sales*, build "Net Sales by Region and Month", save as a Look, add to a dashboard with a region filter.
9. Write `RECOMMENDATION.md` (≤ 1 page): for *Siam Goods*, recommend Looker Studio / Pro / Looker with three reasons, cost considerations and a migration path. Use the chapter 13 §7 table.

**Expected result**
- 5 LookML files that would pass validation; a recommendation memo.

**Checkpoint questions**
1. Where does the chapter 14 KPI `Net Sales` live in Looker vs Looker Studio, and who can change it?
2. Why does `relationship: many_to_one` matter for `total_sales` when products join in?
3. Which chapter 07 blend becomes unnecessary once the explore exists?

**Stretch goal:** Add an aggregate table via `aggregate_table` in the explore for month × channel and explain how aggregate awareness would route the Lab 10 rollup automatically.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** แปล data model และคำนิยาม KPI ของคู่มือเป็น LookML view และ explore — บนกระดาษ (text editor ใดก็ได้) หรือใน Looker trial — และเขียนคำแนะนำ Looker vs Looker Studio หนึ่งหน้า

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Advanced | สัปดาห์ 5 · วันที่ 25 |

**สิ่งที่ต้องมี:** อ่านบทที่ 13 แล้ว; data dictionary ใน `datasets/README.md`; Looker trial (ไม่บังคับ https://cloud.google.com/looker)

**ขั้นตอน**
1. สร้างโฟลเดอร์ `lookml/` ที่มี `sales_orders.view.lkml` จากบทที่ 13 §3 เพิ่ม measure `net_sales` (เฉพาะ completed ใช้ `sql: CASE WHEN ${order_status} = 'Completed' THEN ${sales_amount} END ;;`), `return_rate`, `aov`
2. เขียน `customers.view.lkml`: dimension `customer_id` (primary key), `segment`, `region`, `province`, `age_group`, `loyalty_member` (yesno), dimension_group `signup_date`; measure `customer_count` (count)
3. เขียน `products.view.lkml`: `product_id` pk, `category`, `sub_category`, `brand`, `unit_price`, `status`; measure `avg_unit_price`
4. เขียน `marketing_campaigns.view.lkml` ที่มี dimension_group `start` และ measure `total_spend`, `total_leads`, `roas`, `cpl`
5. เขียน `sales.model.lkml`: connection, include, explore `sales_orders` ที่ join customers และ products (`many_to_one`, `left_outer`); explore ที่สอง `marketing_campaigns`
6. เพิ่ม `access_filter` บน `customers.region` ด้วย user attribute `region` และ `datagroup` `daily_etl` ที่มี `sql_trigger: SELECT MAX(order_date) FROM looker_guide.sales_orders ;;` ใช้กับ `persist_with`
7. ตรวจสอบในใจ (หรือด้วย LookML Validator ใน trial): ทุก `${}` อ้างถึงสิ่งที่มีอยู่; ทุก join มี `relationship`; measure ใช้เฉพาะ field ใน view เดียวกันหรือ `${view.field}`
8. ถ้ามี trial: สร้าง project วางไฟล์ **Validate LookML** เปิด Explore *Sales* สร้าง "Net Sales by Region and Month" บันทึกเป็น Look เพิ่มลง dashboard พร้อม filter region
9. เขียน `RECOMMENDATION.md` (≤ 1 หน้า): สำหรับ *Siam Goods* แนะนำ Looker Studio / Pro / Looker พร้อม 3 เหตุผล ค่าใช้จ่าย และเส้นทาง migration ใช้ตารางในบทที่ 13 §7

**ผลที่ควรได้**
- ไฟล์ LookML 5 ไฟล์ที่น่าจะผ่าน validation; บันทึกคำแนะนำ

**คำถามตรวจสอบ**
1. KPI `Net Sales` ในบทที่ 14 อยู่ที่ไหนใน Looker เทียบกับ Looker Studio และใครเปลี่ยนได้?
2. ทำไม `relationship: many_to_one` สำคัญกับ `total_sales` เมื่อ join products เข้ามา?
3. Blend ไหนในบทที่ 07 ที่ไม่จำเป็นอีกเมื่อมี explore แล้ว?

**Stretch goal:** เพิ่ม aggregate table ผ่าน `aggregate_table` ใน explore สำหรับ month × channel และอธิบายว่า aggregate awareness จะเลือกใช้ rollup จาก Lab 10 อัตโนมัติอย่างไร

---

← [ก่อนหน้า / Previous: Lab 12 — Community Viz](../lab12-community-viz/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/13-looker-overview.md) · [EN](../../docs/en/13-looker-overview.md) | [ถัดไป / Next: Lab 14 — Capstone](../lab14-capstone/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
