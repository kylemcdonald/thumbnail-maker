import os
import subprocess

thumbnail_side = 512
input_dir = '/mnt/input'
thumbnails_dir = f'/mnt/output/thumbnails-{thumbnail_side}'

def list_files(directory):
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            base, ext = os.path.splitext(filename)
            joined = os.path.join(root, filename)
            yield joined

def job(input_fn, verbose=False):
    rel_path = os.path.relpath(input_fn, input_dir)
    output_fn = os.path.join(thumbnails_dir, rel_path) + '.jpg'
    rel_dir = os.path.dirname(rel_path)
    output_dir = os.path.join(thumbnails_dir, rel_dir)
    os.makedirs(output_dir, exist_ok=True)
    if os.path.exists(output_fn):
        return True
    cmd = f'convert \
        -quiet \
        -verbose \
        -density 150 \
        "{input_fn}"[0] \
        -sharpen 0x1.0 \
        +adjoin \
        -background white \
        -alpha remove \
        -resize {thumbnail_side}x{thumbnail_side}\> \
        -quality 80 \
        "{output_fn}"'
    if not verbose:
        cmd += '>/dev/null 2>&1'
    subprocess.run(cmd, shell=True)
    return os.path.exists(output_fn)
    
for fn in list_files(input_dir):
    if not job(fn):
        print('Error', fn)