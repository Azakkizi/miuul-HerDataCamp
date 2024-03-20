# divide_students fonksiyonunu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(list):
    new_list = [[], []]
    for index, student in enumerate(list):
        if index % 2 == 0:
            new_list[0].append(student)
        else:
            new_list[1].append(student)
    return new_list


print(list(divide_students(students)))
