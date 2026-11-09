import time


class Queue:
    #queue with a fixed size and set up front, back, and count variables.
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = 0
        self.back = 0
        self.table = [None] * size
    #check if the queue is empty.
    def isEmpty(self):
        return self.count == 0
    #check if the queue is full.
    def isFull(self):
        return self.count == self.size
    #check if the queue is full.
    #add a record to the back of the queue if it is not full and the record is valid.
    def enqueue(self, record):
        if record[1] < 1 or record[1] > 100:
            print("Print job must contain between 1 and 100 pages.")
            return

        if self.isFull():
            print("Queue is full.")
            return

        self.table[self.back] = record
        self.back = (self.back + 1) % self.size
        self.count += 1

    #remove and return the record at the front of the queue if it is not empty. 
    def dequeue(self):
        if self.isEmpty():
            return None
        #remove and return the record at the front of the queue if it is not empty. 
        record = self.table[self.front]
        self.table[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

        return record

#simulate a printer with a queue of print jobs.
def printer():
    printer_queue = Queue(5)

    print("Printer Simulation")
    print("Printer speed: 18 pages per minute")
    print()

    while True:
        print("1. Add print job")
        print("2. Print next job")
        print("3. Exit")

        choice = input("Enter choice: ")
        #get the user's choice
        if choice == "1":
            job_num = int(input("Enter job number: "))
            pages = int(input("Enter number of pages: "))

            record = (job_num, pages)
            printer_queue.enqueue(record)
            #add the print job to the queue
        elif choice == "2":
            if printer_queue.isEmpty():
                print("No print jobs in the queue.")
            else:
                record = printer_queue.dequeue()

                job_num = record[0]
                pages = record[1]

                print("Printing job:", job_num)
                print("Pages:", pages)

                seconds_per_page = 60 / 18
                #simulate printing each page of the job
                for page in range(1, pages + 1):
                    print("Printing page", page, "of", pages)
                    time.sleep(seconds_per_page)

                print("Job", job_num, "completed.")
        #end of printing job
        elif choice == "3":
            print("Printer stopped.")
            break

        else:
            print("Invalid choice.")

        print()


printer()