# 雙向鏈結串列的加入、刪除、修改及輸出
# File Name: DoubleList.py
# Version

import sys

# 定義一個Node的資料結構(Class)，其資料包含左、右子鏈結，姓名及分數
class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.llink = None
        self.rlink = None

# 初始化串列，建立一空節點為head，將左右鏈結皆指向本身
prev = None
current = None
ptr = None

head = Student()
head.name = ''
head.llink = head
head.rlink = head

# 新增函數，依分數的高低排序
def insert_f():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.name = input('\n  Please enter student name : ')
    ptr.score = eval(input('  Please enter student score : '))
    print()

    prev = head
    current = head.rlink
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.rlink
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink = ptr
    
# 刪除函數
def delete_f():
    global head
    global current
    global prev

    del_name = ''

    if head.rlink == head: # 無資料顯示錯誤
        print('\n     No student record !!\n')
    else:
        del_name = input('   Delete student name : ')

        prev = head
        current = head.rlink
        while current != head and del_name != current.name:
            prev = current
            current = current.rlink

        if head != current:
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            print('     Student %s record deleted!!\n' % del_name)
        else:
            print('     Student %s not found!!\n' % del_name)

# 修改函數
def modify_f():
    global head
    global current
    global prev

    if head.rlink == head:
        print('\n     No student record !!\n')
    else:
        modify_name = input('   Modify student name: ')

        prev = head
        current = head.rlink
        while current != head and modify_name != current.name:
            prev = current
            current = current.rlink
        
        if current != head: # 找到要修改的資料，顯示該筆資料的原始資料
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.rlink = current.rlink # 刪除舊的資料
            current.rlink.llink = prev
            current = None
            # 重新加入新的資料
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.rlink
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.rlink
            ptr.rlink = current
            ptr.llink = prev
            prev.rlink = ptr
        else:
            print('\n Student %s not found!\n' % modify_name) # 找不到資料

    
# 輸出函數
def display_f():
    global head
    global current

    count = 0

    if head.rlink == head: # 無資料顯示錯誤
        print('\n     No student record !!\n')
    else:
        print('\n%-15s %-10s' % ('NAME', 'SCORE'))
        print('----------------------------------')
        current = head.rlink
        while current != head:
            print('%-15s %-3d' % (current.name, current.score))
            count += 1
            current = current.rlink
        print('----------------------------------')
        print('There is(are) %d record(s) found !!\n' % count)

# 主函數
def main():
    option = 0
    
    while True:
        print('***** Doubly linked list *****')
        print('          <1> Insert          ')
        print('          <2> Delete          ')
        print('          <3> Modify          ')
        print('          <4> List            ')
        print('          <5> Exit            ')
        print('******************************')
        
        try:
            option = int(input('     Choice : '))
        except ValueError:
            print()
            print('Not a correct number.')
            print('Try again\n')
            
        if option == 1:
            insert_f() # 新增函數
        elif option == 2:
            delete_f() # 刪除函數
        elif option == 3:
            modify_f() # 修改函數
        elif option == 4:
            display_f() # 輸出函數
        elif option == 5:
            sys.exit(0)

main()
