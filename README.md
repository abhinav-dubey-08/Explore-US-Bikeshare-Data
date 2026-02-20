# 🚲 Explore US Bikeshare Data

An interactive Python program that analyzes bikeshare data from three major US cities using **Pandas** and **NumPy**.  
This project allows users to filter data by city, month, and/or day and generates useful travel statistics.

---

## 📌 Project Overview

This program explores bikeshare data for the following cities:

- Chicago  
- New York City  
- Washington  

Users can:

- Filter data by **month**, **day**, **both**, or **not at all**
- View statistics about:
  - Most frequent travel times
  - Most popular stations and trips
  - Trip duration
  - User demographics
- Display raw trip data (5 rows at a time)

---

## 📂 Datasets

The project uses the following CSV files:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

Each dataset includes:

- Start Time
- End Time
- Start Station
- End Station
- Trip Duration
- User Type
- Gender (not available for Washington)
- Birth Year (not available for Washington)

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Time module

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/explore-us-bikeshare-data.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd explore-us-bikeshare-data
```

### 3️⃣ Install Dependencies

```bash
pip install pandas numpy
```

### 4️⃣ Run the Program

```bash
python bikeshare.py
```

---

## 📊 Features

### 🔹 Time Statistics
- Most common month
- Most common day of week
- Most common start hour

### 🔹 Station Statistics
- Most common start station
- Most common end station
- Most frequent trip combination

### 🔹 Trip Duration Statistics
- Total travel time
- Average travel time

### 🔹 User Statistics
- Counts of user types
- Gender distribution (if available)
- Earliest, most recent, and most common birth year (if available)

### 🔹 Raw Data Viewer
- Displays 5 rows at a time
- User can choose to view more rows interactively

---

## 📁 Project Structure

```
Explore-US-Bikeshare-Data/
│
├── chicago.csv
├── new_york_city.csv
├── washington.csv
├── bikeshare.py
└── README.md
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Data analysis using Pandas
- Working with datetime data
- Filtering datasets dynamically
- Building interactive CLI applications
- Writing modular Python functions

---

## 👤 Author

**Abhinav Dubey**
