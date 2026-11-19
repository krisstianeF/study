Bash stands for Bourne Again SHell, and is arguably the most common shell you will encounter in Unix-like environments. As such, it can be very beneficial to understand how to navigate this shell and use the common commands.

[Bash Review](https://www.freecodecamp.org/learn/relational-databases-v9/review-bash-commands/review-bash-commands)

## CLI Shortcuts Reference

| Action | Input | Availability or context |
| :--- | :--- | :--- |
| Move backward | `Up Arrow` | Linux, macOS, and PowerShell |
| Move forward | `Down Arrow` | Linux, macOS, and PowerShell |
| Complete a suggestion | `Tab` | Linux, macOS, and PowerShell (suggestions depend on the shell, the command you are typing, and your configuration) |
| Clear the terminal | `Control` + `L` | Linux, macOS, and PowerShell (PowerShell's `cls` command clears the screen the same way) |
| Stop a running process | `Control` + `C` | Linux, macOS, and PowerShell (in PowerShell this also copies text, and only interrupts a command when nothing is selected to copy) |
| Suspend the foreground process | `Control` + `Z` | Linux and macOS only, no PowerShell alternative (use `bg` to resume it in the background or `fg` to resume it in the foreground) |
| Rerun the previous command | `!!` | Linux and macOS only, no PowerShell alternative |


## Creating project

```bash
cd project_path
```
```bash
mkdir new_directory_name
```
```bash
touch new_file_name
```
```bash
cp <file> <destination>
```
```bash
mv <filename> <new_filename>/<destination>
```
```bash
echo text >> filename
```

## Options & Flags — Syntax

| Type | Syntax | Example | Description |
| :--- | :--- | :--- | :--- |
| Long | `--option` | `ls --help` |  |
| Short | `-o` | `ls -a` | Single-letter flag |
| Chained | `-abc` | `ls -ahs` | Combine short flags |
| Short + Value | `-o value` | `ls -w 50` | Value after space |
| Long + Value | `--opt=val` / `--opt val` | `ls --width=50` | Value via `=` or space |
| Optional Value | `--opt=val` | `ls --color=never` | Must use `=`; space makes value a filename |


## Bash Scripting

### Operators

File test operators

`-e file`: True if file `exists`
`-f file`: True if file `exists and is a regular file`
`-d file`: True if file `exists and is a directory`
`-r file`: True if file `exists and is readable`
`-w file`: True if file `exists and is writable`
`-x file`: True if file `exists and is executable`
`-s file`: True if file `exists and has size greater than zero`

`-eq` (equal)
`-ne` (not equal)
`-lt` (less than)
`-le` (less than or equal)
`-gt` (greater than)
`-ge` (greater than or equal)

Arithmetic operators

`+` addition
`-` subtraction
`*` multiplication
`/` division
`%` modulo
`**` exponentiation

Assignment operators

`=` assignment
`+=` add and assign
`-=` subtract and assign
`*=` multiply and assign
`/=` divide and assign
`%=` modulo and assign

`++variable` pre-increment
`variable++` post-increment
`--variable` pre-decrement
`variable--` post-decrement

Comparison operators

`==` equal
`!=` not equal
`<` less than
`<=` less than or equal
`>` greater than
`>=` greater than or equal

Bitwise operators: Perform bit-level operations on integers.

`&` (bitwise AND): AND operation on each bit
`\|` (bitwise OR): OR operation on each bit
`^` (bitwise XOR): XOR operation on each bit
`~` (bitwise NOT): Invert all bits
`<<` (left shift): Shift bits to the left
`>>` (right shift): Shift bits to the right

### Exit Status & Command Chaining

| Symbol / Var | Meaning |
|---|---|
| `$?` | Last exit status (`0` = ok) |
| `127` | Command not found |
| `1` | General error |
| `cmd1; cmd2` | Run sequentially |
| `cmd1 && cmd2` | `cmd2` if `cmd1` succeeds |
| `cmd1 \|\| cmd2` | `cmd2` if `cmd1` fails |
| `cmd1 & cmd2` | `cmd1` in background |

### Subshells & Command Substitution

| Syntax | Meaning |
|---|---|
| `( cmds )` | Subshell — separate env, parent vars unchanged |
| `$( cmd )` | Capture stdout as string |
| `$(( expr ))` | Capture arithmetic result |
| `cmd &` | Background |
| `wait` | Wait for background jobs |


## Nano

 Open (and create if not exist) the file:
```bash
nano filename
```
|  |  |
|--|--|
`ctrl` + `k` | clear the line you on
`ctrl` + `x` | exit
`ctrl` + `o` then `enter` | save file

```
^G Help   ^O Write Out    ^F Where Is   ^K Cut      ^T Execute  ^C Location     M-U Undo    M-A Set Mark    M-] To Bracket    M-B Previous
^X Exit   ^R Read File    ^\ Replace    ^U Paste    ^J Justify  ^/ Go To Line   M-E Redo    M-6 Copy        ^B Where Was      M-F Next
```