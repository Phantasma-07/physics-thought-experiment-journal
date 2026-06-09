# journal.py
# The Journal class manages entry display, search,
# and navigation for the Physics Thought Experiment Journal.
# Author: KyberPhantasma

import textwrap
from entries import ENTRIES


# ── Display Helpers ────────────────────────────────────────────────

WIDTH = 60  # Terminal display width


def rule(char="─"):
    """Return a full-width horizontal rule."""
    return char * WIDTH


def wrap(text, indent=2):
    """Wrap text to WIDTH with a left indent."""
    prefix = " " * indent
    return textwrap.fill(text, width=WIDTH - indent, initial_indent=prefix,
                         subsequent_indent=prefix)


def section_header(title):
    """Return a formatted section header."""
    return f"\n  ┌── {title.upper()} {'─' * (WIDTH - len(title) - 7)}┐"


# ── Journal Class ──────────────────────────────────────────────────

class Journal:
    """
    Manages all thought experiment entries.

    Responsibilities:
    - Store and retrieve entries
    - Format and display entry content
    - Handle search by keyword or tag
    - Track which entries have been read
    """

    def __init__(self):
        self.entries = ENTRIES
        self.read_log = set()   # Tracks IDs of entries the user has read

    def count(self):
        """Return total number of entries."""
        return len(self.entries)

    def get_by_id(self, entry_id):
        """
        Retrieve an entry by its ID string (e.g. '001').
        Returns the entry dict or None if not found.
        """
        for entry in self.entries:
            if entry["id"] == entry_id.zfill(3):
                return entry
        return None

    def get_by_index(self, index):
        """
        Retrieve an entry by its list index (0-based).
        Returns the entry dict or None if out of range.
        """
        if 0 <= index < len(self.entries):
            return self.entries[index]
        return None

    def search(self, keyword):
        """
        Search all entries for a keyword (case-insensitive).
        Checks title, subtitle, tags, abstract, and all sections.
        Returns a list of matching entries.
        """
        keyword = keyword.lower()
        results = []
        for entry in self.entries:
            searchable = " ".join([
                entry["title"],
                entry["subtitle"],
                " ".join(entry["tags"]),
                entry["abstract"],
                entry["setup"],
                entry["observation"],
                entry["insight"],
                " ".join(entry["questions"]),
            ]).lower()
            if keyword in searchable:
                results.append(entry)
        return results

    def mark_read(self, entry_id):
        """Mark an entry as read."""
        self.read_log.add(entry_id)

    def is_read(self, entry_id):
        """Return True if this entry has been read."""
        return entry_id in self.read_log

    # ── Formatters ─────────────────────────────────────────────────

    def format_index(self):
        """Return a formatted table of contents."""
        lines = [
            rule("═"),
            "  PHYSICS THOUGHT EXPERIMENT JOURNAL",
            "  KyberPhantasma — Vol. I",
            rule("═"),
            "",
            "  ENTRIES",
            rule(),
        ]
        for entry in self.entries:
            read_mark = "✓" if self.is_read(entry["id"]) else "·"
            lines.append(
                f"  [{read_mark}] {entry['id']}  {entry['title']}"
                f"  —  {entry['subtitle']}"
            )
        lines += [
            rule(),
            f"  {len(self.read_log)} of {self.count()} entries read.",
            rule(),
        ]
        return "\n".join(lines)

    def format_entry(self, entry, section="all"):
        """
        Format a single entry for display.
        section can be: 'all', 'abstract', 'setup',
        'observation', 'questions', or 'insight'.
        """
        lines = [
            "",
            rule("═"),
            f"  ENTRY {entry['id']}",
            f"  {entry['title'].upper()}",
            f"  {entry['subtitle']}",
            rule("═"),
            f"  Tags: {' · '.join(entry['tags'])}",
            rule(),
        ]

        def add_section(name, content):
            lines.append(section_header(name))
            if isinstance(content, list):
                for i, item in enumerate(content, 1):
                    lines.append(f"\n  {i}. ")
                    lines.append(wrap(item, indent=5))
            else:
                lines.append("")
                lines.append(wrap(content, indent=2))
            lines.append("")

        if section in ("all", "abstract"):
            add_section("Abstract", entry["abstract"])

        if section in ("all", "setup"):
            add_section("Experiment Setup", entry["setup"])

        if section in ("all", "observation"):
            add_section("Observation", entry["observation"])

        if section in ("all", "questions"):
            add_section("Open Questions", entry["questions"])

        if section in ("all", "insight"):
            lines.append(section_header("Insight"))
            lines.append("")
            lines.append(wrap(entry["insight"], indent=2))
            lines.append("")

        lines.append(rule("═"))
        return "\n".join(lines)

    def format_search_results(self, keyword, results):
        """Format search results for display."""
        lines = [
            rule(),
            f"  SEARCH: '{keyword}'  —  {len(results)} result(s) found.",
            rule(),
        ]
        if results:
            for r in results:
                lines.append(f"  [{r['id']}] {r['title']} — {r['subtitle']}")
        else:
            lines.append("  No entries matched your search.")
        lines.append(rule())
        return "\n".join(lines)
