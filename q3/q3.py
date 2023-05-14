import matplotlib.pyplot as plt
import numpy as np
import csv


def main():
    f = open("q3.csv")
    data = csv.reader(f)
    header = next(data)

    year = []
    male = []
    female = []

    for row in data:
        year.append(row[0])
        male.append(int(row[1]))
        female.append(int(row[2]))

    plt.title("Gender of Jeju in 2000-2022")
    plt.xlabel("year")
    plt.ylabel("population")
    x = np.arange(len(year))
    plt.xticks(x, year)
    plt.plot(x, male, label="male")
    plt.plot(x, female, label="female")
    plt.legend()
    plt.show()

    f.close()


if __name__ == "__main__":
    main()
