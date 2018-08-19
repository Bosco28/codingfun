import re


if __name__ == '__main__':
    file = open("sample_log.txt", "r")
    lines = file.readlines()

    average_rates = {}

    for line in lines:
        words = line.split()
        time = words[0]
        # parsing old, new and average rates
        old_rate = re.findall(r'\d+\.\d+', words[len(words)-2])
        new_rate = re.findall(r'\d+\.\d+', words[len(words)-1])
        if len(new_rate) == 0 or len(old_rate) == 0:
            continue
        old_rate = float(old_rate[0])
        new_rate = float(new_rate[0])
        average_rate = round((old_rate + new_rate) / 2, 3)
        # storing the rate and its time
        average_rates[average_rate] = time

    rates = sorted(average_rates.keys())
    max_rate = rates[len(rates)-1]
    min_rate = rates[0]
    mid_rate = rates[len(rates)//2]
    print("Max average rate: " + str(max_rate) + "Mbps at " + average_rates[max_rate])
    print("Mid average rate: " + str(mid_rate) + "Mbps at " + average_rates[min_rate])
    print("Min average rate: " + str(min_rate) + "Mbps at " + average_rates[min_rate])
