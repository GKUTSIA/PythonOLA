with open('task_04_read.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()


with open('task_04_write.txt', 'w', encoding = 'utf-8') as f2:
    f2.write(content)