# Gramática

```
S -> I $
I -> try I catch I finally I
   | try I catch I
   | I ; I
   | instr
```

# Máquina Característica LR(1)

### **I0**
```
S -> . I $ {$}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}
```

**Avanzar:**
* `I       => I1`
* `try     => I2`
* `instr   => I3`

### **I1**
```
S -> I . $ {$}
I -> I . ; I {$, ;}
```

**Avanzar:**
* `;       => I4`

### **I2**
```
I -> try . I catch I finally I {$, ;}
I -> try . I catch I {$, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I5`
* `try     => I6`
* `instr   => I7`

### **I3**
```
I -> instr . {$, ;}
```

**Avanzar:**
None

### **I4**
```
I -> I ; . I {$, ;}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}
```

**Avanzar:**
* `I       => I8`
* `try     => I2`
* `instr   => I3`

### **I5**
```
I -> try I . catch I finally I {$, ;}
I -> try I . catch I {$, ;}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `catch   => I9`
* `;       => I10`

### **I6**
```
I -> try . I catch I finally I {catch, ;}
I -> try . I catch I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I11`
* `try     => I6`
* `instr   => I7`

### **I7**
```
I -> instr . {catch, ;}
```

**Avanzar:**
None

### **I8** **Conflicto**
```
I -> I ; I . {$, ;}
I -> I . ; I {$, ;}
```

**Avanzar:**
* `;       => I4`

**Conflicto:**
- `Shift ;, Reduce I -> I ; I`
  * Resuelto con `Reduce I -> I ; I` ya que `;` asocia a izquierda.

### **I9**
```
I -> try I catch . I finally I {$, ;}
I -> try I catch . I {$, ;}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}
```

**Avanzar:**
* `I       => I12`
* `try     => I13`
* `instr   => I14`

### **I10**
```
I -> I ; . I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I15`
* `try     => I6`
* `instr   => I7`

### **I11**
```
I -> try I . catch I finally I {catch, ;}
I -> try I . catch I {catch, ;}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `catch   => I16`
* `;       => I10`

### **I12** **Conflicto**
```
I -> try I catch I . finally I {$, ;}
I -> try I catch I . {$, ;}
I -> I . ; I {finally, ;, $}
```

**Avanzar:**
* `finally => I17`
* `;       => I18`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I`
  * Resuelto con `Shift ;`, ya que catch tiene menor precedencia que `;`

### **I13**
```
I -> try . I catch I finally I {finally, ;, $}
I -> try . I catch I {finally, ;, $}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I19`
* `try     => I6`
* `instr   => I7`

### **I14**
```
I -> instr . {finally, ;, $}
```

**Avanzar:**
None

### **I15** **Conflicto**
```
I -> I ; I . {catch, ;}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `;       => I10`

**Conflicto:**
- `Shift ;, Reduce I -> I ; I`
  * Resuelto con `Reduce I -> I ; I`  ya que `;` asocia a izquierda.

### **I16**
```
I -> try I catch . I finally I {catch, ;}
I -> try I catch . I {catch, ;}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}
```

**Avanzar:**
* `I       => I20`
* `try     => I21`
* `instr   => I22`

### **I17**
```
I -> try I catch I finally . I {$, ;}
I -> . try I catch I finally I {$, ;}
I -> . try I catch I {$, ;}
I -> . I ; I {$, ;}
I -> . instr {$, ;}
```

**Avanzar:**
* `I       => I23`
* `try     => I2`
* `instr   => I3`

### **I18**
```
I -> I ; . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}
```

**Avanzar:**
* `I       => I24`
* `try     => I13`
* `instr   => I14`

### **I19**
```
I -> try I . catch I finally I {finally, ;, $}
I -> try I . catch I {finally, ;, $}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `catch   => I25`
* `;       => I10`

### **I20** **Conflicto**
```
I -> try I catch I . finally I {catch, ;}
I -> try I catch I . {catch, ;}
I -> I . ; I {finally, ;, catch}
```

**Avanzar:**
* `finally => I26`
* `;       => I27`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I`
  * Resuelto con `Shift ;`, ya que `catch` tiene menor precedencia que `;`

### **I21**
```
I -> try . I catch I finally I {finally, ;, catch}
I -> try . I catch I {finally, ;, catch}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I28`
* `try     => I6`
* `instr   => I7`

### **I22**
```
I -> instr . {finally, ;, catch}
```

**Avanzar:**
None

### **I23** **Conflicto**
```
I -> try I catch I finally I . {$, ;}
I -> I . ; I {$, ;}
```

