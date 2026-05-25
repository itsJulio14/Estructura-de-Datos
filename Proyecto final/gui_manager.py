import tkinter as tk
import threading                  # <-- AGREGAR AL INICIO PARA EVITAR QUE SE CONGELE LA VENTANA
from tkinter import messagebox
from tkinter import ttk  
from tkinter import filedialog  # <-- Para abrir archivos de la PC
from logica_lista import LogicaLista
from logica_pila import LogicaPila
from logica_string import LogicaString
from logica_lista_2d import LogicaLista2D
from logica_csv import LogicaCSV  # <-- NUEVA IMPORTACIÓN
from logica_bicola import LogicaBicola
from logica_cola import LogicaCola 
from logica_nodo import LogicaNodo
from logica_bfs import LogicaBFS
from logica_hanoi import LogicaHanoi
from logica_dijkstra import LogicaDijkstra
from logica_prim import LogicaPrim
from logica_kruskal import LogicaKruskal
from logica_ordenamiento import LogicaOrdenamiento

class InterfaceManager:
    def __init__(self, container):
        self.container = container
        self.l_lista = LogicaLista()
        self.l_pila = LogicaPila()
        self.l_string = LogicaString()
        self.l_lista_2d = LogicaLista2D()
        self.l_csv = LogicaCSV()  # <-- NUEVA INSTANCIA
        self.l_cola = LogicaCola() 
        self.l_bicola = LogicaBicola() 
        self.l_nodo = LogicaNodo()
        self.l_bfs = LogicaBFS()
        self.l_hanoi = LogicaHanoi()
        self.l_dijkstra = LogicaDijkstra()
        self.l_prim = LogicaPrim()
        self.l_kruskal = LogicaKruskal()
        self.l_sort = LogicaOrdenamiento()

    def limpiar_pantalla(self):
        for w in self.container.winfo_children(): w.destroy()

    def mostrar_resultado(self, texto):
        messagebox.showinfo("Resultado", str(texto))

    def seccion_inicio(self):
        self.limpiar_pantalla()
        
        # Contenedor principal para centrar absolutamente todo vertical y horizontalmente
        frame_portada = tk.Frame(self.container, bg="white")
        frame_portada.pack(expand=True, fill="both", pady=40)
        
        tk.Label(
            frame_portada, 
            text="PROYECTO FINAL", 
            font=("Arial", 26, "bold"), 
            fg="#0d6efd", 
            bg="white",
            justify="center"
        ).pack(pady=(10, 5))
        
        tk.Label(
            frame_portada, 
            text="Estructuras de Datos y Labolatorio", 
            font=("Arial", 14, "bold"), 
            fg="#495057", 
            bg="white",
            justify="center"
        ).pack(pady=(0, 25))
        
        canvas_linea = tk.Canvas(frame_portada, width=350, height=2, bg="#dee2e6", bd=0, highlightthickness=0)
        canvas_linea.pack(pady=10)
        
        tk.Label(
            frame_portada, 
            text="Universidad Autónoma de Zacatecas", 
            font=("Arial", 16, "bold"), 
            fg="#212529", 
            bg="white",
            justify="center"
        ).pack(pady=(15, 20))
        
        frame_detalles = tk.Frame(frame_portada, bg="white")
        frame_detalles.pack(pady=10)
        
        tk.Label(
            frame_detalles, 
            text="Docente: Jorge Alejandro Morgan Benita", 
            font=("Arial", 12, "italic"), 
            fg="#6c757d", 
            bg="white",
            justify="center"
        ).pack(pady=4)
        
        tk.Label(
            frame_detalles, 
            text="Alumno: Julio Lorenzo Aquino Ibarra", 
            font=("Arial", 13, "bold"), 
            fg="#212529", 
            bg="white",
            justify="center"
        ).pack(pady=4)
        
        tk.Label(
            frame_portada, 
            text="Mayo / 2025", 
            font=("Courier New", 11, "bold"), 
            fg="#868e96", 
            bg="white",
            justify="center"
        ).pack(side="bottom", pady=(30, 10))

    def seccion_lista(self):
        self.limpiar_pantalla()
        tk.Label(self.container, text="GESTIÓN DE LISTAS", font=("Arial", 18, "bold")).pack(pady=10)
        entrada = tk.Entry(self.container, width=50)
        entrada.insert(0, "12, 21, 16, 15, 20, 18, 6, 10, 12, 14, 15, 12") 
        entrada.pack(pady=5)
        tk.Button(self.container, text="Sacar Promedio", command=lambda: self.mostrar_resultado(self.l_lista.sacar_promedio(entrada.get()))).pack(fill="x", pady=2)
        tk.Button(self.container, text="Eliminar Repetidos", command=lambda: self.mostrar_resultado(self.l_lista.eliminar_repetidos(entrada.get()))).pack(fill="x", pady=2)
        tk.Button(self.container, text="Contar Elementos", command=lambda: self.mostrar_resultado(self.l_lista.contar_elementos(entrada.get()))).pack(fill="x", pady=2)
        tk.Button(self.container, text="Clasificar Mayor/Menor al Promedio", command=lambda: self.mostrar_resultado(self.l_lista.clasificar_por_promedio(entrada.get())), bg="#d1e7dd").pack(fill="x", pady=2)

    
    def seccion_string(self):
        self.limpiar_pantalla()
        tk.Label(self.container, text="GESTION DE STRINGS", font=("Arial", 18, "bold")).pack(pady=10)
        entrada = tk.Entry(self.container, width=50)
        entrada.insert(0, "Parangaricutirimicuaro")
        entrada.pack(pady=5)
        tk.Button(self.container, text="Contar Frecuencia de Caracteres", command=lambda: self.mostrar_resultado(self.l_string.contar_frecuencia_caracteres(entrada.get())), bg="#cff4fc").pack(fill="x", pady=5)

    def seccion_lista_2d(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="OPERACIONES CON LISTAS 2D", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        cuaderno = ttk.Notebook(self.container)
        cuaderno.pack(fill="both", expand=True, padx=10, pady=5)
        
        pestana_mult = tk.Frame(cuaderno, bg="white")
        pestana_busq = tk.Frame(cuaderno, bg="white")
        
        cuaderno.add(pestana_mult, text=" Multiplicacion ")
        cuaderno.add(pestana_busq, text="Busqueda de Elementos ")
       
        tk.Label(pestana_mult, text="Multiplicacion de Matrices", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        frame_inputs = tk.Frame(pestana_mult, bg="white")
        frame_inputs.pack()

        f_x = tk.Frame(frame_inputs, bg="white")
        f_x.pack(side="left", padx=15)
        tk.Label(f_x, text="Matriz X:", bg="white", font=("Arial", 10, "bold")).pack()
        txt_x = tk.Text(f_x, height=4, width=22)
        txt_x.insert("1.0", "5,6,13\n3,10,1\n2,11,3")
        txt_x.pack()

        f_y = tk.Frame(frame_inputs, bg="white")
        f_y.pack(side="left", padx=15)
        tk.Label(f_y, text="Matriz Y:", bg="white", font=("Arial", 10, "bold")).pack()
        txt_y = tk.Text(f_y, height=4, width=22)
        txt_y.insert("1.0", "1,2,17\n6,5,15\n3,11,12")
        txt_y.pack()

        tk.Button(pestana_mult, text="Calcular Producto (X * Y)", 
                  command=lambda: self.mostrar_resultado(self.l_lista_2d.multiplicar_matrices(txt_x.get("1.0", "end-1c"), txt_y.get("1.0", "end-1c"))), 
                  bg="#fff3cd", font=("Arial", 10, "bold")).pack(fill="x", pady=20, padx=40)

     
        tk.Label(pestana_busq, text="Búsqueda de Coordenadas", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        tk.Label(pestana_busq, text="Matriz donde buscar (filas separadas por ENTER):", bg="white").pack()
        txt_matriz_buscar = tk.Text(pestana_busq, height=6, width=35)
        txt_matriz_buscar.insert("1.0", "4,7,2,9,5,7\n1,3,7,6,8,0\n9,2,5,7,4,6\n8,7,1,3,7,2\n5,0,6,4,2,9\n7,8,9,2,1,7")
        txt_matriz_buscar.pack(pady=5)

        frame_num = tk.Frame(pestana_busq, bg="white")
        frame_num.pack(pady=10)
        tk.Label(frame_num, text="Número a buscar: ", bg="white", font=("Arial", 10, "bold")).pack(side="left")
        entrada_num = tk.Entry(frame_num, width=8, font=("Arial", 10))
        entrada_num.insert(0, "7")
        entrada_num.pack(side="left")

        tk.Button(pestana_busq, text="Ejecutar Búsqueda", 
                  command=lambda: self.mostrar_resultado(self.l_lista_2d.buscar_numero(txt_matriz_buscar.get("1.0", "end-1c"), entrada_num.get())), 
                  bg="#d1e7dd", font=("Arial", 10, "bold")).pack(fill="x", pady=10, padx=40)
        
    # NUEVA SECCIÓN PARA PROCESAR ARCHIVOS CSV
    def seccion_csv(self):
        self.limpiar_pantalla()
        tk.Label(self.container, text="ANÁLISIS ESTADÍSTICO DE CSV", font=("Arial", 18, "bold")).pack(pady=10)
        
        tk.Label(self.container, text="Ruta del archivo CSV:").pack(anchor="w", padx=20)
        
        entrada_ruta = tk.Entry(self.container, width=55)
        entrada_ruta.insert(0, "/Housing.csv") # Tu ruta original por defecto
        entrada_ruta.pack(pady=5, padx=20)

        def examinar_archivo():
            archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
            if archivo:
                entrada_ruta.delete(0, tk.END)
                entrada_ruta.insert(0, archivo)

        tk.Button(self.container, text="Buscar CSV en mi equipo", command=examinar_archivo).pack(pady=5)
        
        tk.Button(self.container, text="Calcular Métricas Estadísticas", 
                  command=lambda: self.mostrar_resultado(self.l_csv.analizar_csv(entrada_ruta.get())),
                  bg="#e2e3e5", fg="black").pack(fill="x", pady=15, padx=20)
        
    
    def seccion_cola(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ESTRUCTURA DE COLA ", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        cuaderno = ttk.Notebook(self.container)
        cuaderno.pack(fill="both", expand=True, padx=10, pady=5)
        
        pestana_basica = tk.Frame(cuaderno, bg="white")
        pestana_banco = tk.Frame(cuaderno, bg="white")
        
        cuaderno.add(pestana_basica, text=" Operaciones Basicas ")
        cuaderno.add(pestana_banco, text=" Simulador Banco ")

        # --- PESTAÑA 1: COLA BÁSICA ---
        tk.Label(pestana_basica, text="Fila Generica (First In, First Out)", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        entrada_fifo = tk.Entry(pestana_basica, width=30, font=("Arial", 11))
        entrada_fifo.pack(pady=5)
        
        tk.Button(pestana_basica, text="Enqueue (Agregar al Final)", 
                  command=lambda: self.mostrar_resultado(self.l_cola.enqueue(entrada_fifo.get())), bg="#e2e3e5").pack(fill="x", padx=40, pady=3)
        
        tk.Button(pestana_basica, text="Dequeue (Sacar del Frente)", 
                  command=lambda: self.mostrar_resultado(self.l_cola.dequeue()), bg="#f8d7da").pack(fill="x", padx=40, pady=3)
        
        tk.Button(pestana_basica, text="Ver Estado de la Cola", 
                  command=lambda: self.mostrar_resultado(self.l_cola.ver_cola())).pack(fill="x", padx=40, pady=3)

        # --- PESTAÑA 2: SIMULADOR BANCO ---
        tk.Label(pestana_banco, text="Sistema de Transacciones Bancarias", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        frame_monto = tk.Frame(pestana_banco, bg="white")
        frame_monto.pack(pady=5)
        tk.Label(frame_monto, text="Monto ($): ", bg="white", font=("Arial", 10, "bold")).pack(side="left")
        entrada_monto = tk.Entry(frame_monto, width=15, font=("Arial", 10))
        entrada_monto.insert(0, "500")
        entrada_monto.pack(side="left")
        
        tk.Button(pestana_banco, text="Ejecutar Retiro (retiro_w)", 
                  command=lambda: self.mostrar_resultado(self.l_cola.retiro_w(entrada_monto.get())), 
                  bg="#f8d7da").pack(fill="x", padx=40, pady=4)
                  
        tk.Button(pestana_banco, text="Ejecutar Depósito (deposito_w)", 
                  command=lambda: self.mostrar_resultado(self.l_cola.deposito_w(entrada_monto.get())), 
                  bg="#d1e7dd").pack(fill="x", padx=40, pady=4)
                  
        tk.Button(pestana_banco, text="Ver Reporte de Saldos y Turnos", 
                  command=lambda: self.mostrar_resultado(self.l_cola.ver_estado_banco()), 
                  bg="#cff4fc").pack(fill="x", padx=40, pady=4)
        
    def seccion_bicola(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ESTRUCTURA DE BICOLA ", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        cuaderno = ttk.Notebook(self.container)
        cuaderno.pack(fill="both", expand=True, padx=10, pady=5)
        
        pestana_basica = tk.Frame(cuaderno, bg="white")
        pestana_banco = tk.Frame(cuaderno, bg="white")
        pestana_tiempo = tk.Frame(cuaderno, bg="white")
        
        cuaderno.add(pestana_basica, text="Operaciones Doble Extremo")
        cuaderno.add(pestana_banco, text="Banco Simulador")
        cuaderno.add(pestana_tiempo, text="Simulacion Tiempos")

        
        tk.Label(pestana_basica, text="Entrada de datos:", font=("Arial", 10, "bold"), bg="white").pack(pady=5)
        entrada_bi = tk.Entry(pestana_basica, width=30, font=("Arial", 11))
        entrada_bi.pack(pady=5)
        
        frame_botones = tk.Frame(pestana_basica, bg="white")
        frame_botones.pack(pady=10)
        
        frame_izq = tk.LabelFrame(frame_botones, text="Extremo Izquierdo (Frente)", bg="white", padx=10, pady=10)
        frame_izq.pack(side="left", padx=10)
        tk.Button(frame_izq, text="Enqueue Izq", command=lambda: self.mostrar_resultado(self.l_bicola.UI_enque_izq(entrada_bi.get())), bg="#e2e3e5", width=12).pack(pady=2)
        tk.Button(frame_izq, text="Dequeue Izq", command=lambda: self.mostrar_resultado(self.l_bicola.UI_deque_izq()), bg="#f8d7da", width=12).pack(pady=2)

        frame_der = tk.LabelFrame(frame_botones, text="Extremo Derecho (Final)", bg="white", padx=10, pady=10)
        frame_der.pack(side="right", padx=10)
        tk.Button(frame_der, text="Enqueue Der", command=lambda: self.mostrar_resultado(self.l_bicola.UI_enque_der(entrada_bi.get())), bg="#e2e3e5", width=12).pack(pady=2)
        tk.Button(frame_der, text="Dequeue Der", command=lambda: self.mostrar_resultado(self.l_bicola.UI_deque_der()), bg="#f8d7da", width=12).pack(pady=2)
        
        tk.Button(pestana_basica, text="Ver Estado de la bicola", command=lambda: self.mostrar_resultado(self.l_bicola.ver_bicola()), width=25).pack(pady=15)

        tk.Label(pestana_banco, text="Sistema de Turnos Cruzados", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        frame_monto = tk.Frame(pestana_banco, bg="white")
        frame_monto.pack(pady=5)
        tk.Label(frame_monto, text="Monto ($): ", bg="white", font=("Arial", 10, "bold")).pack(side="left")
        entrada_monto = tk.Entry(frame_monto, width=15, font=("Arial", 10))
        entrada_monto.insert(0, "500")
        entrada_monto.pack(side="left")
        
        tk.Button(pestana_banco, text="Retiro", 
                  command=lambda: self.mostrar_resultado(self.l_bicola.head_retiro(entrada_monto.get())), 
                  bg="#f8d7da").pack(fill="x", padx=40, pady=4)
                  
        tk.Button(pestana_banco, text="Depósito", 
                  command=lambda: self.mostrar_resultado(self.l_bicola.tail_deposito(entrada_monto.get())), 
                  bg="#d1e7dd").pack(fill="x", padx=40, pady=4)
                  
        tk.Button(pestana_banco, text="Ver Reporte Saldos", 
                  command=lambda: self.mostrar_resultado(self.l_bicola.ver_estado_banco()), 
                  bg="#cff4fc").pack(fill="x", padx=40, pady=4)

        tk.Button(pestana_banco, text="Reiniciar Simulacion del banco", 
                  command=lambda: [self.l_bicola.inicializar_banco(), self.mostrar_resultado("Banco restablecido a saldos iniciales")], 
                  bg="#fff3cd").pack(fill="x", padx=40, pady=4)

        tk.Label(pestana_tiempo, text="Algoritmo de Reordenamiento y Vaciado", font=("Arial", 12, "bold"), bg="white").pack(pady=5)
        
        lbl_info = tk.Label(pestana_tiempo, text="Peticiones: (1,0), (2,2), (3,4), (4,6), (5,12) | Límite Máx Inicial = 10", bg="#f8f9fa", font=("Arial", 9, "italic"))
        lbl_info.pack(fill="x", padx=40, pady=2)
        
        btn_run = tk.Button(pestana_tiempo, text="Ejecutar Simulación de Tiempo", bg="#d1e7dd", font=("Arial", 10, "bold"),
                            command=lambda: ejecutar_y_mostrar_logs())
        btn_run.pack(fill="x", padx=40, pady=5)
        
        txt_logs = tk.Text(pestana_tiempo, bg="#212529", fg="#f8f9fa", font=("Consolas", 9), wrap="word")
        txt_logs.pack(fill="both", expand=True, padx=20, pady=5)
        
        def ejecutar_y_mostrar_logs():
            txt_logs.delete("1.0", tk.END)
            logs = self.l_bicola.ejecutar_simulacion_tiempo()
            txt_logs.insert(tk.END, logs)

    
    def seccion_pila(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ESTRUCTURA DE PILA", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        cuaderno = ttk.Notebook(self.container)
        cuaderno.pack(fill="both", expand=True, padx=10, pady=5)
        
        pestana_basica = tk.Frame(cuaderno, bg="white")
        pestana_ventas = tk.Frame(cuaderno, bg="white")
        
        cuaderno.add(pestana_basica, text="Operaciones LIFO")
        cuaderno.add(pestana_ventas, text="Ordenador de Ventas")

        tk.Label(pestana_basica, text="Pila ", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        entrada_lifo = tk.Entry(pestana_basica, width=30, font=("Arial", 11))
        entrada_lifo.pack(pady=5)
        
        tk.Button(pestana_basica, text="Push", 
                  command=lambda: self.mostrar_resultado(self.l_pila.push_general(entrada_lifo.get())), bg="#e2e3e5").pack(fill="x", padx=40, pady=3)
        
        tk.Button(pestana_basica, text="Pop", 
                  command=lambda: self.mostrar_resultado(self.l_pila.pop_general()), bg="#f8d7da").pack(fill="x", padx=40, pady=3)
        
        tk.Button(pestana_basica, text="Ver Estado de la Pila", 
                  command=lambda: self.mostrar_resultado(self.l_pila.ver_pila_general())).pack(fill="x", padx=40, pady=3)

        tk.Label(pestana_ventas, text="Algoritmo: Clasificacion de Menor a Mayor en Pila", font=("Arial", 12, "bold"), bg="white").pack(pady=5)
        
        frame_controles = tk.Frame(pestana_ventas, bg="white")
        frame_controles.pack(pady=5)
        
        tk.Label(frame_controles, text="Selecciona Categoria: ", bg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        
        combo_categoria = ttk.Combobox(frame_controles, values=["Dulces", "Conservas", "Bebidas"], state="readonly", width=12)
        combo_categoria.current(0)
        combo_categoria.pack(side="left", padx=5)
        
        tk.Button(frame_controles, text="Ordenar", bg="#d1e7dd", font=("Arial", 9, "bold"),
                  command=lambda: procesar_ordenamiento()).pack(side="left", padx=5)
                  
        tk.Button(frame_controles, text="Ver Tablas Originales", bg="#cff4fc",
                  command=lambda: mostrar_tablas_originales()).pack(side="left", padx=5)
        
        txt_consola = tk.Text(pestana_ventas, bg="#212529", fg="#f8f9fa", font=("Consolas", 9), wrap="word")
        txt_consola.pack(fill="both", expand=True, padx=20, pady=5)
        
        def procesar_ordenamiento():
            cat = combo_categoria.get()
            txt_consola.delete("1.0", tk.END)
            resultado_logs = self.l_pila.ordenar_a_pila(cat)
            txt_consola.insert(tk.END, resultado_logs)
            
        def mostrar_tablas_originales():
            txt_consola.delete("1.0", tk.END)
            tablas = self.l_pila.obtener_reporte_completo()
            txt_consola.insert(tk.END, tablas)

#-------------------------------------------------------------------------------------------------------------
    def seccion_nodo(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ESTRUCTURA DE ARBOL BINARIO", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        cuaderno = ttk.Notebook(self.container)
        cuaderno.pack(fill="both", expand=True, padx=10, pady=5)
        
        pestana_construccion = tk.Frame(cuaderno, bg="white")
        pestana_visualizacion = tk.Frame(cuaderno, bg="white")
        
        cuaderno.add(pestana_construccion, text="Construir Árbol ")
        cuaderno.add(pestana_visualizacion, text="Recorridos y Gráfico ")

        frame_raiz = tk.LabelFrame(pestana_construccion, text=" 1. Nodo Raiz Inicial ", bg="white", font=("Arial", 10, "bold"))
        frame_raiz.pack(fill="x", padx=20, pady=10)
        
        tk.Label(frame_raiz, text="Valor de la Raiz:", bg="white").pack(side="left", padx=10, pady=10)
        entrada_raiz = tk.Entry(frame_raiz, width=15, font=("Arial", 10))
        entrada_raiz.pack(side="left", padx=10)
        tk.Button(frame_raiz, text="Establecer Raiz", bg="#cff4fc",
                  command=lambda: self.mostrar_resultado(self.l_nodo.establecer_raiz(entrada_raiz.get()))).pack(side="left", padx=10)

        frame_hijos = tk.LabelFrame(pestana_construccion, text=" 2. Agregar Hijos (Izquierdo / Derecho) ", bg="white", font=("Arial", 10, "bold"))
        frame_hijos.pack(fill="x", padx=20, pady=10)
        
        grid_frame = tk.Frame(frame_hijos, bg="white")
        grid_frame.pack(pady=10, padx=10)
        
        tk.Label(grid_frame, text="Valor del padre existente:", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        entrada_padre = tk.Entry(grid_frame, width=15, font=("Arial", 10))
        entrada_padre.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(grid_frame, text="Valor del Nuevo Nodo:", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        entrada_nuevo = tk.Entry(grid_frame, width=15, font=("Arial", 10))
        entrada_nuevo.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(grid_frame, text="Posicion/Lado:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        combo_lado = ttk.Combobox(grid_frame, values=["Izquierdo (nodoIzq)", "Derecho (nodoDer)"], state="readonly", width=18)
        combo_lado.current(0)
        combo_lado.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(frame_hijos, text="Insertar Nodo hijo", bg="#d1e7dd", font=("Arial", 10, "bold"),
                  command=lambda: ejecutar_insercion_hijo()).pack(fill="x", padx=40, pady=10)

        tk.Button(pestana_construccion, text="Vaciar Todo el arbol", bg="#f8d7da", fg="black",
                  command=lambda: self.mostrar_resultado(self.l_nodo.limpiar_arbol())).pack(pady=10)

        def ejecutar_insercion_hijo():
            lado_limpio = "izq" if "Izquierdo" in combo_lado.get() else "der"
            res = self.l_nodo.agregar_hijo(entrada_padre.get(), entrada_nuevo.get(), lado_limpio)
            self.mostrar_resultado(res)

       
        frame_botones_rec = tk.Frame(pestana_visualizacion, bg="white")
        frame_botones_rec.pack(pady=10)
        
        tk.Button(frame_botones_rec, text="Ver Preorden", width=14, bg="#e2e3e5",
                  command=lambda: abrir_ventana_recorrido("Preorden")).pack(side="left", padx=5)
        tk.Button(frame_botones_rec, text="Ver Inorden", width=14, bg="#e2e3e5",
                  command=lambda: abrir_ventana_recorrido("Inorden")).pack(side="left", padx=5)
        tk.Button(frame_botones_rec, text="Ver Postorden", width=14, bg="#e2e3e5",
                  command=lambda: abrir_ventana_recorrido("Postorden")).pack(side="left", padx=5)
        
        tk.Button(pestana_visualizacion, text="Formato Gráfico Textual", bg="#fff3cd", font=("Arial", 9, "bold"),
                  command=lambda: refrescar_lienzo_grafico()).pack(fill="x", padx=40, pady=5)
        
        txt_arbol = tk.Text(pestana_visualizacion, bg="#212529", fg="#7bf1a8", font=("Consolas", 12, "bold"), wrap="none")
        txt_arbol.pack(fill="both", expand=True, padx=20, pady=10)

        def abrir_ventana_recorrido(tipo):
            """Genera una sub-ventana flotante independiente (Toplevel) para los recorridos"""
            ventana_rec = tk.Toplevel(self.container)
            ventana_rec.title(f"Recorrido: {tipo}")
            ventana_rec.geometry("400x120")
            ventana_rec.config(bg="white")
            
            tk.Label(ventana_rec, text=f"ORDEN EN {tipo.upper()}:", font=("Arial", 11, "bold"), bg="white").pack(pady=10)
            cadena_orden = self.l_nodo.obtener_recorrido(tipo)
            
            lbl_res = tk.Label(ventana_rec, text=cadena_orden, font=("Consolas", 11), fg="#0d6efd", bg="#f8f9fa", wraplength=360, relief="groove", pady=10)
            lbl_res.pack(fill="x", padx=20)

        def refrescar_lienzo_grafico():
            txt_arbol.delete("1.0", tk.END)
            grafico = self.l_nodo.obtener_grafico_texto()
            txt_arbol.insert(tk.END, grafico)

#-------------------------------------------------------------------------------------------------------------
    def seccion_bfs(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="Recorrido BFS", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_principal = tk.Frame(self.container, bg="white")
        frame_principal.pack(fill="both", expand=True, padx=15, pady=5)
        
        frame_controles = tk.LabelFrame(frame_principal, text="Datos de ejecucion ", bg="white", font=("Arial", 10, "bold"))
        frame_controles.pack(fill="x", pady=5, padx=5)
        
        tk.Label(frame_controles, text="Nodo raiz inicial:", bg="white", font=("Arial", 10)).pack(side="left", padx=10, pady=10)
        
        entrada_raiz = tk.Entry(frame_controles, width=6, font=("Arial", 11, "bold"), justify="center")
        entrada_raiz.insert(0, "A")
        entrada_raiz.pack(side="left", padx=5)
        
        tk.Button(frame_controles, text="Correr Algoritmo BFS", bg="#d1e7dd", font=("Arial", 9, "bold"),
                  command=lambda: ejecutar_simulacion()).pack(side="left", padx=15)
                  
        tk.Button(frame_controles, text="Mostrar Grafo Base", bg="#cff4fc", font=("Arial", 9),
                  command=lambda: mostrar_grafo_original()).pack(side="left", padx=5)
        
        tk.Label(frame_principal, text="Consola de Seguimiento):", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
        
        txt_consola = tk.Text(frame_principal, bg="#212529", fg="#f8f9fa", font=("Consolas", 10), wrap="word")
        txt_consola.pack(fill="both", expand=True, pady=5)
        
        txt_consola.insert(tk.END, self.l_bfs.obtener_conexiones_texto())

        def ejecutar_simulacion():
            txt_consola.delete("1.0", tk.END)
            logs = self.l_bfs.ejecutar_bfs(entrada_raiz.get())
            txt_consola.insert(tk.END, logs)

        def mostrar_grafo_original():
            txt_consola.delete("1.0", tk.END)
            txt_consola.insert(tk.END, self.l_bfs.obtener_conexiones_texto())

#-------------------------------------------------------------------------------------------------------------
    def seccion_hanoi(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="RESOLVEDOR GRÁFICO - TORRES DE HANOI", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_controles = tk.LabelFrame(self.container, text=" Panel de Control ", bg="white", font=("Arial", 10, "bold"))
        frame_controles.pack(fill="x", padx=15, pady=5)
        
        tk.Label(frame_controles, text="Cantidad de Discos (1-7):", bg="white").pack(side="left", padx=10, pady=10)
        spin_discos = tk.Spinbox(frame_controles, from_=1, to=7, width=5, font=("Arial", 10, "bold"), justify="center")
        spin_discos.delete(0, "end")
        spin_discos.insert(0, "4")  
        spin_discos.pack(side="left", padx=5)

        # Botones de Acción directos
        btn_preparar = tk.Button(frame_controles, text="Preparar Torres", bg="#cff4fc", font=("Arial", 9, "bold"), command=lambda: preparar_lienzo())
        btn_preparar.pack(side="left", padx=15)

        btn_resolver = tk.Button(frame_controles, text="Resolver Animación", bg="#d1e7dd", font=("Arial", 9, "bold"), command=lambda: iniciar_animacion_reloj())
        btn_resolver.pack(side="left", padx=5)
        
        # Split para Canvas y Consola lateral
        frame_split = tk.Frame(self.container, bg="white")
        frame_split.pack(fill="both", expand=True, padx=15, pady=5)
        
        canvas = tk.Canvas(frame_split, bg="#f8f9fa", bd=2, relief="ridge", width=550, height=300)
        canvas.pack(side="left", fill="both", expand=True, padx=5)
        
        txt_pasos = tk.Text(frame_split, bg="#212529", fg="#f8f9fa", font=("Consolas", 10), width=38)
        txt_pasos.pack(side="right", fill="both", padx=5)

        # --- MOTOR GRÁFICO DEL CANVAS ---
        def dibujar_estado_actual():
            canvas.delete("all")
            
            ancho_canvas = canvas.winfo_width() if canvas.winfo_width() > 1 else 550
            alto_canvas = canvas.winfo_height() if canvas.winfo_height() > 1 else 300
            
            base_y = alto_canvas - 40
            posiciones_x = {
                'A': ancho_canvas * 0.22,
                'B': ancho_canvas * 0.50,
                'C': ancho_canvas * 0.78
            }
            
            # Dibujar Base de Madera
            canvas.create_rectangle(20, base_y, ancho_canvas - 20, base_y + 15, fill="#8B5A2B", outline="#5c3a1a")
            
            # Dibujar Postes
            for nombre, cx in posiciones_x.items():
                canvas.create_rectangle(cx - 5, base_y - 180, cx + 5, base_y, fill="#D3D3D3", outline="#a8a8a8")
                canvas.create_text(cx, base_y + 25, text=f"Torre {nombre}", font=("Arial", 11, "bold"))
            
            # Dibujar Discos
            colores_discos = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF0", "#FFAF33"]
            alto_disco = 18
            
            for torre_id, discos in self.l_hanoi.torres.items():
                cx = posiciones_x[torre_id]
                for index, tamano_disco in enumerate(discos):
                    ancho_disco = tamano_disco * 22 + 35
                    y1 = base_y - (index * alto_disco) - alto_disco
                    y2 = base_y - (index * alto_disco)
                    x1 = cx - (ancho_disco / 2)
                    x2 = cx + (ancho_disco / 2)
                    
                    color = colores_discos[(tamano_disco - 1) % len(colores_discos)]
                    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=1)
                    canvas.create_text(cx, (y1 + y2)/2, text=str(tamano_disco), font=("Arial", 9, "bold"), fill="black")

            # Refrescar la bitácora textual derecha
            txt_pasos.delete("1.0", tk.END)
            txt_pasos.insert(tk.END, "\n".join(self.l_hanoi.historial_pasos))
            txt_pasos.see(tk.END)

        def preparar_lienzo():
            self.l_hanoi.en_ejecucion = False
            n = int(spin_discos.get())
            self.l_hanoi.inicializar_juego(n)
            dibujar_estado_actual()

        # --- ANIMACIÓN DIRIGIDA POR TICK DE RELOJ NATIVO (1 SEGUNDO) ---
        def iniciar_animacion_reloj():
            if self.l_hanoi.en_ejecucion:
                return
            
            self.l_hanoi.en_ejecucion = True
            # Calculamos la lista de tuplas de movimientos en el backend de un solo golpe
            movimientos = self.l_hanoi.generar_plan_resolucion()
            
            # Disparamos la cola de reproducción controlada por la ventana
            animar_paso_a_paso(movimientos, 0)

        def animar_paso_a_paso(lista_movimientos, indice):
            # Si el usuario reseteó el juego o terminamos la lista
            if not self.l_hanoi.en_ejecucion:
                return
                
            if indice < len(lista_movimientos):
                origen, destino = lista_movimientos[indice]
                self.l_hanoi.mover_disco_en_estado(origen, destino)
                dibujar_estado_actual()
                
                self.container.after(1000, lambda: animar_paso_a_paso(lista_movimientos, indice + 1))
            else:
                self.l_hanoi.historial_pasos.append("\n🏁 ¡Rompecabezas resuelto con éxito!")
                dibujar_estado_actual()
                self.l_hanoi.en_ejecucion = False

        # Forzar dibujo en la carga inicial de la sección
        self.container.after(100, preparar_lienzo)


#-------------------------------------------------------------------------------------------------------------
    def seccion_dijkstra(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="RUTA MINIMA - ALGORITMO DE DIJKSTRA", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_controles = tk.LabelFrame(self.container, text="Datos del grafo ", bg="white", font=("Arial", 10, "bold"))
        frame_controles.pack(fill="x", padx=15, pady=5)
        
        tk.Label(frame_controles, text="Nodo de Inicio (0-7):", bg="white", font=("Arial", 10)).pack(side="left", padx=10, pady=10)
        
        entrada_inicio = tk.Entry(frame_controles, width=5, font=("Arial", 11, "bold"), justify="center")
        entrada_inicio.insert(0, "0")
        entrada_inicio.pack(side="left", padx=5)
        
        tk.Button(frame_controles, text="Calcular Caminos Cortos", bg="#d1e7dd", font=("Arial", 9, "bold"),
                  command=lambda: ejecutar_dijkstra_consola()).pack(side="left", padx=15)
                  
        tk.Button(frame_controles, text="Ver Estructura del Grafo", bg="#cff4fc", font=("Arial", 9),
                  command=lambda: mostrar_grafo_base()).pack(side="left", padx=5)
        
        tk.Label(self.container, text="Consola de Seguimiento:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=2)
        
        txt_consola = tk.Text(self.container, bg="#1e1e1e", fg="#98ff98", font=("Consolas", 10), wrap="none")
        txt_consola.pack(fill="both", expand=True, padx=15, pady=5)
        
        txt_consola.insert(tk.END, self.l_dijkstra.obtener_grafo_texto())

        def ejecutar_dijkstra_consola():
            txt_consola.delete("1.0", tk.END)
            try:
                nodo_start = int(entrada_inicio.get().strip())
                logs = self.l_dijkstra.ejecutar_y_reconstruir(nodo_start)
                txt_consola.insert(tk.END, logs)
            except ValueError:
                txt_consola.insert(tk.END, "Error: Por favor ingresa un número entero válido entre 0 y 7.")

        def mostrar_grafo_base():
            txt_consola.delete("1.0", tk.END)
            txt_consola.insert(tk.END, self.l_dijkstra.obtener_grafo_texto())

#------------------------------------------------------------------------------------------------------------------
    def seccion_prim(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ARBOL DE EXPANSIÓN MINIMA - ALGORITMO DE PRIM", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_controles = tk.LabelFrame(self.container, text="Datos para el algoritm", bg="white", font=("Arial", 10, "bold"))
        frame_controles.pack(fill="x", padx=15, pady=5)
        
        tk.Label(frame_controles, text="Nodo Inicial (Ej: Root, 0, 1):", bg="white", font=("Arial", 10)).pack(side="left", padx=10, pady=10)
        
        entrada_inicio = tk.Entry(frame_controles, width=8, font=("Arial", 11, "bold"), justify="center")
        entrada_inicio.insert(0, "Root")  
        entrada_inicio.pack(side="left", padx=5)
        
        tk.Button(frame_controles, text="Generar MST Mínimo", bg="#d1e7dd", font=("Arial", 9, "bold"),
                  command=lambda: ejecutar_prim_consola()).pack(side="left", padx=15)
                  
        tk.Button(frame_controles, text="Ver Grafo Completo", bg="#cff4fc", font=("Arial", 9),
                  command=lambda: mostrar_grafo_prim_base()).pack(side="left", padx=5)
        
        tk.Label(self.container, text="Consola de Seguimiento:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=2)
        
        txt_consola = tk.Text(self.container, bg="#1e1e1e", fg="#ffd700", font=("Consolas", 10), wrap="none")
        txt_consola.pack(fill="both", expand=True, padx=15, pady=5)
        
        txt_consola.insert(tk.END, self.l_prim.obtener_grafo_texto())

        def ejecutar_prim_consola():
            txt_consola.delete("1.0", tk.END)
            nodo_start = entrada_inicio.get().strip()
            logs = self.l_prim.ejecutar_prim_completo(nodo_start)
            txt_consola.insert(tk.END, logs)

        def mostrar_grafo_prim_base():
            txt_consola.delete("1.0", tk.END)
            txt_consola.insert(tk.END, self.l_prim.obtener_grafo_texto())

#-------------------------------------------------------------------------------------------------------------
    def seccion_kruskal(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="ARBOL DE EXPANION MINIMA - ALGORITMO DE KRUSKAL", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_controles = tk.LabelFrame(self.container, text="Operaciones del Grafo", bg="white", font=("Arial", 10, "bold"))
        frame_controles.pack(fill="x", padx=15, pady=5)
        
        tk.Button(frame_controles, text="Generar MST por Aristas", bg="#d1e7dd", font=("Arial", 9, "bold"),
                  command=lambda: ejecutar_kruskal_consola()).pack(side="left", padx=15, pady=10)
                  
        tk.Button(frame_controles, text="Ver Estructura Base", bg="#cff4fc", font=("Arial", 9),
                  command=lambda: mostrar_grafo_kruskal_base()).pack(side="left", padx=5)
        
        tk.Label(self.container, text="Consola de Seguimiento :", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=2)
        
        txt_consola = tk.Text(self.container, bg="#1e1e1e", fg="#00ffff", font=("Consolas", 10), wrap="none")
        txt_consola.pack(fill="both", expand=True, padx=15, pady=5)
        
        txt_consola.insert(tk.END, self.l_kruskal.obtener_grafo_texto())

        def ejecutar_kruskal_consola():
            txt_consola.delete("1.0", tk.END)
            logs = self.l_kruskal.ejecutar_kruskal_completo()
            txt_consola.insert(tk.END, logs)

        def mostrar_grafo_kruskal_base():
            txt_consola.delete("1.0", tk.END)
            txt_consola.insert(tk.END, self.l_kruskal.obtener_grafo_texto())

#-------------------------------------------------------------------------------------------------------------
    def seccion_ordenamiento(self):
        self.limpiar_pantalla()
        
        tk.Label(self.container, text="VISUALIZADOR DE METODOS DE ORDENAMIENTO", font=("Arial", 16, "bold"), bg="white").pack(pady=5)
        
        frame_lista = tk.LabelFrame(self.container, text="Daros del arreglo", bg="white", font=("Arial", 10, "bold"))
        frame_lista.pack(fill="x", padx=15, pady=5)
        
        tk.Label(frame_lista, text="Elementos (separados por comas):", bg="white").pack(anchor="w", padx=10, pady=2)
        
        entrada_lista = tk.Entry(frame_lista, font=("Consolas", 11), bg="#f8f9fa")
        entrada_lista.insert(0, ", ".join(map(str, self.l_sort.lista_base)))
        entrada_lista.pack(fill="x", padx=10, pady=5)
        
        frame_btn_lista = tk.Frame(frame_lista, bg="white")
        frame_btn_lista.pack(fill="x", padx=10, pady=5)
        
        def aplicar_cambios():
            exito, msg = self.l_sort.actualizar_lista_desde_texto(entrada_lista.get())
            self.mostrar_resultado(msg)

        def aleatorizar():
            msg = self.l_sort.generar_lista_aleatoria(12)
            entrada_lista.delete(0, tk.END)
            entrada_lista.insert(0, ", ".join(map(str, self.l_sort.lista_base)))
            self.mostrar_resultado(msg)

        tk.Button(frame_btn_lista, text="Aplicar cambios", bg="#cff4fc", font=("Arial", 9), command=aplicar_cambios).pack(side="left", padx=5)
        tk.Button(frame_btn_lista, text="Generar lista random", bg="#fff3cd", font=("Arial", 9), command=aleatorizar).pack(side="left", padx=5)

        frame_algoritmos = tk.LabelFrame(self.container, text=" Selecciona el Algoritmo", bg="white", font=("Arial", 10, "bold"))
        frame_algoritmos.pack(fill="both", expand=True, padx=15, pady=10)
        
        f_grid = tk.Frame(frame_algoritmos, bg="white")
        f_grid.pack(expand=True)

        tk.Button(f_grid, text="Bubble Sort", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Bubble Sort", self.l_sort.simular_bubble())).grid(row=0, column=0, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Selection Sort", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Selection Sort", self.l_sort.simular_selection())).grid(row=0, column=1, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Insertion Sort", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Insertion Sort", self.l_sort.simular_insertion())).grid(row=0, column=2, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Merge Sort", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Merge Sort", self.l_sort.simular_merge())).grid(row=1, column=0, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Quick Sort (Central)", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Quick Sort (Central)", self.l_sort.simular_quick(False))).grid(row=1, column=1, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Quick Sort (Random)", width=22, height=2, bg="#f8f9fa", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Quick Sort (Random)", self.l_sort.simular_quick(True))).grid(row=1, column=2, padx=10, pady=10)
                  
        tk.Button(f_grid, text="Counting Sort", width=22, height=2, bg="#d1e7dd", font=("Arial", 10, "bold"),
                  command=lambda: levantar_popup_simulador("Counting Sort", self.l_sort.simular_counting())).grid(row=2, column=0, columnspan=3, sticky="we", padx=10, pady=10)

        
        def levantar_popup_simulador(nombre_algoritmo, fotogramas):
            # Crear subventana independiente
            pop = tk.Toplevel(self.container)
            pop.title(f"Simulando: {nombre_algoritmo}")
            pop.geometry("600x420")
            pop.config(bg="white")
            pop.resizable(False, False)
            
            tk.Label(pop, text=f"Renderizado Animado: {nombre_algoritmo}", font=("Arial", 12, "bold"), bg="white", fg="#0d6efd").pack(pady=5)
            
            canvas_sort = tk.Canvas(pop, bg="#1e1e1e", bd=2, relief="sunken")
            canvas_sort.pack(fill="both", expand=True, padx=20, pady=5)
            
            lbl_paso = tk.Label(pop, text="Cargando fotogramas...", font=("Arial", 10, "italic"), bg="white")
            lbl_paso.pack(pady=5)
            
            pop_activo = {"estado": True}
            def al_cerrar_popup():
                pop_activo["estado"] = False
                pop.destroy()
            pop.protocol("WM_DELETE_WINDOW", al_cerrar_popup)

            def reproducir_fotograma(indice):
                if not pop_activo["estado"]:
                    return
                    
                if indice < len(fotogramas):
                    lbl_paso.config(text=f"Pasos del algoritmo: {indice + 1} / {len(fotogramas)}")
                    
                    canvas_sort.delete("all")
                    lista_actual, idx1, idx2 = fotogramas[indice]
                    
                    c_width = 560
                    c_height = 280
                    
                    num_elementos = len(lista_actual)
                    ancho_barra = (c_width - 40) / num_elementos
                    
                    max_valor = max(lista_actual) if max(lista_actual) > 0 else 1
                    
                    for k, val in enumerate(lista_actual):
                        altura_barra = (val / max_valor) * (c_height - 60)
                        
                        x1 = 20 + (k * ancho_barra) + 2
                        y1 = c_height - 30 - altura_barra
                        x2 = x1 + ancho_barra - 4
                        y2 = c_height - 30
                        
                        if k == idx1 or k == idx2:
                            color = "#ffc107"
                        else:
                            color = "#0dcaf0"
                            
                        canvas_sort.create_rectangle(x1, y1, x2, y2, fill=color, outline="white", width=1)
                        canvas_sort.create_text((x1 + x2)/2, y1 - 10, text=str(val), font=("Consolas", 9, "bold"), fill="white")
                        canvas_sort.create_text((x1 + x2)/2, y2 + 12, text=str(k), font=("Consolas", 8), fill="#a8a8a8")

                    pop.after(400, lambda: reproducir_fotograma(indice + 1))
                else:
                    lbl_paso.config(text=f"¡Arreglo Ordenado con éxito! ({len(fotogramas)} pasos totales).")
                    canvas_sort.update()

            pop.after(100, lambda: reproducir_fotograma(0))