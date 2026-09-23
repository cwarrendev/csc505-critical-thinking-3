Shopping List App Prototype
CSC505: Principles of Software Development - Module 3 Critical Thinking
Author: Chris Warren - CSU Global - September 2026

A preliminary design for a mobile app that manages personal shopping lists:
an architecture diagram, a five-screen paper prototype with navigation flow,
and a Python script that models the screens and flows.

CONTENTS OF THIS SUBMISSION

- shopping_list_prototype.py - Python script modeling the five screens and
  eight navigation links.
- python_output_screenshot.png - screenshot of the script running successfully.
- shopping_architecture.png - preliminary layered component architecture diagram.
- shopping_screens.png - paper prototype: five screens with numbered navigation
  arrows.
- README.md / README.txt - this file.

ARCHITECTURE (STEP 1) - see shopping_architecture.png

The design uses three layers. The user interface layer (the five screens) sends user
actions to a list controller, which validates input (nonempty item name, positive
quantity) and performs add, edit, remove, toggle-purchased, and sort operations. The
controller calls a list repository that owns loading and saving records in local
SQLite storage, so the app works fully offline. A cloud synchronization adapter and
reminder notifications are noted as future extensions behind the repository, keeping
storage decisions out of the screens (Google, n.d.).

PAPER PROTOTYPE (STEP 2) - see shopping_screens.png

The sheet shows the five required screens, each labeled and numbered:

1. Home - choose a list, create a list, or open settings.
2. View List - see unchecked items first and mark purchases.
3. Add Item - enter a name and quantity; save or cancel.
4. Edit/Delete Item - change an item or confirm its deletion.
5. Settings/About - set sorting preferences and read app information.

Solid green arrows are forward navigation (numbered steps 1-8); dashed gray arrows
are Save/Cancel/Back returns. The arrows correspond one-to-one with the eight flow
entries printed by shopping_list_prototype.py.

PROTOTYPE SCRIPT (STEP 3)

Run with Python 3.10 or newer; only the standard library is used:

    python shopping_list_prototype.py

Sample output:

    Screens: Home, Add Item, View List, Edit/Delete Items, Settings/About
    Total Screens: 5

    Screen responsibilities:
    - Home: Choose a list, create a list, or open settings.
    - Add Item: Enter a name and quantity; save or cancel.
    - View List: See unchecked items first and mark purchases.
    - Edit/Delete Items: Change an item or confirm its deletion.
    - Settings/About: Set sorting preferences and read app information.

    Navigation flow:
    Home -> View List [Open or create list]
    View List -> Add Item [Add]
    Add Item -> View List [Save valid item or cancel]
    View List -> Edit/Delete Items [Select item]
    Edit/Delete Items -> View List [Save, confirm delete, or cancel]
    Home -> Settings/About [Settings]
    Settings/About -> Home [Back]
    View List -> Home [Back to lists]

DESIGN ASSUMPTIONS AND NOTES

- Personal, single-device use in version 1; shared lists and accounts are out of scope.
- Delete requires confirmation, and Cancel always preserves the previously saved
  value, following Nielsen's heuristics of user control and system-status visibility
  (Nielsen, 1994).
- The paper prototype is deliberately low fidelity. Both the prototype sheet and the
  architecture diagram were drawn programmatically (Python + matplotlib) so they are
  reproducible; the hand-drawn look of the prototype sheet is intentional.
- The architecture diagram, prototype sheet, and script all use the same screen names.
- The script describes the proposed app; it does not implement mobile screens,
  persistence, or synchronization.

REFERENCES

Google. (n.d.). Guide to app architecture. Android Developers.
https://developer.android.com/topic/architecture

Nielsen, J. (1994, April 24). 10 usability heuristics for user interface design.
Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

Pressman, R. S., & Maxim, B. R. (2020). Software engineering: A practitioner's
approach (9th ed.). McGraw-Hill Education.
