import time

def mensurador(sort_function, data, limite = None):
    start_time = time.time()
    if limite:
        sort_function(data, limite)
    else:
        sort_function(data)
    end_time = time.time()
    return end_time - start_time