def pattern_cipher(x):
    """
    """
    # 1.If the input is empty ("") or None, it is returned unchanged.
    if x is None or x == "":
        print(f"DEBUG: {x} hit Path (Empty or None )") 
        return x

    # 2.Only alphabetic words are transformed.Special characters/punctuation remain unchanged.
    if not isinstance(x, str) or not x.isalpha():
        print(f"DEBUG: {x} hit Path (Not only alphabetic words )") 
        return x

    word = x

    # 3.--- If a word is a palindrome (reads the same forward and backward, case-insensitive), leave it unchanged. ---
    lower = word.lower()
    if lower == lower[::-1]:
        # Rule 1: palindrome unchanged
        print(f"DEBUG: {word} hit Path (Palindrome)") 
        return word

    #4.-------- If the word contains any repeated letters and is not a palindrome, reverse the word. --------
    if len(set(lower)) < len(lower): # set: remove repeated letter
        print(f"DEBUG: {word} hit Path (Repeated, Not Palindrome)") 
        return word[::-1] 

    #5.-------- If all letters are unique, rotate the word left by one character. --------
    # if len(set(lower)) == len(lower):
    #     return word[1:] + word[0]
    else:
        print(f"DEBUG: {word} hit Path (rotate)") 
        return word[1:] + word[0]
        