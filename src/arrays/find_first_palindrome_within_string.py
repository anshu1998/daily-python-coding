"""
Identify palindromes within strings. For example, ‘abcdedc’ has the palindrome ‘cdedc’.


"""


def get_palindromes(str_):
	start = None
	i = 0
	end = None
	j = len(str_) - 1
	is_equal = False

	while i <= j:
		if str_[i] != str_[j]:
			i += 1
			start = i
			is_equal = False
		else:
			if not start:
				if start != 0:
					start = i
					is_equal = True
			if not end:
				end = j
			i += 1
			j -= 1

	start = None
	i = 0
	end = None
	j = len(str_) - 1
	if not is_equal:
		while i <= j:
			if str_[i] != str_[j]:
				j -= 1
				end = j
				is_equal = False
			else:
				if not start:
					if start != 0:
						start = i
						is_equal = True
				if not end:
					end = j
				i += 1
				j -= 1

	if is_equal:
		for k in range(start, end+1):
			print(str_[k], end='')
	else:
		print('No palindrome strings')


if __name__ == '__main__':
	get_palindromes('abcdedbazye')
