# HTMap

A Krita plugin to copy HTML map-like reference coordinates to clipboard.
That is, using the format "`top-left-x, top-left-y, botton-right-x, bottom-right-y`".

## Usage

Run the script aftert making a selection.<br>
Your clipboard now has the value to be pasted into a `<map><area coords>` tag.<br>

## Installation

- Clone this repository.
`git clone git@github.com:fde-capu/htmap`

- Copy all to your `pykrita` directory.
  Example for Linux:
  - Make sure the directory exists:
  `mkdir -p ~/.local/share/krita/pykrita`
  - Do the copying:
  `cp -r htmap/* ~/.local/share/krita/pykrita`

This is how it will look like:

```
~.../pykrita
  ├── htmap
  │   ├── htmap.py
  │   ├── __init__.py
  │   └── Manual.html
  └── htmap.desktop
```

Restart Krita.

#### I need it.

If you find this plugin usefull, feel free to contribute to my existence in this world by donating:
[https://github.com/fde-capu/htmap](https://github.com/fde-capu/htmap).
