import operator

#list = {"z","a","c","b"}

#print(sorted(list))

#default olarak '1'i algilar. Harf olarak duzenlemek icin 2 yazmak gerekli.
#names = [("Ali",2),("Bertug",2),("Ferah",2),("Sema",2),("Mete",2)]

#print(names)

#list_of_dicts = [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

#print(sorted(list_of_dicts , key = operator.itemgetter(1)))

#print(sorted(list_of_dicts , key = operator.itemgetter(1),reverse = False))

class Student :
    def __init__(self,name , grade , age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
                return repr((self.name, self.grade, self.age))

student_objects = [Student('Bertug','A',23), Student('Ali','B',52),Student('Ferah','A',46),Student('Sema','B',22)]

sorted_list =  sorted(student_objects , key = lambda student : student.name)

print(sorted_list)
 
#print(sorted(student_objects, key=operator.attrgetter('name', 'age')))