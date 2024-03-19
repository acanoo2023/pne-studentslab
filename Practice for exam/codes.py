class alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula=matricula
        self.nombre=nombre
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.nota_final=0
    def get_matricula(self):
        return self.matricula
    def get_nombre(self):
        return self.nombre
    def get_notamedia(self):
        self.nota_final=(self.nota1+self.nota2+self.nota3)/3
        return self.nota_final
    def conclusion(self):
        if self.nota_final >=4.8:
            return 'aprobado'
        else:
            return 'suspenso'

alumno=alumno(4229,'Sergio',5,3,8)
print('MATRICULA: ', alumno.get_matricula())
print('NOMBRE: ', alumno.get_nombre())
print('NOTA FINAL: ', alumno.get_notamedia())
print('CONCLUSIÓN: ', alumno.conclusion())