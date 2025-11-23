# Password Cracker 

A small, MD5 dictionary password cracker written in Python.
It reads a file of MD5 hashes (one per line) and a wordlist (one candidate password per line), hashes each candidate with MD5, and reports any matches.

## Files

* **password_cracker.py** — the Python script.

* **hashes.txt** — example file with one MD5 hash per line.

* **wordlist.txt** — example wordlist (one candidate per line).

## Requirements

* Python 3.6+ installed.

* No external libraries required (uses Python standard library hashlib).

## Quick usage

1. Open a terminal.

2. Run:
    
        python3 cracker.py  

3. The program will prompt for(**If file in the directory you can just enter the name of the file. Example: hashes.txt**):

**Enter path to hash file:** — path to the file containing MD5 hashes (one per line).

**Enter path to wordlist file:** — path to the file containing password guesses (one per line).

## How it works 

1. The script reads all target hashes into a set for fast lookup.

2. It reads each candidate password from the wordlist, strips whitespace, encodes to bytes and computes hashlib.md5(word.encode()).hexdigest().

3. If the computed MD5 matches a hash in the set, it prints and stores the match.

4. The script stops early if it cracks all hashes.

## Security & ethics

**This tool is for educational purposes only (learning about hashing and password security).**

**Do not use it to attempt access to systems, accounts, or data you do not own or have explicit permission to test. Unauthorized cracking is illegal and unethical.**

**MD5 is cryptographically broken and should not be used for password storage. Use modern hash functions with salts (e.g., bcrypt, Argon2) in real systems.**
