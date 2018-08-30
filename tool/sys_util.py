import psutil


def memory_stat():
    return 'memory:\n\tavailable {} mb\n\tused {} mb\n\tpercentage {}%'.format(
        psutil.virtual_memory().available / 1000000,
        psutil.virtual_memory().used / 1000000,
        psutil.virtual_memory().percent)


def print_memory_stat():
    print(memory_stat())


if __name__ == '__main__':
    print_memory_stat()
