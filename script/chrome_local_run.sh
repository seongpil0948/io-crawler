docker run \
    --rm \
    -dit \
    -p 4444:4444 \
    -p 7900:7900 \
    --shm-size 2g \
    selenium/standalone-chrome