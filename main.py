# main.py
# Entry point for the Physics Thought Experiment Journal.
# Run this file to launch the interactive journal terminal.
# Author: KyberPhantasma
#
# Usage:
#   python main.py
#
# Requirements:
#   Python 3.6+
#   No external libraries — runs on Pydroid3

from journal import Journal


BANNER = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     PHYSICS THOUGHT EXPERIMENT JOURNAL                   ║
║     KyberPhantasma — Vol. I                              ║
║                                                          ║
║     Sonoluminescence · Quantum Mechanics                 ║
║     Relativity · QM & GR · Spacetime · Light & Time      ║
║                                                          ║
║     "The universe is under no obligation to make         ║
║      sense to you." — Neil deGrasse Tyson                ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""

HELP_TEXT = """
┌─────────────────────────────────────────────────────┐
│  JOURNAL COMMAND REFERENCE                          │
├─────────────────────────────────────────────────────┤
│  index              — List all entries              │
│  read <id>          — Read full entry  (e.g. read 1)│
│  abstract <id>      — Entry abstract only           │
│  setup <id>         — Experiment setup only         │
│  observation <id>   — Observation only              │
│  questions <id>     — Open questions only           │
│  insight <id>       — Core insight only             │
│  search <keyword>   — Search all entries            │
│  progress           — Show reading progress         │
│  help               — Show this menu                │
│  exit               — Close the journal             │
├─────────────────────────────────────────────────────┤
│  EXAMPLES:                                          │
│  read 1                                             │
│  read 4                                             │
│  questions 2                                        │
│  insight 6                                          │
│  search quantum                                     │
│  search time                                        │
└─────────────────────────────────────────────────────┘
"""


def resolve_entry(journal, arg):
    """
    Resolve an entry from user input.
    Accepts a number (1-6) or a zero-padded ID (001-006).
    Returns the entry dict or None.
    """
    arg = arg.strip()
    # Try as a 1-based index first
    if arg.isdigit():
        index = int(arg) - 1
        entry = journal.get_by_index(index)
        if entry:
            return entry
    # Try as a direct ID
    entry = journal.get_by_id(arg)
    return entry


def run():
    """Main interactive loop for the Physics Journal."""
    print(BANNER)

    journal = Journal()

    print(f"  Journal loaded. {journal.count()} entries available.")
    print("  Type 'index' to see all entries or 'help' for commands.\n")

    while True:
        try:
            raw = input("JOURNAL › ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Journal closed. Keep questioning.\n")
            break

        if not raw:
            continue

        parts = raw.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1].strip() if len(parts) > 1 else ""

        # ── Commands ──────────────────────────────────────────────

        if command == "exit":
            print("\n  Journal closed. Keep questioning.\n")
            break

        elif command == "help":
            print(HELP_TEXT)

        elif command == "index":
            print(journal.format_index())

        elif command == "progress":
            read = len(journal.read_log)
            total = journal.count()
            bar_filled = int((read / total) * 30)
            bar = "█" * bar_filled + "░" * (30 - bar_filled)
            print(f"\n  Reading Progress")
            print(f"  [{bar}] {read}/{total} entries read.\n")

        elif command == "search":
            if not argument:
                print("  Usage: search <keyword>")
            else:
                results = journal.search(argument)
                print(journal.format_search_results(argument, results))

        elif command in ("read", "abstract", "setup", "observation", "questions", "insight"):
            if not argument:
                print(f"  Usage: {command} <entry number>  (e.g. {command} 1)")
            else:
                entry = resolve_entry(journal, argument)
                if not entry:
                    print(f"  Entry '{argument}' not found. Type 'index' to list all entries.")
                else:
                    # Map command to section name
                    section = "all" if command == "read" else command
                    journal.mark_read(entry["id"])
                    print(journal.format_entry(entry, section=section))

        else:
            # Allow shorthand: just typing a number opens the entry
            if raw.isdigit():
                entry = resolve_entry(journal, raw)
                if entry:
                    journal.mark_read(entry["id"])
                    print(journal.format_entry(entry))
                else:
                    print(f"  No entry at position {raw}.")
            else:
                print(f"  Unknown command: '{command}'. Type 'help' for options.")


if __name__ == "__main__":
    run()
