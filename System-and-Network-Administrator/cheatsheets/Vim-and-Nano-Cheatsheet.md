# Vim and Nano Text Editors Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [07-Vim-and-Nano.md](../03-Linux-Fundamentals/07-Vim-and-Nano.md) | [Cheatsheets Index](README.md)

---

## 📝 Part 1: Nano Shortcuts (Modeless)

Notation: `^` = `Ctrl` key, `M-` = `Alt` key.

| Shortcut | Action | Operational Description |
|---|---|---|
| `Ctrl + O` | WriteOut (Save) | Prompts for target filename and writes buffer to disk (press Enter). |
| `Ctrl + X` | Exit | Quits Nano. Prompts to save (`Y` or `N`) if modifications exist. |
| `Ctrl + W` | Search ("Where Is") | Prompts for a search string and jumps to the first match. |
| `Ctrl + K` | Cut Line | Cuts the current line into Nano's internal pasteboard. |
| `Ctrl + U` | Uncut (Paste) | Pastes the recently cut line at the cursor's location. |
| `Ctrl + C` | Position Status | Displays current line, column, and character position. |
| `Ctrl + _` | Jump to Line Number | Prompts for line number and moves cursor directly. |
| `Ctrl + R` | Insert File | Reads and merges another file directly into the active buffer. |

---

## ⚡ Part 2: Vim Modal Architecture

| Mode | Purpose | How to Enter | How to Exit |
|---|---|---|---|
| **Normal Mode** | Navigation, copy, paste, delete lines | Default mode upon launch | Press `Esc` |
| **Insert Mode** | Direct text typing and editing | Press `i`, `I`, `a`, `A`, `o`, or `O` | Press `Esc` |
| **Command-Line (Ex)** | Saving, quitting, search/replace, configuration | Type `:` from Normal mode | Press `Esc` or `Enter` |
| **Visual Mode** | Highlighting and selecting text blocks | Type `v` (char), `V` (line), or `Ctrl+v` (block)| Press `Esc` |

---

## 🧭 Vim Normal Mode Navigation

| Key | Movement Action | Description |
|:---:|---|---|
| `h` / `j` / `k` / `l` | Left / Down / Up / Right | Cursor movement without leaving home row. |
| `w` / `b` | Forward / Backward Word | Jumps to start of next word (`w`) or previous word (`b`). |
| `0` (zero) / `$` | Start / End of Line | Jumps to absolute line start (`0`) or line ending (`$`). |
| `gg` | Top of File | Jumps instantly to the very first line of the document. |
| `G` | Bottom of File | Jumps instantly to the very last line of the document. |
| `:<number>` | Jump to Specific Line | e.g., `:52` followed by Enter jumps directly to line 52. |

---

## ✂️ Vim Editing, Copy, and Paste (Normal Mode)

| Command | Action | Operational Description |
|---|---|---|
| `i` / `a` | Insert / Append | Enter insert mode before cursor (`i`) or after cursor (`a`). |
| `o` / `O` | Open Line Below / Above | Inserts blank line below (`o`) or above (`O`) and enters Insert mode. |
| `x` | Delete Character | Deletes single character directly underneath the cursor. |
| `dd` | Delete (Cut) Line | Cuts the entire current line into the paste buffer. |
| `3dd` | Delete 3 Lines | Cuts current line and following 2 lines. |
| `dw` | Delete Word | Cuts from current cursor position to end of word. |
| `yy` | Yank (Copy) Line | Copies the entire current line into the paste buffer. |
| `3yy` | Yank 3 Lines | Copies current line and following 2 lines. |
| `p` / `P` | Paste Below / Above | Pastes buffer below current line (`p`) or above (`P`). |
| `u` | Undo | Undoes the previous modification. |
| `Ctrl + r` | Redo | Redoes the previously undone modification. |

---

## 🔍 Vim Search and Replace

| Command / Pattern | Scope | Description |
|---|---|---|
| `/pattern` | Search Forward | Type `/` followed by search string and press Enter. |
| `n` / `N` | Next / Previous Match | Jump to next occurrence (`n`) or reverse direction (`N`). |
| `:s/old/new/` | Current Line | Replaces first occurrence of 'old' with 'new' on current line. |
| `:s/old/new/g` | Current Line (All) | Replaces all occurrences on the current line. |
| `:%s/old/new/g` | Entire File (All) | Globally replaces all occurrences across the entire document. |
| `:%s/old/new/gc` | Entire File with Confirm | Prompts `(y/n/a/q)` before replacing each match. |

---

## 💾 Vim Saving, Exiting, and Recovery

| Command | Action | Description |
|---|---|---|
| `:w` | Write (Save) | Writes buffer to disk without exiting. |
| `:wq` | Write and Quit | Writes changes to disk and terminates Vim. |
| `:x` | Safe Exit | Saves only if changes were made, then terminates (preferred). |
| `:q` | Quit | Exits Vim. Fails if unsaved modifications exist. |
| `:q!` | Force Quit | `⚠️ DISCARDS CHANGES` Exits immediately without saving modifications. |
| `:set number` | Show Line Numbers | Displays line number margin on the left. |
| `:set nonumber` | Hide Line Numbers | Removes line number margin. |

### Resolving Vim Swap File (`.swp`) Prompts
When a terminal session disconnects unexpectedly, reopening the file shows `ATTENTION: Found a swap file`.
1. Press **`R`** to recover unsaved changes.
2. Confirm the edits and save: `:wq`.
3. ⚠️ **Manually remove the hidden swap file**, or the prompt will repeat:
   ```bash
   rm /path/to/.filename.swp
   ```
