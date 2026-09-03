🌐 [ภาษาไทย](../th/99-publish-to-github.md) | [English](../en/99-publish-to-github.md)

# 99 · Publishing This Repo to GitHub — Step-by-Step Commands

> ⏱ **Estimated time:** 45 min · 📅 **Roadmap day:** Week 6 · Day 30 · 🎯 **Level:** Appendix

**In this chapter**
- [Prerequisites](#1-prerequisites)
- [Create the repository locally](#2-create-the-repository-locally)
- [Create the remote — option A: GitHub CLI](#3-create-the-remote--option-a-github-cli)
- [Create the remote — option B: web UI](#4-create-the-remote--option-b-web-ui)
- [Push, tag v1.0.0, add topics](#5-push-tag-v100-add-topics)
- [Enable GitHub Pages from /docs (optional)](#6-enable-github-pages-from-docs-optional)
- [Ongoing workflow](#7-ongoing-workflow)
- [Publishing your own capstone repo](#8-publishing-your-own-capstone-repo)

## 1. Prerequisites

```bash
git --version            # 2.30+
gh --version             # GitHub CLI 2.x — https://cli.github.com
gh auth login            # choose GitHub.com → HTTPS → login with browser
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
python3 --version        # for the link checker
```

## 2. Create the repository locally

```bash
cd looker-studio-guide            # the folder containing README.md, docs/, labs/, datasets/
git init -b main
python3 scripts/check_links.py    # all internal links must resolve (exit code 0)
git add .
git commit -m "feat: initial release — Looker Studio guide TH/EN with labs, datasets, roadmap"
```

`.gitignore` is already included (OS files, Python caches, secrets, large exports).

## 3. Create the remote — option A: GitHub CLI

```bash
gh repo create thenaritlab/looker-studio-guide \
  --public \
  --description "Bilingual (TH/EN) Google Looker Studio guide — from basics to advanced, with hands-on labs, synthetic datasets, and a 6-week learning roadmap. Includes a self-service BI comparison (Tableau · Power BI · Looker). By The Narit Lab. MIT License." \
  --source=. \
  --remote=origin \
  --push
```

If `thenaritlab` is an organisation you belong to, the command works as is; for a personal account replace `thenaritlab/` with your username.

## 4. Create the remote — option B: web UI

1. Go to **https://github.com/new**.
2. Owner: `thenaritlab` · Repository name: `looker-studio-guide` · Description: paste the text above.
3. **Public**. Do **not** tick "Add a README", ".gitignore" or "license" (we already have them).
4. **Create repository**, then:

```bash
git remote add origin https://github.com/thenaritlab/looker-studio-guide.git
git push -u origin main
```

## 5. Push, tag v1.0.0, add topics

```bash
# tag the release
git tag -a v1.0.0 -m "v1.0.0 — first public release (16 chapters, 13 labs, 6 datasets)"
git push origin v1.0.0

# GitHub release with notes
gh release create v1.0.0 --title "v1.0.0" --notes "First public release. 16 chapters TH/EN, 13 labs, 6 synthetic datasets, 6-week roadmap."

# topics
gh repo edit thenaritlab/looker-studio-guide \
  --add-topic looker-studio --add-topic google-looker --add-topic data-visualization \
  --add-topic bi --add-topic thai --add-topic tutorial

# verify
gh repo view thenaritlab/looker-studio-guide --web
```

Web UI fallback for topics: repo page → ⚙️ next to *About* → **Topics** → type each topic → **Save changes**.

## 6. Enable GitHub Pages from /docs (optional)

Pages will serve the Markdown in `docs/` with the default Jekyll theme.

```bash
gh api -X POST repos/thenaritlab/looker-studio-guide/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
```

Or: repo → **Settings → Pages → Source: Deploy from a branch → Branch: main / folder: /docs → Save**.

Add a minimal `docs/_config.yml` if you want a theme:

```yaml
title: Google Looker Studio — From Basic to Advanced
description: Bilingual TH/EN guide by The Narit Lab
theme: jekyll-theme-cayman
```

Your site appears at `https://thenaritlab.github.io/looker-studio-guide/` within a few minutes. Relative links between `docs/en` and `docs/th` keep working; links to `../../labs/...` resolve to the GitHub repo only if you also copy `labs/` and `datasets/` under `docs/` — or leave Pages off and rely on GitHub's excellent Markdown rendering.

## 7. Ongoing workflow

```bash
git checkout -b docs/ch06-thai-wording     # branch per change
# edit, then
python3 scripts/check_links.py
git commit -am "docs(ch06): improve Thai wording for REGEXP section"
git push -u origin docs/ch06-thai-wording
gh pr create --fill                        # open PR
gh pr merge --squash --delete-branch       # after review
git checkout main && git pull
```

Release a new version when content changes materially:

```bash
git tag -a v1.1.0 -m "v1.1.0 — added Gemini in Looker Studio section" && git push origin v1.1.0
gh release create v1.1.0 --generate-notes
```

## 8. Publishing your own capstone repo

Turn your capstone into a portfolio repo in 10 minutes:

```bash
mkdir siam-goods-dashboard && cd siam-goods-dashboard
git init -b main
cat > README.md <<'MD'
# Siam Goods — Weekly Business Review (Looker Studio)
Live report: <paste share link (Anyone with the link, viewer)>
Video walkthrough: <link>
## What it answers
1. Sales & profit trend vs +15% target  2. Marketing ROI by channel  3. Segment/category drivers
## Data
Synthetic datasets from https://github.com/thenaritlab/looker-studio-guide (MIT)
## Screenshots
![p1](screenshots/p1.png) ![p2](screenshots/p2.png) ![p3](screenshots/p3.png)
MD
mkdir screenshots      # add PNG exports of each page
git add . && git commit -m "feat: capstone dashboard README and screenshots"
gh repo create YOUR_USERNAME/siam-goods-dashboard --public --source=. --push
```

Congratulations — you finished the 6-week roadmap. 🎉

---
← [Previous: 14 · Capstone](14-capstone.md) | Next: —

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](00-toc.md)</sub>
