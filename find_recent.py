import os, glob
files = glob.glob('**/*', recursive=True)
files = [f for f in files if os.path.isfile(f)]
files.sort(key=os.path.getmtime, reverse=True)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(files[:20]))
