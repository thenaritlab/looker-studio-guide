🌐 [ภาษาไทย](../th/12-community-viz.md) | [English](../en/12-community-viz.md)

# 12 · Community Visualizations & Advanced Customization

> ⏱ **Estimated time:** 60 min · 📅 **Roadmap day:** Week 5 · Day 22–23 · 🎯 **Level:** Advanced

**In this chapter**
- [What community visualizations are](#1-what-community-visualizations-are)
- [Using one from the gallery](#2-using-one-from-the-gallery)
- [Security and access settings](#3-security-and-access-settings)
- [Building your own: anatomy](#4-building-your-own-anatomy)
- [Building your own: step by step](#5-building-your-own-step-by-step)
- [Community connectors (Apps Script)](#6-community-connectors-apps-script)
- [Other customization: themes as JSON, images, links, tooltips](#7-other-customization-themes-as-json-images-links-tooltips)
- [When to use, when to avoid](#8-when-to-use-when-to-avoid)

## 1. What community visualizations are

A **community visualization** is a chart written in JavaScript (D3, Chart.js, Vega, plain SVG…) that runs inside Looker Studio, receives the chart's data and style settings, and renders in an iframe. They fill gaps in the native chart set: Sankey, radar, calendar heatmap, gauge variants, waterfall, network graphs, custom KPI cards, animated maps.

Two kinds:
- **Gallery** visualizations — published by Google partners and the community, one click to use.
- **Custom** visualizations — hosted in your own Google Cloud Storage bucket, private to your organisation.

![Gallery](../../assets/images/ch12-01.png)

## 2. Using one from the gallery

1. **Add a chart → Community visualizations and components → Explore more**.
2. Browse the gallery (e.g. *Sankey*, *Gantt*, *Radar*, *Funnel*, *Sunburst*, *Animated bar race*). Click one → **Add**.
3. Configure it like any chart: dimensions, metrics, style options the developer exposed.
4. First use per report prompts to **allow community visualization access** for the data source (see §3).

Popular choices for our datasets: Sankey (`sales_channel → payment_method`), Calendar heatmap (`web_traffic.sessions` by day), Waterfall (profit bridge by category).

## 3. Security and access settings

Community visualizations receive **the chart's data** and run third-party code. Therefore:

- Each **data source** has a switch: **Community visualizations access → On/Off** (data source editor, top bar). Off by default for new sources in many orgs.
- Workspace admins can restrict which visualizations are allowed.
- For sensitive data, use only visualizations you host (custom) or from vendors you trust; review their source (most are open on GitHub).

> **⚠️ Warning** A malicious visualization could exfiltrate the rows it receives. Treat enabling access like installing a browser extension.

## 4. Building your own: anatomy

A custom visualization = 3–4 files in a **Google Cloud Storage** bucket:

| File | Purpose |
|---|---|
| `manifest.json` | Name, description, logo, list of components, paths to JS/CSS/config |
| `viz-config.json` (name is yours) | Which **data fields** (dimensions/metrics, how many) and **style** controls the user sees |
| `viz.js` | Your rendering code; subscribes to data via `dscc` (Data Studio Community Component) library |
| `viz.css` | Optional styles |

The `dscc` helper library provides `subscribeToData(callback, {transform: dscc.objectTransform})`, giving you `data.tables.DEFAULT` rows, `data.fields`, `data.style`, and `data.theme`.

## 5. Building your own: step by step

1. **Set up**
```bash
npm install -g @google/dscc-gen
dscc-gen viz          # scaffold; answer prompts (project name, GCS bucket for dev/prod)
```
   This creates a project with `src/index.js`, `src/index.json` (config), `src/manifest.json`, plus `npm run start` (local dev server) and `npm run build:dev / build:prod`.

2. **Define fields** in `index.json`:
```json
{
  "data": [{"id": "concepts", "label": "Data", "elements": [
    {"id": "dim", "label": "Category", "type": "DIMENSION", "options": {"min": 1, "max": 1}},
    {"id": "met", "label": "Value", "type": "METRIC", "options": {"min": 1, "max": 1}}
  ]}],
  "style": [{"id": "look", "label": "Look", "elements": [
    {"id": "barColor", "label": "Bar color", "type": "FILL_COLOR", "defaultValue": {"color": "#1A73E8"}}
  ]}]
}
```

3. **Render** in `index.js` (minimal bar chart in plain SVG):
```javascript
const dscc = require('@google/dscc');
function draw(data) {
  const rows = data.tables.DEFAULT;                     // [{dim:[...], met:[...]}]
  const color = data.style.barColor.value.color;
  const max = Math.max(...rows.map(r => r.met[0]));
  const w = dscc.getWidth(), h = dscc.getHeight(), bh = h / rows.length;
  document.body.innerHTML = `<svg width="${w}" height="${h}">` +
    rows.map((r, i) => `<rect x="0" y="${i*bh}" width="${r.met[0]/max*w}" height="${bh-4}" fill="${color}"/>
       <text x="4" y="${i*bh+bh/2}" font-size="12" fill="#fff" dominant-baseline="middle">${r.dim[0]}</text>`).join('') +
    `</svg>`;
}
dscc.subscribeToData(draw, {transform: dscc.objectTransform});
```

4. **Test locally**: `npm run start` opens a page with sample data. Then `npm run build:dev` and `npm run push:dev` uploads to your dev bucket.

5. **Use in Looker Studio**: Add a chart → Community visualizations → **Build your own** → paste the manifest path `gs://your-bucket/dev` → **Submit** → add the component.

6. **Publish** (optional): `npm run build:prod && npm run push:prod`; make the bucket objects publicly readable if colleagues outside your project need it; submit to the gallery if you want it public.

![Custom viz manifest in GCS](../../assets/images/ch12-02.png)

> **💡 Tip** Support **theme** colors (`data.theme`) and **interactions** (`dscc.sendInteraction` for cross-filtering) to make your viz feel native.

## 6. Community connectors (Apps Script)

If a connector does not exist for your API (e.g. an internal HR system, a Thai bank's API, LINE OA insights), you can write a **community connector** in Google Apps Script:

- Implement `getAuthType()`, `getConfig()`, `getSchema()`, `getData()`.
- Deploy → copy the deployment ID → in Looker Studio, connector gallery → **Build your own** → paste ID.
- Same access-control caveats as visualizations; connectors can be private to your Workspace.

Chapter 08's parameter concepts apply: `getConfig()` can expose parameters that flow into `getData(request)`.

## 7. Other customization: themes as JSON, images, links, tooltips

- **Themes**: Theme → Customize covers most needs; **Extract theme from image** builds a palette from a logo.
- **Images**: `IMAGE(url)` in a calculated field renders logos/product photos in tables; **Image** component for static branding.
- **Hyperlinks**: `HYPERLINK(url, label)` in tables to jump to CRM records, or to other Looker Studio pages with filter parameters.
- **Rich text / shapes**: layer rectangles behind chart groups; use **Order → Send to back**.
- **Report-level components**: right-click → Make report-level for headers/footers/logos.
- **Custom tooltips**: not supported natively; community visualizations can implement them.

## 8. When to use, when to avoid

| Use a community viz when | Avoid when |
|---|---|
| The native set truly lacks the chart type (Sankey, waterfall, radar) | A sorted bar chart tells the same story |
| You control the code (custom) or trust the vendor | Data is regulated and the viz is third-party |
| You need custom tooltips/animations for a public-facing report | Report must be printed/PDF (some viz render poorly) |
| You need a specific corporate KPI card design | Performance matters — each viz loads an iframe and JS bundle |

---
**Lab:** [Lab 12 — Use a gallery viz and deploy a custom one](../../labs/lab12-community-viz/README.md)

← [Previous: 11 · Sharing & Pro](11-sharing-pro.md) | [Next: 13 · Looker (Enterprise) Overview →](13-looker-overview.md)

<sub>Made by **The Narit Lab** · [MIT License](../../LICENSE) · [Back to TOC](00-toc.md)</sub>
