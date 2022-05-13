
## What is Affine Cipher ?

The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.
## Formula

```
  C = (a * P + b) mod 26
  P = (a ^ -1 * (C - b)) mod 26
```
## Guide
```
 ! Usage: python3 affinecipher.py <type> <string> <a> <b>
  
* type    : {enc: encryption, dec: decryption}
* string  : the text you want to enrypt or decrypt
* a       : the first operand of the key
* b       : the second operand of the key
```
## example 
  python3 affinecipher.py enc kompo 10 12