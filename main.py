from task_processor import TaskProcessor

def main():
    file_path = '/Users/rdaniels/Projects/PyCmpPert/PyCmpPert/test_data_one.txt'
    tp = TaskProcessor(file_path)
    tp.process_tasks()

if __name__ == '__main__':
    main()