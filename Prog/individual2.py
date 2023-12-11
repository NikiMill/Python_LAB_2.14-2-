#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Написать программу, которая будет удалять все комментарии из исходного файла с кодом на языке Python.
#Пройдите по всем строкам в файле на предмет поиска символа #
#Обнаружив его, программа должна удалить все содержимое, начиная с этого символа и до конца строки. 
#Для простоты не будем рассматривать ситуации, когда знак решетки встречается в середине строки.
#Сохраните новое содержимое в созданном файле. 

def delete_comments(source_file, dest_file):
    with open(source_file, 'r') as file:
        lines = file.readlines() 

    modified_lines = []
    for line in lines:
        modified_line = line.split("#")[0]  # Удаляем все, что идет после символа #
        modified_lines.append(modified_line)

    with open(dest_file, 'w') as file:
        file.writelines(modified_lines)

    print("Комментарии удалены. Результат сохранен в файле", dest_file)

if __name__ == '__main__':
    source_file = input("Введите имя исходного файла: ")
    dest_file = input("Введите имя файла назначения: ")

    delete_comments(source_file, dest_file)
