import time

print("Enter to begin, enter to lap, q to quit")
input()
print("Started")
start = time.time()
lastlap = start
lap = 1
total = 0

while True:
    run = input()
    newlap = time.time()
    laptime = newlap - lastlap
    lastlap = newlap
    total += laptime
    print("Lap {}: {}".format(lap, laptime))
    print("Total: {}".format(total))
    lap += 1

    if run == 'q':
        finaltime = time.time()
        break

runtime = finaltime - start
print("Total time = {}".format(runtime))
