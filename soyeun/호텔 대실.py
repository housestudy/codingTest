def solution(book_time):
    answer = 0
    book_times = [[int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:]) + 10] for start, end in
                  book_time]
    book_times.sort()

    rooms = []
    for book_time in book_times:

        if not rooms:
            rooms.append(book_time)
            continue
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[index] = room + book_time
                break
        else:
            rooms.append(book_time)

    return len(rooms)
