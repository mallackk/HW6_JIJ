import matplotlib.pyplot as plt
import csv


def main():
    # Read csv files and store data
    data_list = [
        "Total_temp.csv",
        "Seoul_temp.csv",
        "Daejeon_temp.csv",
        "Busan_temp.csv",
        "Jeju_temp.csv",
    ]
    tmp = []
    total_data = []
    for data in data_list:
        f = open(data, "r", encoding="utf-8")
        data = csv.reader(f, delimiter=",")
        for i in range(8):
            i += 1
            header = next(data)
        for row in data:
            if row[2] == "" or row[3] == "" or row[4] == "":
                continue
            else:
                row[2] = float(row[-1])
                tmp.append(row[2])
        total_data.append(tmp)
        tmp = []
        f.close()

    colorlist = ["red", "blue", "green", "black", "orange"]
    xlabel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.xticks(
        range(13),
        [
            "",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    )
    for i in range(5):
        plt.plot(
            xlabel,
            total_data[i],
            color=colorlist[i],
            label=(data_list[i].replace("_temp.csv", "")),
        )

    plt.title("Regional Average Temperature in Korea, 2022")
    plt.xticks(range(1, 13, 1))
    plt.yticks(range(0, 35, 5))
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()

    analize_data = []
    for i in range(1, 5):
        tmp = []
        for j in range(12):
            tmp.append(round(total_data[i][j] - total_data[0][j], 2))
        analize_data.append(tmp)
        tmp = []

    for i in range(4):
        print(
            "Difference from Total Average Temperature - "
            + data_list[i + 1].replace("_temp.csv", "")
        )
        an = 0
        for j in range(12):
            pm = ""
            if analize_data[i][j] > 0:
                pm = "+"
                an += 1
            print(f"{j+1}월: {pm}{analize_data[i][j]}, ", end="")
            j += 1
        print()
        if an > 12 - an:
            print(
                f"Higher than the Total average temperature. *Higher: {an}, Lower: {12-an}\n"
            )
        else:
            print(
                f"Lower than the Total average temperature. *Higher: {an}, Lower: {12-an}\n"
            )
        i += 1


if __name__ == "__main__":
    main()
