# Contributing / การมีส่วนร่วม

Thanks for helping improve this guide! / ขอบคุณที่ช่วยพัฒนาคู่มือนี้

## Rules
1. Every content page must exist in **both** `docs/en/` and `docs/th/` with the same file name.
2. Follow `docs/STYLE-GUIDE.md` (callouts, headings, navigation footer).
3. Keep technical terms in English inside Thai text (Calculated Field, Blend, Data Source).
4. Run a link check before opening a PR:
   ```bash
   npx markdown-link-check -q README.md docs/**/*.md labs/**/*.md
   ```
5. Datasets must stay synthetic, ≤ 5 MB, and regenerable from `datasets/generate_datasets.py`.

## Workflow
```bash
git checkout -b feat/<short-name>
# edit both TH and EN
git commit -m "docs: <what changed> (th+en)"
git push -u origin feat/<short-name>
gh pr create --fill
```

---
Made by **The Narit Lab** · MIT License
