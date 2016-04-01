#!/bin/bash
BKUP_DATE=`date "+%Y%m%d%H%M"`
ROOT_UID=0
USERNAME=liaohg
PASSWORD=huagong
SOURCE=/opt
COPY_FILE=/root/backup

if [ "$UID" -ne "$ROOT_UID" ];then
    echo "Must be root to run this script."
    exit $E_NOTROOT
fi

echo "start copy time: ${BKUP_DATE}" > copy.log

if [ -d $COPY_FILE ];then
    cd $COPY_FILE
else
    mkdir $COPY_FILE
fi

cd $SOURCE
sudo mount -t cifs //192.168.1.147/backup /root/backup -o username=$USERNAME,password=$PASSWORD
cd $COPY_FILE
tar -cvf ccc2-$BKUP_DATE.tar $SOURCE >> copy.log
echo "end copy time: ${BKUP_DATE}" >> copy.log
exit 0

