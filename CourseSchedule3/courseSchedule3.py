class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Ordenando os cursos por data de término em ordem crescente
        courses.sort(key=lambda x: x[1])

        quantCursos = 0
        terminoUltimoCurso = 0

        for curso in courses:
            duracao, ultimoDia = curso

            # Verificar se o curso atual é compatível com os cursos já realizados
            if terminoUltimoCurso + duracao <= ultimoDia:
                quantCursos += 1
                terminoUltimoCurso += duracao

        return quantCursos