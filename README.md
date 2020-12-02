# Sourcecode-Handwriting-Analysis
*Made by Chu7zpah*

This project analyze programmer's source code graphology with 5 Categories 14 Features.


## Features
### Feature 1. Brace('{') Habits
* Case 1: 'FUNCTION(){'       (**inline** brace with **NO** Space)
            
* Case 2: 'FUNCTION() {'      (**inline** brace **with** Space)
            
* Case 3: 'FUNCTION()\n {'    (**next line** brace)

          
                     
### Feature 2. Comment('//' or '/* */') Habits
        
* Case 1: '//COMMENT'         ('//' with **NO** Space)
            
* Case 2: '// COMMENT'        ('//' **with** Space)
            
* Case 3: '/* COMMENT */'     (Using ' /\* */')
            
### Feature 3. Parenthesis('(') Habits
        
* Case 1: '{if/switch/while/for}('    (Reserved words with **No** Space)
            
* Case 2: '{if/switch/while/for} ('   (Reserved words **with** Space)
            
### Feature 4. Unary Operator(Type Casting) Habits
        
* Case 1: '(TYPE)VARIABLE'        (Type Casting with **NO** Space)
            
* Case 2: '(TYPE) VARIABLE'       (Type Casting **with** Space)
            
        
### Feature 5. Binary Operator(Arithmetic, Assignments, etc.) Habits
        
ex) '+' Operator
            
* Case 1: 'VARIABLE+VARIABLE'     (**NO** Space && Binary Operator && **NO** Space)
            
* Case 2: 'VARIABLE+ VARIABLE'    (**NO** Space && Binary Operator && **Space**)
            
* Case 3: 'VARIABLE +VARIABLE'    (**Space** && Binary Operator && **NO** Space)
            
* Case 4: 'VARIABLE + VARIABLE'   (**Space** && Binary operator && **Space**)
