import os
from random import randint
for day in range(1, 365):
    for commits in range(0, randint(1, 20)):
        day = str(day)+' days ago'
        with open('file.txt', 'a')as file:
            file.write(day)
        os.system('git add .')
        os.system('git commit --date="'+day+'" -m "commit"')
os.system('git push -u origin main ')