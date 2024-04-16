from multi_thread import  process_files_with_threads
from multi_process import process_files_with_multiprocessing

def print_res(res):
    for keyword, paths in res.items():
        print(f"Keyword '{keyword}' found in files:")
        for path in paths:
            print(path)
        print()

if __name__ == "__main__":
    file_paths = ['file1.txt','file2.txt','file3.txt','file4.txt','file5.txt','file6.txt','file7.txt','file8.txt','file9.txt','file10.txt','file11.txt','file12.txt','file13.txt',] 
    keywords = ['Масив','приклад',  'Виведення','Python', 'Семафори',"м'ютекси", 'синхронізації', "пам'ять", 'багатопроцесорному', 'паралельно', 'процесів', 'атрибут', 'рівень', 'потоків', 'Пул',
                'консолі', 'примітиви', 'виконання', 'Контроль', 'Контроль', 'модуля', 'багатоядерних', 'блокування', 'функтор', 'Результат', 'операційна система', 'Конкурентне', 'програмування']    


    res_using_threads = process_files_with_threads(file_paths, keywords, num_threads=4)
    res_using_processes = process_files_with_multiprocessing(file_paths, keywords, num_processes=4)
    
    print_res(res_using_threads)
    print_res(res_using_processes)
    


    