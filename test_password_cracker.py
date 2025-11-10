# test_simple.py
import hashlib
from password_cracker import crack_passwords

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

def test_cracks_one_hash(tmp_path):
    # prepare files
    hashes = tmp_path / "hashes.txt"
    words = tmp_path / "wordlist.txt"

    # write one hash (for "password") and a small wordlist
    hashes.write_text(md5("password") + "\n")
    words.write_text("notit\npassword\n")

    results = crack_passwords(str(hashes), str(words))

    assert isinstance(results, dict)
    assert md5("password") in results
    assert results[md5("password")] == "password"

def test_empty_hash_file_returns_empty(tmp_path):
    hashes = tmp_path / "hashes.txt"
    words = tmp_path / "wordlist.txt"

    # empty hash file, wordlist has entries
    hashes.write_text("")
    words.write_text("password\n1234\n")

    results = crack_passwords(str(hashes), str(words))
    assert results == {}
