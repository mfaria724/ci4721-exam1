# Grafo

## Nodos:

#### Notación:
* Nodo
  - Sucesor 1
  - Sucesor 2
  ...

#### Nodos del Grafo
* g-try
  - f-$
  - f-finally
  - f-try,g-catch
  - f;
  - f-catch,g-finally
* g-instr
  - f-$
  - f-finally
  - f-try,g-catch
  - f;
  - f-catch,g-finally
* g-;
  - f-$
  - f-catch,g-finally
* f-;
  - g-$
  - g-;
* f-finally
  - g-$
  - f-catch,g-finally
* f-try,g-catch
  - g-$
  - f-$
* f-catch,g-finally
  - g-$
  - f-$
  f-try,g-finally
* f-instr
  - g-;
  - f-catch, g-finally
  - f-try,g-catch
  - g-$
* g-$
* f-$

## Funciones *f* y *g*

``` json
f = { 
  "try": 1,
  "catch": 2,
  "finally": 3,
  "instr": 4,
  ";": 4,
  "$": 0,
}

g = { 
  "try": 5,
  "catch": 1,
  "finally": 2,
  "instr": 5,
  ";": 3,
  "$": 0,
}
```
