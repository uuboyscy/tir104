cat run.sh
#!/usr/bin/env bash

MOUNT_DOWNLOAD_FOLDER=/home/seluser/Downloads
GCS_BUCKET=data-synced

mkdir -p ${MOUNT_DOWNLOAD_FOLDER}
chmod -R 777 ${MOUNT_DOWNLOAD_FOLDER}

if [ "X${ENV}" = "Xdev" ]
then
    GCS_BUCKET=data-synced-dev
fi

GOOGLE_APPLICATION_CREDENTIALS=/home/seluser/cloud-run-secret.json gcsfuse --only-dir crawler/ ${GCS_BUCKET} "${MOUNT_DOWNLOAD_FOLDER}"

touch ${MOUNT_DOWNLOAD_FOLDER}/connected.txt

# nginx -c "/root/nginx.conf" &

/opt/bin/entry_point.sh
