# Physics Thought Experiment Journal ⚛

**By KyberPhantasma**
**Status: Work in Progress — Vol. I**

---

## Overview

An interactive command-line journal of structured physics thought experiments.
Each entry covers a deep concept in modern physics — from sonoluminescence
to the incompatibility of Quantum Mechanics and General Relativity.

Built in Python to demonstrate structured data handling, object-oriented
design, and clean CLI architecture.

---

## Entries

| ID | Title | Subtitle |
|---|---|---|
| 001 | Sonoluminescence | When Sound Becomes Light |
| 002 | Quantum Mechanics | Reality as Probability |
| 003 | Relativity | Space, Time and the Speed of Light |
| 004 | QM and Relativity | The Great Divide |
| 005 | The Fabric of Spacetime | Geometry as Physics |
| 006 | Time and Light | The Photon's Eternal Present |

---

## How to Run

**Requirements:** Python 3.6+ (no external libraries needed)

```bash
python main.py
```

**Example commands:**

```
JOURNAL › index
JOURNAL › read 1
JOURNAL › questions 4
JOURNAL › insight 6
JOURNAL › search quantum
JOURNAL › search time
JOURNAL › progress
```

Each entry has five sections you can read independently:
`abstract` · `setup` · `observation` · `questions` · `insight`

---

## Project Structure

```
physics-thought-experiment-journal/
│
├── main.py       # Entry point — interactive journal terminal
├── journal.py    # Journal class — display, search, read tracking
├── entries.py    # All thought experiment content (data layer)
└── README.md     # This file
```

---

## Concepts Demonstrated

- Object-Oriented Programming (classes, methods, encapsulation)
- Separation of concerns (data layer, logic layer, UI layer)
- String formatting and text wrapping
- List and dictionary manipulation
- User input handling and command parsing
- Search across nested data structures
- Progress tracking with sets

---

## Roadmap

- [ ] Export entries to formatted PDF or Markdown files
- [ ] Add LaTeX equation rendering for formulas
- [ ] Add more entries: Thermodynamics, Electromagnetism, Cosmology
- [ ] Build a quiz mode testing comprehension of each entry
- [ ] Add a comparison mode to contrast two entries side by side

---

*"The most beautiful thing we can experience is the mysterious." — Einstein*
