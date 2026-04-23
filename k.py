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
#         for j in range(0, n - i - 1):
#             index_highlight1 = j
#             index_highlight2 = j + 1
#             colors = ["steelblue"] * len(values)
#             colors[index_highlight1] = "tomato"
#             colors[index_highlight2] = "tomato"
#             plt.clf()
#             plt.bar(range(len(values)), values, color=colors)
#             plt.title("Bubble Sort")
#             plt.pause(0.1)
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             plt.ioff()
#             plt.show()
#
#     return nums
# # print(bubble_sort(numbers))
# #
# help(sorted)

import matplotlib.pyplot as plt

plt.ion()

def bubble_sort(numbers):
    nums = numbers.copy()
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1

            colors = ["steelblue"] * len(nums)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(nums)), nums, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

values =[7, 15, 7, 14, 20, 14, 3]
print(bubble_sort(values))

plt.ioff()
plt.show()

