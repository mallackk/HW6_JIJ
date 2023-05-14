import random as rand
import csv
import matplotlib.pyplot as plt

trial = [100, 1000, 10000, 100000]


def main():
    i = 0
    result = [[0 for j in range(6)] for i in range(len(trial))]
    for trynum in trial:
        for j in range(trynum):
            idx = rand.randint(1, 6)
            result[i][idx - 1] += 1
        i += 1
    file_name = f"./sample{trynum}.csv"
    f = open(file_name, "w", encoding="cp949")
    writer = csv.writer(f)
    writer.writerows(result)

    f.close()

    f = open(file_name)
    data = csv.reader(f)

    for line in data:
        num = 1
        if line:
            lst = []
            for i in line:
                for j in range(int(i)):
                    lst.append(num)
                num += 1
            plt.hist(lst)
            plt.xlabel("dice number")
            plt.ylabel("count")
            plt.xlim(1, 6)
            plt.show()

    f.close()


if __name__ == "__main__":
    main()
