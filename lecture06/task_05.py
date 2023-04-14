with open('task_05_file01.txt', 'r', encoding = 'utf-8') as f1:
    content1 = f1.read()


with open('task_05_file02.txt', 'r', encoding = 'utf-8') as f2:
    content2 = f2.read()


with open('task_05_file03.txt', 'a', encoding = 'utf-8') as f3:
    f3.write(content1)
    f3.write(content2)