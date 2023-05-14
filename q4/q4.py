import matplotlib.pyplot as plt
import csv


plt.rcParams["font.family"] = "Malgun Gothic"
plt.rc("xtick", labelsize=5)


def main():
    f = open("card03.csv")
    data = csv.reader(f)
    next(data)
    next(data)

    sub_data = [[], [], []]

    for row in data:
        for i in range(3, 7):
            row[i] = int(row[i])

        on = row[3] + row[5]
        off = row[4] + row[6]
        onoff = on + off
        sub_data[0].append([on, row[2]])
        sub_data[1].append([off, row[2]])
        sub_data[2].append([onoff, row[2]])

    for i in range(3):
        sub_data[i].sort(reverse=True)
        sub_data[i] = sub_data[i][:30]

    title = ["get on", "get off", "get on+off"]
    plt.figure(figsize=(100, 10))

    for i in range(3):
        plt.subplot(3, 1, i + 1)
        plt.title(title[i])
        plt.xlabel("역")
        plt.ylabel("인원수")
        plt.xticks()

        pdata = [[], [], []]
        for ii in range(30):
            pdata[0].append(sub_data[i][ii][0])
            pdata[1].append(sub_data[i][ii][1])
        plt.bar(pdata[1], pdata[0], color="pink")

    plt.show()
    f.close()


if __name__ == "__main__":
    main()
