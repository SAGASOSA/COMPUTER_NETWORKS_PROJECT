# PROJECT_25 Documentation Files

Below are the generated files as requested. You can copy each section into its respective file inside your project directory.

---

## 📄 **README.md (Main Project Root)**

```md
# PROJECT_25 – Network Utilities Toolkit

This project is a Streamlit-based toolkit containing multiple network-related utilities such as:

- Subnet Calculator
- Address Class Analyzer
- Subnetting Visualizer
- Port Scanner

The application is built using Python and Streamlit and provides an interactive GUI for all tools.

## 📁 Project Structure

```

PROJECT_25/ │ ├── README.md ├── requirements.txt │ ├── 1_Home.py │ ├── videos/ │   └── (Add your tutorial/demo videos here) │ └── pages/ ├── 1_Subnet_Calculator.py ├── 2_Address_Class_Analyzer.py ├── 3_Subnetting_Visualizer.py └── 4_Port_Scanner.py

```

## 📦 Install Dependencies

Create a **requirements.txt** file with the following content:
```

streamlit
pandas

````

Then install the dependencies:
```bash
pip install -r requirements.txt
````

*(Note: pandas is used for `st.dataframe` in the Subnetting Visualizer.)*

---

## 🚀 Run the Project

1. Install dependencies:

```

pip install -r requirements.txt

```

2. Run Streamlit:

```

streamlit run 1_Home.py

```

3. Navigate between tools using the sidebar.

---

## 🛠 Features

### 1. Subnet Calculator

* Calculate network address, broadcast address, number of hosts, wildcard mask, etc.

### 2. Address Class Analyzer

* Determines IP class (A/B/C/D/E), default mask, valid ranges.

### 3. Subnetting Visualizer

* Explains subnetting steps with diagrams.

### 4. Port Scanner

* Scans specified ports on a target host.

---

## 📁 videos/

Use this folder to store:

* Demo videos
* Tutorials
* Explanatory animations

---

## 👍 Author

Created by **Samyak Kamble** for CN Lab Project (2025–26).

````

---

## 📄 **requirements.txt**

```txt
streamlit
pandas
numpy
python-dotenv
requests
python-nmap
ipaddress
````

---

## 📄 **pages/README.md (Optional – Inside pages folder)**

```md
# Pages Module – Overview

This folder contains individual Streamlit pages used in the PROJECT_25 application.

## Files

### 1️⃣ 1_Subnet_Calculator.py
Provides IP subnet calculations.

### 2️⃣ 2_Address_Class_Analyzer.py
Analyzes IP class and properties.

### 3️⃣ 3_Subnetting_Visualizer.py
Explains subnetting with visuals.

### 4️⃣ 4_Port_Scanner.py
Scans ports on a given IP.

Each page is automatically loaded by Streamlit when placed in the **pages/** directory.
```


PROJECT_25/ │ ├── 1_Home.py ├── README.md <-- Your overall project README ├── requirements.txt <-- Your project dependencies │ ├── pages/ │ ├── 1_Subnet_Calculator.py │ ├── 2_Address_Class_Analyzer.py │ ├── 3_Subnetting_Visualizer.py │ └── 4_Port_Scanner.py <-- (Added .py extension) │ └── videos/ <-- Your new videos folder └── (Your video files will go here)
