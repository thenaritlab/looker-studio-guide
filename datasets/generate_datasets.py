#!/usr/bin/env python3
"""
generate_datasets.py — Deterministic synthetic datasets for the
"Google Looker Studio — From Basic to Advanced" guide by The Narit Lab.

Usage:
    python3 generate_datasets.py            # writes CSVs next to this script
    python3 generate_datasets.py --out DIR  # writes CSVs to DIR

All data is synthetic (no real people, companies, or transactions).
Regeneration is deterministic: the same SEED always yields identical files.
License: MIT — Created by The Narit Lab (2026).
"""
import argparse
import csv
import os
import random
from datetime import date, datetime, timedelta

SEED = 20260907  # roadmap start date, for fun
rng = random.Random(SEED)

START = date(2024, 1, 1)
END = date(2026, 8, 31)
DAYS = (END - START).days + 1

REGIONS = {
    "Bangkok": ["Bangkok", "Nonthaburi", "Pathum Thani", "Samut Prakan"],
    "Central": ["Ayutthaya", "Chonburi", "Rayong", "Nakhon Pathom"],
    "North": ["Chiang Mai", "Chiang Rai", "Lampang", "Phitsanulok"],
    "Northeast": ["Khon Kaen", "Nakhon Ratchasima", "Udon Thani", "Ubon Ratchathani"],
    "South": ["Phuket", "Songkhla", "Surat Thani", "Krabi"],
}
SEGMENTS = ["Consumer", "Corporate", "SMB"]
CHANNELS_SALES = ["Online Store", "Marketplace", "Retail Shop", "Sales Rep"]
PAYMENTS = ["Credit Card", "PromptPay", "Bank Transfer", "Cash on Delivery"]
CATEGORIES = {
    "Electronics": ["Headphones", "Keyboard", "Monitor", "Webcam", "Power Bank", "Smart Speaker"],
    "Office": ["Desk Lamp", "Notebook", "Pen Set", "Standing Desk", "Ergonomic Chair", "Whiteboard"],
    "Home & Living": ["Air Purifier", "Coffee Maker", "Rice Cooker", "Blender", "Vacuum", "Fan"],
    "Sports": ["Yoga Mat", "Running Shoes", "Dumbbell Set", "Water Bottle", "Cycling Helmet", "Jump Rope"],
    "Beauty": ["Sunscreen", "Serum", "Shampoo", "Face Mask", "Hair Dryer", "Lip Balm"],
}
BRANDS = ["Narita", "Siam Tech", "Chao Phraya", "Lanna Goods", "Andaman Co", "Isan Works"]
FIRST_NAMES = ["Somchai", "Suda", "Anan", "Kanya", "Prasert", "Malee", "Wichai", "Nok", "Tanawat",
               "Pim", "Krit", "Ploy", "Boon", "Fah", "Chai", "Mint", "Ton", "Bee", "Aek", "Noon",
               "James", "Emily", "Wei", "Yuki", "Priya", "Ahmed", "Sofia", "Lucas", "Mei", "Omar"]
LAST_INITIALS = "ABCDEFGHJKLMNPRSTVW"
DEPARTMENTS = ["Sales", "Marketing", "Engineering", "Finance", "Operations", "HR", "Customer Success"]
LEVELS = ["Junior", "Mid", "Senior", "Lead", "Manager"]
MKT_CHANNELS = ["Facebook Ads", "Google Ads", "LINE OA", "TikTok", "Email", "YouTube", "SEO Content"]
TRAFFIC_CHANNELS = ["Organic Search", "Paid Search", "Social", "Direct", "Email", "Referral"]
DEVICES = ["Desktop", "Mobile", "Tablet"]


def seasonal_factor(d: date) -> float:
    """Simple annual seasonality with a year-end peak and a soft April dip."""
    m = d.month
    base = {1: 0.95, 2: 0.9, 3: 0.95, 4: 0.85, 5: 0.95, 6: 1.0,
            7: 1.0, 8: 1.05, 9: 1.0, 10: 1.05, 11: 1.25, 12: 1.4}[m]
    weekday = 1.1 if d.weekday() >= 5 else 1.0  # weekend bump for consumer buying
    growth = 1 + 0.15 * ((d - START).days / DAYS)  # ~15% growth over the period
    return base * weekday * growth


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    size_kb = os.path.getsize(path) / 1024
    print(f"  wrote {os.path.basename(path):26s} {len(rows):>7,} rows  {size_kb:>8.1f} KB")


