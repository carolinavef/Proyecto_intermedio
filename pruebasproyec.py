def repeticion(self, pattern):
 
    
        matches = []  # Inicializa una lista para almacenar coincidencias
        i = 0  # Inicializa una variable 'i' para rastrear la posición actual en el texto

        while i < len(self.text):  # Itera mientras no hayamos llegado al final del texto
            # Encuentra el carácter antes de las llaves
            char_repetido = pattern.split('{')[0]

            # Encuentra la parte dentro de las llaves (número de repeticiones)
            repeticiones = pattern.split('{')[1].split('}')[0]

            # Verifica si el carácter antes de las llaves coincide
            if self._match_pattern_at_index(char_repetido, i, flag_global=True):
                # Si coincide, intenta encontrar múltiples repeticiones
                count = 0  # Inicializa una variable para rastrear el número de repeticiones encontradas
                while i < len(self.text) and count < int(repeticiones):
                    # Verifica si el carácter antes de las llaves coincide en la posición actual
                    if self._match_pattern_at_index(char_repetido, i, flag_global=True):
                        i += 1  # Avanza a la siguiente posición en el texto
                        count += 1  # Incrementa el contador de repeticiones encontradas
                    else:
                        break  # Si no hay coincidencia, detiene la búsqueda

                # Si se encontraron suficientes repeticiones, agrega a las coincidencias
                if count == int(repeticiones):
                    matches.append(self.text[i - count:i])  # Agrega la secuencia repetida a las coincidencias
            else:
                i += 1  # Si no hay coincidencia en la posición actual, avanza a la siguiente posición en el texto

        return matches  # Retorna la lista de coincidencias