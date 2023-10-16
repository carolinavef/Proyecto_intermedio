class RegEx:
    def __init__(self):
        self.text = ""
        self.pattern = ""

    def set_text(self, text):
        """Establece el texto en el que se realizará la coincidencia."""
        self.text = text

    #Leer el patrón (f/fr, regEx, g/i)
    def match(self, pattern):
            matches = []
            if pattern[0] == "f":
                if pattern[1] == "r":
                    pattern_to_find = pattern[2:]
                else:
                    pattern_to_find = pattern[1:]
                if pattern[-1] == "g":
                    flag_global = True
                elif pattern[-1] == "i":
                    flag_global = False
                else:
                    flag_global = False

                i = 0
                while i < len(self.text):
                    if self._match_pattern_at_index(pattern_to_find, i, flag_global):
                        matches.append(self.text[i:i+len(pattern_to_find)])
                        i += len(pattern_to_find)
                    else:
                        i += 1
            return matches

    def _match_pattern_at_index(self, pattern, index, flag_global):
        for i in range(len(pattern)):
            if index + i >= len(self.text) or (pattern[i] != self.text[index + i] and pattern[i] != '.'):
                return False
        if flag_global:
            return True
        elif index > 0 and self.text[index - 1].isalpha():
            return False
        elif index + len(pattern) < len(self.text) and self.text[index + len(pattern)].isalpha():
            return False
        return True

    def replace(self, pattern, replacement):
        new_text = self.text
        if pattern[0] == "f" and pattern[1] == "r":
            pattern_to_find = pattern[2:]
            i = 0
            while i < len(new_text):
                if new_text[i:i + len(pattern_to_find)] == pattern_to_find:
                    new_text = new_text[:i] + replacement + new_text[i + len(pattern_to_find):]
                    i += len(replacement)
                else:
                    i += 1
        return new_text
    

    #Búsqueda simple
    def busqueda_simple(self, pattern):
        pass

    #Rango de letras y numeros entre corchetes cuadrados
    def rangos(self, pattern):
        pass

    #Conjunto de letras entre corchetes
    def conjuntos(self, pattern):
        pass

    #Letra intermedia antes del signo ? puede o no aparecer en el match encontrado
    def puede_aparecer(self, pattern):
        pass

    #El operador | funciona como un or lógico. El texto puede hacer match con la string de la izq o der
    def izq_or_der(self, pattern):
        pass

    #Operador de repetición
    def repeticion(self, pattern):
        pass

    def comodin(self, pattern):
        pass

    # Leer funciones y realizar el comodin
    def leer(self, pattern):
        if pattern.isalpha():
            return self.busqueda_simple(pattern)
        elif '[' in pattern and ']' in pattern:
            return self.rangos(pattern) or self.conjuntos(pattern)
        elif '*' in pattern:
            return self.comodin(pattern)
        elif '?' in pattern:
            return self.puede_aparecer(pattern)
        elif '|' in pattern:
            return self.izq_or_der(pattern)
        elif '{' in pattern and '}' in pattern:
            return self.repeticion(pattern)
        else:
            print("Patrón no válido")


