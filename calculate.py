import pystray
from PIL import Image

# Load the icon image
icon_image = Image.open("path/to/jarvis.png")  # Relative path


# Create a Pystray icon
icon = pystray.Icon("name", icon_image, "Desktop Application")

# Define the menu items (optional)
menu_items = [
    pystray.MenuItem("Item 1", lambda: print("Item 1 clicked")),
    pystray.MenuItem("Item 2", lambda: print("Item 2 clicked")),
    pystray.MenuItem("Exit", lambda: icon.stop()),
]

# Add the menu items to the icon
icon.menu = pystray.Menu(*menu_items)

# Run the icon
icon.run()
