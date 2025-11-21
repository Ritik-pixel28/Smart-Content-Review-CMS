# Smart Content Review & Publish Flow System (Mini CMS)

##  Team Members
- Ritik Arya (PST-25-0129)
- Prakhar Joshi (PST-25-0215)

## 📌 Project Type
Open Source Developer — OJT Project

## 🧰 Tech Stack
- Python 3.14
- Django
- Wagtail CMS
- HTML / CSS / JavaScript

---

# 1️⃣ Problem Statement
In many CMS platforms, content gets published without proper validation or review.
This causes issues such as:
- Missing metadata
- Poor content quality
- SEO issues
- Policy violations

Our project introduces a **smart pre-publish checklist system** inside Wagtail.
A page cannot be published until:
- All required fields are filled
- Reviewer approves the checklist
- Audit log is created

---

# 2️⃣ Why This Project is Important
This system ensures:
✔ Editorial quality  
✔ Proper workflow  
✔ Better collaboration  
✔ No accidental publishing  
✔ Complete accountability through audit logs  

---

# 3️⃣ Features (Planned)
- Dynamic checklist for each page  
- Approve / Reject workflow  
- Reviewer comments  
- Publishing block logic  
- Audit log for actions  
- Sidebar UI showing progress  

---

# 4️⃣ Week-1 Deliverables (Completed)
✔ Installed Django & Wagtail  
✔ Created Wagtail project (`smartcms`)  
✔ Created virtual environment  
✔ Created new Django app: `checklist`  
✔ Added app to `INSTALLED_APPS`  
✔ Created empty models for planning  
✔ Project structure ready  
✔ README.md created  

---

# 5️⃣ Folder Structure
smartcms/
checklist/
models.py
views.py
admin.py
…
home/
search/
smartcms/
settings/
urls.py
manage.py


# 6️⃣ How to Run the Project 
python3 -m venv myenv
source myenv/bin/activate
pip install wagtail
python3 manage.py migrate
python3 manage.py runserver

---

# 7️⃣ Next Week (Week 2) Plan
- Implement checklist model  
- Add audit log model  
- Add Wagtail hooks (`before_publish_page`)  
- Block publish until checklist complete  
- Initial UI for checklist panel  