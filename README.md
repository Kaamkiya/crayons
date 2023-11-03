# crayons

crayons is a Python module to print things with color and other special effects in the terminal.

It uses [ANSI escape sequences](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences) to do this.

## Installation

> [!NOTE]
> git is **required** for installation.

Run the following command to install crayons:

```bash
pip install git+https://github.com/Kaamkiya/crayons.git
```

If `pip` doesn't work, try `pip3`.

This will clone all of the files in the repo, and allow you to import it as a module. 

## Usage

To first test to see if you have crayons installed, enter the following:

```bash
python -m crayons
```

This should print something like this:

![Example Output](https://github.com/Kaamkiya/crayons/assets/138614660/f0e55c26-c6fc-4bb7-ab66-b69ea88ba360)


If it doesn't, try `python3` instead of `python` or file a bug report.

## What you can do

The crayons module comes with the following functions:

* `fg`
* `bg`
* `fg_rgb`
* `bg_rgb`
* `effect`
* `goto`
* `reset`

---

`fg` sets the foreground color of the text, and `bg` sets the background color. 

Permitted values for these two functions are:

* `red`
* `green`
* `yellow`
* `blue`
* `purple`
* `cyan`

---

The next two functions are `fg_rgb` and `bg_rgb`.

They set the background and foreground color, respectively, of the output.

For example, `fg_rgb(170, 170, 255)` would set the foreground color to a light blue.

---

`effect` sets a text effect for the output.

Currently, the only supported option is 'bold'.

---

`goto` sets the cursor position in the terminal.

`goto(4, 7)` would move the cursor to the fourth column and seventh row.

---

`size` returns two values: the width and height of the terminal.

---

`reset` resets all of the settings back to normal.
