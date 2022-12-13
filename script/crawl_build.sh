# sh script/chrome_local_run.sh
cp $GOOGLE_APPLICATION_CREDENTIALS secrets/io-box-firebase.json

docker build . --tag  asia-northeast3-docker.pkg.dev/io-box/common/io-crawler-image:latest
docker push asia-northeast3-docker.pkg.dev/io-box/common/io-crawler-image:latest

# docker run \
#     --name io-crawler-container \
#     --rm \
# 	--env SELENIUM_URL=https://chrome-service-gvozj7um2q-du.a.run.app/wd/hub \
# 	--env CREDENTIAL_PATH=secrets/io-box-firebase.json \
#     asia-northeast3-docker.pkg.dev/io-box/common/io-crawler-image:latest