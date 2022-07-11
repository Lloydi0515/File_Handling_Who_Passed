
import pickle as p

def count_rec():
    f = open("students.dat", "rb")
    count = 0
    while True:
        try:
            t = p.load(f)
            if t[2] > 75:
                count = count + 1
                print(t)
        except EOFError:
            break
    print(f"Number of student with per greater 75%", count)
count_rec()


# import pickle as p
# def count_rec():
#     count = 0
#     f = open("students.dat", "rb")
#     while True:
#      try:
#         t = p.load(f)
#         if t[2] > 75:
#          count = count + 1

#      except EOFError:
#       break

#     f.close()
#     print(f"Number of student with per greater 75%:", count)
# count_rec()
