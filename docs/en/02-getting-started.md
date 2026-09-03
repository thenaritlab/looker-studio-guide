🌐 [ภาษาไทย](../th/02-getting-started.md) | [English](../en/02-getting-started.md)

# 02 · Getting Started: Account, UI Tour, First Report in 15 Minutes

> ⏱ **Estimated time:** 45 min (+ Lab 45 min) · 📅 **Roadmap day:** Week 1 · Day 2 · 🎯 **Level:** Basic

**In this chapter**
- [Sign in and the home page](#1-sign-in-and-the-home-page)
- [Reports, data sources, explorer — the three objects](#2-reports-data-sources-explorer--the-three-objects)
- [UI tour of the report editor](#3-ui-tour-of-the-report-editor)
- [Your first report in 15 minutes](#4-your-first-report-in-15-minutes)
- [Edit mode vs view mode, autosave and version history](#5-edit-mode-vs-view-mode-autosave-and-version-history)
- [Keyboard shortcuts worth learning](#6-keyboard-shortcuts-worth-learning)

## 1. Sign in and the home page

1. Go to **https://lookerstudio.google.com** and sign in with any Google account (personal Gmail or Google Workspace).
2. Accept the terms on first use. Country and marketing preferences can be changed later under **Settings**.
3. You land on the **Home** page. The left rail shows **Reports**, **Data sources**, **Explorer**, and **Templates**; the top has **Create** and the search box.

> **💡 Tip** If your company uses Google Workspace, an admin may have turned Looker Studio off. If you see "You don't have access", ask IT to enable the *Looker Studio* service in the Admin console rather than using a personal account with company data.

## 2. Reports, data sources, explorer — the three objects

| Object | What it is | Analogy |
|---|---|---|
| **Data source** | A saved connection to one table/sheet/query plus its field list, types, and default aggregations. Reusable across reports | Tableau published data source / Power BI dataset |
| **Report** | One or more pages of charts and controls. Reports reference data sources | Workbook / .pbix |
| **Explorer** | A scratchpad for quick ad-hoc charts, not shared by default | Tableau "Ask Data" sheet |

A data source can be **embedded** (lives only inside one report) or **reusable** (appears in the Data sources list and can be shared). We create embedded ones today and reusable ones in chapter 03.

## 3. UI tour of the report editor

Click **Create → Report** and add any data source to open the editor. Four zones:

1. **Toolbar** (top): undo/redo, **Add page**, **Add data**, **Add a chart**, **Add a control**, text/image/shape, **Theme and layout**, **View / Edit** toggle, **Share**.
2. **Canvas** (center): the page. Default size 1200 × 900 px; change under **Theme and layout → Layout**.
3. **Properties panel** (right): for the selected component — **Setup** tab (data source, dimensions, metrics, sort, filters) and **Style** tab (colors, fonts, axes).
4. **Data panel** (far right): all fields of the added data sources. Green = dimension, blue = metric, purple = parameter. Drag fields onto a chart or onto the canvas to auto-create a chart.

Menus you will use constantly:
- **Resource → Manage added data sources** — edit fields, refresh schema.
- **File → Report settings** — default data source, data freshness, Google Analytics tracking, GA4 filter behaviour.
- **Page → Current page settings** — page-level data source and filters.

## 4. Your first report in 15 minutes

We will use `sales_orders.csv`. Load it into a Google Sheet first (see [datasets/README.md](../../datasets/README.md)).

1. **Create → Report**.
2. In **Add data to report**, choose **Google Sheets**, pick your spreadsheet and the `sales_orders` worksheet. Leave **Use first row as headers** and **Include hidden and filtered cells** ticked. Click **Add**, then **Add to report**.
3. Looker Studio drops a default table on the canvas. Delete it (select, press Delete).
4. **Add a chart → Scorecard**. In **Setup**, set Metric = `sales_amount` (aggregation SUM). Rename the label to *Total Sales* by clicking the pencil icon next to the metric.
5. **Add a chart → Time series**. Dimension = `order_date`, Metric = `sales_amount`. In **Style**, tick **Show data labels** off and set line weight 2.
6. **Add a chart → Table**. Dimension = `sales_channel`, Metrics = `sales_amount`, `profit`, `Record Count`. Sort by `sales_amount` descending.
7. **Add a control → Date range control**. Place it top-right. Default = *Last 12 months*.
8. Click **Theme and layout** and pick any theme; the whole page restyles.
9. Rename the report (top-left title) to *Sales Overview — Lab 02*.
10. Click **View** to see it as a reader would. Change the date range and watch all three charts update.

> **🧪 Lab** [Lab 02](../../labs/lab02-getting-started/README.md) repeats these steps with checkpoints and adds a second page.

## 5. Edit mode vs view mode, autosave and version history

- There is **no Save button**. Every change is saved immediately.
- **View** mode is what viewers see; **Edit** mode is for editors. The toggle is top-right.
- **File → Version history** lets you name a version ("Before redesign") and restore an older one — the only safety net you have, so name versions before big changes.
- **File → Make a copy** duplicates the report; you can choose to keep or swap the data sources, which is how templates work.

> **⚠️ Warning** Because saving is instant, editing a live report changes what viewers see in real time. For anything important, work on a copy and swap it in when done (chapter 11 covers a proper dev → prod flow).

## 6. Keyboard shortcuts worth learning

| Action | Shortcut |
|---|---|
| Copy / paste component (works across reports) | Ctrl/⌘ + C / V |
| Duplicate | Ctrl/⌘ + D |
| Undo / redo | Ctrl/⌘ + Z / Shift + Z |
| Nudge selected component | Arrow keys (Shift = 10 px) |
| Align / distribute | Right-click → Align |
| Toggle View / Edit | Ctrl/⌘ + Shift + E |
| Show data (underlying rows of a chart) | Right-click chart → Show data |

---
**Lab:** [Lab 02 — Your first report](../../labs/lab02-getting-started/README.md)

← [Previous: 01 · BI Landscape](01-bi-landscape.md) | [Next: 03 · Data Sources & Connectors →](03-data-sources.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](00-toc.md)</sub>
