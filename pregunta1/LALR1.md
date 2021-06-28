# Máquina Característica LALR(1)

### **I0**
```
S -> . I $ {$}
I -> . try I catch I finally I    {$, ;}
I -> . try I catch I              {$, ;}
I -> . I ; I                      {$, ;}
I -> . instr                      {$, ;}
```

**Avanzar:**
* `I       => I1`
* `try     => I2`
* `instr   => I3`

### **I1**
```
S -> I . $                        {$}
I -> I . ; I                      {$, ;}
```

**Avanzar:**
* `;       => I4`

### **I2,6,13,21**
```
I -> try . I catch I finally I    {$, ;, catch, finally}
I -> try . I catch I              {$, ;, catch, finally}
I -> . try I catch I finally I    {catch, ;}
I -> . try I catch I              {catch, ;}
I -> . I ; I                      {catch, ;}
I -> . instr                      {catch, ;}
```

**Avanzar:**
* `I       => I5,11,19,28`
* `try     => I2,6,13,21`
* `instr   => I3,7,14,22`

### **I3,7,14,22**
```
I -> instr .                      {$, ;, catch, finally}
```

**Avanzar:**
None

### **I4,10,18,27**
```
I -> I ; . I                      {$, ;, catch, finally}
I -> . try I catch I finally I    {$, ;, catch, finally}
I -> . try I catch I              {$, ;, catch, finally}
I -> . I ; I                      {$, ;, catch, finally}
I -> . instr                      {$, ;, catch, finally}
```

**Avanzar:**
* `I       => I8,15,24,31`
* `try     => I2,6,13,21`
* `instr   => I3,7,14,22`

### **I5,11,19,28**
```
I -> try I . catch I finally I    {$, ;, catch, finally}
I -> try I . catch I              {$, ;, catch, finally}
I -> I . ; I                      {catch, ;}
```

**Avanzar:**
* `catch   => I9,16,25,32`
* `;       => I4,10,18,27`

### **I8,15,24,31**
```
I -> I ; I .        {$, ;, catch, finally}
I -> I . ; I        {$, ;, catch, finally}
```

**Avanzar:**
* `;       => I4,10,18,27`



### **I9,16,25,32**
```
I -> try I catch . I finally I      {finally, ;, $, catch}
I -> try I catch . I                {finally, ;, $, catch}
I -> . try I catch I finally I      {finally, ;, $, catch}
I -> . try I catch I                {finally, ;, $, catch}
I -> . I ; I                        {finally, ;, $, catch}
I -> . instr                        {finally, ;, $, catch}
```

**Avanzar:**
* `I       => I12,20,29,34`
* `try     => I2,6,13,21`
* `instr   => I3,7,14,22`

### **I12,20,29,34**
```
I -> try I catch I . finally I      {$, ;, catch, finally}
I -> try I catch I .                {$, ;, catch, finally}
I -> I . ; I                        {finally, ;, $, catch}
```

**Avanzar:**
* `finally => I17,26,33,36`
* `;       => I4,10,18,27`

### **I17,26,33,36**
```
I -> try I catch I finally . I        {$, ;, catch, finally}
I -> . try I catch I finally I        {$, ;, catch, finally}
I -> . try I catch I                  {$, ;, catch, finally}
I -> . I ; I                          {$, ;, catch, finally}
I -> . instr                          {$, ;, catch, finally}
```

**Avanzar:**
* `I       => I23,30,35,37`
* `try     => I2,6,13,21`
* `instr   => I3,7,14,22`

### **I23,30,35,37**
```
I -> try I catch I finally I .        {$, ;, catch, finally}
I -> I . ; I                          {$, ;, catch, finally}
```

**Avanzar:**
* `;       => I4,10,18,27`
