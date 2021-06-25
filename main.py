import sys
from node import Node
from element import Element

rules = {}
precedences = {}
precedence_op_names = {
  '>': 'mayor',
  '<': 'menor',
  '=': 'igual'
}
f_g_functions = {'f': {}, 'g': {}}

def is_ascii(string: str) -> bool:
  """
    checks if string is an ascii string
  """
  return all(ord(char) < 128 for char in string)

def check_non_terminal(symbol: str) -> bool:
  """
    checks if a token is a non-terminal symbol
    to be a non-terminal, must have 1 character long, should be in uppercase
    and should be an ascii string.
  """
  return len(symbol) == 1 and symbol.isupper() and is_ascii(symbol)

def check_terminal(symbol: str) -> bool:
  """
    checks if a token is a terminal symbol.
    to be a terminal symbol should't contain end marker '$', should be
    an ascii string and should be lowercase.
  """

  # check if contains uppercase letters
  for char in symbol:
    if char.isalpha() and char.isupper():
      return False

  return all(char != '$' for char in symbol) and is_ascii(symbol)

def check_op(symbol: str) -> bool:
  """
    checks if a token represents a valid operator
  """
  return symbol in ['>', '<', '=']

def define_rule(args: list):
  """
    starts the definition of a new grammar rule
  """

  # as second parameter is a list of dynamic lenght, we separate the firts 
  # element
  non_terminal = args[0]
  symbols = args[1:]

  # check if left side of the rule is non-terminal
  if not check_non_terminal(non_terminal):
    print('Los símbolos NO terminales deben tener un sólo caracter y estar en ')
    print('mayúsculas.')
    return

  # warning if defining a lambda production
  if not len(symbols):
    print(f'WARNING: La regla ${non_terminal} -> lambda" debe ser inicializada'+\
           'como la regla inicial, ya que es una lambda producción.')

  rule_str = ' '.join(symbols)

  # check if first symbol is terminal or non-terminal symbol.
  if not check_non_terminal(symbols[0]) and not check_terminal(symbols[0]):
    print(f'ERROR: La regla "{non_terminal} -> {rule_str}" ' + \
            'no corresponde a una gramática de operadores.')
    return    

  # take each pair (if exists) and review that there are no 2 or more 
  # consecutive non-terminal symbols.
  # also uses the cycle to check that all of them are terminals or non-terminals
  for index in range(1, len(symbols)):

    # take the current and the previous one
    current = symbols[index]
    prev = symbols[index - 1]

    # if it is a non terminal, previous one can't be a non-terminal.
    if check_non_terminal(current):
      if check_non_terminal(prev):
        print(f'ERROR: La regla "{non_terminal} -> {rule_str}" ' + \
               'no corresponde a una gramática de operadores.')
        return
    # if it isn't non-terminal, it has to be terminal.
    elif not check_terminal(current):
      print(f'ERROR: La regla "{non_terminal} -> {rule_str}" ' + \
              'no corresponde a una gramática de operadores.')
      return

  # prints the result to the user  
  rules[rule_str] = non_terminal
  print(f'Regla {non_terminal} -> {rule_str} agregada a la gramática.')

def set_init_symbol(args: list):
  """
    sets a initi symbol for the grammar
  """

  # should contain a single argument (the initial symbol)
  if len(args) != 1:
    print('Número de argumentos inválido.')
    return

  # check if the symbol is a non terminal symbol
  if not check_non_terminal(args[0]):
    print('El token no es un símbolo no-terminal.')
    return

def check_terminal_precedence(symbol):
  return symbol == '$' or check_terminal(symbol)

def set_precedence(args: list):
  """
    sets the precedence between terminal symbols
  """
  try:
    # extract the operands and operator
    operand1, op, operand2 = args

    # check the format of the operands
    if not check_terminal_precedence(operand1):
      print('El operador 1 no es un símbolo terminal.')
      return

    if not check_terminal_precedence(operand2):
      print('El operador 1 no es un símbolo terminal.')
      return

    # check the format of the operator
    if not check_op(op):
      print('Operador inválido.')
      return

    if not operand1 in precedences:
      precedences[operand1] = {}

    operand1_precedences = precedences[operand1]

    if not op in operand1_precedences:
      operand1_precedences[op] = []

    operand1_op = operand1_precedences[op]

    operand1_op.append(operand2)

    print(f'"{operand1}" tiene {precedence_op_names[op]} precedencia que "{operand2}"')

  except Exception as e:
    print(e)
    # return an error if wrong format has been used
    print('El número de operandos es incorrecto.')
    return

def build_syntactic_analizer():
  """
  Builds the syntactic analizer with the computation of functions 'f' and 'g'
  """

  nodes = []
  nodes_by_element = {}

  # initialize nodes with 'f' functions
  for key in precedences:

    # create the 'f' node
    element = Element('f', key)
    node = Node(element)
    nodes.append(node)

    # create a references between the name and the node
    nodes_by_element[f'f-{key}'] = node
    key_prec = precedences[key]

    # for each operator in for f-symbol.
    for op in key_prec:

      # take each g-symbol
      g_symbols = key_prec[op]
      for symb in g_symbols:
        
        # same equivalence class, no need to create a new node
        if op == '=':
          new_element = Element('g', symb)
          node.add_element(new_element)
          nodes_by_element[f'g-{symb}'] = node          
        # different equivalence class, cloud be necessary to create a new node
        else:
          
          # if g-symbol is already in used, just take it from cache
          if f'g-{symb}' in nodes_by_element:
            right_node = nodes_by_element[f'g-{symb}']
          # if it hasn't been used, create the node.
          else:
            new_element = Element('g', symb)
            right_node = Node(new_element)
            nodes.append(right_node)
            nodes_by_element[f'g-{symb}'] = right_node

          # create the reference for graph edges.
          if op == '<':
            right_node.add_child(node)
          elif op == '>':
            node.add_child(right_node)

  # before doing this reset the max path lenght to none to avoid using cache from
  # previous build. 
  for nod in nodes:
    nod.reset_max_path()

  try:
    # get the element in the node
    for nod in nodes:
      node_elems = nod.get_elements()

      # for each element in the node, get the max path.
      for elem in node_elems:
        function_dict = f_g_functions[elem.get_function()]
        function_dict[elem.get_symbol()] = nod.get_max_path([])
  except Exception as e:
    # graph contains a cycle.
    print('ERROR: No se pudo construir la gramática.')

  # print the result of the functions
  for func in f_g_functions:
    print(f'Valores para {func}')
    func_values = f_g_functions[func]
    for symbol in func_values:
      print(f'  {symbol}: {func_values[symbol]}')

if __name__ == '__main__':

  # welcome message
  print('           ¡Bienvenido al')
  print('Generador de Analizadores Sintácticos')
  print('   para Gramáticas de Operadores!')

  # infinite terminal loop
  while True:

    # ask for input and divide it by blank spaces
    cmd = input('$> ')
    tokens = cmd.split(' ')

    # check if option is valid
    if tokens[0] == 'RULE':
      define_rule(tokens[1:])
    elif tokens[0] == 'INIT':
      set_init_symbol(tokens[1:])
    elif tokens[0] == 'PREC':
      set_precedence(tokens[1:])
    elif tokens[0] == 'BUILD':
      build_syntactic_analizer()
    elif tokens[0] == 'PARSE':
      print('parsing...')
    elif tokens[0] == 'EXIT':
      print('¡Esperamos verlo de vuelta! :)')
      exit(0)
    else:
      print('Opción inválida. Por favor selecione una opción correcta.')
