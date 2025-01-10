README: Caesar Cipher Encoding in Python

This Python script implements a Caesar Cipher to encode a given string by 
shifting its characters by a specified number of steps in the alphabet. The 
cipher works for both uppercase and lowercase letters, while non-alphabetic 
characters remain unchanged.
How It Works:

User Input:
        The script prompts the user to enter a string (sentence) to encode.
        The user specifies a numeric value for the shift.

Encoding Logic:
        Each alphabetic character in the string is shifted by the given value.
        The character wrapping ensures that:
            z becomes a for lowercase letters.
            Z becomes A for uppercase letters.
        Non-alphabetic characters like spaces and punctuation remain unchanged.

Output:
        The encoded string is displayed as output.

Code Explanation:
  Function: encoding(string, shift)
Parameters:
        string: The input string to be encoded.
        shift: The number of steps to shift each alphabetic character.

Returns:
        A new string with the encoded text.
Logic:
        For each character in the string:
            If it's a lowercase letter, apply the Caesar Cipher logic for lowercase ('a' to 'z').
            If it's an uppercase letter, apply the logic for uppercase ('A' to 'Z').
            Append the result to a new string.
            For non-alphabetic characters, append them unchanged.
