import hashlib

def crack_passwords(hash_file_path, wordlist_path):
    hashes = set()
    with open(hash_file_path, "r", encoding="utf-8", errors="ignore") as hf:
        for line in hf:
            line = line.strip()         
            if line:                    
                hashes.add(line.lower())

    found = {}  

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wf:
        for word_line in wf:
            word = word_line.strip()   
            if not word:
                continue               

            h = hashlib.md5(word.encode()).hexdigest()

            if h in hashes and h not in found:
                found[h] = word
                print(f"Found: {h} -> {word}")

                if len(found) == len(hashes):
                    break

    return found


def main():
    print("Simple MD5 dictionary cracker")
    hash_file = input("Enter name of the file: ").strip()
    wordlist = input("Enter name of the file: ").strip()

    try:
        results = crack_passwords(hash_file, wordlist)
    except FileNotFoundError as e:
        print("File not found:", e)
        return
    except Exception as e:
        print("An error occurred:", e)
        return

    if not results:
        print("No passwords were cracked.")
    else:
        print("\nSummary of cracked passwords:")
        for h, pw in results.items():
            print(f"{h} : {pw}")
        print(f"Total cracked: {len(results)}")


if __name__ == "__main__":
    main()

