# Codebase Map & Symbol Catalog 🗺️

> **AUTO-GENERATED & VERIFIED BY `scripts/update_knowledge_base.py`**
> This document provides an automated, up-to-date registry of all modules, classes, and exported functions across this repository.

---

## 📊 Codebase Metrics
- **Total Python Modules**: `4`
- **Total Classes**: `1`
- **Total Top-Level Functions**: `1`
- **Total Class Methods**: `3`
- **Total Source Lines**: `66`

---

## 📦 Modules & Exported Symbols

### [`demo.py`](demo.py)
> *Headless scripted drive: prints WORLD-DELTA lines, no input, exits 0.*

**Size**: `10` lines (`361` bytes)

---

### [`inventory.py`](inventory.py)
> *Project-owned UI inventory: one `kind|name|locator` line per control.*

**Size**: `6` lines (`233` bytes)

---

### [`tests/__init__.py`](tests/__init__.py)
> *Regression tests for compat-sample-headless.*

**Size**: `1` lines (`51` bytes)

---

### [`tests/test_compat.py`](tests/test_compat.py)
> *Regression shield for the headless compat drive (stdlib only).*

**Size**: `49` lines (`1608` bytes)

**Classes:**
- `class CompatDriveTest`
  - Method `.test_inventory_lines_are_kind_name_locator()`
  - Method `.test_scripted_drive_prints_world_delta()`
  - Method `.test_scripted_drive_requires_flag()`

**Functions:**
- `def run_script(name, *args, timeout)`

---
