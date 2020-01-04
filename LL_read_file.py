from LinkedList.SingleLL import SingleLinkedList
from People.People import *

if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.add_to_tail(Employee("test", 1, "test", "test"))
    file = open("test_file.txt", "r")
    for line in file:
        spl = line.split(":")
        if spl[0].lower() == "person":
            name = spl[1]
            age = spl[2]
            addr = spl[3]
            ll.add_to_tail(Person(name, age, addr))
        if spl[0].lower() == "student":
            ll.add_to_tail(Student(spl[1], spl[2], spl[3], spl[4]))
        if spl[0].lower == "professor":
            name = spl[1]
            age = spl[2]
            addr = spl[3]
            tenure = bool(spl[4])
            ll.add_to_tail(Professor(name, age, addr, tenure))
        if spl[0].lower == "employee":
            name = spl[1]
            age = spl[2]
            addr = spl[3]
            employer = spl[4]
            ll.add_to_tail(Employee(name, age, addr, employer))
        if spl[0] == "endline":
            file.close()
    ll.print_list()