**Avanzar:**
* `;       => I4`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I finally I`
  * Resuelto con `Reduce I -> try I catch I finally I` ya que `finally` tiene mayor precedencia que `;`.

### **I24**
```
I -> I ; I . {finally, ;, $}
I -> I . ; I {finally, ;, $}
```

**Avanzar:**
* `;       => I18`

Shift ;, Reduce I -> I ; I

### **I25**
```
I -> try I catch . I finally I {finally, ;, $}
I -> try I catch . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}
```

**Avanzar:**
* `I       => I29`
* `try     => I13`
* `instr   => I14`

### **I26**
```
I -> try I catch I finally . I {catch, ;}
I -> . try I catch I finally I {catch, ;}
I -> . try I catch I {catch, ;}
I -> . I ; I {catch, ;}
I -> . instr {catch, ;}
```

**Avanzar:**
* `I       => I30`
* `try     => I6`
* `instr   => I7`

### **I27**
```
I -> I ; . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}
```

**Avanzar:**
* `I       => I31`
* `try     => I21`
* `instr   => I22`

### **I28**
```
I -> try I . catch I finally I {finally, ;, catch}
I -> try I . catch I {finally, ;, catch}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `catch   => I32`
* `;       => I10`

### **I29** **Conflicto**
```
I -> try I catch I . finally I {finally, ;, $}
I -> try I catch I . {finally, ;, $}
I -> I . ; I {finally, ;, $}
```

**Avanzar:**
* `finally => I33`
* `;       => I18`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I`
  * Resuelto con `Shift ;`, ya que `catch` tiene menor precedencia que `;`.
- `Shift finally, Reduce I -> try I catch I`
  * Resuelto con `Shift finally`, ya que `finally` tiene mayor precedencia que `;`

### **I30** **Conflicto**
```
I -> try I catch I finally I . {catch, ;}
I -> I . ; I {catch, ;}
```

**Avanzar:**
* `;       => I10`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I finally I`
  * Resuelto con` Reduce I -> try I catch I finally I`, ya que `finally` tiene mayor precedencia que `;`.

### **I31** **Conflicto**
```
I -> I ; I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}
```

**Avanzar:**
* `;       => I27`

**Conflicto:**
- `Shift ;, Reduce I -> I ; I`
  * Resuelto con `Reduce I -> I ; I`, ya que `;` asocia a la izquierda.

### **I32**
```
I -> try I catch . I finally I {finally, ;, catch}
I -> try I catch . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}
```

**Avanzar:**
* `I       => I34`
* `try     => I21`
* `instr   => I22`

### **I33**
```
I -> try I catch I finally . I {finally, ;, $}
I -> . try I catch I finally I {finally, ;, $}
I -> . try I catch I {finally, ;, $}
I -> . I ; I {finally, ;, $}
I -> . instr {finally, ;, $}
```

**Avanzar:**
* `I       => I35`
* `try     => I13`
* `instr   => I14`

### **I34** **Conflicto**
```
I -> try I catch I . finally I {finally, ;, catch}
I -> try I catch I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}
```

**Avanzar:**
* `finally => I36`
* `;       => I27`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I`
  * Resuelto con `Shift ;`, ya que `catch` tiene menor precedencia que `;`.
- `Shift finally, Reduce I -> try I catch I`
  * Resuelto con `Shift finally`, ya que `finally` se asocia al `try` más interno.

### **I35** **Conflicto**
```
I -> try I catch I finally I . {finally, ;, $}
I -> I . ; I {finally, ;, $}
```

**Avanzar:**
* `;       => I18`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I finally I`
  * Resuelto con `Reduce -> I try I catch I finally I` ya que `finally` tiene mayor precedencia que `;`.

### **I36**
```
I -> try I catch I finally . I {finally, ;, catch}
I -> . try I catch I finally I {finally, ;, catch}
I -> . try I catch I {finally, ;, catch}
I -> . I ; I {finally, ;, catch}
I -> . instr {finally, ;, catch}
```

**Avanzar:**
* `I       => I37`
* `try     => I21`
* `instr   => I22`

### **I37** **Conflicto**
```
I -> try I catch I finally I . {finally, ;, catch}
I -> I . ; I {finally, ;, catch}
```

**Avanzar:**
* `;       => I27`

**Conflicto:**
- `Shift ;, Reduce I -> try I catch I finally I`
  * Resuelto con `Reduce I -> try I catch I finally I` ya que `finally` tiene mayor precedencia que `;`.
