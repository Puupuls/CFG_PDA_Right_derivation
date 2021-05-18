rules = {
	"S": ["aSA", "Ab", ""],
	"A": ["abSA", "b"]
}
word = "aababbbababbbb"
search_depth = 30

start = "S"
stack_start_symbol = 'Z'


# From here on magic happens

result = []
path = []


def generate(word, stack, depth=40):
	if not depth:
		return False

	suc = False
	if len(stack) == 0 and len(word) == 0:
		return True
	
	if len(stack) == 0:
		return False
	
	if word and stack[-1] == word[-1]:
		suc = generate(word[:-1], stack[:-1], depth-1)
		if suc:
			path.append((word, stack))
		return suc
	else:
		if stack[-1] in rules:
			t_stack = stack[:-1]
			for r in rules[stack[-1]]:
				suc = generate(word, t_stack+r, depth-1)
				if suc:			
					path.append((word, stack))
					result.append(r)
					return True
				
		else:
			return False
	
	
generate(word, start, search_depth)
result.append(start)
result = result[::-1]

if len(result) > 1:
	print("CFG Right hand derivation")
	t_string = result[0]
	for idx, r in enumerate(result):
		print(t_string)
		for i in range(len(t_string)):
			if t_string[-i-1] in rules:

				if i != 0:
					t_string = t_string[:-i-1] + result[idx+1] + t_string[-i:]  
				else:
					t_string = t_string[:-i-1] + result[idx+1]
				break
		

	print("\n\nPDA states")

	def print_formatted(w1, w2):
		print("(q, {0}, {1})".format(w1 if w1 else 'e', w2 if w2 else 'e'))


	print_formatted(word,stack_start_symbol)	
	for w, s in path:
		if s and word and s[-1] == word[0]:
			word = word[1:]
		print_formatted(word, s[::-1]+stack_start_symbol)
	print_formatted('','')	
else:
	print("Could not derive this word, you can try increasing search depth if deriviation could need more than {0} steps".format(search_depth))



