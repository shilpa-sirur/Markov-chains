import sys
import random
import string


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    source_file = open(corpus)
    all_word_list = []
    bigram_dict = {}
    
    
    for line in source_file:
        # print bigram
        seperate_words = line.rstrip().split(" ")
        all_word_list.extend(seperate_words)

        # print seperate_words
    for i in range(len(all_word_list)-2):
        bigram = (all_word_list[i], all_word_list[i+1])
        value_word = all_word_list[i+2]

        if bigram not in bigram_dict:
            bigram_dict[bigram] = []
        bigram_dict[bigram].append(value_word)  
    # print bigram_dict
    return bigram_dict
chains = make_chains("green-eggs.txt")

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""  

# grab the key tuple and the associated value, index the second word of 
# the key tuple and combine it with the value and from that find the new 
# associated value 
#This gets the first key pair and the value and turns the key tuples into a string
    random_key1 = random.choice(chains.keys())
    random_value = random.choice(chains[random_key1])
    random_text = str(random_key1[0] + " " + random_key1[1]) + " " + str(random_value)
    new_key1 = (random_key1[1], random_value)
    # print new_key1
    while new_key1 in chains: 
        # This will select second word of key pair and combine it with value to create new key
        new_value1 = random.choice(chains[new_key1])
        new_key1 = (new_key1[1], new_value1)
        random_text = random_text + " " + new_value1 + " "
    print random_text
        # random_text2 = str(new_key1) + " " + str(new_value1)
make_text(chains)    



