# 🚀 Network Addressing & Subnet Calculator

A multi-page web application built with Streamlit designed as a practical utility for network engineering students and professionals. This tool performs essential IPv4 calculations, including subnetting, address analysis, and subnet visualization.

This project directly aligns with core Computer Networks syllabus topics, such as IPv4 addressing, classful addressing, subnetting, and CIDR.

---

## 🔧 Features

This application is structured as a multi-page app with the following tools:

### 1. Subnet Calculator (Main Page)
The primary tool for analyzing a network. The user provides an IP address in CIDR notation (e.g., `192.168.1.10/24`), and the app instantly calculates:

* **Network Address:** The first address in the network.
* **Broadcast Address:** The last address in the network.
* **Subnet Mask:** The dotted-decimal notation of the mask.
* **Host Range:** The first and last usable IP addresses for hosts.
* **Total Number of Hosts:** The count of usable IP addresses.
* **Address Type:** Identifies if the IP is Private, Public, Loopback, etc.

### 2. Address Class Analyzer
A simple utility to demonstrate the concept of "Classful" addressing. The user enters a single IP, and the app identifies:

* Its traditional class (e.g., Class A, B, or C).
* Its default (classful) subnet mask.

### 3. Subnetting Visualizer
An interactive tool to plan and visualize subnetting. The user:
1.  Enters a large parent network (e.g., `10.0.0.0/8`).
2.  Uses a slider to select a new, smaller subnet prefix (e.g., `/16`).
3.  The app generates and displays a table of all the resulting subnets, showing the network address, host range, and broadcast address for each.

---

## 💻 Tech Stack

* **Framework:** [Streamlit](https://streamlit.io/)
* **Language:** [Python 3](https://www.python.org/)
* **Core Network Library:** Python's built-in `ipaddress` module.

---

## 🚀 How to Run Locally

### Prerequisites
* Python 3.7 or newer
* `pip` (Python package installer)

### 1. Clone the Repository (or Create Files)
If this is a git repository, clone it:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

install the dependencies:

Bash

pip install -r requirements.txt
(Note: pandas is used for st.dataframe in the Subnetting Visualizer).

4. Run the App
Assuming your main script is named 1_Subnet_Calculator.py:

Bash

streamlit run 1_Subnet_Calculator.py


PROJECT_25/
│
├── 1_Subnet_Calculator.py
│
└── pages/
    │
    ├── 2_Address_Class_Analyzer.py
    │
    └── 3_Subnetting_Visualizer.py   <-- (This is the new file)
