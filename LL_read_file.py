from LinkedList.SingleLL import SingleLinkedList
from People.People import *

if __name__ == "__main__":
    ll = SingleLinkedList()
    file = open("test_file.txt", "r")
    for line in file:
        spl = line.split(":")
        if spl[0].lower() == "person":
            ll.add_to_tail(Person(spl[1], spl[2], spl[3].rstrip()))
        if spl[0].lower() == "student":
            ll.add_to_tail(Student(spl[1], spl[2], spl[3], spl[4].rstrip()))
        if spl[0].lower() == "professor":
            ll.add_to_tail(Professor(spl[1], spl[2], spl[3], bool(spl[4].rstrip())))
        if spl[0].lower() == "employee":
            ll.add_to_tail(Employee(spl[1], spl[2], spl[3], spl[4].rstrip()))
        if spl[0] == "endline":
            file.close()
    ll.print_list()
