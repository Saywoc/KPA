import hashlib, os, shelve, re,glob




# Function to check if the password matches the pattern
def regex_password(psw):
    
    password_REGEX = r'^[a-zA-Z0-9!"#$&]+$'
    
    return bool(re.match(password_REGEX, psw))
  
#Function to prompt the user to enter a password and check if it complies with the pattern
def get_password(PROMPT_REQUEST: str):

    while True:
        password_On_Clear = input(PROMPT_REQUEST)
        if regex_password(password_On_Clear):
            break
        else:
            print('Please enter a non-empty Clear_Text that contains only alphanumeric characters and some special characters.')
  
    return password_On_Clear

# Function to hash password
def create_hash(Clear_password: str):

    salt = os.urandom(16)
    password_with_salt = Clear_password.encode('utf-8') + salt
    hash_object = hashlib.sha256(password_with_salt)
    hash_value = hash_object.hexdigest()

    return hash_value, salt
# End Create_hash

# Function to save hash and salt to file
def save_hash(hash_value: str, salt: bytes):
    
    key_dir = os.path.join(os.getcwd(), 'kpa', 'KEY')
    os.makedirs(key_dir, exist_ok=True)   
    shelfFile = shelve.open(os.path.join('kpa', 'KEY','HASH'))
    hash = ('{},{}'.format(hash_value, salt))                       
    shelfFile['hash'] = hash
    
    shelfFile.close()
    
    return True
# End save_hash

# Function to load hash and salt from file
def load_hash():
    # Load the hash and the salt from the HASH file
    shelfFile =  shelve.open(os.path.join('KPA', 'KEY', 'HASH'))
    shelfFile['hash']
    HASH = str(shelfFile['hash']).split(',')
    SALT = HASH[1]

    return HASH[0], SALT
# End load_hash

# Function to check if the entered password is correct
def check_password(password: str):
    HASH , SALT= load_hash() 
    password_Hash, salt = create_hash(password)
    if  password_Hash == HASH and salt == SALT:
        return False
    else:
        return True
# End check_password


if __name__ == '__main__':
    None

