import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
# print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
numbers = random_numbers(50, low=0, high=20)  # 5 čísel v rozsahu 0–20
# print((numbers))
# min=small[0]
# for i in range(len(small)):
#     print(small)
#     if small[i]<min:
#         min=small[i]
#         small.remove(min)
#         small.insert(0,min)
# print(small)
# print(small[0])

# n=len(values)
# for idx_ukladany in range(n):
#     idx_min=idx_ukladany
#     for idx_prohledavany in range(idx_ukladany+1,n):
#         if values[idx_min]>values


# # buble
# plt.ion()
# plt.show()
# def bubble_sort(numbers):
#     nums = numbers.copy()
#     n = len(nums)
#     for i in range(n):
# #         for j in range(0, n - i - 1):
# #             index_highlight1 = j
# #             index_highlight2 = j + 1
# #             colors = ["steelblue"] * len(values)
# #             colors[index_highlight1] = "tomato"
# #             colors[index_highlight2] = "tomato"
# #             plt.clf()
# #             plt.bar(range(len(values)), values, color=colors)
# #             plt.title("Bubble Sort")
# #             plt.pause(0.1)
# #             if nums[j] > nums[j + 1]:
# #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
# #             plt.ioff()
# #             plt.show()
# #
# #     return nums
# # # print(bubble_sort(numbers))
# # #
# # help(sorted)
#
# import matplotlib.pyplot as plt
#
# plt.ion()
#
# def bubble_sort(numbers):
#     nums = numbers.copy()
#     n = len(nums)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             index_highlight1 = j
#             index_highlight2 = j + 1
#
#             colors = ["steelblue"] * len(nums)
#             colors[index_highlight1] = "tomato"
#             colors[index_highlight2] = "tomato"
#
#             plt.clf()
#             plt.bar(range(len(nums)), nums, color=colors)
#             plt.title("Bubble Sort")
#             plt.pause(0.1)
#
#             if nums[j] > nums[j + 1]:
#
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#
#     return nums
#
# values =[7, 15, 7, 14, 20, 14, 3]
# print(bubble_sort(values))
#
# plt.ioff()
# plt.show()
#
# p

from sorting import random_numbers


import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        result = []

        for i in range(len(self.scores)):
            if self.scores[i] == value:
                result.append(i)

        return result

    def get_sorted(self):
        nums = self.scores.copy()
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


def main():

    # kolik studentů
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Pocet studentu:", results.count())

    # vypis studentu
    for i in range(len(results.scores)):
        score = results.scores[i]
        grade = results.get_grade(i)
        print("Student", i, ":", score, "points -", grade)

    # kdo měl 100
    print("Studenti s 100 body:")
    print(results.find(100))

    # seřazení
    print("Serazene vysledky:", results.get_sorted())

    # random data
    random_scores = random_numbers(50, 0, 100)
    random_results = StudentsGrades(random_scores)

    print("\nRandom data")

    # kolik studentů
    print("Pocet studentu:", random_results.count())

    # vypis studentu
    for i in range(len(random_results.scores)):
        score = random_results.scores[i]
        grade = random_results.get_grade(i)
        print("Student", i, ":", score, "points -", grade)

    # seřazení
    print("Serazene:", random_results.get_sorted())

    # graf
    plt.hist(random_scores, bins=10, edgecolor="black")
    plt.title("Rozdělení bodů")
    plt.xlabel("Body")
    plt.ylabel("Počet studentů")
    plt.show()


if __name__ == "__main__":
    main()