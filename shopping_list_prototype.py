"""Describe an offline shopping-list prototype; no mobile app is implemented."""
SCREENS = {
    "Home": "Choose a list, create a list, or open settings.",
    "Add Item": "Enter a name and quantity; save or cancel.",
    "View List": "See unchecked items first and mark purchases.",
    "Edit/Delete Items": "Change an item or confirm its deletion.",
    "Settings/About": "Set sorting preferences and read app information.",
}
FLOWS = [
    ("Home", "View List", "Open or create list"),
    ("View List", "Add Item", "Add"),
    ("Add Item", "View List", "Save valid item or cancel"),
    ("View List", "Edit/Delete Items", "Select item"),
    ("Edit/Delete Items", "View List", "Save, confirm delete, or cancel"),
    ("Home", "Settings/About", "Settings"),
    ("Settings/About", "Home", "Back"),
    ("View List", "Home", "Back to lists"),
]

def main():
    print("Screens: " + ", ".join(SCREENS))
    print(f"Total Screens: {len(SCREENS)}")
    print("\nScreen responsibilities:")
    for name, description in SCREENS.items():
        print(f"- {name}: {description}")
    print("\nNavigation flow:")
    for origin, destination, action in FLOWS:
        print(f"{origin} -> {destination} [{action}]")

if __name__ == "__main__":
    main()
