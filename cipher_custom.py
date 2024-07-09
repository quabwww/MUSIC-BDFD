import re

class Cipher:
    def __init__(self):
        pass

    def get_throttling_function_name(self):
        # Expresión regular para buscar un patrón específico
        function_patterns = [
            r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*',
            r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        ]
        # Código para buscar y devolver el nombre de la función de throttling
        source_code = """
        // Aquí va tu código fuente donde buscas la función de throttling
        var a = {
            b: 123,
            c: function() {
                var n = "test";
                a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b), Bpa.length || iha(""));
            }
        };
        """
        for pattern in function_patterns:
            match = re.search(pattern, source_code)
            if match:
                return match.group(1)  # Devolver la coincidencia encontrada
        return None  # Devolver None si no se encuentra ninguna coincidencia

# Ejemplo de uso
if __name__ == "__main__":
    cipher = Cipher()
    result = cipher.get_throttling_function_name()
    print("Resultado:", result)


