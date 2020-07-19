import sys

if len(sys.argv) < 2:
	print('Usage: python bcrewcheck.py space_separated_crewnames')

bcrews = []

with open('bannedcrewlist.txt', 'r') as bcrewlist:
	for bcrew in bcrewlist:
		bcrews.append(bcrew.strip())
		
inbcrews = []

for crew in sys.argv[1:]:
	if crew.upper() in bcrews:
		inbcrews.append(crew)
		
if not inbcrews:
	print("User is not in any of the banned crews.")
	
else:
	print("User is in the following banned crews: ")
	for crew in inbcrews:
		print(crew.upper())
