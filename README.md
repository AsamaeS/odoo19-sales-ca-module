# Odoo 19 – Sales module with real‑time revenue (CA)

Custom Odoo 19 module for sales management. Features computed field for instant total revenue (CA), XML views (list/form), CSV security, and Power BI integration via ODBC. Deployed on Debian VM.

## 🧱 Tech stack
- Odoo 19
- PostgreSQL 15
- Power BI
- Debian 12 / WinSCP / PyCharm

## 📂 Project structure (arborescence)

![Arborescence du module](docs/screenshots/arborescence.png)

## 🚀 Installation
1. Copy `code/ventes/` into `/usr/lib/python3/dist-packages/odoo/addons/`
2. Restart Odoo: `sudo systemctl restart odoo`
3. Activate "Compta CA" from Apps

## 📸 Screenshots
Place your screenshots inside `docs/screenshots/` and link them:
![Odoo form](docs/screenshots/odoo_form.png)
![Power BI dashboard](docs/screenshots/powerbi_dashboard.png)

## 👤 Author
Asmae SERJI – Academic project supervised by Pr. Abdellah ZAOUIA
