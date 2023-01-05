# NOTE: it's used in dockerfile, not use direct declare env
# export SELENIUM_URL=https://chrome-service-gvozj7um2q-du.a.run.app/wd/hub
# export SELENIUM_URL=http://localhost:4444/wd/hub
export CREDENTIAL_PATH=secrets/io-box-firebase.json
python -m lib.crawler.sinsang
python export.py