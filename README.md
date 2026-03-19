# Mtaa Mart — Community Enterprise PWA

A Progressive Web App for RA-governed community bulk buying cooperatives in Kenya.

## Live Deploy to GitHub Pages (5 minutes)

### Step 1 — Create a GitHub account
Go to [github.com](https://github.com) and sign up for free if you don't have an account.

### Step 2 — Create a new repository
1. Click the **+** button (top right) → **New repository**
2. Name it: `mtaa-mart` (or anything you like)
3. Set it to **Public**
4. Click **Create repository**

### Step 3 — Upload files
1. Click **uploading an existing file** on the empty repo page
2. Drag and drop ALL files from this folder:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `icons/icon-192.png`
   - `icons/icon-512.png`
3. For the icons folder: click **create new file**, type `icons/icon-192.png`, then upload
4. Click **Commit changes**

### Step 4 — Enable GitHub Pages
1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Under **Source**, select **Deploy from a branch**
3. Branch: **main**, Folder: **/ (root)**
4. Click **Save**

### Step 5 — Your live URL
After 2–3 minutes your app will be live at:
```
https://[your-github-username].github.io/mtaa-mart/
```

Share this URL in the estate WhatsApp group. Members can:
- Open it in any browser (works on all phones)
- Tap "Add to Home Screen" to install it like a native app
- Use it fully offline once installed

---

## What the app does

| Tab | Who uses it | Purpose |
|-----|------------|---------|
| **How it works** | Everyone | Dynamic infographic — updates when admin changes any rule |
| **Survey** | Households | Anonymous demand survey — goods, services, budget |
| **Sign up** | All stakeholders | Named commitment sheet for RA committee |
| **Results** | Committee | Live bar charts, sign-up sheet, export for manufacturer pitch |
| **Admin** | Committee (PIN-protected) | Change ALL rules — Hisa, margins, products, boda fees, estate details |

## Admin PIN
Default PIN: **1234**
Change it immediately after first login in the Admin → Security section.

## Data storage
All data is stored in the browser's **localStorage** on the device running the admin panel.
For a shared setup, one committee member should serve as the data host (they open the app
on their phone/laptop and it stores data there).

For a fully shared cloud database, the committee can export data weekly using the
"Export" buttons and share the files via WhatsApp or email.

## Customisation (Admin panel)
Everything is editable without touching code:
- Estate name, chairman, secretary, treasurer, paybill number
- Hisa earning rules (referral points, loyalty bonus, threshold for Co-Owner)
- Financial assumptions (bulk discount %, member saving %, mart margin %)
- Boda boda delivery fee per drop, bonus threshold, Hisa award schedule
- Full product catalogue (add, edit, remove products with retail and bulk prices)
- Services list shown in the survey

All changes instantly update the infographic on the "How it works" tab.

## Offline capability
Once installed, the app works completely offline. This is critical for estates
with intermittent internet connectivity.

## Files
```
mtaa-mart-pwa/
├── index.html      ← The entire app (single file, no dependencies)
├── manifest.json   ← PWA metadata
├── sw.js           ← Service worker (offline support)
├── icons/
│   ├── icon-192.png
│   └── icon-512.png
└── README.md       ← This file
```

## Sharing the URL
Once deployed, share the GitHub Pages URL via:
- Estate WhatsApp group (pin the message)
- Estate noticeboard (print as QR code at any Mpesa agent)
- Word of mouth — the URL is short and memorable

## Support
Built for Kenyan Residents' Associations under the Co-operatives Act.
Governed by your RA committee. Not an MLM.
