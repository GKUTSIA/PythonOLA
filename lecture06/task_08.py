with open('task_08_read.txt', 'r', encoding = 'utf-8') as f1:
    lines = f1.readlines()

result = " ".join(lines).replace("\n", "")

with open('task_08_write.txt', 'w', encoding='utf-8') as f2:
    f2.write(result)

