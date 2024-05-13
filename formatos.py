#Para importar al codigo fuente

#NEGRITA
def negrita(texto):
    texto.tag_add("negrita", "sel.first", "sel.last")#Ponemos en negrita del 1r caracter selccionado hasta el ultimo
    texto.tag_config("negrita", font=("Arial", 12, "bold"))#Config de negrita

#KURSIVA
def kursiva(texto):
    texto.tag_add("cursiva", "sel.first", "sel.last")
    texto.tag_config("cursiva", font=("Arial", 12, "italic"))

#SUBRAYADO
def subrayado(texto):
    texto.tag_add("subrayado", "sel.first", "sel.last")
    texto.tag_config("subrayado", underline=True)

#NEGRITAKURSIVA
def neku(texto):
    texto.tag_add("neku", "sel.first", "sel.last")#Ponemos en negrita del 1r caracter selccionado hasta el ultimo
    texto.tag_config("neku", font=("Arial", 12, "bold", "italic"))#Config de negrita
