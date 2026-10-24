# Regular Expressions Cheatsheet

| Pattern | Meaning | Example |
|---|---|---|
| `BSIT` | Contains literal text | `grep 'BSIT' students.txt` |
| `^A` | Starts with A | `grep '^A' students.txt` |
| `BSCS$` | Ends with BSCS | `grep 'BSCS$' students.txt` |
| `[0-9]` | Contains a digit | `grep '[0-9]' file.txt` |
| `[0-9][0-9]` | Two consecutive digits | `grep '[0-9][0-9]' file.txt` |
| `^[A-Z]` | Starts with uppercase letter | `grep '^[A-Z]' file.txt` |
| `grep -E 'cat|dog' file` | Extended regex alternation | Matches cat or dog |

`^` and `$` are line anchors. Regex syntax differs between tools; examples assume common GNU/Linux grep behavior. Quote patterns.
Related note: [Regular Expressions](../04-Networking/02-Regular-Expressions.md)
