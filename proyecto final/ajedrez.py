import tkinter as tk
from collections import defaultdict
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import random

class Casilla:
    def __init__(self, fila, col):
        self.fila = fila
        self.col = col
        self.pieza = None
        self.color = "#F0D9B5" if (fila + col) % 2 == 0 else "#B58863"

class GrafoAjedrez:
    def __init__(self):
        self.tablero = [[Casilla(fila, col) for col in range(8)] for fila in range(8)]
        self.grafo = defaultdict(list)
        self.crear_conexiones()
        self.inicializar_piezas()
        self.turno_blancas = True
        self.historial_movimientos = []
        self.ahogado = False

    def crear_conexiones(self):
        for fila in range(8):
            for col in range(8):
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if df == 0 and dc == 0:
                            continue
                        nf, nc = fila + df, col + dc
                        if 0 <= nf < 8 and 0 <= nc < 8:
                            self.grafo[(fila, col)].append((nf, nc))
                             #liberia de direcciones ya que las f y c tineen lugareas vecinos donde las piezas pueden moverse 
    def inicializar_piezas(self):
        piezas_negras = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        piezas_blancas = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        for col in range(8):
            self.tablero[1][col].pieza = "♟"
            self.tablero[6][col].pieza = "♙"
            self.tablero[0][col].pieza = piezas_negras[col]
            self.tablero[7][col].pieza = piezas_blancas[col]

    def es_pieza_aliada(self, pieza):
        if self.turno_blancas:
            return pieza in ["♙", "♖", "♘", "♗", "♕", "♔"]
        return pieza in ["♟", "♜", "♞", "♝", "♛", "♚"]

    def obtener_movimientos_validos(self, fila, col):
        movimientos = [] #guardar movimientos validos
        pieza = self.tablero[fila][col].pieza
        if not pieza or not self.es_pieza_aliada(pieza):
            return []

        if pieza == "♙":
            if fila > 0 and not self.tablero[fila-1][col].pieza:  
                movimientos.append((fila-1, col))
                if fila == 6 and not self.tablero[fila-2][col].pieza:
                    movimientos.append((fila-2, col))
            for dc in [-1, 1]: #calculc coolunma destino
                if 0 <= col+dc < 8 and fila > 0:#limites del tableo y el peon no puede capturar mas si ya lleglo a 0
                    target = self.tablero[fila-1][col+dc].pieza #para capturar 
                    if target and not self.es_pieza_aliada(target): # target es igual a nada si no se cumple la condicion 
                        movimientos.append((fila-1, col+dc))

        elif pieza == "♟":
            if fila < 7 and not self.tablero[fila+1][col].pieza: #que no este en la ultima fila
                movimientos.append((fila+1, col))
                if fila == 1 and not self.tablero[fila+2][col].pieza:
                    movimientos.append((fila+2, col))
            for dc in [-1, 1]:
                if 0 <= col+dc < 8 and fila < 7:#el peon no puede capturar si esta en la ultima fila 
                    target = self.tablero[fila+1][col+dc].pieza
                    if target and not self.es_pieza_aliada(target):
                        movimientos.append((fila+1, col+dc))

        elif pieza in ["♖", "♜"]:
            for df, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nf, nc = fila + df, col + dc  #d=cambio
                while 0 <= nf < 8 and 0 <= nc < 8: #dentro del tablerp
                    if not self.tablero[nf][nc].pieza:
                        movimientos.append((nf, nc))
                    elif not self.es_pieza_aliada(self.tablero[nf][nc].pieza):
                        movimientos.append((nf, nc))
                        break #no puede saltar piezas
                    else:  #pieza aliada
                        break
                    nf += df
                    nc += dc

        elif pieza in ["♗", "♝"]:
            for df, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                nf, nc = fila + df, col + dc
                while 0 <= nf < 8 and 0 <= nc < 8:
                    if not self.tablero[nf][nc].pieza:
                        movimientos.append((nf, nc))
                    elif not self.es_pieza_aliada(self.tablero[nf][nc].pieza):
                        movimientos.append((nf, nc))
                        break
                    else:
                        break
                    nf += df
                    nc += dc

        elif pieza in ["♕", "♛"]:
            for df, dc in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                nf, nc = fila + df, col + dc
                while 0 <= nf < 8 and 0 <= nc < 8:
                    if not self.tablero[nf][nc].pieza:
                        movimientos.append((nf, nc))
                    elif not self.es_pieza_aliada(self.tablero[nf][nc].pieza):
                        movimientos.append((nf, nc))
                        break
                    else:
                        break
                    nf += df
                    nc += dc

        elif pieza in ["♔", "♚"]:
            for df, dc in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                nf, nc = fila + df, col + dc
                if 0 <= nf < 8 and 0 <= nc < 8:
                    if not self.tablero[nf][nc].pieza or not self.es_pieza_aliada(self.tablero[nf][nc].pieza):
                        movimientos.append((nf, nc)) # if en lugar de while porque es una casilla

        elif pieza in ["♘", "♞"]:
            for df, dc in [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]:
                nf, nc = fila + df, col + dc
                if 0 <= nf < 8 and 0 <= nc < 8:
                    if not self.tablero[nf][nc].pieza or not self.es_pieza_aliada(self.tablero[nf][nc].pieza):
                        movimientos.append((nf, nc))

        return movimientos

    def hay_movimientos_legales(self):
        for fila in range(8):
            for col in range(8):
                pieza = self.tablero[fila][col].pieza
                if pieza and self.es_pieza_aliada(pieza):
                    if self.obtener_movimientos_validos(fila, col):
                        return True
        return False

    def es_ahogado(self):
        return not self.hay_movimientos_legales()

    def mover_pieza(self, f_orig, c_orig, f_dest, c_dest):
        pieza = self.tablero[f_orig][c_orig].pieza
        self.tablero[f_orig][c_orig].pieza = None
        self.tablero[f_dest][c_dest].pieza = pieza
        self.turno_blancas = not self.turno_blancas #si era turno de las blancas true y si no false y viseversa
        self.historial_movimientos.append((f_orig, c_orig, f_dest, c_dest))
        
        if self.es_ahogado():
            self.ahogado = True  #llama ahogado pa ver si hay mas  movimientos

    def obtener_estado_juego(self):
        valores = {"♙":1, "♟":1, "♖":5, "♜":5, "♘":3, "♞":3, 
                  "♗":3, "♝":3, "♕":9, "♛":9, "♔":0, "♚":0}
        
        blancas = sum(valores.get(cas.pieza, 0) for fila in self.tablero for cas in fila if cas.pieza in ["♙", "♖", "♘", "♗", "♕", "♔"])
        negras = sum(valores.get(cas.pieza, 0) for fila in self.tablero for cas in fila if cas.pieza in ["♟", "♜", "♞", "♝", "♛", "♚"])
        
        movilidad_blancas = sum(len(self.obtener_movimientos_validos(fila, col)) 
                             for fila in range(8) for col in range(8) 
                             if self.tablero[fila][col].pieza and self.tablero[fila][col].pieza in ["♙", "♖", "♘", "♗", "♕", "♔"])
                             #solo casillas con piezas blancass
          

        movilidad_negras = sum(len(self.obtener_movimientos_validos(fila, col)) 
                           for fila in range(8) for col in range(8) 
                           if self.tablero[fila][col].pieza and self.tablero[fila][col].pieza in ["♟", "♜", "♞", "♝", "♛", "♚"])
        

        #en el ajedrez el centro es muy importante por lo que tenemos que definirlo aqui tamabioe+

        centro = [(3,3), (3,4), (4,3), (4,4)]
        control_blancas = sum(1 for (f,c) in centro 
                          if any((f,c) in self.obtener_movimientos_validos(fila, col)  #comprueba si alguna pieza blanaca esta aqui
                               for fila in range(8) for col in range(8)  
                               if self.tablero[fila][col].pieza and self.tablero[fila][col].pieza in ["♙", "♖", "♘", "♗", "♕", "♔"]))
                                 #filtra 

        control_negras = sum(1 for (f,c) in centro 
                           if any((f,c) in self.obtener_movimientos_validos(fila, col) 
                                for fila in range(8) for col in range(8) 
                                if self.tablero[fila][col].pieza and self.tablero[fila][col].pieza in ["♟", "♜", "♞", "♝", "♛", "♚"]))
        
        rey_blanco_seguro = 1 if all(self.tablero[f][c].pieza not in ["♟", "♜", "♞", "♝", "♛"] 
                                    for f in range(6,8) for c in range(8)) else 0
        rey_negro_seguro = 1 if all(self.tablero[f][c].pieza not in ["♙", "♖", "♘", "♗", "♕"] 
                                  for f in range(0,2) for c in range(8)) else 0
        
        peones_doblados_blancas = sum(1 for col in range(8) 
                                    if sum(1 for fila in range(8) 
                                    if self.tablero[fila][col].pieza == "♙") > 1)
        peones_doblados_negras = sum(1 for col in range(8) 
                                   if sum(1 for fila in range(8) 
                                   if self.tablero[fila][col].pieza == "♟") > 1)
        
        return np.array([      #contenedor de datos numerico s
            blancas, negras,  #suma de puntos 
            movilidad_blancas, movilidad_negras, #movimientos legales 
            control_blancas, control_negras, #control central 
            rey_blanco_seguro, rey_negro_seguro,
            peones_doblados_blancas, peones_doblados_negras,
            len(self.historial_movimientos)
        ])
  
  #el ramdon forest procesa este array  asi  tipo array de estado, procesamiento,
  #prediccion de modelo y finalmente desicion del modimiento 

   
