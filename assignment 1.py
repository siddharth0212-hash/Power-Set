def print_substrings(s):
    n = len(s) 
    
    for i in range(n):
        for j in range(i + 1, n + 1):
          
            # Print the substring from index i to j
            print(s[i:j])

# Single test case
s = "anki"
print_substrings(s)