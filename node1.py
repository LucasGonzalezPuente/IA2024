class Node:
    def __init__(self, name, id=-1):     #  construtor do nodo....."
        self.m_id = id
        self.m_name = str(name)
        # posteriormente podera ser colocodo um objeto que armazena informação em cada nodo.....

    def __str__(self):
        return self.m_name

    def __repr__(self):
        return self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.m_name == other.m_name
        return False
    def __hash__(self):
        return hash(self.m_name)


