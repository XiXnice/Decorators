from datetime import datetime
import os

def trace_decorator(path, name):
    if path is None:
        place = os.path.join(os.getcwd())
    else:
        place = os.path.join(os.path.abspath(path))

    file_path = os.path.join(place, name)
    def file(some_function):
        def _file(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = some_function.__name__
            input_data = f'вводные данные:{args} и {kwargs}'
            output_data = some_function(*args, **kwargs)
            result_line = f'вызвана функция {func_name} \n' \
                          f'дата и время вызова : {log_date} \n' \
                          f'{input_data} \n' \
                          f'результирующее значение функции {func_name}: {output_data}\n'
            with open(file_path, "w+", encoding='utf-8') as f:
                f.write(result_line)
            return output_data
        return _file
    return file
