# Gramática

S -> I $
I -> try I catch I finally I
   | try I catch I
   | I ; I
   | instr

# Máquina Característica LR(1)

## I0 [OK]
S -> . I $ {$}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}

**Avanzar:**
I       => I1
try     => I2
instr   => I3

## I1 [OK]
S -> I . $ {$}
I -> I . ; I {$, ;}

**Avanzar:**
;       => I4

## I2 [OK]
I -> try . I catch I finally I {$, ;}
I -> try . I catch I {$, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I5
try     => I6
instr   => I7

## I3 [OK]
I -> instr . {$, ;}

**Avanzar:**
None

## I4 [OK]
I -> I ; . I {$, ;}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}

**Avanzar:**
I       => I8
try     => I2
instr   => I3

## I5 [OK]
I -> try I . catch I finally I {$, ;}
I -> try I . catch I {$, ;}
I -> I . ; I {catch, ;}

**Avanza:**
catch   => I9
;       => I10

## I6 [OK]
I -> try . I catch I finally I {catch, ;}
I -> try . I catch I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I11
try     => I6
instr   => I7

## I7 [OK]
I -> instr . {catch, ;}

**Avanzar:**
None

## I8 [OK]
I -> I ; I . {$, ;}
I -> I . ; I {$, ;}

**Avanzar:**
;       => I4

**Conflicto:**
Shift ;, Reduce I -> I ; I

## I9 [OK]
I -> try I catch . I finally I {$, ;}
I -> try I catch . I {$, ;}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}

**Avanzar:**
I       => I12
try     => I13
instr   => I14

## I10 [OK]
I -> I ; . I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I15
try     => I6
instr   => I7

## I11 [OK]
I -> try I . catch I finally I {catch, ;}
I -> try I . catch I {catch, ;}
I -> I . ; I {catch, ;}

**Avanzar:**
catch   => I16
;       => I10

## I12 [OK]
I -> try I catch I . finally I {$, ;}
I -> try I catch I . {$, ;}
I -> I . ; I {finally, ;, $}

**Avanzar:**
finally => I17
;       => I18

**Conflicto:**
Shift ;, Reduce I -> try I catch I

## I13 [OK]
I -> try . I catch I finally I {finally, ;, $}
I -> try . I catch I {finally, ;, $}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I19
try     => I6
instr   => I7

## I14 [OK]
I -> instr . {finally, ;, $}

**Avanzar:**
None

## I15 [OK]
I -> I ; I . {catch, ;}
I -> I . ; I {catch, ;}

**Avanzar:**
;       => I10

**Conflicto:**
Shift ;, Reduce I -> I ; I

## I16 [OK]
I -> try I catch . I finally I {catch, ;}
I -> try I catch . I {catch, ;}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}

**Avanzar:**
I       => I20
try     => I21
instr   => I22

## I17 [OK]
I -> try I catch I finally . I {$, ;}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}

**Avanzar:**
I       => I23
try     => I2
instr   => I3

## I18 [OK]
I -> I ; . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}

**Avanzar:**
I       => I24
try     => I13
instr   => I14

## I19 [OK]
I -> try I . catch I finally I {finally, ;, $}
I -> try I . catch I {finally, ;, $}
I -> I . ; I {catch, ;}

**Avanzar:**
catch   => I25
;       => I10

## I20 [OK]
I -> try I catch I . finally I {catch, ;}
I -> try I catch I . {catch, ;}
I -> I . ; I {finally, ;, catch}

**Avanzar:**
finally => I26
;       => I27

**Conflicto:**
Shift ;, Reduce I -> try I catch I

## I21 [OK]
I -> try . I catch I finally I {finally, ;, catch}
I -> try . I catch I {finally, ;, catch}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I28
try     => I6
instr   => I7

## I22 [OK]
I -> instr . {finally, ;, catch}

**Avanzar:**
None

## I23 [OK]
I -> try I catch I finally I . {$, ;}
I -> I . ; I {$, ;}

**Avanzar:**
;       => I4

**Conflicto:**
Shift ;, Reduce I -> try I catch I finally I

## I24 [OK]
I -> I ; I . {finally, ;, $}
I -> I . ; I {finally, ;, $}

**Avanzar:**
;       => I18

Shift ;, Reduce I -> I ; I

## I25 [OK]
I -> try I catch . I finally I {finally, ;, $}
I -> try I catch . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}

**Avanzar:**
I       => I29
try     => I13
instr   => I14

## I26 [OK]
I -> try I catch I finally . I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}

**Avanzar:**
I       => I30
try     => I6
instr   => I7

## I27 [OK]
I -> I ; . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}

**Avanzar:**
I       => I31
try     => I21
instr   => I22

## I28 [OK]
I -> try I . catch I finally I {finally, ;, catch}
I -> try I . catch I {finally, ;, catch}
I -> I . ; I {catch, ;}

**Avanzar:**
catch   => I32
;       => I10

## I29 [OK]
I -> try I catch I . finally I {finally, ;, $}
I -> try I catch I . {finally, ;, $}
I -> I . ; I {finally, ;, $}

**Avanzar:**
finally => I33
;       => I18

**Conflicto:**
- Shift ;, Reduce I -> try I catch I
- Shift finally, Reduce I -> try I catch I

## I30 [OK]
I -> try I catch I finally I . {catch, ;}
I -> I . ; I {catch, ;}

**Avanzar:**
;       => I10

**Conflicto:**
- Shift ;, Reduce I -> try I catch I finally I

## I31 [OK]
I -> I ; I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}

**Avanzar:**
;       => I27

**Conflicto:**
- Shift ;, Reduce I -> I ; I

## I32 [OK]
I -> try I catch . I finally I {finally, ;, catch}
I -> try I catch . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}

**Avanzar:**
I       => I34
try     => I21
instr   => I22

## I33 [OK]
I -> try I catch I finally . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}

**Avanzar:**
I       => I35
try     => I13
instr   => I14

## I34 [OK]
I -> try I catch I . finally I {finally, ;, catch}
I -> try I catch I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}

**Avanzar:**
finally => I36
;       => I27

**Conflicto:**
- Shift ;, Reduce I -> try I catch I
- Shift finally, Reduce I -> try I catch I

## I35 [OK]
I -> try I catch I finally I . {finally, ;, $}
I -> I . ; I {finally, ;, $}

**Avanzar:**
;       => I18

**Conflicto:**
- Shift ;, Reduce I -> try I catch I finally I

## I36 [OK]
I -> try I catch I finally . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}

**Avanzar:**
I       => I37
try     => I21
instr   => I22

## I37 [OK]
I -> try I catch I finally I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}

**Avanzar:**
;       => I27

**Conflicto:**
- Shift ;, Reduce I -> try I catch I finally I
