# 🐧 MintWatch

> A lightweight Linux system observer built to understand what is happening under the hood.

MintWatch is a small Python project for observing and understanding a Linux machine from the terminal.

The idea is simple:

**ask Linux what's happening — and make the answer useful to humans.**

This project started as a hands-on experiment while learning more about Linux, Python, shell environments, system information, and terminal tooling.

It is intentionally being built incrementally, from the filesystem and `/proc` all the way to a useful terminal dashboard.

---

## Why MintWatch?

Linux already exposes a huge amount of information about itself.

Operating system details, uptime, memory, processes, disks, network activity and much more are available through interfaces such as:

```text
/etc/os-release
/proc
/sys
```

MintWatch explores those interfaces and turns them into a simple, readable view of the machine.

The goal isn't to reinvent `top`, `htop`, `neofetch` or other excellent tools.

The goal is to **learn by building**.

---

## Current status

🚧 **Early development — v0.1.0**

The project currently has:

* Python project structure using `src/`
* isolated virtual environment
* editable package installation
* Git + GitHub workflow
* Linux OS information collection
* basic OS name detection

Example:

```python
from mintwatch.system import get_os_name

print(get_os_name())
```

```text
Linux Mint
```

---

## Roadmap

The first versions will progressively explore different parts of the Linux system.

### System information

* [x] Operating system
* [x] OS name
* [ ] OS version
* [ ] Kernel version
* [ ] Hostname
* [ ] Uptime

### Hardware & resources

* [ ] CPU usage
* [ ] Memory usage
* [ ] Disk usage
* [ ] Disk I/O
* [ ] Network statistics
* [ ] Temperature

### Processes

* [ ] Running processes
* [ ] CPU-hungry processes
* [ ] Memory-hungry processes
* [ ] Process tree

### Terminal experience

* [ ] Human-readable output
* [ ] Rich terminal interface
* [ ] Live monitoring mode
* [ ] Configurable views

### Future ideas

* [ ] Historical metrics
* [ ] Parquet-based storage
* [ ] Optional dashboard
* [ ] Alerts
* [ ] More Linux internals

---

## Project structure

```text
mintwatch/
├── src/
│   └── mintwatch/
│       ├── __init__.py
│       ├── cli.py
│       └── system.py
├── tests/
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## Development

Clone the repository and create a virtual environment:

```bash
git clone <repository-url>
cd mintwatch

python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

---

## Philosophy

MintWatch is being built with a simple rule:

> **Understand the thing before abstracting it.**

Instead of immediately reaching for a library, the project will first explore what Linux itself provides.

Instead of building a huge architecture, each feature should earn its place.

Instead of optimizing for complexity, optimize for understanding.

---

## License

License to be defined.
