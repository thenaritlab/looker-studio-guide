🌐 [ภาษาไทย](../th/99-publish-to-github.md) | [English](../en/99-publish-to-github.md)

# 99 · เผยแพร่ repo นี้ขึ้น GitHub — คำสั่งทีละขั้นตอน

> ⏱ **เวลาโดยประมาณ:** 45 นาที · 📅 **วันตาม Roadmap:** สัปดาห์ 6 · วันที่ 30 · 🎯 **ระดับ:** ภาคผนวก

**ในบทนี้**
- [สิ่งที่ต้องมีก่อน](#1-สิ่งที่ต้องมีก่อน)
- [สร้าง repository ในเครื่อง](#2-สร้าง-repository-ในเครื่อง)
- [สร้าง remote — ทางเลือก A: GitHub CLI](#3-สร้าง-remote--ทางเลือก-a-github-cli)
- [สร้าง remote — ทางเลือก B: หน้าเว็บ](#4-สร้าง-remote--ทางเลือก-b-หน้าเว็บ)
- [Push, tag v1.0.0, เพิ่ม topic](#5-push-tag-v100-เพิ่ม-topic)
- [เปิด GitHub Pages จาก /docs (ไม่บังคับ)](#6-เปิด-github-pages-จาก-docs-ไม่บังคับ)
- [Workflow การทำงานต่อเนื่อง](#7-workflow-การทำงานต่อเนื่อง)
- [เผยแพร่ repo capstone ของคุณเอง](#8-เผยแพร่-repo-capstone-ของคุณเอง)

## 1. สิ่งที่ต้องมีก่อน

```bash
git --version            # 2.30+
gh --version             # GitHub CLI 2.x — https://cli.github.com
gh auth login            # เลือก GitHub.com → HTTPS → login ผ่าน browser
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
python3 --version        # สำหรับ link checker
```

## 2. สร้าง repository ในเครื่อง

```bash
cd looker-studio-guide            # โฟลเดอร์ที่มี README.md, docs/, labs/, datasets/
git init -b main
python3 scripts/check_links.py    # ลิงก์ภายในต้อง resolve ทั้งหมด (exit code 0)
git add .
git commit -m "feat: initial release — Looker Studio guide TH/EN with labs, datasets, roadmap"
```

`.gitignore` มีให้แล้ว (ไฟล์ OS, Python cache, secret, export ขนาดใหญ่)

## 3. สร้าง remote — ทางเลือก A: GitHub CLI

```bash
gh repo create thenaritlab/looker-studio-guide \
  --public \
  --description "Bilingual (TH/EN) Google Looker Studio guide — from basics to advanced, with hands-on labs, synthetic datasets, and a 6-week learning roadmap. Includes a self-service BI comparison (Tableau · Power BI · Looker). By The Narit Lab. MIT License." \
  --source=. \
  --remote=origin \
  --push
```

ถ้า `thenaritlab` เป็น organisation ที่คุณเป็นสมาชิก คำสั่งใช้ได้ทันที; บัญชีส่วนตัวให้แทน `thenaritlab/` ด้วย username ของคุณ

## 4. สร้าง remote — ทางเลือก B: หน้าเว็บ

1. ไปที่ **https://github.com/new**
2. Owner: `thenaritlab` · Repository name: `looker-studio-guide` · Description: วางข้อความด้านบน
3. **Public** **ไม่ต้อง** ติ๊ก "Add a README", ".gitignore" หรือ "license" (เรามีอยู่แล้ว)
4. **Create repository** แล้ว

```bash
git remote add origin https://github.com/thenaritlab/looker-studio-guide.git
git push -u origin main
```

## 5. Push, tag v1.0.0, เพิ่ม topic

```bash
# tag release
git tag -a v1.0.0 -m "v1.0.0 — first public release (16 chapters, 13 labs, 6 datasets)"
git push origin v1.0.0

# GitHub release พร้อม note
gh release create v1.0.0 --title "v1.0.0" --notes "First public release. 16 chapters TH/EN, 13 labs, 6 synthetic datasets, 6-week roadmap."

# topic
gh repo edit thenaritlab/looker-studio-guide \
  --add-topic looker-studio --add-topic google-looker --add-topic data-visualization \
  --add-topic bi --add-topic thai --add-topic tutorial

# ตรวจสอบ
gh repo view thenaritlab/looker-studio-guide --web
```

ทางเลือกหน้าเว็บสำหรับ topic: หน้า repo → ⚙️ ข้าง *About* → **Topics** → พิมพ์แต่ละ topic → **Save changes**

## 6. เปิด GitHub Pages จาก /docs (ไม่บังคับ)

Pages จะเสิร์ฟ Markdown ใน `docs/` ด้วย theme Jekyll เริ่มต้น

```bash
gh api -X POST repos/thenaritlab/looker-studio-guide/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
```

หรือ: repo → **Settings → Pages → Source: Deploy from a branch → Branch: main / folder: /docs → Save**

เพิ่ม `docs/_config.yml` แบบเล็กสุดถ้าอยากได้ theme

```yaml
title: Google Looker Studio — From Basic to Advanced
description: Bilingual TH/EN guide by The Narit Lab
theme: jekyll-theme-cayman
```

เว็บจะขึ้นที่ `https://thenaritlab.github.io/looker-studio-guide/` ภายในไม่กี่นาที ลิงก์ relative ระหว่าง `docs/en` และ `docs/th` ยังใช้ได้; ลิงก์ไป `../../labs/...` จะ resolve ไปที่ GitHub repo ก็ต่อเมื่อคุณ copy `labs/` และ `datasets/` ไว้ใต้ `docs/` ด้วย — หรือไม่เปิด Pages แล้วพึ่งการ render Markdown ที่ดีอยู่แล้วของ GitHub

## 7. Workflow การทำงานต่อเนื่อง

```bash
git checkout -b docs/ch06-thai-wording     # หนึ่ง branch ต่อการเปลี่ยนแปลง
# แก้ไข แล้ว
python3 scripts/check_links.py
git commit -am "docs(ch06): improve Thai wording for REGEXP section"
git push -u origin docs/ch06-thai-wording
gh pr create --fill                        # เปิด PR
gh pr merge --squash --delete-branch       # หลัง review
git checkout main && git pull
```

ออก version ใหม่เมื่อเนื้อหาเปลี่ยนอย่างมีนัยสำคัญ

```bash
git tag -a v1.1.0 -m "v1.1.0 — added Gemini in Looker Studio section" && git push origin v1.1.0
gh release create v1.1.0 --generate-notes
```

## 8. เผยแพร่ repo capstone ของคุณเอง

เปลี่ยน capstone เป็น repo portfolio ใน 10 นาที

```bash
mkdir siam-goods-dashboard && cd siam-goods-dashboard
git init -b main
cat > README.md <<'MD'
# Siam Goods — Weekly Business Review (Looker Studio)
Live report: <วางลิงก์แชร์ (Anyone with the link, viewer)>
Video walkthrough: <ลิงก์>
## What it answers
1. Sales & profit trend vs +15% target  2. Marketing ROI by channel  3. Segment/category drivers
## Data
Synthetic datasets from https://github.com/thenaritlab/looker-studio-guide (MIT)
## Screenshots
![p1](screenshots/p1.png) ![p2](screenshots/p2.png) ![p3](screenshots/p3.png)
MD
mkdir screenshots      # ใส่ PNG ที่ export จากแต่ละหน้า
git add . && git commit -m "feat: capstone dashboard README and screenshots"
gh repo create YOUR_USERNAME/siam-goods-dashboard --public --source=. --push
```

ยินดีด้วย — คุณจบ roadmap 6 สัปดาห์แล้ว 🎉

---
← [ก่อนหน้า: 14 · Capstone](14-capstone.md) | ถัดไป: —

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [กลับสารบัญ](00-toc.md)</sub>
