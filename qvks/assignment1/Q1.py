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
	print(is_anagram("ab", "ba"))
	print(is_anagram("ab", "bab"))
	print(is_anagram("AbC", "CBA"))

main()

