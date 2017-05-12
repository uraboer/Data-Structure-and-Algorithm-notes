# coding:utf-8
# Part I-Basics
# Basics Data Structure
# String

s1 = str()
s2 = "shaunwei"  # in python '' or "" is the same
s2len = len(s2)

print(s2[-3:])  # wei
print(s2[5:8])  # wei

s3 = s2[:5]
print(s3)  # shaun
s3 += "wei"
print(s3)  # shaunwei

s2list = list(s3)  # ['s', 'h', 'a', 'u', 'n', 'w', 'e', 'i']
print(s2list)

print(s2[4])  # index 4 "n"

print(s2.index("w"))  # find index at first,return 5,if not found, throw ValueError

print(s2.find("w"))  # return 5, if not found ,return -1
