# demohub
DemoHub – A Django reference project demonstrating permission-driven UI, role-based access control, clean redirects, and reusable decorators without unnecessary database tables.

# DemoHub 🚀

DemoHub is a **Django reference project** demonstrating:

- Permission-based navigation (sidebar auto-hides links)
- Clean role-based access control (RBAC)
- Reusable permission decorators
- Unauthorized access handling (no 403 errors)
- Layout separation for protected vs public pages

This project is ideal for:
- Learning Django permissions
- Admin dashboards
- Enterprise systems
- Teaching best practices

---

## 🔐 Permission Strategy

DemoHub uses **Django permissions without creating unnecessary models**.

Permissions are:
- Attached to apps
- Created manually or via migration hooks
- Checked via a custom decorator

Example permissions:
- `accounts.view_dashboard`
- `demo.view_demo`
- `hub.view_hub`
- `setup.view_setup`


 ## 👨‍💻 Author

**ENG KAYOMBO**

- Backend Engineer (Django, REST, Permissions)
- Mobile & Web Systems Architect
- Focus: secure, scalable business systems

📍 Tanzania  
📫 Contact: gasperkayombo57@gmail.com  
🔗 GitHub: https://github.com/intersofthubtz
