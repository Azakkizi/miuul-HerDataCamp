##################################################################################
### Virtual Environment (Sanal Ortam)  ve (Package Managment) Paket Yönetimi   ###
##################################################################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi:
# conda upgrade –all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

# CONDA Export environment
# conda env export > environment.yaml

# PIP Export environment
# pip ... requirements.txt

# Environment silme
# conda env remove -n myenv

# YAML dosyasından environment oluşturma
# conda env create -f environment.yaml


###############
###   zip   ###
###############

# Ayrı listeleri tuple yaparak tek bir liste içerisine toplar

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

output = [('John', 'mathematics', 23),
          ('Mark', 'statistics', 30),
          ('Venessa', 'physics', 26),
          ('Mariam', 'astronomy', 22)]


##################
###   lambda   ###
##################

# Kullan-at fonksiyon olşturmaya yarar

def summer(a, b):
    return a+b

new_sum = lambda a, b: a + b

new_sum(3, 5)


###############
###   map   ###
###############

# Bir fonksiyonu iteratif bir nesneye döngüsüz uygulamayı sağlar

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

# del new_sum

list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))


##################
###   filter   ###
##################

# İteratif bir nesnede gezerek koşulu sağlayanları filtreler

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, list_store))


##################
###   reduce   ###
##################

# İteratif bir nesnedeki peşpeşe(?) elemanlara bir işlem uygulayarak sonucu kaydedip elemanları atar

from functools import reduce

list_store = [1, 2, 3, 4]

reduce(lambda a, b: a + b, list_store)


########################################################################################################################

### COMPREHENSIONS ###

### List Comprehensions ###

salaries = [1000, 2000, 3000, 4000, 5000]

# def new_salary(x):
#    return x * 20 / 100 + x
#
# for salary in salaries:
#    print(new_salary(salary))
#
# list(map(new_salary, salaries))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

### --- o --- ###

students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

# Amaç: İstenmeyen öğrencilerin isimlerini küçük harfle, istenen öğrencilerin isimlerini büyük harfle yazma

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]


### Dict Comprehensions ###






