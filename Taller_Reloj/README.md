# AstraClock: Advanced DCLL World Clock System

## Overview
AstraClock is a professional-grade digital clock system built with **Python** and **CustomTkinter**. The core of the system is powered by a **Doubly Circular Linked List (DCLL)**, an advanced data structure that allows for seamless, infinite bidirectional traversal through multiple world clocks.

This project demonstrates the practical application of DCLL in an event-driven graphical environment, focusing on memory efficiency and algorithmic complexity.

## Academic Context
Inspired by the technical workshops of the **Universidad Cooperativa de Colombia**, this project bridges theoretical data structure concepts with professional software engineering practices. Each clock node in the system points to its predecessor and successor, forming a closed cycle that mirrors the cyclic nature of time and global time zones.

## Core Data Structure: Doubly Circular Linked List
The DCLL is implemented in `app/core/dcll.py`. Unlike a standard linked list, the DCLL ensures:
- **Infinite Traversal**: The last node links back to the head.
- **Bidirectional Navigation**: Each node has `prev` and `next` pointers.
- **O(1) Navigation**: Moving to the next or previous clock is a constant time operation.

### Algorithmic Complexity (Big O)
| Operation | Complexity | Description |
|-----------|------------|-------------|
| **Insertion (End)** | O(1) | Constant time as we maintain a reference to the head and its previous node. |
| **Deletion** | O(n) | Linear time to find the specific node to remove. |
| **Search** | O(n) | Linear traversal through nodes. |
| **Navigation (Next/Prev)** | O(1) | Immediate access via pointers. |
| **Traversing all Clocks** | O(n) | Iterating through all nodes once. |

## Features
- **Analog & Digital Display**: High-fidelity real-time rendering.
- **World Clock Management**: Dynamically add and remove cities from the DCLL.
- **Circular Navigation**: Infinite "Next" and "Previous" rotation between time zones.
- **Advanced UI**: Modern dark mode with multiple dynamic themes (Cyberpunk, Deep Sea, etc.).
- **Manual Adjustments**: Left panel controls for system overrides.
- **Modular Architecture**: Strict separation between data structures, business logic, and UI (MVC Pattern).

## Requirements
- Python 3.8+
- `customtkinter`
- `pytz`
- `pillow` (for Tkinter image handling if needed)

## How to Run
```bash
python main.py
```

## Technical Implementation Details
- **Threading**: Background threads handle the stopwatch and timer accuracy without blocking the main GUI loop.
- **Pointer Management**: Strict logic in `dcll.py` ensures that head and tail references are always consistent after insertions or deletions.
- **Object-Oriented Design**: Encapsulation of logic within Service classes and UI components.
