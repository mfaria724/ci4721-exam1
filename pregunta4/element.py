class Element:
  """
    Represents an element inside a node. Each node could have multiple values
    that belong to the same equivalence class.
  """

  # function should be 'f' or 'g', representing left or right side of the 
  # precedence, respectively
  function = None
  symbol = None

  def __init__(self, function: str, symbol: str) -> None:
    """
    Inits an element with the function and name provided.
    """
    self.function = function
    self.symbol = symbol

  def get_function(self):
    return self.function

  def get_symbol(self):
    return self.symbol

  def __str__(self) -> str:
    return f'{self.function}-{self.symbol}'
