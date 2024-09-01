
#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

# Example usage:
print(return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: [2, 4, 6, 8, 10]

    


    

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]