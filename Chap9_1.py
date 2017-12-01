#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open("mbox-short.txt")
count = 0
lst = list()
dic = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    lst = line.split()
    email = lst[1]
    dic[email] = dic.get(email,0)+1

largest = None
for a in dic:
    if largest is None or dic[a] > largest:
        largest = dic[a]
        address = a

print(address,largest)
