# Command-Line Text Editors Cheatsheet: Vim and Nano

> **Operational Quick Reference for System Administrators & BSIT Students**  
> Companion detailed notes: [07-Vim-and-Nano.md](../03-Linux-Fundamentals/07-Vim-and-Nano.md)

---

## 📝 GNU Nano Essential Shortcuts

$$\text{Note: The caret symbol}\ \mathbf{\hat{\ }}\ \text{represents the}\ \mathbf{Ctrl}\ \text{key}\quad (\text{e.g.,}\ \mathbf{\hat{\ }O} = \mathbf{Ctrl + O})$$

| Keystroke | Command Name | Operational Action Performed |
|---|---|---|
| **`Ctrl + O`** | **WriteOut** | Saves the file to disk without exiting |
| **`Ctrl + X`** | **Exit** | Closes Nano (prompts to save if modified) |
| **`Ctrl + W`** | **Where Is** | Searches for a text string forward |
| **`Ctrl + K`** | **Cut Line** | Deletes (cuts) the current line and stores it in buffer |
| **`Ctrl + U`** | **Uncut Line** | Pastes the cut buffer at the current cursor position |
| **`Ctrl + C`** | **Location** | Displays current line and column numbers |
| **`Ctrl + _`** | **Go To Line** | Prompts for a line number to jump to directly |
| **`Alt + U`** | **Undo** | Reverses the last text editing action |
| **`Alt + E`** | **Redo** | Re-applies the last undone editing action |

---

## ⚡ Vim Modal Engine Transitions

```text
[ NORMAL MODE ]  ──Press 'i', 'a', or 'o'──>  [ INSERT MODE ]
[ NORMAL MODE ]  <──────Press 'Escape'───────  [ INSERT MODE ]

[ NORMAL MODE ]  ─────Press 'v' or 'V'─────>  [ VISUAL MODE ]
[ NORMAL MODE ]  <──────Press 'Escape'───────  [ VISUAL MODE ]

[ NORMAL MODE ]  ───────Press ':' (Colon)───>  [ COMMAND-LINE (EX) MODE ]
[ NORMAL MODE ]  <──────Press 'Escape'───────  [ COMMAND-LINE (EX) MODE ]
```

---

## 🧭 Vim Normal Mode Navigation

| Key | Movement Action | Key | Movement Action |
|:---:|---|:---:|---|
| **`h`** | Move cursor Left one character | **`w`** | Jump forward to the start of next word |
| **`j`** | Move cursor Down one line | **`b`** | Jump backward to the start of previous word |
| **`k`** | Move cursor Up one line | **`0`** | Jump to absolute beginning of current line |
| **`l`** | Move cursor Right one character | **`$`** | Jump to absolute end of current line |
| **`gg`** | Jump to the very first line of file | **`G`** | Jump to the very last line of file |
| **`<N>G`** | Jump directly to line number N (e.g. `45G`) | **`H` / `L`**| Jump to High (top) or Low (bottom) of screen |

---

## ✂️ Vim Normal Mode Editing Commands

| Command | Action Performed | Command | Action Performed |
|:---:|---|:---:|---|
| **`x`** | Delete (cut) character under cursor | **`p`** | Paste yanked/cut buffer **below** cursor |
| **`dd`** | Delete (cut) current entire line | **`P`** | Paste yanked/cut buffer **above** cursor |
| **`<N>dd`**| Delete N consecutive lines (e.g., `5dd`) | **`u`** | **Undo** the last editing action |
| **`dw`** | Delete from cursor to start of next word | **`Ctrl + r`** | **Redo** the last undone action |
| **`d$`** | Delete from cursor to end of line | **`.`** | Repeat the immediately preceding command |
| **`yy`** | **Yank (copy)** current line into memory | **`<N>yy`** | Yank N lines into memory (e.g., `3yy`) |

---

## ✍️ Entering Insert Mode from Normal Mode

| Key | Action Performed |
|:---:|---|
| **`i`** | Insert text **before** the current cursor position |
| **`I`** | Insert text at the **start** of the current line |
| **`a`** | Append text **after** the current cursor position |
| **`A`** | Append text at the **end** of the current line |
| **`o`** | Open a brand-new blank line **below** the cursor and enter Insert Mode |
| **`O`** | Open a brand-new blank line **above** the cursor and enter Insert Mode |

---

## ⚙️ Vim Command-Line (Ex) Mode Commands

| Command | Action Performed |
|---|---|
| **`:w`** | Write (save) buffer to disk |
| **`:q`** | Quit Vim (fails if unsaved changes exist) |
| **`:wq`** or **`:x`** | Save changes and quit Vim cleanly (or `ZZ` in Normal Mode) |
| **`:q!`** | **Force quit immediately**, discarding all unsaved changes |
| **`:set number`** | Enable line numbering display (`:set nonumber` to disable) |
| **`/pattern`** | Search forward for pattern (press `n` for next match, `N` for previous) |
| **`:%s/old/new/g`** | **Search and replace globally** across entire file without confirmation |
| **`:%s/old/new/gc`**| Search and replace globally with interactive confirmation (`y/n`) |

---

## 🚨 Vim Crash & Swap File (`.swp`) Recovery

If your terminal disconnects while editing and Vim displays `E325: ATTENTION Found a swap file`:
1. Press **`R`** to recover unsaved changes into memory buffer.
2. Review text and save file: **`:wq`**
3. **Manually delete the residual hidden swap file:**
   ```bash
   rm .filename.swp
   ```
