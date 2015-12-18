class Queue:
    def __init__(self):
        self.holder = []

    def push(self,val):
        self.holder.append(val)

    def pop(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]   
        except:
            pass

        return val  

    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result

    def peek(self):
        return self.holder[0]

    def display(self):
        queue = ""
        for ele in self.holder:
            queue += str(ele) + " "
        print queue

print " \n --------- This is Queue Solution ------------ \n"
que = Queue()
def choicePush(que):
    val = input("Enter element to PUSH ")
    que.push(val)

def choicePop(que):
    if que.IsEmpty():
        print "\n Queue is Empty, Nothing to pop"
        return
    print 'Popped {0}'.format(que.pop())

def choicePeek(que):
    if que.IsEmpty():
        print "\n Queue is Empty, Nothing to peek"
        return
    print (que.peek())

def choiceDisplay(que):
    que.display()

while(True):
    print " \n Enter \n"
    print "1 -> PUSH"
    print "2 -> POP"
    print "3 -> PEEK"
    print "4 -> DISPLAY"
    print "5 -> To End \n"
    choice = input("Please make your choice ")
    # import pdb;pdb.set_trace()
    if choice == 1:
        choicePush(que)
    elif choice == 2:
        choicePop(que)
    elif choice == 3:
        choicePeek(que)
    elif choice == 4:
        choiceDisplay(que)
    else:
        print "\n Thank You \n"
        break