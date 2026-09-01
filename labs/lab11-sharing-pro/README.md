# Lab 11 · Share, Schedule, Embed and Row-Level Security / แชร์ ตั้งเวลา Embed และ RLS

🌐 English first · ภาษาไทยด้านล่าง · Chapter: [EN](../../docs/en/11-sharing-pro.md) | [TH](../../docs/th/11-sharing-pro.md)

---

## 🇺🇸 English

**Objective:** Publish the Lab 09 report safely: viewer access, a scheduled PDF, an embedded copy, and per-user row filtering — then document a dev → prod process.

| ⏱ Time | 🎯 Level | 📅 Roadmap |
|---|---|---|
| 60 min | Advanced | Week 5 · Day 21 |

**Prerequisites:** Lab 09 report; a second Google account (or a colleague) to test as viewer.

**Steps**
1. Rename the report `Sales Overview` and make a copy `[DEV] Sales Overview`. Work on DEV from now on; promote at the end.
2. **Share** → add your test account as **Viewer**; link settings *Restricted*. Under *Manage access* tick *Disable downloading, printing and copying for viewers*. Open the link as the test account — confirm it works and that Export is missing.
3. Switch `[LSG] sales_orders (BQ)` to **Viewer's credentials**, reload as the test account → observe the *no access to underlying data* error. Grant `BigQuery Data Viewer` on the dataset to the test account **or** switch back to Owner's credentials. Write one sentence on which you would use in production and why.
4. **Row-level security**: upload a Sheet `rep_access` with columns `email`, `sales_rep_region` (your two emails → two regions). Blend it with sales (or add `region` via view) and set **Filter by email** on the `rep_access` data source using the `email` field. Test with both accounts.
5. **Schedule delivery**: Monday 08:00 Asia/Bangkok, pages 1–2, subject "Weekly Business Review". Set region control first and tick *include current filter state*. Send a test now.
6. **Embed**: File → Embed report → enable; paste the iframe into a Google Site (or an HTML file opened locally) and confirm it renders for a signed-in viewer.
7. **Report link with state**: Share → Get report link → *Link to current report state*; verify it opens with your controls pre-set.
8. **Promote**: name a version in DEV ("v1.0 – lab 11"), then copy the changed components into `Sales Overview` (Ctrl/⌘+C → paste in prod). Record the steps in an *About* page.
9. If you have **Looker Studio Pro**: create a Team workspace, move both reports and the data sources, assign a second Manager; note what changes in the Share dialog.

**Expected result**
- Test account sees only its region, cannot export, receives a PDF, and the embedded report loads.

**Checkpoint questions**
1. Why is "public link + owner's credentials" dangerous even for a demo dataset?
2. Which RLS method survives a viewer copying the report? Which does not?
3. Name two things a Team workspace solves that sharing cannot.

**Stretch goal:** Implement the same RLS in BigQuery with `CREATE ROW ACCESS POLICY` and viewer credentials; compare behaviour with the email filter.

---

## 🇹🇭 ภาษาไทย

**เป้าหมาย:** เผยแพร่รายงาน Lab 09 อย่างปลอดภัย: สิทธิ์ viewer, PDF ตามเวลา, สำเนา embed และการกรองแถวต่อผู้ใช้ — แล้วเขียนกระบวนการ dev → prod

| ⏱ เวลา | 🎯 ระดับ | 📅 Roadmap |
|---|---|---|
| 60 นาที | Advanced | สัปดาห์ 5 · วันที่ 21 |

**สิ่งที่ต้องมี:** รายงาน Lab 09; Google account ที่สอง (หรือเพื่อนร่วมงาน) เพื่อทดสอบเป็น viewer

**ขั้นตอน**
1. เปลี่ยนชื่อรายงานเป็น `Sales Overview` และทำสำเนา `[DEV] Sales Overview` ทำงานบน DEV ตั้งแต่นี้; promote ตอนจบ
2. **Share** → เพิ่มบัญชีทดสอบเป็น **Viewer**; link settings *Restricted* ที่ *Manage access* ติ๊ก *Disable downloading, printing and copying for viewers* เปิดลิงก์ด้วยบัญชีทดสอบ — ยืนยันว่าใช้ได้และไม่มี Export
3. สลับ `[LSG] sales_orders (BQ)` เป็น **Viewer's credentials** โหลดใหม่ด้วยบัญชีทดสอบ → เจอ error *no access to underlying data* ให้สิทธิ์ `BigQuery Data Viewer` บน dataset แก่บัญชีทดสอบ **หรือ** สลับกลับเป็น Owner's credentials เขียนหนึ่งประโยคว่าจะใช้แบบไหนใน production และทำไม
4. **Row-level security**: อัปโหลด Sheet `rep_access` ที่มีคอลัมน์ `email`, `sales_rep_region` (อีเมล 2 บัญชี → 2 ภูมิภาค) blend กับ sales (หรือเพิ่ม `region` ผ่าน view) และตั้ง **Filter by email** ที่ data source `rep_access` ด้วย field `email` ทดสอบทั้งสองบัญชี
5. **Schedule delivery**: จันทร์ 08:00 Asia/Bangkok, หน้า 1–2, หัวเรื่อง "Weekly Business Review" ตั้ง control region ก่อนแล้วติ๊ก *include current filter state* ส่งทดสอบตอนนี้
6. **Embed**: File → Embed report → เปิดใช้; วาง iframe ใน Google Site (หรือไฟล์ HTML ที่เปิดในเครื่อง) และยืนยันว่า render ให้ viewer ที่ล็อกอิน
7. **ลิงก์รายงานพร้อมสถานะ**: Share → Get report link → *Link to current report state*; ตรวจว่าเปิดมาพร้อม control ที่ตั้งไว้
8. **Promote**: ตั้งชื่อ version ใน DEV ("v1.0 – lab 11") แล้ว copy component ที่เปลี่ยนเข้า `Sales Overview` (Ctrl/⌘+C → paste ใน prod) บันทึกขั้นตอนไว้ในหน้า *About*
9. ถ้ามี **Looker Studio Pro**: สร้าง Team workspace ย้ายรายงานทั้งสองและ data source เข้าไป มอบ Manager คนที่สอง; จดว่า Share dialog เปลี่ยนไปอย่างไร

**ผลที่ควรได้**
- บัญชีทดสอบเห็นเฉพาะภูมิภาคของตัวเอง export ไม่ได้ ได้รับ PDF และรายงานที่ embed โหลดได้

**คำถามตรวจสอบ**
1. ทำไม "ลิงก์สาธารณะ + owner's credentials" อันตรายแม้เป็น dataset สาธิต?
2. วิธี RLS ไหนยังปลอดภัยเมื่อ viewer copy รายงาน? วิธีไหนไม่?
3. บอก 2 สิ่งที่ Team workspace แก้ได้แต่การแชร์แก้ไม่ได้

**Stretch goal:** ทำ RLS แบบเดียวกันใน BigQuery ด้วย `CREATE ROW ACCESS POLICY` และ viewer credentials; เปรียบเทียบพฤติกรรมกับ email filter

---
<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](../../docs/en/00-toc.md) · [กลับสารบัญ](../../docs/th/00-toc.md)</sub>
