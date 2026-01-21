
```md
# DemoHub 🚀  
**A Django Permission-Driven Demo Platform**

DemoHub is a **reference Django project** that demonstrates how to build a clean, secure, and user-friendly system using **permission-based access control**, **role-aware navigation**, and **reusable decorators** — without unnecessary database complexity.

This repository is designed to be **educational, reusable, and production-inspired**.

---

## ✨ Key Features

- 🔐 **Permission-driven access control**
- 🧠 **Reusable custom permission decorators**
- 🧭 **Sidebar navigation auto-hides unauthorized links**
- 🚫 **No Django 403 errors shown to users**
- 🧼 **Clean redirect flow (login → authorized → logout)**
- 🧱 **Layout separation for protected vs public pages**
- 🎯 **No extra models required just for permissions**
- ⚡ **Lightweight UI using Tailwind CSS + Alpine.js**

---

## 🎯 Project Goal

The main goal of DemoHub is to show **how permissions should drive both backend logic and frontend UI** in a Django application.

Instead of:
- hard-coding links
- relying on raw 403 pages
- duplicating permission logic everywhere

DemoHub centralizes **all access control logic** and applies it consistently across:
- views
- templates
- navigation
- redirects

---

## 🗂️ Project Structure

```

demohub/
│
├─ demohub/                 # Project settings
│   ├─ settings.py
│   ├─ urls.py
│   └─ wsgi.py
│
├─ accounts/                # Authentication & dashboard
│   ├─ views.py
│   ├─ urls.py
│   └─ templates/accounts/
│
├─ demo/                    # Demo module
├─ hub/                     # Hub module
├─ setup/                   # Setup module
│
├─ common/                  # Shared logic
│   ├─ decorators.py        # Permission decorators
│   └─ context_processors.py
│
├─ templates/
│   ├─ base.html
│   ├─ accounts/
│   │   ├─ sidebar.html
│   │   ├─ header.html
│   │   └─ unauthorized.html
│
├─ static/
├─ requirements.txt
├─ README.md
└─ LICENSE

```

---

## 🔐 Permission Strategy (Core Idea)

DemoHub uses **Django’s built-in permission system**, but in a **cleaner and more intentional way**.

### ✔ No unnecessary database tables  
### ✔ No permission logic scattered in views  
### ✔ No UI leaks  

Permissions are defined per app, for example:

- `accounts.view_dashboard`
- `demo.view_demo`
- `hub.view_hub`
- `setup.view_setup`

---

## 🧠 Custom Permission Decorator

All access control logic lives in **one place**:

```

common/decorators.py

````

### Example Usage

```python
from common.decorators import permission_required_redirect

@permission_required_redirect("hub.view_hub")
def hub_list(request):
    return render(request, "hub/hub_list.html")
````

### Behavior

| Situation                            | Result                                |
| ------------------------------------ | ------------------------------------- |
| User not authenticated               | Redirect to logout → session cleared  |
| User authenticated but no permission | Redirect to `/accounts/unauthorized/` |
| User has permission                  | View renders normally                 |

✅ No Django 403 pages
✅ No broken layouts
✅ No exposed internal routes

---

## 🚫 Unauthorized Access Handling

When a user accesses a page they are **not allowed to see**:

* They are redirected to a **plain Unauthorized page**
* **No sidebar**
* **No header**
* **No internal navigation**

This avoids:

* UI confusion
* permission leakage
* broken user experience

---

## 🧭 Permission-Aware Sidebar

The sidebar automatically adapts to the logged-in user.

```django
{% if sidebar_perms.demo %}
  <a href="{% url 'demo:demo_list' %}">Demo</a>
{% endif %}
```

Users **only see what they are allowed to access**.

---

## 👤 Authentication Flow

1. User visits any protected page
2. If not logged in → redirected to login
3. If logged in but unauthorized → redirected to Unauthorized page
4. Logout clears session and redirects to login

This flow is:

* predictable
* secure
* user-friendly

---

## 🧪 Ideal Use Cases

DemoHub is useful for:

* Learning Django permissions
* Admin dashboards
* Internal tools
* Enterprise systems
* Teaching RBAC concepts
* Bootstrapping real projects

---

## ⚙️ Installation

```bash
git clone https://github.com/intersofthubtz/demohub.git
cd demohub
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📌 Notes

* Database (`db.sqlite3`) is intentionally excluded
* Permissions should be created via Django admin or migration hooks
* This is a **reference architecture**, not a feature-heavy app

---

## 👨‍💻 Author

**ENG KAYOMBO**
Backend Engineer | Django & System Architecture

* Focus: secure, scalable, permission-driven systems
* GitHub: [https://github.com/intersofthubtz](https://github.com/intersofthubtz)

---

## 📄 License

MIT License – free to use, modify, and learn from.

---

## ⭐ Final Note

If you are building a Django system that requires **clean permissions, safe navigation, and a professional UX**, DemoHub shows **how it should be done**.

```

---

### My honest opinion

This README positions your project as:
- **intentional**
- **architectural**
- **professional**

It clearly communicates *thinking*, not just code — which is what makes a repo valuable.

If you want next, I can:
- Add **screenshots section**
- Add **permission auto-seeding**
- Write **tests**
- Optimize README for recruiters

Just say the word.
```
