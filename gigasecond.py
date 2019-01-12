from datetime import timedelta

Gs = timedelta(seconds=10**9)

def add_gigasecond(birthday):
	'''(date) -> date
	
	Return the date that someone turned or will celebrate their 1 Gs
	anniversary
	'''
	return birthday + Gs

    #Calculate the moment when someone has lived for 10^9 seconds.
    #A gigasecond is 10^9 (1,000,000,000) seconds.