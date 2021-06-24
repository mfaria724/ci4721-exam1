import sys

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
    to be a terminal symbol should't contain end marker '$' and should be
    an ascii string.
  """
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

  # TODO: remove testing prints
  print('non-terminal: ', non_terminal)
  print('symbols: ', symbols)

  # check if left side of the rule is non-terminal
  if not check_non_terminal(non_terminal):
    print('Los símbolos NO terminales deben tener un sólo caracter y estar en ')
    print('mayúsculas.')
    return

  # check if right side of the rule is terminal or non-terminal
  if not all(check_non_terminal(symb) or check_terminal(symb) for symb in symbols):
    print('Alguno de los tokens pertenecientes a la regla no cumplen con la')
    print('condición de ser terminales o no-terminales')
    return

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

def set_precedence(args: list):
  """
    sets the precedence between terminal symbols
  """
  try:
    # extract the operands and operator
    operand1, op, operand2 = args

    # check the format of the operands
    if not check_terminal(operand1):
      print('El operador 1 no es un símbolo terminal.')
      return

    if not check_terminal(operand2):
      print('El operador 1 no es un símbolo terminal.')
      return

    # check the format of the operator
    if not check_op(op):
      print('Operador inválido.')
      return

  except:
    # return an error if wrong format has been used
    print('El número de operandos es incorrecto.')
    return

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
    print('Entered: ' + str(tokens))

    # check if option is valid
    if tokens[0] == 'RULE':
      define_rule(tokens[1:])
    elif tokens[0] == 'INIT':
      set_init_symbol(tokens[1:])
    elif tokens[0] == 'PREC':
      set_precedence(tokens[1:])
    elif tokens[0] == 'BUILD':
      print('building syntactic analizer...')
    elif tokens[0] == 'PARSE':
      print('parsing...')
    elif tokens[0] == 'EXIT':
      print('¡Esperamos verlo de vuelta! :)')
      exit(0)
    else:
      print('Opción inválida. Por favor selecione una opción correcta.')
