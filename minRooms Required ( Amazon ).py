
# Hotel XYZ wants to conduct N meetings on particular day. You are given start time and end time for each meetings. You have to return minimum numbers of rooms required in XYZ hotel.
#
# Example:
#
# input – N : 6,   meetings timing – [9:00, 9:45], [9:30, 10:30], [10:40, 12:00], [11:00, 13:00], [11:45, 14:00], [16:00, 17:00]
#
# output – 3 rooms required.

def minRoomsRequired(arr):

#     if the array is not already sorted
#     arr.sort(key=lambda x:x[0])

    minRooms = 0

    for i in range(1 ,len(arr)):

        meetTimings = arr[i]
        prevMeetTimings = arr[ i -1]

        if meetTimings[0] < prevMeetTimings[1]:
            minRooms + =1

    return minRooms


N = [[900, 945], [930, 1030], [1040, 1200], [1100, 1300], [1145, 1400], [1600, 1700]]
print(minRoomsRequired(N))


