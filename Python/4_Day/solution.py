import sys
import time
import re
import numpy as np


def solve(lines):
    guardsToSleepTime = groupSleepTimesByGuard(naturalSortInput(lines))
    laziestGuard = findLaziestGuard(guardsToSleepTime)
    sleepiestMinute, _ = findSleepiestMinute(guardsToSleepTime[laziestGuard])

    return laziestGuard, sleepiestMinute


def solve2(lines):
    guardsToSleepTime = groupSleepTimesByGuard(naturalSortInput(lines))

    laziestGuard, sleepiestMinute, smFrequency = 0, 0, 0
    for guard in guardsToSleepTime:
        minute, freq = findSleepiestMinute(guardsToSleepTime[guard])
        if freq > smFrequency:
            laziestGuard = guard
            sleepiestMinute = minute
            smFrequency = freq

    return laziestGuard, sleepiestMinute


def findSleepiestMinute(sleepTimes):
    minutes = np.zeros(60, np.int8)
    for time in sleepTimes:
        timeSlept = minutes[time[0]: time[1]]
        timeSlept[:] = timeSlept + 1
    return np.where(minutes == minutes.max())[0][0], minutes.max()


def findLaziestGuard(guardsToSleepTime):
    sleepiestGuard = 0
    sleepiestTime = 0
    for guard in guardsToSleepTime:
        sleepTime = 0
        for sleep in guardsToSleepTime[guard]:
            sleepTime += sleep[1] - sleep[0]
        if sleepTime > sleepiestTime:
            sleepiestGuard = guard
            sleepiestTime = sleepTime
    return sleepiestGuard


def groupSleepTimesByGuard(lines):
    guardsToSleepTime = {}
    currentGuard = None
    i = 0
    while i < len(lines):
        guardNo = re.findall(r"#([0-9]+)", lines[i])
        if len(guardNo) == 1:
            if not guardNo[0] in guardsToSleepTime:
                guardsToSleepTime[guardNo[0]] = []
            currentGuard = guardNo[0]
            i += 1
        timeIn = int(re.findall(r":([0-9]+)", lines[i])[0])
        timeOut = int(re.findall(r":([0-9]+)", lines[i+1])[0])
        guardsToSleepTime[currentGuard].append([timeIn, timeOut])
        i += 2
    return guardsToSleepTime


def naturalSortInput(lines):
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(lines, key=alphanum_key)


def main():
    runMain = True
    if runMain:
        with open('input.sdx') as file_object:
            contents = file_object.read().splitlines()
            start = time.time()
            guard, minute = solve(contents)
            print("Part 1 solution (strategy 1): " + str(guard) + "*" + str(minute)
                  + "=" + str(int(guard)*minute) + " found in " + str(time.time() - start))
            start = time.time()
            guard, minute = solve2(contents)
            print("Part 2 solution (strategy 2): " + str(guard) + "*" + str(minute)
                  + "=" + str(int(guard)*minute) + " found in " + str(time.time() - start))


if __name__ == '__main__':
    main()