def gen_products(out):
    rows = []
    pid = 1
    for cat, names in CATEGORIES.items():
        for name in names:
            for brand in rng.sample(BRANDS, 2):
                cost = round(rng.uniform(150, 6000), 2)
                price = round(cost * rng.uniform(1.3, 2.2), 2)
                rows.append([f"P{pid:04d}", f"{brand} {name}", cat, name, brand,
                             price, cost, rng.choice(["Active", "Active", "Active", "Discontinued"])])
                pid += 1
    write_csv(os.path.join(out, "products.csv"),
              ["product_id", "product_name", "category", "sub_category", "brand",
               "unit_price", "unit_cost", "status"], rows)
    return rows


def gen_customers(out, n=2000):
    rows = []
    for i in range(1, n + 1):
        region = rng.choice(list(REGIONS))
        prov = rng.choice(REGIONS[region])
        seg = rng.choices(SEGMENTS, weights=[60, 15, 25])[0]
        signup = START - timedelta(days=rng.randint(0, 900))
        rows.append([f"C{i:05d}", f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_INITIALS)}.",
                     seg, region, prov, signup.isoformat(),
                     rng.choice(["Male", "Female", "Prefer not to say"]),
                     rng.choice(["18-24", "25-34", "35-44", "45-54", "55+"]),
                     rng.choice(["Yes", "No"])])
    write_csv(os.path.join(out, "customers.csv"),
              ["customer_id", "customer_name", "segment", "region", "province",
               "signup_date", "gender", "age_group", "loyalty_member"], rows)
    return rows


def gen_sales(out, products, customers, target_rows=18000):
    rows = []
    prod_ids = [p[0] for p in products]
    prod_price = {p[0]: p[5] for p in products}
    prod_cost = {p[0]: p[6] for p in products}
    cust_ids = [c[0] for c in customers]
    oid = 100000
    per_day = target_rows / DAYS
    for i in range(DAYS):
        d = START + timedelta(days=i)
        k = max(0, int(rng.gauss(per_day * seasonal_factor(d), per_day * 0.3)))
        for _ in range(k):
            oid += 1
            pid = rng.choice(prod_ids)
            qty = rng.choices([1, 2, 3, 4, 5], weights=[55, 25, 10, 6, 4])[0]
            disc = rng.choices([0, 0.05, 0.1, 0.15, 0.2], weights=[60, 15, 12, 8, 5])[0]
            price = prod_price[pid]
            sales = round(price * qty * (1 - disc), 2)
            cost = round(prod_cost[pid] * qty, 2)
            ship_days = rng.choices([1, 2, 3, 5, 7], weights=[30, 35, 20, 10, 5])[0]
            status = rng.choices(["Completed", "Returned", "Cancelled"], weights=[92, 5, 3])[0]
            rows.append([f"SO{oid}", d.isoformat(), (d + timedelta(days=ship_days)).isoformat(),
                         rng.choice(cust_ids), pid, rng.choice(CHANNELS_SALES),
                         rng.choice(PAYMENTS), qty, price, disc, sales, cost,
                         round(sales - cost, 2), status])
    write_csv(os.path.join(out, "sales_orders.csv"),
              ["order_id", "order_date", "ship_date", "customer_id", "product_id",
               "sales_channel", "payment_method", "quantity", "unit_price", "discount",
               "sales_amount", "cost_amount", "profit", "order_status"], rows)


