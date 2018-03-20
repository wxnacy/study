#!/usr/bin/env bash
# 设置开发环境
#__author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
#__copyright__ = "Copyright of GoChinaTV (2017)."
ENV=$1


if [ ! ${ENV} ]
then
    ENV=local
fi

export PYTHONPATH=./

# dev local product test
export FLASK_CONFIG=${ENV}
