from multiprocessing import Queue, Process
from time import time

def search_files_for_keywords(files, keywords, results):

    res = {}

    for path in files:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        if keyword not in res:
                            res[keyword] = []
                        res[keyword].append(path)
        except Exception as e:
            print(f"Error processing file {path}: {e}")

    results.put(res)

def process_files_with_multiprocessing(file_paths, keywords, num_processes=4):
    timer = time()

    res_queue = Queue()
    processes = []

    files_per_process = len(file_paths) // num_processes
    
    for i in range(num_processes):
        start_index = i * files_per_process
        end_index = start_index + files_per_process if i < num_processes - 1 else len(file_paths)
        process_files = file_paths[start_index:end_index]

        process = Process(target=search_files_for_keywords, args=(process_files, keywords, res_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    final_res = {}
    while not res_queue.empty():
        result = res_queue.get()
        for keyword, paths in result.items():
            if keyword not in final_res:
                final_res[keyword] = []
            final_res[keyword].extend(paths)
    
    print(f"Execution time using Multiprocessing: {time() - timer} seconds")
    return final_res

