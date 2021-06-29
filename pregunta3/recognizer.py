import sys

look_ahead = None
input_str = None

def print_state():
  """
    Prints the state of the input 
  """
  result = ''
  for char in input_str:
    result += char + ' '
  print(result)

def get_token_type(token):
  """
    Gets the type of the given token. Token should be of the format instr_<TYPE>
  """
  if token[:6] != 'instr_':
    raise Exception(f'Invalid token {token}')
  else:
    return token[6:]

def K(k_in):
  """
  Regla:
    K -> finally I      { K.tipo = I.tipo }
      |  lambda         { K.tipo = K.in }
  """
  
  if look_ahead == 'finally':
    f'Expandir \033[1mS -> I\033[0m'
    print(f'\033[1mExpando K -> finally I\033[0m')

    try:
      shift('finally')
    except:
      raise Exception('No se pudo expandir con K')

    return I(None)
  elif look_ahead in ['try', ';', '$'] or look_ahead[:6] == "instr_": 
    print_state()
    print(f'\033[1;31mExpando K -> lambda\033[0m')
    return k_in
  else:
    print('la: ', look_ahead)
    raise Exception('No se pudo expandir con K')
        
def H(h_in):
  """
  Regla:
    H -> try I1         { I2.in = I1.tipo } 
         catch I2       { K.in = Either I1.tipo I2.tipo } 
         K              { H.tipo = K.tipo }     
      |  instr          { H.tipo = instr.tipo } 
  """
  if look_ahead == 'try':
    print_state()
    print(f'\033[1;31mExpando H -> try I1 catch I2 K\033[0m')

    try:
      shift('try')
    except:
      raise Exception('No se pudo expandir con H')

    i1_type = I(None)

    try:
      shift('catch')
    except:
      raise Exception('No se pudo expandir con H')

    i2_type = I(i1_type)
    return K(f'Either {i1_type} {i2_type}')
  elif look_ahead[:6] == "instr_":
    print_state()
    print(f'\033[1;31mExpando H -> instr\033[0m')
    token = look_ahead
    
    try:
      shift(token)
    except:
      raise Exception('No se pudo expandir con H')

    return get_token_type(token)
  else:
    raise Exception('No se pudo expandir con H')

def R(r_in):
  """
  Regla:
    R -> ; H            { R1.in = H.tipo } 
           R1           { R.tipo = R1.tipo }
      |  lambda         { R.tipo = R.in }
  """
  if look_ahead == ';':
    print_state()
    print(f'\033[1;31mExpando R -> ;\033[0m H')

    try:
      shift(';')
    except:
      raise Exception('No se pudo expandir con H')

    h_type = H(None)
    return R(h_type)
  elif (look_ahead in ['try', 'catch', 'finally', '$'] or 
        look_ahead[:6] == "instr_"):
    print_state()
    print(f'\033[1;31mExpando R -> lambda\033[0m')
    return r_in
  else:
    raise Exception('No se pudo expandir con R')

def I(i_in):
  """
  Regla:
    I -> H              { R.in = H.tipo }
         R              { I.tipo = R.tipo }
  """
  if look_ahead == 'try' or look_ahead[:6] == "instr_":
    print_state()
    print(f'\033[1;31mExpando I -> H R\033[0m')
    h_type = H(None)
    return R(h_type)
  else:
    raise Exception('No se pudo expandir con I')

def S():
  """
  Regla:
    S -> I $            { S.tipo = I.tipo }
  """
  if look_ahead == 'try' or look_ahead[:6] == "instr_":
    print_state()
    print(f'\033[1;31mExpando S-> I $\033[0m')
    i_type = I(None)

    try:
      shift('$')
    except:
      raise Exception('No se pudo expandir con S')

    print('Aceptar')
    return i_type
  else:
    raise Exception('No se pudo expandir con S')

def shift(token):
  """
    Shifts a token in the input str.
  """
  global input_str 
  global look_ahead

  if len(input_str) > 0 and input_str[0] != token:
    raise Exception('Invalid token to be shifted.')
  else:
    input_str = input_str[1:]
    if len(input_str):
      look_ahead = input_str[0]
    else:
      look_ahead = None


def parse_string(args):
  global look_ahead, input_str
  input_str = args + ['$']
  look_ahead = input_str[0]

  my_type = S()
  print('Tipo: ', my_type)


if __name__ == '__main__':
  """
    Main menu
  """

  print('¡Bienvenido!')

  while True:
    cmd = input('$> ')

    tokens = cmd.split(' ')

    # options switch
    try:
      if tokens[0] == 'PARSE':
        parse_string(tokens[1:])
      elif tokens[0] == 'EXIT':
        print('Hasta luego!')
        sys.exit(0)
      else:
        print('Usage PARSE <string>')
        print('      EXIT')
    except Exception as e:
      if e.args[0].startswith('No se pudo'):
        print('Rechazar')

      print(e.args[0])  
