from pprint import pprint

def get_dict_files(file):
    """
    Функция принимает на вход файл и считывает его содержимое.
    """
    with open(file, encoding='utf-8') as f_obj:
        result_dict = {}
        lines = f_obj.readlines()
        counter = len(lines)
        result_dict['name'] = file
        result_dict['count'] = counter
        result_dict['text'] = ''.join(lines).replace('\n', ' ')
    return result_dict

first_file = '1.txt'
second_file = '2.txt'
third_file = '3.txt'

list_files = [first_file, second_file, third_file]
for file in list_files:
    get_dict_files(file)


def create_sorted_file(file_list, output_file):
    """
    Функция создает новый файл txt с отсортированным содержимым исходных файлов.
    """
    result_dict_list = []
    for file in file_list:
        result_dict_list.append(get_dict_files(file))
    
    sorted_result_dict_list = sorted(result_dict_list, key=lambda x: x['count'])
    
    with open(output_file, 'w', encoding='utf-8') as f_obj:
        for result_dict in sorted_result_dict_list:
            f_obj.write(f"Имя файла: {result_dict['name']}\n")
            f_obj.write(f"Количество строк: {result_dict['count']}\n")
            f_obj.write(result_dict['text'] + '\n')
            
    print(f"Создан файл {output_file} с отсортированным содержимым исходных файлов.")

first_file = '1.txt'
second_file = '2.txt'
third_file = '3.txt'
output_file = 'output.txt'

list_files = [first_file, second_file, third_file]
create_sorted_file(list_files, output_file)