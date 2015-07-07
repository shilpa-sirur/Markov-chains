import sys


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
    print bigram_dict
    return bigram_dict
make_chains("green-eggs.txt")

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
