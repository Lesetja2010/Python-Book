class SnailRun:
    def __init__(self, snail_name, finish_time):
        self.name = snail_name
        self.time = finish_time

    def show(self):
        return ("%s finished the race with a time of: %f" % (self.name, self.time))

    def __cmp__(self, other):
        if self.time < other.time:
            return -1
        elif self.time > other.time:
            return 1
        else:
            return 0

    def __str__(self):
        """
            function returns a string representation of the class
        """
        return ("name: %s, time: %f" % (self.name, self.time))


race4 =[]
input_file = open("trees.txt", "r")

for line in input_file:
    fields = line.split(" ")
    snail = SnailRun(fields[1].rstrip(), float(fields[0]))
    race4.append(snail)

input_file.close()    

race4.sort()

print "Race Results:"
print ("%3s %5s %s-10" %("pos", "time", "name") )

snails = len(race4)

for i  in range(snails):
    print "%3d %5.1f %-10s" % (i+1, race4[i].time, race4[i].name)
    
for snail in race4:
    print snail
