# bu bir denemedir mesela
```c
#include "graphics.c"
#include "font.c"
#include "input.c"
#include "graphics_elements.c"
#include "task.c"
#include "main.c"
```

## Mesela bir de python dosyası deneyelim

lorem ipsum sit amet

```python
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

input_stream = InputStream(input('? '))

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))


```
