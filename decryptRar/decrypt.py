# coding=utf-8
import rarfile
import zipfile
import itertools as its
import time
import os
import sys


def extract(file_path, pwd):
    if file_path.endswith('rar'):
        file = rarfile.RarFile(file_path)
    else:
        file = zipfile.ZipFile(file_path)
    try:
        file.extractall(pwd=pwd.encode())
        print('find password: ' + pwd)
        return True
    except Exception as e:
        print('password is wrong: ' + pwd + " exception:" +
              str(e))
        return False
    finally:
        file.close()


def get_pwd(min_digits, max_digits, words):
    count = min_digits
    while count <= max_digits:
        pwds = its.product(words, repeat=count)
        for item in pwds:
            pwd = ''.join(item)
            print('try pwd: ' + pwd)
            yield pwd
        count += 1


words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# words = '0123456789'
pwds = get_pwd(4, 6, words)
start = time.time()
rarPath = sys.argv[1]
while True:
    pwd = next(pwds)
    if extract(rarPath, pwd):
        break

end = time.time()
print('耗时：' + str(end - start))