class InterfazAjedrez:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajedrez Inteligente")
        self.root.geometry("700x750")
        self.root.configure(bg="#2c3e50")
        
        self.style = {
            "font_pieces": ("Arial", 32),
            "font_labels": ("Helvetica", 12, "bold"),
            "font_messages": ("Helvetica", 14, "bold"),
            "bg_dark": "#2c3e50",
            "bg_light": "#34495e",
            "fg": "#ecf0f1",
            "highlight": "#e74c3c",
            "selected": "#3498db"
        }
        
        self.juego = GrafoAjedrez()  #crea el tablero y la logica del ajedrez
        self.botones = [[None for _ in range(8)] for _ in range(8)] 
        self.casilla_seleccionada = None #swe huarada la casilla deleccionada por q¿q 
        self.vs_ia = False
        self.modelo = self.entrenar_modelo_ml()
        
        #root ventana principal 
        self.main_frame = tk.Frame(root, bg=self.style["bg_dark"])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.info_panel = tk.Frame(self.main_frame, bg=self.style["bg_light"], bd=2, relief=tk.RAISED)
        self.info_panel.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
        
        self.turno_label = tk.Label(self.info_panel, text="Turno: Blancas", font=self.style["font_labels"], 
                                  bg=self.style["bg_light"], fg=self.style["fg"])
        self.turno_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.modo_label = tk.Label(self.info_panel, text="Modo: ", font=self.style["font_labels"], 
                                 bg=self.style["bg_light"], fg=self.style["fg"])
        self.modo_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.message_label = tk.Label(self.info_panel, text="", font=self.style["font_labels"], 
                                    bg=self.style["bg_light"], fg="#e74c3c")
        self.message_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
        self.board_frame = tk.Frame(self.main_frame, bg=self.style["bg_dark"])
        self.board_frame.pack()
        
        self.control_frame = tk.Frame(self.main_frame, bg=self.style["bg_dark"])
        self.control_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(self.control_frame, text="Reiniciar", command=self.reiniciar_juego,
                 font=self.style["font_labels"], bg="#e74c3c", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.control_frame, text="Cambiar Modo", command=self.cambiar_modo,
                 font=self.style["font_labels"], bg="#3498db", fg="white").pack(side=tk.LEFT, padx=5)
        
        self.seleccionar_modo()

    def reiniciar_juego(self):
        self.juego = GrafoAjedrez()
        self.actualizar_tablero()
        self.actualizar_turno()
        self.message_label.config(text="")

    def cambiar_modo(self):
        self.reiniciar_juego()
        self.seleccionar_modo()

    def generar_datos_entrenamiento(self, num_muestras=1000):
        X = []
        y = []
        #eqiuoñibrada
        for _ in range(num_muestras // 3):
            blancas = random.randint(30, 39)
            negras = random.randint(30, 39)
            movilidad_b = random.randint(20, 50)
            movilidad_n = random.randint(20, 50)
            control_b = random.randint(1, 4)
            control_n = random.randint(1, 4)
            seguridad_b = random.randint(0, 1)
            seguridad_n = random.randint(0, 1)
            peones_dob_b = random.randint(0, 2)
            peones_dob_n = random.randint(0, 2)
            movimientos = random.randint(0, 40)
            
            X.append([blancas, negras, movilidad_b, movilidad_n, control_b, control_n, 
                     seguridad_b, seguridad_n, peones_dob_b, peones_dob_n, movimientos])
            y.append(1 if (blancas + movilidad_b/10 + control_b*2 + seguridad_b*3) > 
                    (negras + movilidad_n/10 + control_n*2 + seguridad_n*3) else 0)
        
        #ventaja blacas 33%
        for _ in range(num_muestras // 3):
            blancas = random.randint(35, 45)
            negras = random.randint(20, 30)
            movilidad_b = random.randint(30, 60)
            movilidad_n = random.randint(10, 30)
            control_b = random.randint(2, 4)
            control_n = random.randint(0, 2)
            seguridad_b = 1
            seguridad_n = 0
            peones_dob_b = random.randint(0, 1)
            peones_dob_n = random.randint(1, 3)
            movimientos = random.randint(10, 40)
            
            X.append([blancas, negras, movilidad_b, movilidad_n, control_b, control_n, 
                     seguridad_b, seguridad_n, peones_dob_b, peones_dob_n, movimientos])
            y.append(1)
        
        #blancas negras
        for _ in range(num_muestras // 3):
            blancas = random.randint(20, 30)
            negras = random.randint(35, 45)
            movilidad_b = random.randint(10, 30)
            movilidad_n = random.randint(30, 60)
            control_b = random.randint(0, 2)
            control_n = random.randint(2, 4)
            seguridad_b = 0
            seguridad_n = 1
            peones_dob_b = random.randint(1, 3)
            peones_dob_n = random.randint(0, 1)
            movimientos = random.randint(10, 40)
            
            X.append([blancas, negras, movilidad_b, movilidad_n, control_b, control_n, 
                     seguridad_b, seguridad_n, peones_dob_b, peones_dob_n, movimientos])
            y.append(0)  #0 y 1 por ser entrenamientos opuestos
        
        return np.array(X), np.array(y)
#Para que la IA vea muchas variaciones diferentes y aprenda reglas generales (no solo memorice ejemplos).
   
   #cerebro de la ia
    def entrenar_modelo_ml(self):
        X, y = self.generar_datos_entrenamiento(3000)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        #divide daros 80% entreamiento y 2o prueba 
        pipeline = Pipeline([
            ('scaler', StandardScaler()), #nrmaliza los datos # Normaliza los datos (resta media, divide por desviación Para que todas las características (ej: "material" y "movilidad") tengan la misma importancia aunque usen escalas diferentes.


            ('model', RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))
        ])                                  #100 arbjkane de desisidiodon limita ka profunfifad  
        
        pipeline.fit(X_train, y_train)  #2,400 ejemplos de posiciones de ajedrez (80% de los 3,000 datos)

            # Cada ejemplo tiene 11 características (material, movilidad, control centro, etc.)
        scores = cross_val_score(pipeline, X, y, cv=5)# evitar memorizacion 
        print(f"Precisión validación cruzada: {scores.mean():.2f} (+/- {scores.std():.2f})")
        test_score = pipeline.score(X_test, y_test) #datos de prueba
        print(f"Precisión en conjunto de prueba: {test_score:.2f}")
        
        return pipeline

    def seleccionar_modo(self):
        self.mode_window = tk.Toplevel(self.root) #vemtana secundaria
        self.mode_window.title("Seleccionar modo de juego")
        self.mode_window.geometry("400x200")
        self.mode_window.configure(bg=self.style["bg_dark"])
        
        tk.Label(self.mode_window, text="Elige modo de juego:", 
                font=self.style["font_labels"], bg=self.style["bg_dark"], fg=self.style["fg"]).pack(pady=20)
        
        btn_frame = tk.Frame(self.mode_window, bg=self.style["bg_dark"])
        btn_frame.pack()
        
        tk.Button(btn_frame, text="Jugador vs Jugador", font=self.style["font_labels"],
                 bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white",
                 command=lambda: self.iniciar_juego(False)).pack(side=tk.LEFT, padx=10, pady=5, ipadx=10, ipady=5)
        
        tk.Button(btn_frame, text="Jugador vs IA", font=self.style["font_labels"],
                 bg="#2980b9", fg="white", activebackground="#3498db", activeforeground="white",
                 command=lambda: self.iniciar_juego(True)).pack(side=tk.LEFT, padx=10, pady=5, ipadx=10, ipady=5)
        
        self.mode_window.grab_set()

    def iniciar_juego(self, ia):
        self.vs_ia = ia
        self.modo_label.config(text=f"Modo: {'Jugador vs IA' if ia else 'Jugador vs Jugador'}")
        self.mode_window.destroy()
        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(8):
            for col in range(8):
                casilla = self.juego.tablero[fila][col]
                btn = tk.Button(self.board_frame, text=casilla.pieza if casilla.pieza else " ",
                              width=3, height=1, bg=casilla.color,
                              font=self.style["font_pieces"],
                              fg="#2c3e50" if casilla.pieza and casilla.pieza in ["♙", "♖", "♘", "♗", "♕", "♔"] else "#c0392b",
                              activebackground=self.style["selected"],
                              relief=tk.FLAT,
                              command=lambda f=fila, c=col: self.manejar_click(f, c))
                btn.grid(row=fila, column=col, padx=1, pady=1)
                self.botones[fila][col] = btn

    def manejar_click(self, fila, col):
        if self.juego.ahogado:
            return
            
        if self.casilla_seleccionada is None:
            if self.juego.tablero[fila][col].pieza and self.juego.es_pieza_aliada(self.juego.tablero[fila][col].pieza):
                self.casilla_seleccionada = (fila, col)
                self.botones[fila][col].config(bg=self.style["selected"])
                self.mostrar_movimientos(fila, col)
        else:
            f_orig, c_orig = self.casilla_seleccionada
            movimientos = self.juego.obtener_movimientos_validos(f_orig, c_orig)
            if (fila, col) in movimientos:
                self.juego.mover_pieza(f_orig, c_orig, fila, col)
                self.actualizar_tablero()
                self.actualizar_turno()
                
                if self.juego.es_ahogado():
                    self.mostrar_mensaje("maloooo perdiste")
                    self.juego.ahogado = True
                
                if self.vs_ia and not self.juego.turno_blancas and not self.juego.ahogado:
                    self.root.after(500, self.movimiento_ia)
            self.limpiar_seleccion()

    def mostrar_movimientos(self, fila, col):
        for mf, mc in self.juego.obtener_movimientos_validos(fila, col):
            self.botones[mf][mc].config(bg=self.style["highlight"])

    def actualizar_tablero(self):
        for fila in range(8):
            for col in range(8):
                pieza = self.juego.tablero[fila][col].pieza
                color = self.juego.tablero[fila][col].color
                self.botones[fila][col].config(text=pieza if pieza else " ", bg=color,
                                             fg="#2c3e50" if pieza and pieza in ["♙", "♖", "♘", "♗", "♕", "♔"] else "#c0392b")

    def actualizar_turno(self):
        turno = "Blancas" if self.juego.turno_blancas else "Negras"
        self.turno_label.config(text=f"Turno: {turno}")

    def limpiar_seleccion(self):
        self.actualizar_tablero()
        self.casilla_seleccionada = None

    def mostrar_mensaje(self, mensaje):
        message_window = tk.Toplevel(self.root)
        message_window.title("Fin del juego")
        tk.Label(message_window, text=mensaje, font=self.style["font_messages"]).pack(padx=30, pady=20)
        tk.Button(message_window, text="Aceptar", command=message_window.destroy).pack(pady=10)
        message_window.grab_set()

    def movimiento_ia(self):
        mejor_valor = -float('inf')
        mejor_jugada = None
        
        for fila in range(8):
            for col in range(8):
                pieza = self.juego.tablero[fila][col].pieza
                if pieza and self.juego.es_pieza_aliada(pieza):
                    movimientos = self.juego.obtener_movimientos_validos(fila, col)
                    for f2, c2 in movimientos:
                        copia = self.simular_movimiento(fila, col, f2, c2)
                        estado = copia.obtener_estado_juego()
                        valor = self.modelo.predict_proba([estado])[0][1]
                        
                        pieza_capturada = self.juego.tablero[f2][c2].pieza
                        if pieza_capturada:
                            valores = {"♙":1, "♟":1, "♖":5, "♜":5, "♘":3, "♞":3, 
                                      "♗":3, "♝":3, "♕":9, "♛":9, "♔":0, "♚":0}
                            valor += valores.get(pieza_capturada, 0) * 0.1
                        
                        if valor > mejor_valor:
                            mejor_valor = valor
                            mejor_jugada = (fila, col, f2, c2)
        
        if mejor_jugada:
            f1, c1, f2, c2 = mejor_jugada
            self.juego.mover_pieza(f1, c1, f2, c2)
            self.actualizar_tablero()
            self.actualizar_turno()
            
            if self.juego.es_ahogado():
                self.mostrar_mensaje("¡Ahogado! Empate")
                self.juego.ahogado = True

    def simular_movimiento(self, f1, c1, f2, c2):
        sim = GrafoAjedrez()
        for fila in range(8):
            for col in range(8):
                sim.tablero[fila][col].pieza = self.juego.tablero[fila][col].pieza
        sim.turno_blancas = self.juego.turno_blancas
        sim.historial_movimientos = self.juego.historial_movimientos.copy()
        sim.mover_pieza(f1, c1, f2, c2)
        return sim

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazAjedrez(root)
    root.mainloop()