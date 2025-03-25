import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

class RAG_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resource Allocation Graph Simulator")
        self.graph = nx.DiGraph()  # Directed graph

        # Buttons
        tk.Button(master, text="Add Process", command=self.add_process).pack()
        tk.Button(master, text="Add Resource", command=self.add_resource).pack()
        tk.Button(master, text="Allocate Resource", command=self.allocate_resource).pack()
        tk.Button(master, text="Release Resource", command=self.release_resource).pack()
        tk.Button(master, text="Detect Deadlock", command=self.detect_deadlock).pack()
        tk.Button(master, text="Show Graph", command=self.show_graph).pack()

    def add_process(self):
        process = simpledialog.askstring("Input", "Enter Process Name (P1, P2...):")
        if process and process not in self.graph:
            self.graph.add_node(process, type="process")
            messagebox.showinfo("Success", f"Process {process} added!")

    def add_resource(self):
        resource = simpledialog.askstring("Input", "Enter Resource Name (R1, R2...):")
        if resource and resource not in self.graph:
            self.graph.add_node(resource, type="resource")
            messagebox.showinfo("Success", f"Resource {resource} added!")

    def allocate_resource(self):
        process = simpledialog.askstring("Input", "Enter Process Name:")
        resource = simpledialog.askstring("Input", "Enter Resource Name:")
        if process in self.graph and resource in self.graph:
            self.graph.add_edge(process, resource)
            messagebox.showinfo("Success", f"{process} → {resource} allocated.")

    def release_resource(self):
        process = simpledialog.askstring("Input", "Enter Process Name:")
        resource = simpledialog.askstring("Input", "Enter Resource Name:")
        if self.graph.has_edge(process, resource):
            self.graph.remove_edge(process, resource)
            messagebox.showinfo("Success", f"{process} released {resource}.")

    def detect_deadlock(self):
        from graph_processing import detect_deadlock
        deadlocked_processes = detect_deadlock(self.graph)
        if deadlocked_processes:
            messagebox.showwarning("Deadlock Detected", f"Deadlocked Processes: {deadlocked_processes}")
        else:
            messagebox.showinfo("No Deadlock", "System is in a safe state.")

    def show_graph(self):
        plt.figure(figsize=(6, 4))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=2000, font_size=10)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    gui = RAG_GUI(root)
    root.mainloop()
