# Style Guide / แนวทางการเขียน

This guide keeps all 16 chapters × 2 languages consistent. Follow it for any new or edited page.

## 1. Page skeleton (every chapter, both languages)

```markdown
🌐 [ภาษาไทย](../th/NN-slug.md) | [English](../en/NN-slug.md)

# NN · Chapter Title

> ⏱ **Estimated time:** 60 min · 📅 **Roadmap day:** Week W · Day D (date) · 🎯 **Level:** Basic

**In this chapter**
- [Section 1](#section-1)
- …

(content)

---
**Lab:** [Lab NN — name](../../labs/labNN-slug/README.md)

← [Previous: …](NN-1.md) | [Next: … →](NN+1.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](00-toc.md)</sub>
```

## 2. Headings

- `#` — chapter title only (one per page).
- `##` — major sections, numbered `## 1. …` in chapters (not in labs).
- `###` — sub-steps. Do not go deeper than `###`.

## 3. Callouts

| Use | Syntax |
|---|---|
| Helpful shortcut | `> **💡 Tip** …` |
| Something that breaks or costs money | `> **⚠️ Warning** …` |
| Hands-on task inside a chapter | `> **🧪 Lab** …` |
| Feature only in Looker Studio Pro | `> **🔒 Pro only** …` |
| Compare with Tableau / Power BI | `> **🔁 Coming from Tableau/Power BI?** …` |

## 4. Steps and UI

- Numbered steps `1.` `2.` for anything the reader clicks.
- UI labels in **bold** exactly as shown on screen: **Add data**, **Resource → Manage added data sources**.
- Menu paths with `→`.
- Field names and formulas in `code`: `sales_amount`, `SUM(profit) / SUM(sales_amount)`.
- Formula blocks use fenced code with `sql` highlighting (closest match for Looker Studio functions).

## 5. Tables and diagrams

- Comparison matrices as Markdown tables; first column is the criterion.
- Use Mermaid (`flowchart`, `sequenceDiagram`, `gantt`, `erDiagram`) when flow or timing matters. Keep each diagram under ~15 nodes.

## 6. Screenshots

(Optional, for future editions) `![alt text](../../assets/images/chNN-YY.png)` — YY is a two-digit sequence within the chapter. Add the description to `assets/images/README.md`. The current edition is text-first and ships without screenshots.

## 7. Language rules

**English (US):** short sentences, active voice, second person ("you"). Serial comma. No marketing fluff.

**ภาษาไทย:** ใช้ภาษาเขียนที่เป็นธรรมชาติ สุภาพ ไม่ใช่สำนวนแปลตรงตัว ลงท้ายประโยคแบบไม่มี "ครับ/ค่ะ" ในเนื้อหาหลัก (ใช้ได้ใน callout ที่เป็นบทสนทนา) คงคำศัพท์เทคนิคเป็นภาษาอังกฤษตามที่คนทำงานใช้จริง เช่น Calculated Field, Blend, Data Source, Parameter, Scorecard, Dimension, Metric ไม่แปลเป็น "เขตข้อมูลที่คำนวณ" หรือ "มิติ" คำที่แปลได้ธรรมชาติให้แปล เช่น รายงาน, แผนภูมิ, ตัวกรอง (ใช้สลับกับ Filter ได้)

Tone examples:
- ✅ "ลาก `region` ไปวางในช่อง Dimension แล้วเปลี่ยน Metric เป็น `SUM(sales_amount)`"
- ❌ "ทำการลากเขตข้อมูลภูมิภาคไปยังส่วนมิติและทำการเปลี่ยนตัววัด"

## 8. Names of things

| Write | Not |
|---|---|
| Looker Studio | Data Studio, Google Data Studio (mention once in Ch 01 for history) |
| Looker Studio Pro | Looker Studio Premium |
| Looker (enterprise) | Looker Core (Google's SKU name — mention once in Ch 13) |
| BigQuery | Big Query |
| Google Sheets | GSheet |
| data source (Looker Studio object) | dataset (reserve for BigQuery/CSV) |

## 9. Do / Don't

- Do state when a feature is Pro-only or subject to change.
- Do give the expected result after each lab step.
- Don't leave `TODO`, `TBD`, or lorem ipsum.
- Don't paste large screenshots of data with personal information.

---
Made by **The Narit Lab** · MIT License
