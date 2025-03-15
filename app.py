# Application
from datetime import datetime
import calendar

class MeetingScheduler:
    def __init__(self):
        self.working_hours = (9, 17)
        self.holidays = {"2025-03-18"}
        self.schedule = {}

    def is_working_day(self, date):
        return date.weekday() < 5 and date.strftime("%Y-%m-%d") not in self.holidays

    def book_meeting(self, user, date_str, start, end):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if not self.is_working_day(date) or not (self.working_hours[0] <= start < end <= self.working_hours[1]):
            return "Invalid meeting time!"
        self.schedule.setdefault(user, {}).setdefault(date_str, []).append((start, end))
        return "Meeting scheduled successfully!"

    def available_slots(self, user, date_str):
        booked = sorted(self.schedule.get(user, {}).get(date_str, []))
        slots, start = [], self.working_hours[0]
        for s, e in booked:
            if start < s:
                slots.append(f"{start}:00 - {s}:00")
            start = e
        if start < self.working_hours[1]:
            slots.append(f"{start}:00 - {self.working_hours[1]}:00")
        return slots or ["No slots available"]

    def view_meetings(self, user):
        return self.schedule.get(user, "No meetings scheduled")

scheduler = MeetingScheduler()
print(scheduler.book_meeting("Alice", "2025-03-18", 10, 11))
print("Available slots:", scheduler.available_slots("Alice", "2025-03-18"))
