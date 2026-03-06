## 2

**Output**
```bash
-- specification  G (Bit1 <->  X Bit1)  is false
-- as demonstrated by the following execution sequence
Trace Description: LTL Counterexample 
Trace Type: Counterexample 
  -> State: 1.1 <-
    Bit1 = FALSE
    Bit2 = FALSE
    state = s1
  -> Input: 1.2 <-
    input = FALSE
  -> State: 1.2 <-
  -> Input: 1.3 <-
    input = TRUE
  -> State: 1.3 <-
    Bit1 = TRUE
    state = s2
  -> Input: 1.4 <-
  -- Loop starts here
  -> State: 1.4 <-
    Bit2 = TRUE
    state = s4
  -> Input: 1.5 <-
  -- Loop starts here
  -> State: 1.5 <-
  -> Input: 1.6 <-
  -> State: 1.6 <-
  ```

The program finds a counterexample where `Bit1` changes value. For model-checker implementation reasons it also finds an infinite loop. 

## 3

### a)
**Counterexample:**
```bash
-- specification  G !(state = stop)    is false
-- as demonstrated by the following execution sequence
Trace Description: BMC Counterexample 
Trace Type: Counterexample 
  -> State: 1.1 <-
    state = stop
-- no counterexample found with bound 0
```

### b)

`G !(state = stop)`
| | t0 
| --- | --- 
inputs | 
outputs | stop

### c)

`G !(state = slow) `
|       |  t0  | t1
| ---   | ---  | ---
inputs  |  accelerate |
outputs | stop | slow

`G !(state = fast) `
|       |  t0  | t1 | t2
| ---   | ---  | --- | ---
inputs  |  accelerate | accelerate |
outputs | stop | slow | fast

## 4

### a)
**Counterexample**
```bash
-- specification  G ((state = stop & accelerate) ->  X !(state = slow))    is false
-- as demonstrated by the following execution sequence
Trace Description: BMC Counterexample 
Trace Type: Counterexample 
  -> State: 1.1 <-
    state = stop
  -> Input: 1.2 <-
    accelerate = TRUE
    brake = FALSE
  -> State: 1.2 <-
    state = slow
```

### b)

`G ((state = stop & accelerate) ->  X !(state = slow))`
|       |  t0  | t1
| ---   | ---  | ---
inputs  | accelerate |
outputs | stop | slow
 
### c)

Since LTL can only make assertions about the states and variables, the "edges" are implied by the formula. If there are multiple ways to transition from one state to another, it's important to constrain the formula in a way that ensures the correct edge is taken. Otherwise the test cases may falsly give 100% EC, even if the tests do not actually take every edge. 

To ensure we take the "!accelerate" edge, we must also not brake, since if we did, we would have no way of knowing if the "!accelerate" edge was taken or the "brake" edge was taken.

`G (((state = slow & !accelerate) & !brake) ->  X !(state = stop))`
|       |  t0  | t1 | t2
| ---   | ---  | --- | ---
inputs  | accelerate | |
outputs | stop | slow | stop

Like before, if we want to ensure that the "brake" edge is taken, which means we can't allow "!accelerate". So counterintuatively we must accelerate to take the brake edge. Notably there is an edge for "accelerate", but since this edge takes us to the "fast" state, our LTL expression can discern which edge was taken regardless. 

`G (((state = slow & brake) & accelerate) ->  X !(state = stop))`

|       |  t0  | t1 | t2
| ---   | ---  | --- | ---
inputs  | accelerate | brake, accelerate |
outputs | stop | slow | stop

`G ((state = slow & accelerate) ->  X !(state = fast))`

|       |  t0  | t1 | t2
| ---   | ---  | --- | ---
inputs  | accelerate | accelerate |
outputs | stop | slow | fast

`G ((state = fast & brake) ->  X !(state = stop))`

|       |  t0  | t1 | t2 | t3
| ---   | ---  | --- | --- | ---
inputs  | accelerate | accelerate | brake
outputs | stop | slow | fast | stop


`G ((state = fast & !accelerate) ->  X !(state = slow))`

|       |  t0  | t1 | t2 | t3
| ---   | ---  | --- | --- | ---
inputs  | accelerate | accelerate | 
outputs | stop | slow | fast | slow

