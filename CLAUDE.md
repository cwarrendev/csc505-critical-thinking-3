# CSC505 Module 3 — Critical Thinking (Shopping List App Prototype)

Coursework for CSU Global CSC505. Deliverable is a ZIP submitted to Canvas:
architecture diagram, paper prototype screens, `shopping_list_prototype.py`,
a screenshot of the script running, and README.txt with APA 7 references.
Assignment: https://csuglobal.instructure.com/courses/122516/assignments/2255427

## Environment

Python 3.14 with a uv-managed venv (only needed to regenerate the prototype sheet):

```
uv venv .venv
uv pip install --python .venv matplotlib
```

`shopping_list_prototype.py` itself is stdlib-only by design (assignment requirement
to keep it simple) — do not add dependencies to it.

## Files

- `shopping_list_prototype.py` — Step 3 deliverable: screens/flows model, prints summary.
- `execution_output.txt` — captured output of a successful run.
- `make_paper_prototype.py` — generates `shopping_screens.png` (Step 2 deliverable).
  Regenerate with: `.venv\Scripts\python.exe make_paper_prototype.py`
- `shopping_screens.png` — the paper prototype sheet: 5 phone wireframes with
  numbered navigation arrows and a legend.
- `shopping_architecture.uxf` / `shopping_architecture.png` — UMLet architecture
  diagram source and preview (Step 1 deliverable).
- `assignment_draft.docx` — Word draft that embeds the PNGs by filename.
- `README.txt` — ships inside the submission ZIP (write it for the instructor).

## Decisions

- Paper prototype is script-generated (Python + matplotlib sketch/xkcd mode), chosen
  over Figma because it is automatable and reproducible; Figma cannot create content
  headlessly. The squiggly hand-drawn look is intentional (assignment asks for
  low-fidelity). Tooling is documented in README.txt, not inside the image.
- Keep the filename `shopping_screens.png` stable — the Word draft references it.
- Navigation flows in the PNG must stay consistent with `FLOWS` in
  `shopping_list_prototype.py`.

## Remaining work before submission

- [ ] Capture IDE screenshot of `shopping_list_prototype.py` running successfully.
- [ ] Open `.uxf` in UMLet, adjust layout, export final PNG/PDF.
- [ ] Verify textbook citation + at least two additional APA 7 references.
- [ ] Assemble the submission ZIP with exactly the required deliverables (no venv,
      no generator internals unless desired).
