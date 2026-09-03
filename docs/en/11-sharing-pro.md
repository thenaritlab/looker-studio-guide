🌐 [ภาษาไทย](../th/11-sharing-pro.md) | [English](../en/11-sharing-pro.md)

# 11 · Sharing, Scheduling, Embedding, Access Control, Looker Studio Pro

> ⏱ **Estimated time:** 60 min · 📅 **Roadmap day:** Week 4 · Day 20 + Lab Week 5 · Day 21 · 🎯 **Level:** Advanced

**In this chapter**
- [Sharing a report](#1-sharing-a-report)
- [Sharing data sources and credential implications](#2-sharing-data-sources-and-credential-implications)
- [Row-level security options](#3-row-level-security-options)
- [Scheduled delivery](#4-scheduled-delivery)
- [Embedding](#5-embedding)
- [Download, export and the report link](#6-download-export-and-the-report-link)
- [Looker Studio Pro](#7-looker-studio-pro)
- [Dev → prod workflow and governance](#8-dev--prod-workflow-and-governance)

## 1. Sharing a report

Click **Share** (top-right):

| Setting | Meaning |
|---|---|
| **Add people and groups** | Viewer or Editor per email / Google Group |
| **Link settings** | *Restricted* (only added people), *Anyone in your organisation*, *Anyone with the link* (public — never for internal data) |
| **Manage access** tab | Owner can *prevent editors from changing access*, *disable downloading, printing and copying for viewers* |
| **Transfer ownership** | To a service/shared account before someone leaves |

![Share dialog](../../assets/images/ch11-01.png)

Viewers need **two** things: access to the *report* and (depending on credentials) access to the *data*. Most support tickets are the second one.

## 2. Sharing data sources and credential implications

- With **Owner's credentials**, viewers see data through the owner — share only the report.
- With **Viewer's credentials**, share the report *and* grant each viewer access to the Sheet/BigQuery dataset (or they get "You don't have access to the underlying data").
- Sharing a **reusable data source** as *Editor* lets others build new reports on it; *Viewer* lets them use it read-only.
- **Transfer ownership** of both the report and its data sources when an owner leaves; otherwise reports die with the account.

> **⚠️ Warning** A public link + owner's credentials means the whole internet sees your BigQuery table. Double-check link settings before sending.

## 3. Row-level security options

| Method | How | Notes |
|---|---|---|
| **Email filter** (data source) | Data source → **Filter by email** → pick a field containing viewer emails | Free, simple; needs an email column in the data (or a mapping table blended in) |
| **BigQuery RLS policies** + viewer credentials | `CREATE ROW ACCESS POLICY … GRANT TO ('user:…')` | Enforced in the database, strongest |
| **Authorized views** + viewer credentials | View filters by `SESSION_USER()` | Classic pattern |
| **Custom query with `@DS_USER_EMAIL`** | `WHERE owner_email = @DS_USER_EMAIL` | Works with owner's credentials too |
| **Separate reports per audience** | Copy report, fixed filters | Simple but many copies |

## 4. Scheduled delivery

**Share → Schedule delivery** (email icon):
- Recipients (email), pages to include, **repeat** (daily/weekly/monthly, time and time zone), start date, custom subject/message.
- Delivers a **PDF** (and link). Report filter/control state can be captured: set controls first, then schedule → *include current filter state*.
- Free tier: email only. **🔒 Pro only:** deliver to **Google Chat spaces**, more schedules per report, and schedules owned by the workspace (survive employee departure).

![Schedule delivery](../../assets/images/ch11-02.png)

## 5. Embedding

**File → Embed report** (or Share → Embed):
1. Enable embedding.
2. Copy the `<iframe>` snippet or the embed URL; set width/height.
3. Paste into your website, Google Sites, Notion, Confluence, or a portal.

Access rules still apply: viewers must be signed in to a Google account that has access, unless the link is *Anyone with the link*. Pass filters/parameters in the embed URL (chapter 08 §8) to personalise per page.

![Embed dialog](../../assets/images/ch11-03.png)

> **🔁 Coming from Tableau/Power BI?** There is no embed SDK or JS API for filters/events in Looker Studio; embedding is iframe + URL parameters. For app-grade embedding use Looker (chapter 13).

## 6. Download, export and the report link

- **File → Download → PDF**: choose pages, custom background, password, expiry link.
- Chart header → **Export** → CSV / Google Sheets (respects current filters). Owners can disable this for viewers.
- **Share → Get report link → Link to current report state** produces a URL with the viewer's control selections.
- **File → Report and page settings → Google Analytics** to track report usage in GA4.

## 7. Looker Studio Pro

Pro is a paid subscription per user per Google Cloud project (billed via Google Cloud). What you get:

| Feature | Free | Pro |
|---|---|---|
| Team workspaces (shared ownership, folders, roles) | — | ✔ |
| Google Cloud technical support + SLA | — | ✔ |
| Scheduled delivery to Google Chat; more schedules | Email only | ✔ |
| Personal report links for Looker-connected reports | — | ✔ |
| Looker Studio **mobile app** | — | ✔ |
| **Gemini in Looker Studio** (chart generation, calculated-field help, slide/summary generation) | Limited/rolling out | ✔ |
| Admin controls: audit logs, disable public sharing at org level | Basic | ✔ |
| Enterprise-grade data governance via Looker | — | ✔ |

![Team workspace](../../assets/images/ch11-04.png)

When to buy: any team of >5 people maintaining reports, any client-facing agency, or any org where "the owner left and the report broke" has happened once. When not: solo analysts and small businesses on Sheets.

Enable: Google Cloud console → **Looker Studio Pro** → choose project → assign licences by user/group; then in Looker Studio create a **Team workspace** and move reports/data sources in.

## 8. Dev → prod workflow and governance

1. **Naming**: `[DEV] Sales Overview`, `Sales Overview` (prod). Same for data sources.
2. **Develop on a copy**: File → Make a copy → DEV. Change data sources to DEV tables if you have them.
3. **Promote**: when DEV is approved, either (a) copy components into prod (Ctrl/⌘+C/V across reports), or (b) make prod a copy of DEV and swap the link — the second is cleaner but breaks bookmarks; Pro team workspaces reduce the pain.
4. **Version history**: name a version before each promotion ("v1.3 – added ROI page").
5. **Ownership**: reports and data sources owned by a service account or team workspace, never a personal account.
6. **Documentation**: a "About this report" page with data sources, owners, refresh time, definitions.
7. **Access review** quarterly: Share → Manage access; remove leavers, replace individuals with Google Groups.

---
**Lab:** [Lab 11 — Share, schedule, embed and set up row-level security](../../labs/lab11-sharing-pro/README.md)

← [Previous: 10 · Performance](10-performance.md) | [Next: 12 · Community Visualizations →](12-community-viz.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](00-toc.md)</sub>
