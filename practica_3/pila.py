class pila:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        else:
            return "Pila vacia"

    def peek(self):
        if not self.is_empty():
            return self.elementos[-1]
        else:
            return "Pila vacia"

    def top(self):
        if not self.is_empty():
            return self.elementos[-1]
        else:
            return "Pila vacia"
        
    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)