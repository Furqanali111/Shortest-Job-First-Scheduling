# 200901073
# Furqan Ali
def bubbleSort(burst_arr, arrival_arr, process_id_arr):
    n = len(arrival_arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arrival_arr[j] > arrival_arr[j + 1]:
                swapped = True
                burst_arr[j], burst_arr[j + 1] = burst_arr[j + 1], burst_arr[j]
                arrival_arr[j], arrival_arr[j + 1] = arrival_arr[j + 1], arrival_arr[j]
                process_id_arr[j], process_id_arr[j + 1] = process_id_arr[j + 1], process_id_arr[j]

            if arrival_arr[j] == arrival_arr[j + 1]:
                swapped = True
                if burst_arr[j] > burst_arr[j + 1]:
                    burst_arr[j], burst_arr[j + 1] = burst_arr[j + 1], burst_arr[j]
                    arrival_arr[j], arrival_arr[j + 1] = arrival_arr[j + 1], arrival_arr[j]
                    process_id_arr[j], process_id_arr[j + 1] = process_id_arr[j + 1], process_id_arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


if __name__ == '__main__':
    total_processes = int(input("Enter no of processes: "))
    process_id = []
    Arrival_time = []
    burst_time = []
    completion_time = []
    turn_around_time = []
    waiting_time = []
    # taking input
    for i in range(0, total_processes):
        x = int(input("Enter process id:"))
        process_id.append(x)
        y = int(input("Enter Arrival time:"))
        Arrival_time.append(y)
        z = int(input("Enter Burst time:"))
        burst_time.append(z)
        print()
    # Sorting on the basses of Arrival time
    bubbleSort(burst_time, Arrival_time, process_id)

    # Calculating completion time
    x = burst_time[0] + Arrival_time[0]
    completion_time.append(x)
    for i in range(1, total_processes):

        if Arrival_time[i] >= completion_time[i - 1]:
            y = Arrival_time[i] - completion_time[i - 1]
            z = burst_time[i] + completion_time[i - 1] + y
            completion_time.append(z)
        else:
            y = burst_time[i] + completion_time[i - 1]
            completion_time.append(y)

    #  Calculating Turn around time
    for i in range(0, total_processes):
        x = completion_time[i] - Arrival_time[i]
        turn_around_time.append(x)

    # Calculating Waiting time
    for i in range(0, total_processes):
        x = turn_around_time[i] - burst_time[i]
        waiting_time.append(x)

    # Printing sorted array
    print("Process Id\tArrival Time\tBurst Time\tCompletion Time\tTurn Around time\tWaiting time")
    for i in range(0, total_processes):
        print("%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d" % (
        process_id[i], Arrival_time[i], burst_time[i], completion_time[i], turn_around_time[i], waiting_time[i]))
        print()

    x=0
    y=0
    # Calculating average TAT and Waiting time
    for i in range(0, total_processes):
        x=x+turn_around_time[i]
        y=y+waiting_time[i]

    avgTAT=x/total_processes
    avgWT=y/total_processes

    print("\nAverage Turn around time: ",avgTAT)
    print("Waiting time: ",avgWT)
