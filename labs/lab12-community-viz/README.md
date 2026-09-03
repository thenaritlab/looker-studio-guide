# Lab 12 · Use a Gallery Viz and Deploy a Custom One / ใช้ viz จาก gallery และ deploy viz ของตัวเอง

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/12-community-viz.md) | [TH](../../docs/th/12-community-viz.md)

---

## 🇺🇸 English

**Objective:** Add two gallery visualizations to a report, then scaffold, build and deploy a minimal custom visualization to a Cloud Storage bucket.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Advanced | Week 5 · Day 23 |

**Prerequisites:** Node.js 18+, `gsutil`/`gcloud` authenticated, a Google Cloud project with billing (Cloud Storage is a few cents); Lab 04 sources.

**Steps**
1. New report *Community Viz – Lab 12*. Data source editor → **Community visualizations access → On** for `[LSG] sales_orders (BQ)`.
2. **Add a chart → Community visualizations → Explore more** → add **Sankey**: dimensions `sales_channel` → `payment_method`, metric `sales_amount`. Style: node color from theme.
3. Add a **Calendar heatmap** (or *Gantt*) on `[LSG] web_traffic (upload)`: date `date`, metric `sessions`.
4. Scaffold a custom viz:
   ```bash
   npm install -g @google/dscc-gen
   dscc-gen viz            # name: narit-bar, dev bucket: gs://<your-bucket>/narit-bar/dev, prod: .../prod
   cd narit-bar && npm install
   ```
5. Replace `src/index.json` and `src/index.js` with the chapter 12 §5 config and bar-chart code. In `src/manifest.json` set `name: "The Narit Lab – Simple Bar"` and your logo URL (or leave the default).
6. `npm run start` → confirm the local preview renders sample bars. `npm run build:dev && npm run push:dev`.
7. In Looker Studio: **Add a chart → Community visualizations → Build your own** → manifest path `gs://<your-bucket>/narit-bar/dev` → **Submit** → add it with `sales_channel` / `sales_amount`. Change *Bar color* in Style.
8. Add `dscc.sendInteraction` to make clicking a bar cross-filter the page (see dscc docs: `interactions` in `index.json` with `type: FILTER`). Re-push and test.
9. Turn **Community visualizations access → Off** on the data source and observe what happens to all three viz. Turn it back on.
10. Write a short *Security note* Text box: who can see the data these viz receive.

**Expected result**
- Sankey shows channel → payment flows; heatmap shows weekday/weekend pattern and Nov–Dec intensity; your custom bar renders with theme colors and re-colors from the Style panel.

**Checkpoint questions**
1. Why is a gallery viz a data-governance decision, not just a design one?
2. What does the `dscc` library provide that plain `fetch` cannot?
3. Which of the three visualizations would you keep in a production executive report, and why?

**Stretch goal:** Publish the custom viz to a public bucket, share the manifest path with a peer, and have them use it in their report.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** เพิ่ม visualization จาก gallery 2 ตัวในรายงาน แล้ว scaffold สร้าง และ deploy custom visualization แบบเล็กสุดขึ้น Cloud Storage bucket

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Advanced | สัปดาห์ 5 · วันที่ 23 |

**สิ่งที่ต้องมี:** Node.js 18+, `gsutil`/`gcloud` ที่ล็อกอินแล้ว, Google Cloud project ที่เปิด billing (Cloud Storage ค่าใช้จ่ายไม่กี่เซนต์); source จาก Lab 04

**ขั้นตอน**
1. รายงานใหม่ *Community Viz – Lab 12* Data source editor → **Community visualizations access → On** สำหรับ `[LSG] sales_orders (BQ)`
2. **Add a chart → Community visualizations → Explore more** → เพิ่ม **Sankey**: dimension `sales_channel` → `payment_method`, metric `sales_amount` Style: สี node จาก theme
3. เพิ่ม **Calendar heatmap** (หรือ *Gantt*) บน `[LSG] web_traffic (upload)`: date `date`, metric `sessions`
4. Scaffold custom viz
   ```bash
   npm install -g @google/dscc-gen
   dscc-gen viz            # ชื่อ: narit-bar, dev bucket: gs://<your-bucket>/narit-bar/dev, prod: .../prod
   cd narit-bar && npm install
   ```
5. แทน `src/index.json` และ `src/index.js` ด้วย config และโค้ด bar chart จากบทที่ 12 §5 ใน `src/manifest.json` ตั้ง `name: "The Narit Lab – Simple Bar"` และ URL logo ของคุณ (หรือคงค่าเริ่มต้น)
6. `npm run start` → ยืนยันว่า preview ในเครื่อง render แท่งตัวอย่าง `npm run build:dev && npm run push:dev`
7. ใน Looker Studio: **Add a chart → Community visualizations → Build your own** → พาธ manifest `gs://<your-bucket>/narit-bar/dev` → **Submit** → เพิ่มด้วย `sales_channel` / `sales_amount` เปลี่ยน *Bar color* ใน Style
8. เพิ่ม `dscc.sendInteraction` ให้คลิกแท่งแล้ว cross-filter ทั้งหน้า (ดูเอกสาร dscc: `interactions` ใน `index.json` ด้วย `type: FILTER`) push ใหม่แล้วทดสอบ
9. ปิด **Community visualizations access → Off** ที่ data source แล้วดูว่าเกิดอะไรกับ viz ทั้งสาม เปิดกลับ
10. เขียน Text box *Security note* สั้น ๆ: ใครเห็นข้อมูลที่ viz เหล่านี้ได้รับ

**ผลที่ควรได้**
- Sankey แสดงการไหลจากช่องทาง → วิธีจ่าย; heatmap แสดงรูปแบบวันทำงาน/สุดสัปดาห์และความเข้มช่วง พ.ย.–ธ.ค.; bar ของคุณ render ด้วยสี theme และเปลี่ยนสีได้จากแผง Style

**คำถามตรวจสอบ**
1. ทำไมการใช้ viz จาก gallery เป็นการตัดสินใจด้าน data governance ไม่ใช่แค่ดีไซน์?
2. ไลบรารี `dscc` ให้อะไรที่ `fetch` ธรรมดาให้ไม่ได้?
3. viz 3 ตัวนี้ตัวไหนที่คุณจะเก็บไว้ในรายงานผู้บริหาร production และทำไม?

**Stretch goal:** เผยแพร่ custom viz ไป bucket สาธารณะ แชร์พาธ manifest ให้เพื่อน แล้วให้เขาใช้ในรายงานของเขา

---

← [ก่อนหน้า / Previous: Lab 11 — Sharing & Pro](../lab11-sharing-pro/README.md) | 📖 [บทเรียนของ Lab นี้ / Chapter: TH](../../docs/th/12-community-viz.md) · [EN](../../docs/en/12-community-viz.md) | [ถัดไป / Next: Lab 13 — Looker Overview](../lab13-looker-overview/README.md) →

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](../../docs/th/00-toc.md) · [Back to TOC](../../docs/en/00-toc.md)</sub>
