import pyscreenshot

def take_screenshot():
    # To capture the screen
    image = pyscreenshot.grab()

    # To display the captured screenshot
    image.show()

    # To save the screenshot
    image.save("screenshot.png")
