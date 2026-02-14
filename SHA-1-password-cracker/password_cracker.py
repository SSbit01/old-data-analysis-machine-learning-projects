import hashlib

def crack_sha1_hash(hash, use_salts=False):
  with open("top-10000-passwords.txt") as passwords_file:
    passwords = passwords_file.read().splitlines()
    if use_salts:
      with open("known-salts.txt") as salts_file:
        salts = salts_file.read().splitlines()
        for i in passwords:
          for j in salts:
            if hash == hashlib.sha1((i + j).encode("utf-8")).hexdigest() or hash == hashlib.sha1((j + i).encode("utf-8")).hexdigest():
              return i
    else:
      for i in passwords:
        if hash == hashlib.sha1(i.encode("utf-8")).hexdigest():
          return i
  return "PASSWORD NOT IN DATABASE"