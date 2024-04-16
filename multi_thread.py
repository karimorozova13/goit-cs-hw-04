import threading
from time import time

def search_files_for_keywords(files, keywords, results):
    
    thread_id = threading.get_ident()
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

    results[thread_id] = res

def process_files_with_threads(file_paths, keywords, num_threads=4):
    timer = time()

    results = {}
    threads = []

    files_per_thread = len(file_paths) // num_threads
    
    for i in range(num_threads):
        start_i = i * files_per_thread
        end_i = start_i + files_per_thread if i < num_threads - 1 else len(file_paths)
        thread_files = file_paths[start_i:end_i]

        thread = threading.Thread(target=search_files_for_keywords, args=(thread_files, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_res = {}
    
    for _, thread_result in results.items():
        for keyword, paths in thread_result.items():
            if keyword not in final_res:
                final_res[keyword] = []
            final_res[keyword].extend(paths)
    
    print(f"Execution time using Multithreading: {time() - timer} seconds")
    return final_res

