class Node:
  """
  Represents a node in the graph to calculate f and g.
  """

  # each node could have multiple symbols that belong to the same equivalence class.
  elements = None 
  # nodes to which there's an edge to
  childs = None
  # maximun path length, is stored to avoid recomputation
  max_path_length = None

  def __init__(self, init_elem) -> None:
    """
    Initializes an empty node with a single element
    """
    self.elements = []
    self.childs = []
    self.elements = [init_elem]

  def get_max_path(self, visited: list) -> int:
    """
    Get's the the longest possible path from this node. Needs to get track of 
    the visited to detect cycles.
    """
    # check if this node has been already visited, if it has, there's a cycle.
    if self in visited:
      print('ERROR: Ha sido detectado un ciclo en el grafo creado para computar las ' \
            'funciones "f" y "g".')

      cycle = 'CICLO: '
      for node in visited:
        cycle += node._print_elements() + ' -> '
      cycle += visited[0]._print_elements()
      print(cycle)
      
      raise Exception('cycle found in graph!')

    # if max path hasn't been computed, compute it.
    if self.max_path_length is None:
      if self.childs:
        self.max_path_length = max(
          [child.get_max_path(visited + [self]) for child in self.childs]
        ) + 1
      else:
        self.max_path_length = 0

    return self.max_path_length

  def add_element(self, element):
    self.elements.append(element)

  def get_elements(self):
    return self.elements

  def add_child(self, child):
    self.childs.append(child)

  def _print_elements(self):
    result = '['
    for elem in self.elements:
      result += str(elem) + ','

    return result + ']'

  def reset_max_path(self):
    self.max_path_length = None

  def __str__(self) -> str:

    result = 'NODE:\n'
    result += 'ELEMENTS: ['

    for elem in self.elements:
      result += str(elem) + ','
    
    result += ']\n'

    result += 'CHILDS: ['

    for child in self.childs:
      result += child._print_elements() + ','
    
    result += ']\n'

    return result
