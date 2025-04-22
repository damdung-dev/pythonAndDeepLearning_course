import random
list_coursename=["java",".net","c/c++"]
for i in range(1,9):
        print(f'''"{list_coursename[random.randint(0,2)]}", ''',end='')
