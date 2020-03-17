import gc


class mentorLearner: 
	#list with stack of interest
	stack = []
	
	#status will determine whether the object is of a learner or a mentor(0 for learner, 1 for mentor, by default it is 0)
	status = 0 
	
	#time available for the mentor, 0th index for beginning and 1st index for ending
	time = []

	#method to add a particular interest
	def addStacks(skill):
		skill = skill.upper()
		stack.append(skill)

	#method to set mentor or learner
	def setMentorOrLearner(val):
		if val == 1:
			status = 1

	#method for setting available time for mentors
	#assuming the time slots begin and end at hours corresponding to an integer ie. only at 2, not 2:30 and 24hr format is used 
	def setAvailableTime(begin,end):
		begin = int(begin)
		end = int(end)
		time.append(begin)
		time.append(end)

	#method for searching a suitable mentor
	#slot is a list with 2 integer elements giving the beginning and ending time required
	#tech is the stack required
	#this underlying block of code was suggested by my friend, I don't really understand it completely.
	def getMentor(slot, tech ):
		tech = tech.upper()
		for obj in gc.get_objects():
			if isinstance(obj, mentorLearner):
				if obj.status == 1 and (slot[0]>obj.time[0] or slot[1]<obj.time[1]) and tech in obj.stack:
					return obj
						







