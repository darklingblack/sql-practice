import string

text = "Monty Python's Flying Circus"

print "upper", "=>", text.upper()
print "lower", "=>", text.lower()
print "split", "=>", text.split()
print "join", "=>", "+".join(text.split())
print "replace", "=>", text.replace("Python", "Perl")
print "find", "=>", text.find("Python"), text.find("Perl")
print "count", "=>", text.count("n")

#upper => MONTY PYTHON'S FLYING CIRCUS
#lower => monty python's flying circus
#split => ['Monty', "Python's", 'Flying', 'Circus']
#join => Monty+Python's+Flying+Circus
#replace => Monty Perl's Flying Circus
#find => 6 -1
#count => 3

species = 'cat'

species.upper()

dna = 'gcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgg'

dna.replace("a", "A")

phrase = "      Thank goodness it's Friday"

phrase.replace("      ", "")

dna = 'gcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgg'

dna.count("a")

dna.count("")


answers = [42, 0, 'money', 'children', 'friends', 'dancing', 'cheetos', "ERROR: THIS IS A VIOLATION OF SKYNET'S QUERY POLICY. A TERMINATOR WILL ARRIVE SHORTLY"]

for i in answers:
    print(f"The ultimate answer to the ultimate question of life, the universe, and everything is:{i}")