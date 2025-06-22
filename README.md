# 🤖 Django Telegram Bot with Celery & Redis

A Django-based Telegram Bot integrated with Celery and Redis for asynchronous task handling. This project supports user registration, command-based interaction via Telegram, and background task execution like simulated email logging.

## 🤖 Telegram Bot

Start chatting with the bot here: [@pingforce_bot](https://t.me/pingforce_bot)

---

## 🛠️ Tech Stack

- **Django 5**
- **Django REST Framework**
- **Celery**
- **Redis**
- **python-telegram-bot v13.15**
- **PostgreSQL/SQLite**
- **Python 3.10+**

---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/PavaniReddy65/django-telegram-bot.git
   cd django-telegram-bot
Create virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate  # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure .env:

env
Copy code
TELEGRAM_BOT_TOKEN=your_token_here
Apply migrations:

bash
Copy code
python manage.py migrate
Run Celery:

bash
Copy code
celery -A myproject worker -l info --pool=solo
Run the bot:

bash
Copy code
python manage.py telegrambot
(Optional) Run the Django server:

bash
Copy code
python manage.py runserver
🤖 Telegram Bot Commands
Command	Description
/start	Greets the user
/register	Registers the user in memory
/status	Shows total registered users
/menu	Displays two interactive buttons
/sendemail	Triggers Celery task to send a dummy email

📨 Celery Task: send_welcome_email
Accepts Telegram username

Logs dummy email to the EmailLog model

Viewable in Django Admin

📸 Screenshots
Here are some examples of how the bot responds:

Screenshots will be added later.

👩‍💻 Author
Pavani Pitti
B.Tech in AI & Data Science
St. Mary’s Women’s Engineering College
GitHub: PavaniReddy65

📄 License
This project is for educational and internship assessment purposes only.

yaml
Copy code

2. Go back to Notepad and **right-click inside it → Paste** (or press `Ctrl + V`).

---

### Step 4: Save as README.md

1. Click **File** → **Save As**.
2. In the **Save As** window:  
   - Navigate to the folder you created on Desktop (`C:\Users\hi\Desktop\django-telegram-bot`)  
   - In **File name** type exactly:  
     ```
     README.md
     ```  
   - In **Save as type**, select **All Files (*.*)**  
   - In **Encoding**, select **UTF-8** (if available)  
3. Click **Save**.

---

### Step 5: Confirm the file is saved

- Go to your Desktop → open `django-telegram-bot` folder.
- You should see the file named **README.md** (with the icon like a markdown file).

---

### Step 6: Next steps (push to GitHub)

After this, you can open PowerShell and run:

```bash
cd C:\Users\hi\Desktop\django-telegram-bot
git init
git remote add origin https://github.com/PavaniReddy65/django-telegram-bot.git
git add README.md
git commit -m "📝 Added README.md"
git branch -M main
git push -u origin main