#!/usr/bin/env bash
TAG_NAME=$1
MSG=$2

deploy(){
    echo '******************************'
    echo '********开始远程部署tag：' ${TAG_NAME}
    echo '******************************'
    ./push_tag.sh ${TAG_NAME} ${MSG}
    ansible-playbook deploy_remote_api.yml --extra-vars "tag_name=${TAG_NAME}" --inventory-file=ansible_hosts
    echo '******************************'
    echo '********部署成功'
    echo '******************************'
}



if [ ! ${TAG_NAME} ]
then
    echo 'UAGE: ./git_push.sh <regex:tag_name>'
else
    deploy
fi