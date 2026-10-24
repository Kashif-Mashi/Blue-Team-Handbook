# Regular Expressions (Regex) Cheatsheet

> **Operational Quick Reference for System Administrators & Security Analysts**  
> Companion detailed notes: [02-Regular-Expressions.md](../04-Networking/02-Regular-Expressions.md)

---

## 🔣 Regex Metacharacters Quick Matrix

| Metacharacter | Name | Operational Matching Behavior | Example Match |
|:---:|---|---|---|
| **`^`** | Caret Anchor | Matches the absolute beginning of a line | `^root` matches lines starting with `root` |
| **`$`** | Dollar Anchor | Matches the absolute end of a line | `/bin/bash$` matches lines ending in shell |
| **`^$`** | Empty Line | Matches lines with zero characters between start & end | Used with `grep -v "^$"` to strip blank lines |
| **`.`** | Dot / Period | Matches any single character (except newline) | `r.t` matches `rot`, `r1t`, `r-t` |
| **`*`** | Kleene Star | Repeats the preceding token **0 or more times** | `colou*r` matches `color`, `colour` |
| **`+`** | Plus (ERE) | Repeats the preceding token **1 or more times** | `[0-9]+` matches one or more consecutive digits |
| **`?`** | Question (ERE)| Matches preceding token **0 or 1 time** (optional) | `https?` matches `http` or `https` |
| **`{n}`** | Exact Count | Matches preceding token exactly n times | `[0-9]{4}` matches 4 digits (e.g. `2026`) |
| **`{m,n}`**| Range (ERE) | Matches preceding token between m and n times | `[0-9]{1,3}` matches between 1 and 3 digits |
| **`\|`** | Alternation (ERE)| Logical **OR** between expressions | `ERROR\|WARNING` matches either word |
| **`(...)`** | Grouping (ERE)| Groups tokens together into a single unit | `(01\|02)` matches `01` or `02` |

---

## 📦 Character Sets and Bracket Classes

| Bracket Pattern | Character Set Definition | Matches | Negated Pattern (`[^...]`) |
|---|---|---|---|
| **`[0-9]`** | Any single decimal digit | `0`, `1`, `7`, `9` | `[^0-9]` (Any non-digit) |
| **`[a-z]`** | Any single lowercase letter | `a`, `k`, `z` | `[^a-z]` (Any non-lowercase) |
| **`[A-Z]`** | Any single uppercase letter | `A`, `M`, `Z` | `[^A-Z]` (Any non-uppercase) |
| **`[a-zA-Z]`** | Any single alphabet letter | `b`, `G`, `q` | `[^a-zA-Z]` (Symbols, numbers, spaces) |
| **`[0-9a-fA-F]`**| Any hexadecimal digit | `3`, `b`, `E`, `F` | Matches valid hex characters |

---

## ⚡ BRE vs. ERE: Syntax Comparison

| Feature | Basic Regular Expression (BRE - `grep`) | Extended Regular Expression (ERE - `grep -E` / `egrep`) |
|---|---|---|
| **Plus Quantifier** | Treated as literal `+`. Requires escape: `\+` | Native operator: `+` |
| **Optional Quantifier** | Treated as literal `?`. Requires escape: `\?` | Native operator: `?` |
| **Alternation (OR)** | Treated as literal `\|`. Requires escape: `\|` | Native operator: `\|` |
| **Interval Quantifier** | Requires escape: `\{1,3\}` | Native operator: `{1,3}` |
| **Subexpression Groups**| Requires escape: `\( ... \)` | Native operator: `( ... )` |

---

## 🔍 Practical Field Pattern & Log Triage One-Liners

```bash
# 1. Clean Configuration Files (Strip all comments and blank lines):
grep -v "^#" /etc/httpd/conf/httpd.conf | grep -v "^$"

# 2. Extract Valid IPv4 Addresses from Logs (-o prints only the match):
grep -E -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/httpd/access_log

# 3. Detect Failed SSH Login Attempts:
grep -E "Failed password for .* from [0-9.]+" /var/log/secure

# 4. Filter Users with Interactive BASH Logins:
grep "/bin/bash$" /etc/passwd

# 5. Case-Insensitive Multi-Keyword Log Search:
grep -E -i "error|critical|fatal|timeout" /var/log/messages

# 6. Parse Inventory Records (Start with 'A', 2-digit ID, end with 'DEV'):
grep -E "^A.*[0-9]{2}.*DEV$" records.txt
```
