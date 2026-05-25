import tkinter as tk
from gui_manager import InterfaceManager

class AppPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Integral de Estructuras de Datos")
        self.root.geometry("850x600")
        self.root.config(bg="white")
        
        self.container = tk.Frame(self.root, bg="white")
        self.container.pack(fill="both", expand=True)
        
        self.gui = InterfaceManager(self.container)
        
        self.configurar_menu()
        
        self.gui.seccion_inicio()
        
    def configurar_menu(self):
        menu_bar = tk.Menu(self.root)
        menu_e = tk.Menu(menu_bar, tearoff=0)
        
        menu_e.add_command(label="Pantalla de Inicio", command=self.gui.seccion_inicio)
        menu_e.add_separator()
        
        # Todas tus estructuras y algoritmos en el mismo menú
        menu_e.add_command(label="Listas", command=self.gui.seccion_lista)
        menu_e.add_command(label="Colas", command=self.gui.seccion_cola)
        menu_e.add_command(label="Strings", command=self.gui.seccion_string)
        menu_e.add_command(label="Listas 2D", command=self.gui.seccion_lista_2d)
        menu_e.add_command(label="Análisis CSV", command=self.gui.seccion_csv)
        menu_e.add_command(label="Bicolas", command=self.gui.seccion_bicola) 
        menu_e.add_command(label="Pilas", command=self.gui.seccion_pila)
        menu_e.add_command(label="Nodos (Árbol Binario)", command=self.gui.seccion_nodo)
        menu_e.add_command(label="Recorrido BFS", command=self.gui.seccion_bfs)
        menu_e.add_command(label="Torres de Hanói", command=self.gui.seccion_hanoi)
        menu_e.add_command(label="Rutas Cortas Dijkstra", command=self.gui.seccion_dijkstra)
        menu_e.add_command(label="Árbol Mínimo Prim", command=self.gui.seccion_prim)
        menu_e.add_command(label="Árbol Mínimo Kruskal", command=self.gui.seccion_kruskal)
        menu_e.add_command(label="Simulador de Ordenamiento", command=self.gui.seccion_ordenamiento)
        
        menu_e.add_separator()
        menu_e.add_command(label="Salir", command=self.root.quit)
        
        menu_bar.add_cascade(label="Seleccionar Estructura", menu=menu_e)
        self.root.config(menu=menu_bar)

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    root_window = tk.Tk()
    
    app = AppPrincipal(root_window)
    app.iniciar()