import os

def modify_pytube_cipher():
    pytube_cipher_path = '/usr/local/lib/python3.11/site-packages/pytube/cipher.py'  # Ruta en el contenedor
    new_patterns = """
    [
        r'a\\.[a-zA-Z]\\s*&&\\s*\\([a-z]\\s*=\\s*a\\.get\\("n"\\)\\)\\s*&&.*?\\|\\|\\s*([a-z]+)',
        r'\\([a-z]\\s*=\\s*([a-zA-Z0-9$]+)(\\[\\d+\\])?\\([a-z]\\)',
        r'\\([a-z]\\s*=\\s*([a-zA-Z0-9$]+)(\\[\\d+\\])\\([a-z]\\)',
    ]
    """
    
    with open(pytube_cipher_path, 'r') as file:
        lines = file.readlines()
    
    with open(pytube_cipher_path, 'w') as file:
        for line in lines:
            if line.strip().startswith("function_patterns = ["):
                file.write(f"    function_patterns = {new_patterns}\n")
            else:
                file.write(line)

if __name__ == "__main__":
    modify_pytube_cipher()
