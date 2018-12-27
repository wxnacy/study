#!/usr/bin/env bash
SOURCE_PATH=src
VIM_PROJECT_HOME=./
TARGET=target
CLASS_PATH=${TARGET}/classes
SOURCE_TXT=${VIM_PROJECT_HOME}/.source
list_file(){
    # 遍历源码目录并输出到 ${SOURCE_TXT} 中
    for file in `ls $1`
    do
        if test -f $file
        then
            echo $file >> ${SOURCE_TXT}
        else
            list_file $1/$file
        fi
    done
}
compile(){
    # 编译
    if [ ! -d "${VIM_PROJECT_HOME}"  ]; then
        mkdir ${VIM_PROJECT_HOME}
    fi
    if [ ! -d "${TARGET}"  ]; then
        mkdir ${TARGET}
    fi
    rm -rf ${CLASS_PATH}
    if [ ! -d "${CLASS_PATH}"  ]; then
        mkdir ${CLASS_PATH}
    fi
    rm -rf ${SOURCE_TXT}
    touch ${SOURCE_TXT}
    list_file ${SOURCE_PATH}
    cat ${SOURCE_TXT}
    javac -cp ${CLASS_PATH} -d ${CLASS_PATH} @${SOURCE_TXT}
}
compile
java -cp ${CLASS_PATH} Main
