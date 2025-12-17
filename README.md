# Django Recipe Project

## Prerequisites
- Python 3.8+
- pip

## Setup Instructions

1. **Clone or Download** this project structure.

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access Application**:
   Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)