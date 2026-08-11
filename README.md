# 🎓 RupeeMate — Student Expense & Budget Tracker

**RupeeMate** is a modern, full-featured personal and shared financial management web application tailored specifically for students. Built with Python Flask, SQLite, SQLAlchemy, Chart.js, and a sleek responsive frontend design system.

---

## 🚀 Key Features

* **Multi-User Authentication & Security**:
  * Secure user registration, password hashing (Werkzeug), and session management.
  * **Google Sign-In / OAuth** integration via Google Identity Services.
  * Complete per-user data isolation across all financial records.

* **Smart Student Dashboard**:
  * **Real-time KPI Cards**: Available Balance, Active Budget, Total Spent, Remaining Budget, and Recommended Daily Allowance.
  * **Dynamic Budget Pacing**: Multi-state visual progress bar (Healthy, Warning, Critical, Danger) with days-remaining countdown.
  * **Interactive Chart.js Visuals**: Category doughnut breakdown and 30-day daily spending trend bar charts.
  * **Recent Transactions & Smart Insights**: Automatic detection of high spending categories and velocity alerts.

* **Expense Management with Receipt Upload**:
  * Full CRUD (Create, Read, Update, Delete) with validation and delete protection.
  * Search by description, notes, and category.
  * Filter by category, payment method (UPI, Cash, Debit Card, Credit Card, Bank Transfer, Other), and date ranges.
  * **Quick Date Preset Chips**: *Today*, *This Week*, *This Month*, *Last Month*, *All Time*.
  * **Receipt / Bill Attachment**: Upload images (PNG/JPG/WEBP) or PDF receipts directly to expenses.

* **⚡ SMS & UPI Transaction Text Parser**:
  * Paste any bank/UPI SMS (GooglePay, PhonePe, Paytm, HDFC, SBI, ICICI, etc.) and auto-extract amount, merchant, date, and suggested student category in 1 second.

* **👥 Roommate & Shared Expense Splitting (Splitwise-style)**:
  * Create groups (e.g. *Room 304 Flatmates*, *Goa Trip 2026*, *Mess Committee*).
  * Add friends by name and email.
  * Log shared bills with equal or custom splits.
  * Automatic pairwise balance calculation and **simplified debt matrix** (*"Who owes whom"*).
  * Direct debt settlement workflow with payment notes.

* **🎯 Overall & Category-Specific Budgets**:
  * Set overall monthly, weekly, or custom date-range budget targets.
  * Set **individual monthly limits per category** (e.g. max ₹3,000 on Food, max ₹1,000 on Entertainment) with visual progress meters and overspend alerts.

* **Income & Allowance Tracking**:
  * Log pocket money, allowances, scholarships, part-time jobs, and freelance gigs.
  * Real-time net balance calculations (`Total Income − Total Expenses`).

* **Category Customization**:
  * 11 default student categories (🍔 Food & Dining, 🚌 Transport, 📚 Books & Supplies, 🎓 College Fees, 🏠 Hostel & Rent, 💻 Tech & Subscriptions, 👕 Shopping, 🍿 Entertainment, 💊 Healthcare, 🏋️ Gym & Fitness, 📦 Other).
  * Create, edit, and delete custom categories with custom icons and theme colors.
  * **Safe Deletion**: Prompt to reassign existing expenses to another category before deletion.

* **Savings Goals**:
  * Set goals for laptops, semester fees, trips, or emergency funds.
  * Deposit workflow with progress meters.

* **Recurring Subscriptions & Bills**:
  * Track monthly/weekly bills (Netflix, Spotify, WiFi, Hostel Rent).
  * "Mark Paid & Advance" feature that automatically logs the expense and computes the next due date.

* **Export & Monthly Statements**:
  * Filtered CSV download.
  * Printable, branded monthly student statement with summary KPIs.

* **🤖 Smart AI Finance Advisor**:
  * Natural language Q&A for student budgeting, affordability checks, and spending analysis.
  * Built-in local rules engine with **optional live Google Gemini 1.5 Flash API integration** (`GEMINI_API_KEY`).

* **📱 Progressive Web App (PWA) & Shortcuts**:
  * Installable on Android & iOS homescreens via `manifest.json` and Service Worker (`sw.js`).
  * Global Keyboard Shortcuts: <kbd>N</kbd> (New Expense), <kbd>/</kbd> (Search), <kbd>T</kbd> (Theme Toggle), <kbd>P</kbd> (SMS Paste), <kbd>Esc</kbd> (Close Modal).

---

## 🛠️ Project Architecture

```
Student Expense & Budget Tracker/
├── app.py                      # Flask application factory & routes
├── config.py                   # Configuration & environment variables
├── wsgi.py                     # WSGI production server entry point
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
├── models/                     # SQLAlchemy data models
│   ├── __init__.py
│   ├── user.py
│   ├── category.py
│   ├── expense.py
│   ├── income.py
│   ├── budget.py
│   ├── category_budget.py
│   ├── savings.py
│   ├── recurring.py
│   └── group.py
├── services/                   # Business logic services
│   ├── budget_service.py
│   ├── analytics_service.py
│   ├── insight_service.py
│   ├── export_service.py
│   ├── ai_service.py
│   ├── sms_parser_service.py
│   └── group_service.py
├── routes/                     # Modular API endpoints
│   ├── auth.py
│   ├── expenses.py
│   ├── incomes.py
│   ├── budgets.py
│   ├── category_budgets.py
│   ├── categories.py
│   ├── analytics.py
│   ├── savings.py
│   ├── recurring.py
│   ├── export.py
│   ├── ai.py
│   ├── groups.py
│   └── sms_parser.py
├── templates/
│   └── index.html              # Modern SPA dashboard template
├── static/
│   ├── manifest.json           # PWA Web App manifest
│   ├── sw.js                   # Service Worker cache script
│   ├── css/
│   │   └── style.css           # CSS design system (Dark & Light themes)
│   ├── js/
│   │   └── app.js              # Complete client-side controller
│   └── uploads/
│       └── receipts/           # Local receipt storage directory
└── tests/                      # Automated Pytest suite (27 passing tests)
```

---

## ⚡ Quick Start

### 1. Installation
```bash
# Clone or navigate to the directory
cd "Student Expense & Budget Tracker"

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)
Copy `.env.example` to `.env` to configure Google Sign-In or Gemini AI:
```bash
cp .env.example .env
```

### 3. Run Development Server
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

### 4. Run Automated Tests
```bash
pytest tests/ -v
```

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```
The app will be accessible at `http://localhost:5000`.