"""Generate the digital paper-prototype sheet (shopping_screens.png).

Draws five hand-sketch-style phone wireframes with numbered navigation
arrows using matplotlib's xkcd (sketch) mode. Run inside the uv venv:

    uv run --python .venv make_paper_prototype.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

PHONE_W, PHONE_H = 3.0, 6.0
INK = "#1a1a2e"
PAPER = "#fdfcf7"
ACCENT = "#2f6f4f"


def phone_frame(ax, x, y, number, title):
    """Draw a phone outline with status bar and title; return content origin."""
    ax.add_patch(FancyBboxPatch((x, y), PHONE_W, PHONE_H,
                                boxstyle="round,pad=0.06,rounding_size=0.22",
                                fc="white", ec=INK, lw=2))
    # speaker slot and home indicator
    ax.add_patch(FancyBboxPatch((x + PHONE_W / 2 - 0.35, y + PHONE_H - 0.18), 0.7, 0.07,
                                boxstyle="round,pad=0.02", fc=INK, ec=INK))
    ax.plot([x + PHONE_W / 2 - 0.4, x + PHONE_W / 2 + 0.4],
            [y + 0.12, y + 0.12], color=INK, lw=2)
    # numbered badge
    ax.add_patch(Circle((x - 0.05, y + PHONE_H + 0.18), 0.26, fc=ACCENT, ec=INK, lw=1.5, zorder=5))
    ax.text(x - 0.05, y + PHONE_H + 0.18, str(number), color="white",
            ha="center", va="center", fontsize=13, weight="bold", zorder=6, path_effects=[])
    # screen title above the phone
    ax.text(x + PHONE_W / 2 + 0.1, y + PHONE_H + 0.18, title,
            ha="center", va="center", fontsize=13, weight="bold", color=INK)
    return x + 0.22, y + PHONE_H - 0.45  # content origin (top-left inside screen)


def header(ax, cx, cy, text, back=False):
    ax.text(cx + (0.35 if back else 0.0), cy, text, fontsize=10.5, weight="bold", va="top", color=INK)
    if back:
        ax.text(cx, cy, "<", fontsize=11, weight="bold", va="top", color=ACCENT)
    ax.plot([cx, cx + PHONE_W - 0.44], [cy - 0.28, cy - 0.28], color=INK, lw=1)


def field(ax, cx, cy, label, value):
    ax.text(cx, cy, label, fontsize=8.5, va="top", color=INK)
    ax.add_patch(Rectangle((cx, cy - 0.42), PHONE_W - 0.44, 0.32, fc=PAPER, ec=INK, lw=1))
    ax.text(cx + 0.08, cy - 0.26, value, fontsize=8.5, va="center", color="#555", style="italic")


def button(ax, cx, cy, text, w=None, filled=True, danger=False):
    w = w or (PHONE_W - 0.44)
    color = "#b3372f" if danger else ACCENT
    ax.add_patch(FancyBboxPatch((cx, cy), w, 0.36, boxstyle="round,pad=0.03,rounding_size=0.1",
                                fc=(color if filled else "white"), ec=color, lw=1.5))
    ax.text(cx + w / 2, cy + 0.18, text, ha="center", va="center", fontsize=9,
            color=("white" if filled else color), weight="bold", path_effects=[])


def list_row(ax, cx, cy, text):
    ax.text(cx, cy, text, fontsize=8.5, va="center", color=INK)
    ax.text(cx + PHONE_W - 0.58, cy, ">", fontsize=10, va="center", color=ACCENT, weight="bold")
    ax.plot([cx, cx + PHONE_W - 0.44], [cy - 0.2, cy - 0.2], color="#bbb", lw=1)


def check_row(ax, cx, cy, text, checked=False, pencil=True):
    ax.add_patch(Rectangle((cx, cy - 0.1), 0.2, 0.2, fc="white", ec=INK, lw=1.2))
    if checked:
        ax.plot([cx + 0.03, cx + 0.09, cx + 0.19], [cy, cy - 0.08, cy + 0.12], color=ACCENT, lw=2)
    ax.text(cx + 0.32, cy, text, fontsize=8.5, va="center", color=INK)
    if pencil:
        ax.text(cx + PHONE_W - 0.62, cy, "[edit]", fontsize=7, va="center", color=ACCENT)


def toggle(ax, cx, cy, text, on=True):
    ax.text(cx, cy, text, fontsize=8.5, va="center", color=INK)
    tx = cx + PHONE_W - 0.95
    ax.add_patch(FancyBboxPatch((tx, cy - 0.09), 0.5, 0.18, boxstyle="round,pad=0.02,rounding_size=0.09",
                                fc=(ACCENT if on else "#bbb"), ec=INK, lw=1))
    ax.add_patch(Circle((tx + (0.41 if on else 0.09), cy), 0.1, fc="white", ec=INK, lw=1))


def nav_arrow(ax, p0, p1, label, step, rad=0.0, dashed=False, label_dx=0.0, label_dy=0.0):
    arrow = FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}",
                            arrowstyle="-|>,head_width=4,head_length=8",
                            color=(ACCENT if not dashed else "#666"), lw=2,
                            linestyle=("--" if dashed else "-"), zorder=3)
    ax.add_patch(arrow)
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + rad * 1.6
    ax.add_patch(Circle((mx + label_dx, my + label_dy + 0.32), 0.2, fc="white", ec=INK,
                        lw=1.2, zorder=4))
    ax.text(mx + label_dx, my + label_dy + 0.32, str(step), ha="center", va="center",
            fontsize=10, weight="bold", zorder=5, path_effects=[])
    ax.text(mx + label_dx, my + label_dy - 0.04, label, ha="center", va="top", fontsize=8.5,
            style="italic", color="#444", zorder=5)


def main():
    plt.xkcd(scale=0.8, length=120, randomness=1.6)
    matplotlib.rcParams["font.family"] = "Comic Sans MS"
    fig, ax = plt.subplots(figsize=(17, 15.2))
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 15.2)
    ax.axis("off")
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    ax.text(8.5, 14.85, "Shopping List App - Paper Prototype and Navigation Flow",
            ha="center", fontsize=17, weight="bold", color=INK)

    # -- top row -------------------------------------------------------------
    cx, cy = phone_frame(ax, 1.0, 8.2, 1, "Home")
    header(ax, cx, cy, "Shopping Lists")
    list_row(ax, cx, cy - 0.62, "Weekly Groceries (8)")
    list_row(ax, cx, cy - 1.12, "Party Supplies (3)")
    button(ax, cx, cy - 1.95, "+ New List")
    button(ax, cx, cy - 2.55, "Settings", filled=False)
    ax.text(cx, cy - 3.3, "Tap a list to open it.\nGear opens Settings.", fontsize=7.5, color="#666", va="top")

    cx, cy = phone_frame(ax, 7.0, 8.2, 2, "View List")
    header(ax, cx, cy, "Weekly Groceries", back=True)
    check_row(ax, cx, cy - 0.62, "Milk  x2")
    check_row(ax, cx, cy - 1.12, "Bread  x1", checked=True)
    check_row(ax, cx, cy - 1.62, "Eggs  x12")
    button(ax, cx, cy - 2.45, "+ Add Item")
    ax.text(cx, cy - 3.1, "Checked items sort last.\n[edit] opens Edit/Delete.", fontsize=7.5, color="#666", va="top")

    cx, cy = phone_frame(ax, 13.0, 8.2, 3, "Add Item")
    header(ax, cx, cy, "Add Item", back=True)
    field(ax, cx, cy - 0.55, "Item name", "Milk")
    field(ax, cx, cy - 1.35, "Quantity", "2")
    button(ax, cx, cy - 2.35, "Save")
    button(ax, cx, cy - 2.95, "Cancel", filled=False)
    ax.text(cx, cy - 3.55, "Empty name shows an\ninline error message.", fontsize=7.5, color="#666", va="top")

    # -- bottom row ----------------------------------------------------------
    cx, cy = phone_frame(ax, 1.0, 0.4, 5, "Settings / About")
    header(ax, cx, cy, "Settings", back=True)
    toggle(ax, cx, cy - 0.6, "Unchecked first", on=True)
    toggle(ax, cx, cy - 1.1, "Reminders", on=False)
    ax.text(cx, cy - 1.6, "Storage: this device", fontsize=8.5, va="center", color=INK)
    ax.plot([cx, cx + PHONE_W - 0.44], [cy - 1.95, cy - 1.95], color="#999", lw=1)
    ax.text(cx, cy - 2.2, "About Shopping Lists\nVersion 0.1 (prototype)", fontsize=8, va="top", color="#666")

    cx, cy = phone_frame(ax, 7.0, 0.4, 4, "Edit / Delete Item")
    header(ax, cx, cy, "Edit Item", back=True)
    field(ax, cx, cy - 0.55, "Item name", "Milk")
    field(ax, cx, cy - 1.35, "Quantity", "2")
    button(ax, cx, cy - 2.35, "Save Changes")
    button(ax, cx, cy - 2.95, "Delete (confirm)", danger=True)
    ax.text(cx, cy - 3.55, "Delete asks 'Are you\nsure?' before removing.", fontsize=7.5, color="#666", va="top")

    # -- navigation arrows ---------------------------------------------------
    nav_arrow(ax, (4.25, 11.6), (6.8, 11.6), "tap a list", 1)
    nav_arrow(ax, (10.25, 11.6), (12.8, 11.6), "tap + Add Item", 2)
    nav_arrow(ax, (13.0, 10.1), (10.3, 10.3), "Save / Cancel", 3, rad=-0.3, dashed=True)
    nav_arrow(ax, (8.55, 8.1), (8.55, 6.85), "tap [edit]", 4, label_dx=-1.0, label_dy=0.15)
    nav_arrow(ax, (9.7, 6.85), (9.7, 8.1), "Save / Delete\n/ Cancel", 5, dashed=True,
              label_dx=1.35, label_dy=0.15)
    nav_arrow(ax, (2.55, 8.1), (2.55, 6.85), "tap Settings", 6, label_dx=1.15, label_dy=0.15)
    nav_arrow(ax, (1.45, 6.85), (1.45, 8.1), "Back", 7, dashed=True, label_dx=-0.75, label_dy=0.15)

    # legend
    ax.text(12.6, 3.4, "Legend", fontsize=11, weight="bold", color=INK)
    ax.add_patch(FancyArrowPatch((12.6, 3.0), (13.6, 3.0),
                                 arrowstyle="-|>,head_width=4,head_length=8", color=ACCENT, lw=2))
    ax.text(13.8, 3.0, "forward navigation (numbered step)", fontsize=8.5, va="center")
    ax.add_patch(FancyArrowPatch((12.6, 2.55), (13.6, 2.55),
                                 arrowstyle="-|>,head_width=4,head_length=8", color="#666",
                                 lw=2, linestyle="--"))
    ax.text(13.8, 2.55, "return navigation (Save / Cancel / Back)", fontsize=8.5, va="center")
    ax.text(12.6, 2.0, "Generated with Python + matplotlib\n(sketch mode) - make_paper_prototype.py",
            fontsize=7.5, color="#666", va="top")

    fig.savefig("shopping_screens.png", dpi=200, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print("Wrote shopping_screens.png")


if __name__ == "__main__":
    main()
