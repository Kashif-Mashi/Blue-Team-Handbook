# Regular Expressions (Regex) Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [02-Regular-Expressions.md](../04-Networking/02-Regular-Expressions.md) | [Cheatsheets Index](README.md)

---

## 🧩 Metacharacter Reference Guide

| Metacharacter | Pattern Meaning | Example Match | Note |
|:---:|---|---|---|
| `^` | **Line Start Anchor** | `^Root` matches "Root admin", not "The Root" | Binds match to column 1. |
| `$` | **Line End Anchor** | `bash$` matches "/bin/bash", not "bash shell" | Binds match to end of line. |
| `^$` | **Empty Line** | `grep -c '^$' file.txt` | Matches lines with zero characters. |
| `.` | **Any Character** | `r..t` matches "root", "rest", "r12t" | Matches any single character except newline. |
| `*` | **Zero or More** | `ab*c` matches "ac", "abc", "abbc", "abbbc" | Applies to immediately preceding token. |
| `+` | **One or More** (ERE) | `ab+c` matches "abc", "abbc" (not "ac") | Requires `grep -E` or `\+` in BRE. |
| `?` | **Zero or One** (ERE) | `https?` matches "http" and "https" | Requires `grep -E` or `\?` in BRE. |
| `\|` | **Alternation / OR** (ERE)| `error\|critical` matches either word | Requires `grep -E` or `\|` in BRE. |
| `()` | **Grouping** (ERE) | `(abc)+` matches "abc", "abcabc" | Groups sub-expressions. |
| `{n,m}` | **Range Quantifier** (ERE)| `[0-9]{2,4}` matches 2 to 4 digits | Requires `grep -E` or `\{n,m\}` in BRE. |

---

## 🔤 Character Classes and Sets

| Bracket Expression | Matches | Example Matches | Inverted Equivalent |
|---|---|---|---|
| `[0-9]` | Any single digit | `0`, `4`, `9` | `[^0-9]` (Any non-digit character) |
| `[a-z]` | Any lowercase letter | `a`, `k`, `z` | `[^a-z]` (Any non-lowercase character) |
| `[A-Z]` | Any uppercase letter | `A`, `M`, `Z` | `[^A-Z]` (Any non-uppercase character) |
| `[a-zA-Z]` | Any alphabet letter | `b`, `G`, `q` | `[^a-zA-Z]` (Symbols, numbers, spaces) |
| `[aeiou]` | Any lowercase vowel | `a`, `e`, `i`, `o`, `u` | `[^aeiou]` (Consonants and symbols) |
| `[0-9a-fA-F]` | Any hexadecimal digit | `3`, `b`, `E`, `F` | Matches valid hex characters |

---

## 🎓 Coursework & Field Pattern Reference

| Syllabus / Operational Pattern | Regex Syntax | Command Example | Expected Match Behavior |
|---|---|---|---|
| **Lines starting with capital 'A'** | `^A` | `grep '^A' students.txt` | Matches "Ali", "Ahmed", "Ayesha" at start of line. |
| **Lines starting with 'root'** | `^root` | `grep '^root' /etc/passwd` | Matches user `root` in `/etc/passwd`. |
| **Single numerical digit** | `[0-9]` | `grep '[0-9]' records.txt` | Matches any line containing at least one digit. |
| **Exactly two consecutive digits** | `[0-9][0-9]` | `grep '[0-9][0-9]' records.txt` | Matches two adjacent numbers (e.g., ages 18-99). |
| **Lines ending with 'BSCS'** | `BSCS$` | `grep 'BSCS$' students.txt` | Matches student records enrolled in BSCS program. |
| **Lines ending with interactive shell**| `/bin/bash$` | `grep '/bin/bash$' /etc/passwd` | Filters users with full interactive BASH logins. |
| **Filter out comments and blanks** | `grep -v '^#' \| grep -v '^$'` | `grep -v '^#' /etc/httpd/conf/httpd.conf \| grep -v '^$'` | Strips out all hash comments and blank whitespace lines. |
| **Extract valid IPv4 addresses** | `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}` | `grep -E -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' log.txt` | Extracts dotted-decimal IP addresses from logs. |

---

## ⚡ BRE vs. ERE: Syntax Comparison

| Feature | Basic Regular Expression (BRE - `grep`) | Extended Regular Expression (ERE - `grep -E` / `egrep`) |
|---|---|---|
| **Alternation (OR)** | `grep 'cat\|dog' file` | `grep -E 'cat|dog' file` |
| **One or More (`+`)** | `grep 'go\+l' file` | `grep -E 'go+l' file` |
| **Optional (`?`)** | `grep 'colou\?r' file` | `grep -E 'colou?r' file` |
| **Quantifiers (`{m,n}`)** | `grep '[0-9]\{2,4\}' file` | `grep -E '[0-9]{2,4}' file` |
| **Grouping** | `grep '\(abc\)\+' file` | `grep -E '(abc)+' file` |

> ⚠️ **Safety Tip:** Always enclose regex expressions in single quotes (`'...'`). If you omit quotes or use double quotes without escaping, the BASH shell will expand metacharacters (`*`, `$`, `?`) as filenames or variables before passing them to `grep`!
