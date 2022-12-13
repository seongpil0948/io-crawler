docker pull selenium/standalone-chrome

docker tag selenium/standalone-chrome asia-northeast3-docker.pkg.dev/io-box/common/chrome
docker push asia-northeast3-docker.pkg.dev/io-box/common/chrome:latest