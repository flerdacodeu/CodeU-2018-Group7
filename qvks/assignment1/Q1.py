import string
import sys

# the function is case insensitive
def is_anagram(s1, s2):
	s1 = s1.lower()
	s2 = s2.lower()
	if len(s1) != len(s2):
		return False

	return sorted(s1)==sorted(s2)

def main():
	assert(is_anagram("ab", "ba"))
	assert(not is_anagram("ab", "bab"))
	assert(is_anagram("AbC", "CBA"))

main()

