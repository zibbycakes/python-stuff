#import numpy as np

global unique;
global name;
global time;

global MONDAY;

Schedule = [[0 for x in range(16)] for x in range(5)];

def enum(**enums):
    return type('Enum', (), enums);

def parseTime(given, index):
	clean = given[0:-1];
	times_by_day = clean.split(", ");
	#print(times_by_day);
	time = times_by_day[index];
	chopped = time.split();
	day = getDay(time);
	print(day);
	#figure out start index
	time_start = chopped[1];
	time_start = militaryTime(time_start) + chopped[1][-2:0];
	start_index = getTimeIndex(time_start);
	print("This is the start index: " + str(start_index));
	#figure out end index
	time_end = chopped[3];
	time_end = militaryTime(time_end) + chopped[3][-2:0];
	end_index = getTimeIndex(time_end);
	print("This is the end index: " + str(end_index));
	print("This class happens from " + time_start + " to " + time_end + " on " + chopped[0]);

	return [day, start_index, end_index];

def getDay(time):
	chopped = time.split();
	#switch(chopped[0]):
	if(chopped[0] == 'M'):
		day = Days.M;
	elif(chopped[0] == 'T'):
		day = Days.T;
	elif(chopped[0] == 'W'):
		day = Days.W;
	elif(chopped[0] == 'H'):
		day = Days.H;
	elif(chopped[0] == 'F'):
		day = Days.F;
	return(day);

def parseHour(time):
	chopped = time.split(":");
	hour = int(chopped[0]);
	return hour;

def isThirty(time):
	return time.split(":")[1] == '30';

def getTimeIndex(time):
	#milTime = militaryTime(int(parseHour(time)));
	index = (int(parseHour(time[0:-2]))-8)*2;
	if(isThirty(time)):
		index = index + 1;
	return index;	

def militaryTime(time):
	if(time[-2:] == 'PM' and int(parseHour(time)) != 12):
		return str(12+int(parseHour(time[0:-2]))) + ":00";
	return str(time);

def addToSchedule(course, day, start, end):
	goodtogo = checkClear(course, day, start, end);
	if(goodtogo):
		for x in range (start,end):
			day[x] = course;

def checkClear(course, day, start, end):
	for x in range (start, end):
		if(day[x] != 0):
			if(day[x] != course):
				print("Scheduling conflict for " + course + " with " + day[x]);
				return False;
	return True;
	#add more cases

#use stand for loop instead
def printSchedule():
	for day in Schedule:
		index = 0;
		for time in day:
			actual_time = standardTime(indexToMTime(time));
			print(time);

def indexToMTime(index):
	if(int(index)%2 == 0):
		hour = (index/2) + 8;
		return str(int(hour)) + ":00";
	else:
		return str(int(((int(index)-1)/2)+8)) + ":30";

def standardTime(milTime):
	print(milTime);
	milHour = parseHour(milTime);
	milMin = isThirty(milTime);
	isPM = False;
	answer = milTime;
	if(milHour > 12):
		answer = int(milHour)-12;
		isPM = True;
	elif(milHour == 12):
		return "12:00PM";
	answer = int(milHour);
	if(milMin):
		answer = str(answer) + ":30";
	else:
		answer = str(answer) + ":00";
	if(isPM):
		answer = str(answer) + "PM";
	else:
		answer = str(answer) + "AM";
	return answer;	

Days = enum(M = 0, T = 1, W = 2, H = 3, F = 4);
read = open("course_input.txt",'r');
courses = read.readlines();
#print(courses);
#MONDAY  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
unique = [];
name = [];
time = [];
for line in courses:
    if(line != "\n"):
        here = line.split(" | ");
        unique.append(here[0]);
        name.append(here[1]);
        time.append(here[2]);
#this_time = time[unique.index('51210')];
this_time = time[unique.index('51165')];
#print(this_time);
parsed1 = parseTime(this_time, 0);
addToSchedule(name[time.index(this_time)], Schedule[parsed1[0]], parsed1[1], parsed1[2]);
this_time = time[unique.index('51210')];
parsed2 = parseTime(this_time,0);
addToSchedule(name[time.index(this_time)], Schedule[parsed2[0]], parsed2[1], parsed2[2]);
this_time = time[unique.index('31435')];
parsed3 = parseTime(this_time, 0);
addToSchedule(name[time.index(this_time)], Schedule[parsed3[0]], parsed2[1], parsed2[2]);
printSchedule();

#USE THIS INSTEAD
#Matrix = [[0 for x in range(16)] for x in range(5)] 



#example: print name[unique.index('51210')];
#def scheduleDay(day):

