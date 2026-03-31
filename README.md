# Soko Mart — Seller-First Order Aggregation PWA

> Know what to buy before you go to market. Sell everything. Waste nothing.

One HTML file. Zero backend. Works offline. Deploy free on GitHub Pages in 5 minutes.

## The core pivot from Mtaa Mart

Instead of bypassing the local vendor to go to a bulk supplier, this system **empowers the local vendor**. A mama mboga who knows by Thursday night that she has 23 confirmed tomato orders, 15 unga requests, and 8 egg trays goes to market at 4AM and buys **exactly that**. Zero waste. Zero guesswork. Everything sells.

## What's inside

| Tab | Who uses it | What it does |
|-----|------------|--------------|
| **How it works** | Everyone | Dynamic infographic — updates when admin changes any setting |
| **4-Week Test** | Operator | Zero-cost viability protocol + data tracker |
| **WhatsApp Templates** | Vendor | 3 ready-to-send Monday morning broadcast messages (Swahili/English) |
| **Manuals** | Each stakeholder | 8 expandable instruction manuals (Vendor, Customer, Boda Rider, Aggregator, Sanifu AI, Farm Supplier, RA, Operator) |
| **Workbook** | Vendor/Operator | 8 tabs: Dashboard · Order Capture · Thursday Tally · Shopping List · Waste Log · Aggregator Pool · Sanifu Export · P&L |
| **Survey** | Customers | Demand survey — products, pre-order willingness, trust signals |
| **Seller Sign-up** | Vendors | Pilot sign-up with waste baseline and WhatsApp group size |
| **Results** | Operator | Live charts + export to .txt pitch brief, Sanifu CSV, full .xlsx |
| **Admin (PIN)** | Operator | Edit all settings — vendor profile, products, prices, Sanifu webhook |

## Deploy to GitHub Pages in 5 minutes

1. github.com → New repository → name `soko-mart` → Public
2. Upload all files (drag-and-drop, upload icons/ folder separately)
3. Settings → Pages → Deploy from branch: main → Save
4. Live at: `https://[your-username].github.io/soko-mart/`

## First-time setup

1. Open app → Admin → PIN: `1234` → **change immediately**
2. Enter vendor/operator name, location, M-Pesa paybill
3. Add your products with market price and sell price
4. Set your current waste % baseline (honest estimate)
5. Save → entire app updates

## The Sanifu AI integration path

**Phase 1 (now):** Thursday tally generates a structured CSV. Operator emails or WhatsApps it to Sanifu manually. Zero code needed.

**Phase 2:** Add Sanifu's webhook URL in Admin → Sanifu Integration. App posts JSON demand signal automatically on Thursday night.

**Phase 3:** Sanifu sends reorder recommendations back. Bi-directional real-time sync.

The demand layer (Soko Mart) feeds the inventory layer (Sanifu). Neither needs to build the other's side.

## The 4-week zero-cost viability test

Built into the app. Track:
- Thursday replies collected (intent signal)
- Prepaid even Ksh 50 (trust signal)  
- No-show rate (commitment signal)
- Vendor waste % week-on-week (impact signal)

No prepayment in Week 1. Add deposit ask in Week 3 only.

## Workbook tabs explained

| Tab | Purpose |
|-----|---------|
| Dashboard | Live KPIs: orders, GMV, deliveries, waste % |
| Order Capture | Enter each customer's WhatsApp reply + M-Pesa status |
| Thursday Tally | Auto-sums all confirmed (paid) orders per product |
| Shopping List | Clean printable list — take this to market, buy only this |
| Waste Log | Log unsold stock after every Friday — learning data |
| Aggregator Pool | Shows this vendor's contribution to the pooled wholesale order |
| Sanifu Export | Structured JSON/CSV demand signal for Sanifu AI |
| P&L | Weekly and annualised profit including waste cost |

## Files
```
soko-mart-pwa/
├── index.html     ← The entire app (132KB, single file)
├── manifest.json  ← PWA metadata
├── sw.js          ← Service worker (offline)
├── icons/         ← App icons
└── README.md      ← This file
```

Zero capital to start. WhatsApp + this app + one honest vendor.
