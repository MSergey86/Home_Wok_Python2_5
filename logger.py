
import datetime
import os

def logger(catalog_name):
    base_path = os.getcwd()
    file_name = "logger.txt"
    full_path = os.path.join(base_path, catalog_name, file_name)
    def logger_(some_function):
        def new_function(*args, **kwargs):
            date_time = datetime.datetime.now()
            function_name = some_function.__name__
            arguments = args, kwargs
            result = some_function(*args, **kwargs)

            data = f'{date_time}\n{function_name}\n{arguments}\nРезультат: {result}'
            print(data)

            with open(full_path, 'w') as f:
                f.write(data)

            print(f'Файл {file_name} создан, путь к файлу: {catalog_name}')
            return result
        return new_function
    return logger_
