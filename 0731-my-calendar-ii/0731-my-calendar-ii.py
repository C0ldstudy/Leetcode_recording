from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedList() 
        #self.calendar: A SortedList to store all bookings.
        self.booked = SortedList() 
        #self.booked: A SortedList to store intervals where double bookings occur.

    #book: This method attempts to add a new booking and returns True if successful, False otherwise.
    def book(self, start: int, end: int) -> bool:
        for booking in self.booked:
            s, e = booking[:]
            if start < e and end > s:
                return False
        #Double Booking Check: Iterates through self.calendar to check for overlaps with existing bookings. If an overlap is found, the overlapping interval is added to self.booked.
        for booking in self.calendar:
            s, e = booking[:]
            if start < e and end > s:
                self.booked.add((max(s, start), min(e, end)))
        
        self.calendar.add((start, end)) #Add Booking: Adds the new booking to self.calendar.

        return True #Return: If no triple booking is detected, the method returns True, indicating the booking was successful.
        
        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)