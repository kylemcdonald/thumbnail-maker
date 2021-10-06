docker run \
    -v `pwd`/src:/mnt/src:ro \
    -v `pwd`/input:/mnt/input:ro \
    -v `pwd`/output:/mnt/output \
    thumbnail-maker python3 /mnt/src/run.py