def sum_of_list(numbers):
    return sum(numbers)

def average(sum, n):
        return sum / n


def final_data(data):
    for item in data:
        try:
            print("Average: ",average(sum_of_list(item), len(item)))
        except ZeroDivisionError:
            print("No se imprimieron todos los resultados porque una de las listas está vacía")


list1 = [10, 20, 30, 40, 50]

list2 = [100, 200, 300, 400, 500]

list3 = []

lists = [list1, list2, list3]

final_data(lists)