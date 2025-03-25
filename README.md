# Graphical Simulator for Resource Allocation Graphs

## 📌 Project Overview
The **Graphical Simulator for Resource Allocation Graphs** is a tool designed to visualize and analyze resource allocation in an operating system. It allows users to add processes and resources, allocate resources to processes, detect potential deadlocks, and resolve them through deadlock recovery. The primary goal is to help students and professionals understand **deadlock detection and prevention mechanisms** in an interactive manner.

## 🎯 Features
### 🔹 **Process and Resource Management**
- Add and remove **processes** (P1, P2, ...)
- Add and remove **resources** (R1, R2, ...)
- Allocate and release resources dynamically

### 🔹 **Graph Visualization**
- Displays the **Resource Allocation Graph (RAG)**
- Uses **NetworkX** for graph representation
- Uses **Matplotlib** for graphical visualization

### 🔹 **Deadlock Detection and Recovery**
- Detects **cycles** in the graph to identify deadlocks
- Provides recovery strategies (e.g., **terminating** a process to resolve deadlock)

---

## 🏗️ Project Modules
### 1️⃣ **Graphical User Interface (GUI)**
- Uses **Tkinter** for an interactive interface
- Buttons for adding processes, adding resources, allocating resources, releasing resources, and detecting deadlock

### 2️⃣ **Graph Processing (Backend Logic)**
- **NetworkX** to construct and manipulate the **Resource Allocation Graph (RAG)**
- Implements deadlock detection using **cycle detection** algorithms
- Implements deadlock recovery by terminating a process

### 3️⃣ **Data Visualization**
- Uses **Matplotlib** to render the graph with nodes and directed edges
- Visualizes the allocation of resources and potential deadlocks

---

## 🚀 Installation & Setup
### 🔧 Prerequisites
Make sure you have **Python 3.10+** installed.

### 📦 Install Dependencies
Run the following command in your terminal:
```sh
pip install networkx matplotlib tkinter pandas
```

### 🏃‍♂️ Running the Project
After installing the dependencies, execute:
```sh
python main.py
```
This will launch the graphical simulator.

---

## 📌 How to Use
1. **Add Processes and Resources**  
   - Click "Add Process" → Enter process name (e.g., `P1`, `P2`).
   - Click "Add Resource" → Enter resource name (e.g., `R1`, `R2`).

2. **Allocate Resources**  
   - Click "Allocate Resource" → Enter process and resource names (e.g., `P1 -> R1`).

3. **Release Resources**  
   - Click "Release Resource" → Enter process and resource to remove allocation.

4. **Detect Deadlock**  
   - Click "Detect Deadlock" → Checks for **cycles** and alerts if deadlock exists.

5. **Visualize Graph**  
   - Click "Show Graph" to see the **Resource Allocation Graph (RAG)**.

---

## 🖼️ Example Scenario
### Given the following allocations:
1. **P1 requests R1** → `P1 → R1`
2. **R1 allocated to P2** → `R1 → P2`
3. **P2 requests R2** → `P2 → R2`
4. **R2 allocated to P1** → `R2 → P1`

**🔴 Deadlock Detected!** (Cycle exists: `P1 → R1 → P2 → R2 → P1`)

---

## 🛠️ Technologies Used
- **Python** (Primary language)
- **Tkinter** (Graphical User Interface)
- **NetworkX** (Graph representation and cycle detection)
- **Matplotlib** (Graph visualization)
- **Pandas** (Handling resource data if needed)

---

## 📌 Future Enhancements
✅ Implement **Banker’s Algorithm** for deadlock avoidance  
✅ Support **multiple deadlock recovery strategies**  
✅ Add **log files** to track changes in the RAG  

---

## 👨‍💻 Contributing
Feel free to contribute! Open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

