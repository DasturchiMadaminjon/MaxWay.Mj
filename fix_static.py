import re

def fix_static_paths(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace src="assets/..." with src="{% static 'assets/...' %}"
    content = re.sub(r'src="assets/([^"]+)"', r'src="{% static \'assets/\1\' %}"', content)

    # I have checked href="assets/" before and I already changed style.css in earlier steps, but just parsing to be safe
    content = re.sub(r'href="assets/([^"]+)"', r'href="{% static \'assets/\1\' %}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_static_paths('templates/index_1.html')
# fix_static_paths('templates/order.html') # wait, my order.html replaces the whole file earlier and didn't use `assets/img/bitmap.png`, it used `{% static 'assets/img/logo.svg' %}`. I will just run index_1.html.
print('Finished updating static files')
