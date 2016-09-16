class Node():
    """
    A node keeps track of itself and the nodes it points to
    """

    def createFromString(self, str):
        arr = str.split()
        for i,v in enumerate(arr):
            arr[i] = int(v)
        self.setAttributes(arr[0],arr[1:])

    def setAttributes(self, name, vertices):
        self.name = name
        self.vertices = vertices

    def combine(self, otherNode):
        # to implement
        return;

