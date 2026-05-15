# Odoo 19 – Sales module with real‑time revenue (CA)

Custom Odoo 19 module for sales management. Features computed field for instant total revenue (CA), XML views (list/form), CSV security, and Power BI integration via ODBC. Deployed on Debian VM.

## 🧱 Tech stack
- Odoo 19
- PostgreSQL 15
- Power BI
- Debian 12 / WinSCP / PyCharm

## 📂 Project structure (arborescence)

![Arborescence du module](docs/screenshots/Arborescence%20du%20module.png)


## 🚀 Installation
1. Copy `code/ventes/` into `/usr/lib/python3/dist-packages/odoo/addons/`
2. Restart Odoo: `sudo systemctl restart odoo`
3. Activate "Compta CA" from Apps

## 📸 Screenshots
![Odoo form](docs/screenshots/odoo_form.png)
![Power BI dashboard](docs/screenshots/powerbi_dashboard.png)
![Odoo CA](docs/screenshots/odoo_CA.png)
![ODBC config](docs/screenshots/odbc_config.png)


## 👤 Author
Asmae SERJI – Academic project supervised by Pr. Abdellah ZAOUIA
