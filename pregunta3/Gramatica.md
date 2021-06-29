# Gramática S-atribuida

```
S -> I $                            { S.tipo = I.tipo }
I -> try I1 catch I2 finally I3     { I.tipo = I3.tipo }
  |  try I1 catch I2                { I.tipo = Either I1.tipo I2.tipo }
  |  I1 ; I2                        { I.tipo = I2.tipo }
  |  instr                          { I.tipo = instr.tipo }
```

# Gramática L-atribuida

```
S -> I $            { S.tipo = I.tipo }         
I -> H              { R.in = H.tipo }
     R              { I.tipo = R.tipo }
R -> ; H            { R1.in = H.tipo } 
       R1           { R.tipo = R1.tipo }
  |  lambda         { R.tipo = R.in }
H -> try I J        { H.tipo = J.tipo }              
  |  instr          { H.tipo = instr.tipo }              
J -> catch I        { K.in = I.tipo }
           K        { J.tipo = K.tipo }
K -> finally I      { K.tipo = I.tipo }
  |  lambda         { K.tipo = K.in }
```
