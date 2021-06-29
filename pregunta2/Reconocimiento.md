# Frase a Reconocer

`instr ; try instr catch instr ; try instr catch instr finally instr ; instr`

### Enumeración de las Reglas de la Gramática

```
0: S -> I $
1: I -> try I catch I finally I
2:    | try I catch I
3:    | I ; I
4:    | instr
```

### Ejecución

#### PASO 0:
```
ENTRADA:  instr ; try instr catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0
ACCCION:  shift 
```

#### PASO 1:

```
ENTRADA:  ; try instr catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I3
ACCCION:  reduce 4
```

#### PASO 2:

```
ENTRADA:  ; try instr catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1
ACCCION:  shift
```

#### PASO 3:

```
ENTRADA:  try instr catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4
ACCCION:  shift
```

#### PASO 4:

```
ENTRADA:  instr catch instr ; try instr catch instr finally instr ; instr $ 
PILA:     $ I0 I1 I4 I2
ACCCION:  shift
```

#### PASO 5:

```
ENTRADA:  catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I3
ACCCION:  reduce 4
```

#### PASO 6:
 
```                                                                 
ENTRADA:  catch instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 
ACCCION:  shift 
```

### PASO 7:
  
```                                                                 
ENTRADA:  instr ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9
ACCCION:  shift 
```

### PASO 8:
  
```                                                                 
ENTRADA:  ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I3
ACCCION:  reduce 4 
```

### PASO 9:
  
```                                                                 
ENTRADA:  ; try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12
ACCCION:  shift 
```

### PASO 10:

```
ENTRADA:  try instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4
ACCCION:  shift
```

#### PASO 11:

```
ENTRADA:  instr catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2
ACCCION:  shift
```

#### PASO 12:

```
ENTRADA:  catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I3
ACCCION:  reduce 4
```

#### PASO 13:

```
ENTRADA:  catch instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5
ACCCION:  shift
```

#### PASO 14:

```
ENTRADA:  instr finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9
ACCCION:  shift
```

#### PASO 15:

```
ENTRADA:  finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9 I3
ACCCION:  reduce 4
```

#### PASO 16:

```
ENTRADA:  finally instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9 I12
ACCCION:  shift
```

#### PASO 17:

```
ENTRADA:  instr ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9 I12 I17
ACCCION:  shift
```

#### PASO 18:

```
ENTRADA:  ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9 I12 I17 I3
ACCCION:  reduce 4
```

#### PASO 19:

```
ENTRADA:  ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I2 I5 I9 I12 I17 I23
ACCCION:  reduce 1
```

#### PASO 20:

```
ENTRADA:  ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I8
ACCCION:  reduce 3
```

#### PASO 21:

```
ENTRADA:  ; instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12
ACCCION:  shift
```

#### PASO 22:

```
ENTRADA:  instr $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4
ACCCION:  shift
```

#### PASO 23:

```
ENTRADA:  $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I3
ACCCION:  reduce 4
```

#### PASO 24:

```
ENTRADA:  $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4
ACCCION: 
```

#### PASO 25:

```
ENTRADA:  $
PILA:     $ I0 I1 I4 I2 I5 I9 I12 I4 I8
ACCCION:  reduce 3
```

#### PASO 26:

```
ENTRADA:  $
PILA:     $ I0 I1 I4 I2 I5 I9 I12
ACCCION:  reduce 2
```

#### PASO 27:

```
ENTRADA:  $
PILA:     $ I0 I1 I4 I8
ACCCION:  reduce 4
```

#### PASO 28:

```
ENTRADA:  $
PILA:     $ I0 I1
ACCCION:  shift
```

#### PASO 29:

```
ENTRADA:  
PILA:     $ I0 I1 I38
ACCCION:  accept
```
