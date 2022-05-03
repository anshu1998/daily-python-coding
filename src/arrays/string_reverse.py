"""
program to reverse string
constraint: the special characters should remain at whatever place they are

case 1:
input: ab-cd
output: dc-ba

case 2:
input: ab!cD-ef+=ghI!!
output: Ih!gf-eD+=cba!!
"""


def reverse_string(str_):
	result = ''
	if str_:
		str_list = list(str_)
		j = len(str_) - 1
		i = 0
		last_index = None
		while j >= 0:
			if str_[j].isalnum():
				if last_index is None:
					while not str_list[i].isalnum():
						i += 1
					last_index = i
					str_list[last_index] = str_[j]
				else:
					for l in range(last_index + 1, len(str_)):
						if not str_list[l].isalnum():
							continue
						str_list[l] = str_[j]
						last_index = l
						break
			j -= 1
		result = ''.join(str_list)
	return result


if __name__ == '__main__':
	input_ = 'ab-cd'
	input_ = 'ab!cD-ef+=ghI!!'
	output = reverse_string(input_)
	print(output)