def gen_marketing(out):
    rows = []
    cid = 1
    d = START.replace(day=1)
    while d <= END:
        for ch in MKT_CHANNELS:
            if rng.random() < 0.75:
                budget = round(rng.uniform(5000, 120000), -2)
                spend = round(budget * rng.uniform(0.7, 1.0), 2)
                impressions = int(spend * rng.uniform(15, 60))
                clicks = int(impressions * rng.uniform(0.005, 0.05))
                leads = int(clicks * rng.uniform(0.02, 0.15))
                conversions = int(leads * rng.uniform(0.1, 0.4))
                revenue = round(conversions * rng.uniform(800, 4500), 2)
                end = (d.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
                rows.append([f"MK{cid:04d}", f"{ch} {d.strftime('%b %Y')}", ch,
                             rng.choice(["Awareness", "Lead Gen", "Conversion", "Retargeting"]),
                             d.isoformat(), end.isoformat(), budget, spend,
                             impressions, clicks, leads, conversions, revenue])
                cid += 1
        d = (d.replace(day=28) + timedelta(days=4)).replace(day=1)
    write_csv(os.path.join(out, "marketing_campaigns.csv"),
              ["campaign_id", "campaign_name", "channel", "objective", "start_date", "end_date",
               "budget", "spend", "impressions", "clicks", "leads", "conversions", "revenue"], rows)


def gen_web_traffic(out):
    rows = []
    for i in range(DAYS):
        d = START + timedelta(days=i)
        f = seasonal_factor(d)
        for ch in TRAFFIC_CHANNELS:
            base = {"Organic Search": 1800, "Paid Search": 700, "Social": 900,
                    "Direct": 600, "Email": 250, "Referral": 200}[ch]
            for dev in DEVICES:
                share = {"Desktop": 0.4, "Mobile": 0.52, "Tablet": 0.08}[dev]
                sessions = max(1, int(rng.gauss(base * f * share, base * share * 0.15)))
                users = int(sessions * rng.uniform(0.75, 0.95))
                pageviews = int(sessions * rng.uniform(1.8, 4.5))
                bounce = round(rng.uniform(0.3, 0.7), 3)
                avg_dur = round(rng.uniform(45, 240), 1)
                conv = int(sessions * rng.uniform(0.005, 0.03))
                rows.append([d.isoformat(), ch, dev, sessions, users, pageviews,
                             bounce, avg_dur, conv])
    write_csv(os.path.join(out, "web_traffic.csv"),
              ["date", "channel", "device", "sessions", "users", "pageviews",
               "bounce_rate", "avg_session_duration_sec", "conversions"], rows)


def gen_hr(out):
    rows = []
    d = START.replace(day=1)
    headcount = {dep: rng.randint(8, 45) for dep in DEPARTMENTS}
    while d <= END:
        for dep in DEPARTMENTS:
            hires = rng.choices([0, 1, 2, 3], weights=[50, 30, 15, 5])[0]
            exits = rng.choices([0, 1, 2], weights=[65, 25, 10])[0]
            headcount[dep] = max(3, headcount[dep] + hires - exits)
            for lvl in LEVELS:
                share = {"Junior": 0.3, "Mid": 0.3, "Senior": 0.2, "Lead": 0.12, "Manager": 0.08}[lvl]
                hc = max(0, int(round(headcount[dep] * share)))
                if hc == 0:
                    continue
                rows.append([d.isoformat(), dep, lvl, hc,
                             round(rng.uniform(25000, 45000) * {"Junior": 1, "Mid": 1.5, "Senior": 2.2,
                                                                 "Lead": 2.8, "Manager": 3.5}[lvl], -2),
                             rng.choices(["Bangkok HQ", "Rayong Plant", "Chiang Mai Hub"],
                                         weights=[70, 20, 10])[0]])
            rows.append([d.isoformat(), dep, "_movement", hires, exits, "ALL"])
        d = (d.replace(day=28) + timedelta(days=4)).replace(day=1)
    # Two record types share one file on purpose (lab 06 teaches CASE + filters to split them)
    write_csv(os.path.join(out, "hr_headcount.csv"),
              ["month", "department", "level", "headcount_or_hires", "avg_salary_or_exits",
               "location"], rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    print(f"Generating datasets (seed={SEED}) into {args.out}")
    products = gen_products(args.out)
    customers = gen_customers(args.out)
    gen_sales(args.out, products, customers)
    gen_marketing(args.out)
    gen_web_traffic(args.out)
    gen_hr(args.out)
    print("Done.")


if __name__ == "__main__":
    main()
