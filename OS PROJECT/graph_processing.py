import networkx as nx

def detect_deadlock(graph):
    try:
        cycle = nx.find_cycle(graph, orientation="original")  # Detect cycle
        deadlocked_processes = {node for edge in cycle for node in edge if node.startswith("P")}
        print(f"Deadlock Detected! Processes involved: {list(deadlocked_processes)}")
        return list(deadlocked_processes)
    except nx.NetworkXNoCycle:
        print("No deadlock detected. System is in a safe state.")
        return []


def recover_from_deadlock(graph):
    deadlocked_processes = detect_deadlock(graph)
    if not deadlocked_processes:
        return "No deadlock detected."

    # Choose the first process to terminate
    process_to_terminate = deadlocked_processes[0]
    
    # Remove all edges connected to this process
    graph.remove_node(process_to_terminate)

    print(f"Process {process_to_terminate} terminated. Deadlock resolved.")
    return f"Process {process_to_terminate} terminated to resolve deadlock."
