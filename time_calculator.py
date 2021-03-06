def add_time(start, duration, day=False):

    days = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]
    # convert duration to minutes
    durationInMinutes = int(duration.split(
        ":")[0]) * 60 + int(duration.split(":")[1])

    # extract the important data from the start string
    sHour = int(start.split(":")[0])
    sMinute = int((start.split(":")[1]).split(" ")[0])
    sDayIndex = days.index(day.lower()) if day else False
    sFormate = (start.split(":")[1]).split(" ")[1]
    dayCount = 0

    # convert the start hour to 24h format
    sHour = sHour + 12 if sFormate == "PM" else sHour

    # Running a loop to add minute by minute
    for _ in range(durationInMinutes):
        if sMinute < 59:
            sMinute += 1
        else:
            sMinute = 0
            if sHour < 23:
                sHour += 1
            else:
                sHour = 0  # Midnight 12
                dayCount += 1
                if sDayIndex < 6:
                    sDayIndex += 1
                else:
                    sDayIndex = 0  # Monday

    # Formatting the output
    sFormate = "AM" if sHour < 12 else "PM"
    sHour = sHour - 12 if sHour > 12 else sHour
    sHour = str(sHour+12) if sHour == 0 else str(sHour)
    sMinute = str(sMinute) if sMinute > 9 else "0" + str(sMinute)
    dayName = ", " + days[sDayIndex].capitalize() if day else ""
    dayCount = " (next day)" if dayCount == 1 else (
        " (" + str(dayCount) + " days later)" if dayCount > 1 else "")

    return sHour + ":" + sMinute + " " + sFormate + dayName + dayCount
