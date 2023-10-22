import climage

# FYI THIS is pronouced C- L- image ;)

# Main menu poison sticker
def main_menu_img():
    # Convert an image to a 50 character wide image.
    output = climage.convert('lib/img/new poison.png', is_unicode=True, width=50, is_256color=True, is_16color=False, is_8color=False)
    print(output)

# Dumper-2-D2 sticker
def web_m_dumper():
    output = climage.convert('lib/img/new dumper2-d2.png', is_unicode=True, width=50, is_256color=True, is_16color=False, is_8color=False)
    print(output)