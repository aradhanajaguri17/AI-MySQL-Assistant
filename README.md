# AI MySQL Assistant

A simple AI assistant that converts natural-language questions into MySQL SELECT queries and displays the results using Streamlit.

## Architecture

User -> Streamlit -> Groq AI -> SQL -> MySQL -> Result -> AI Answer

## Setup

### 1. Create virtual environment (optional)

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Create the MySQL database

Open MySQL Workbench or MySQL terminal and run:

```bash
mysql -u root -p < setup.sql
```

Or paste the contents of `setup.sql` into MySQL Workbench.

### 4. Configure environment variables

Rename `.env.example` to `.env` and add:

```env
GROQ_API_KEY=your_groq_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=ai_assistant
```

### 5. Run Streamlit

```bash
streamlit run app.py
```

## Sample Questions

1. Show me all customers
2. Show customers from Chandigarh
3. What is the total sales?
4. Show all orders above 5000
5. Which product generated the most sales?
6. Show the customers who bought a laptop

## Important

This demo allows only SELECT queries. Do not expose your database credentials publicly.
