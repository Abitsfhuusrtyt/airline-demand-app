# ✈️ Airline Booking Market Demand Dashboard

A web-based dashboard that fetches, processes, and visualizes real-time airline booking demand data. Built to help hostel chains in Australia track flight route trends, price variations, and peak travel periods.

## 📌 Features

- ✅ Scrapes or pulls flight data via open travel APIs
- ✅ Visualizes popular routes, pricing trends, and demand peaks
- ✅ Includes filterable UI for cities and time periods
- ✅ Optional integration with OpenAI for summary insights
- ✅ Built with open-source tools and minimal setup

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Abitsfhuusrtyt/air-demand-app.git
cd air-demand-app

### 2.Install the requirements

pip install -r requirements.txt

### 3. run the App

python -m uvicorn app.main:app --reload


### 4. Libraries used

| Library               | Purpose                                    |
| --------------------- | ------------------------------------------ |
| **Streamlit**         | Web UI and dashboard interface             |
| **pandas**            | Data processing                            |
| **plotly**            | Interactive charts and graphs              |
| **requests**          | API calls to external flight data services |
| **OpenAI**            | To generate summary insights               |
| **SQLAlchemy**        | Local data storage (SQLite)                |


### 5. Demo screenshots.
![Alt text]("C:\Users\prasanth-23177\.vscode\airline-demand-app\images\Screenshot 2025-07-07 231525.png")
![Alt text]("C:\Users\prasanth-23177\.vscode\airline-demand-app\images\Screenshot 2025-07-07 231541.png")


### 6.Example API Sources
   Aviationstack

   TravelPayouts API

    OpenSky API

### 7. Author
 Github id - Abitsfhuusrtyt




