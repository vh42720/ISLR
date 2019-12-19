import random

yes_win_count = 0
no_win_count = 0
i = 0

while i < 100000:
	# shuffle the prize
	state = [1, 0, 0]
	random.shuffle(state)

	door = [0, 1, 2]
	prize = state.index(1)
	choose = random.choice(door)
	others = [item for item in door if (item != choose)]
	to_reveal = [item for item in door if (item != choose and item != prize)][0]
	to_switch = [item for item in others if item != to_reveal][0]

	# print(state)
	# print(' -- Prize is in door:', prize, '--  We choose door:', choose, '\n',
	#       '-- The other doors are:', others, '\n',
	#       '-- Doors to reveal:', to_reveal, '-- Door to switch to:', to_switch)

	choose_if_yes = to_switch
	if choose_if_yes == prize:
		yes_win_count += 1
	if choose == prize:
		no_win_count += 1

	i += 1

print('Yes win: ', yes_win_count, '\n',
      'No win: ', no_win_count)
