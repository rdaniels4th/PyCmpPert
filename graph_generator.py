import networkx as nx
import matplotlib.pyplot as plt
from task_processor import TaskProcessor

class GraphGenerator:
    def __init__(self, task_processor):
        self.task_processor = task_processor
        self.graph = nx.DiGraph()

    def create_graph(self):
        for task in self.task_processor.tasks.values():
            self.graph.add_node(task['name'], duration=task['duration'])
            for dependency in task['dependencies']:
                if dependency != -1:
                    self.graph.add_edge(dependency, task['name'])

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'duration')
        nx.draw(self.graph, pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.graph, pos)
        plt.savefig('graph.png')

if __name__ == '__main__':
    file_path = 'data/test_data1.txt'
    tp = TaskProcessor(file_path)
    tp.process_tasks()
    gg = GraphGenerator(tp)
    gg.create_graph()
    gg.draw_graph()
