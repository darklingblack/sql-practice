number_of_birds = [28, 32, 1, 0, 10, 22, 30, 19, 145, 27, 36,
                   25, 9, 38, 21, 12, 122, 87, 36, 3, 0, 5, 55,
				   62, 98, 32, 900, 33, 14, 39, 56, 81, 29, 38,
				   1, 0, 143, 37, 98, 77, 92, 83, 34, 98, 40,
				   45, 51, 17, 22, 37, 48, 38, 91, 73, 54, 46,
				   102, 273, 600, 10, 11]

#1 How many sites are there? Hint: the function len() works on lists as well as strings.
len(number_of_birds)

#2 How many birds were counted at site 42? Remember, the number of the site and the number of its position may not be exactly the same.
print(number_of_birds[41])

#3 How many birds were counted at the last site? Have the computer choose the last site automatically in some way, not by manually entering its position.
print(number_of_birds[-1])

#4 What is the total number of birds counted across all of the sites?
print(sum(number_of_birds))

#5 What is the smallest number of birds counted?
print(min(number_of_birds))

#6 What is the largest number of birds counted?
print(max(number_of_birds))

#7 What is the average number of birds seen at a site? You will need to combine two built-in functions.
print((sum(number_of_birds))/len(number_of_birds))

number_of_birds[26] = '90'
number_of_birds[58] = '60'

print(number_of_birds[26])
print(number_of_birds[58])

unentered_sites = [27, 24, 16, 9, 23, 39, 102, 0, 14, 3, 9, 93, 64]

total_sites = number_of_birds + unentered_sites

total_sites = [int(x) for x in total_sites]

print(total_sites)

#1 What is the total number of birds counted across all of the sites?
print(sum(total_sites))

#2 What is the largest number of birds counted?
print(max(total_sites))

#3 What is the smallest number of birds counted?
print(min(total_sites))

#4 What is the average number of birds seen at a site?
print((sum(total_sites)))/(len(total_sites))

bird_counts = total_sites

def n_site_count(bird_counts, start_site, number_of_sites):
    """Count the total number of birds at a given number of sites starting
    at a given start site."""
    if start_site < 0:
        sub_sites = bird_counts[start_site:]
    else:
        start_site = start_site - 1 #convert start site to Python index
        sub_sites = bird_counts[start_site:start_site + number_of_sites]
    total_sites = sum(sub_sites)
    return total_sites


start_site = 74

number_of_sites = 10

print(n_site_count(bird_counts, start_site, number_of_sites))