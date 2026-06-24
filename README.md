# Checksum Checker

A lightweight, cross-platform Command Line Interface tool built in Python to generate and verify file checksums. Doesn't require any dependencies.

## 🚀 Features

- **Generate Checksums:** Computes the hash of any file using algorithms like SHA-256, SHA-1, MD5, etc.
- **Verify Integrity:** Matches a file's calculated checksum against an expected hash string to detect file corruption or any tampering.
- **Memory Efficient:** Processes large files safely in small chunks which is better for memory.
- **Cross-Platform:** Works natively on Windows, macOS, and Linux thanks to math and Python's built-in hashlib.

## Prerequisites

- **Python 3.10 or higher** (The script utilizes structural pattern matching `match/case` syntax).
- No external libraries are necessary.

## Usage

1. Clone or download this repository to your local machine.

`git clone github.com/piarsquared/Checksum-Checker`

3. Open your terminal or command prompt and navigate to the project directory.
4. Run the script using Python:

`python checksum_tool.py`
