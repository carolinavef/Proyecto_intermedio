class RegEx:
    def __init__(self):
        self.text = ""
        self.pattern = ""
        self.flag_global = False

    def set_text(self, text):
        """Establece el texto en el que se realizará la coincidencia."""
        self.text = text

    #Leer el patrón (f/fr, regEx, g/i)
    def match(self, pattern):
            matches = []#lista para almacenar coincidencias
            if pattern[0] == "f":# checa que la primera posicion si es f
                if pattern[1] == "r":#checa que  si la segunda es r
                    pattern_to_find = pattern[2:]#2: apartir del tercer elemeto, nueva variable
                else:
                    pattern_to_find = pattern[1:]#1: a partir del segundo, nueva variable
                if pattern[-1] == "g":#si ultimo caracter es g
                    self.flag_global = True
                elif pattern[-1] == "i":#si el ultimo caracter es i
                    self.flag_global = False
                else:#no se cumple ninguna 
                    self.flag_global = False

             
            return matches

    def _match_pattern_at_index(self, pattern, index):#patron coincide
        for i in range(len(pattern)):#atraves de caracteres de patron
            if index + i >= len(self.text) or (pattern[i] != self.text[index + i] and pattern[i] != '.'):
            #verifica si estas mas alla del final/cqracterpatron no coincide con caractertexto en i/caracter noes punto
               
                return False#si se cumple, false porque no hay coincidencia
            
        if self.flag_global:
            return True#ha encontrado coincidencia
        
        
        elif index > 0 and self.text[index - 1].isalpha():#******
            return False
        elif index + len(pattern) < len(self.text) and self.text[index + len(pattern)].isalpha():
            return False
        return True#***********************************************

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
        matches = []
        i = 0
        while i < len(self.text):
            #
            if self._match_pattern_at_index(pattern, i):#bandera para que busque todas las coincidencias
                matches.append(self.text[i:i + len(pattern)])#pedazode texto que empieza en i y termina en i+lenpattern
                i += 1#encontro coincidencia, avanza de posicion
            else:
                i +=1  #noencontro, avanza siguiente caracter
        return matches

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
        
        matches = [] 
        i = 0  

        while i < len(self.text):  
          
            char_repetido = pattern.split('{')[0]#con el 0 ya abarcas todo lo antes del {

            repeticiones = pattern.split('{')[1].split('}')[0]
            
            complemento= pattern.split('{')[1].split('}')[2:] #Para analizar lo despues de } 

            if self._match_pattern_at_index(char_repetido, i, flag_global=True):
                count = 0 
                
                while i < len(self.text) and count < int(repeticiones):
                    if self._match_pattern_at_index(char_repetido, i, flag_global=True):
                        i += 1# debria de aumentar el tamanio del patron? no solo un lugar??
                        count += 1
                        if complemento:
                            if self._match_pattern_at_index(complemento, i, flag_global=True) :
                                i += 1
                                count += 1
                        else:
                            break
                    else:
                        break 
                if count == int(repeticiones):
                    matches.append(self.text[i - count:i]) 
            else:
                i += 1 
        return matches 
    
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


