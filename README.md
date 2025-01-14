# E-Commerce Customer Behavior Dashboard
### 🚀 Overview
This project is a web-based dashboard that provides businesses with key insights into customer behavior, inventory status, and sales trends. Leveraging Airbyte for data integration and Motherduck (DuckDB) for efficient querying, the dashboard is built with Streamlit for a modern and interactive user interface.

### 📂 Directory Structure

E-COMMERCE-BEHAVIOR-ANALYSIS  
├── src  
│   ├── app.py                 
│   ├── utils  
│   │   ├── database.py        
│   └── config  
│       ├── config.py             
├── .venv                        
├── .env                                    
├── README.md                  


### 🛠️ Technologies Used
Airbyte: For seamless data integration.
Motherduck (DuckDB): Fast and lightweight SQL engine.
Streamlit: Interactive web-based dashboard framework.
Python: Core language for backend and data processing.
Plotly: For creating intuitive and interactive visualizations.

### ⚙️ Features
Inventory Status

Monitor stock levels and identify low-stock items.
Sales Trends

Analyze total sales over time with interactive line charts.
Customer Insights
Identify top customers by total spending.

## 🚀 Getting Started
### 1. Clone the Repository

`git clone https://github.com/your-username/E-COMMERCE-BEHAVIOR-ANALYSIS.git`  

`cd E-COMMERCE-BEHAVIOR-ANALYSIS`

### 2. Set Up Virtual Environment

`python -m venv .venv`  
Activate the environment:


### For Command Prompt  
`.\.venv\Scripts\activate`  

### For PowerShell  
`.\.venv\Scripts\Activate.ps1`  



### 3. Configure Environment Variables
Create a .env file in the project root and add your Motherduck Token:

MOTHERDUCK_TOKEN=your_token_here  

### 4. Run the Application

`streamlit run src/app.py`

## 📊 Dashboard Overview

Inventory Status: Displays available stock for each product.
Sales Trends: Interactive line chart showing sales over time.
Customer Insights: Bar chart of top customers by total spend.
📝 Example Queries
Sales Trends Query


`SELECT  
    date,  
    SUM(CAST(Quantity AS INTEGER) * UnitPrice) AS TotalSales  
FROM my_db.main.data  
GROUP BY date  
ORDER BY date;  
Customer Insights Query`

`SELECT  
    customerid,  
    SUM(CAST(Quantity AS INTEGER) * UnitPrice) AS TotalSpend  
FROM my_db.main.data  
GROUP BY customerid  
ORDER BY TotalSpend DESC  
LIMIT 10;`

## 🛡️ Security
Sensitive tokens (e.g., MOTHERDUCK_TOKEN) are stored securely in the .env file and not committed to version control.

## 🙌 Contributing
Fork the repository.
Create a new branch for your feature (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a pull request.

##  Running Application Link
https://super-winner-rwq77gg459xhx9jq-8501.app.github.dev/

## 📄 License
This project is licensed under the MIT License.

## 💬 Contact
For any questions, feel free to reach out:

Email: nitishmlng@gmail.com
