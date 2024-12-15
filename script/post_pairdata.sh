#!/bin/zsh
work_dir="pair_data_v2"
useful_work_dir="pair_data_u_v2"
if [ ! -d "../${useful_work_dir}" ]; then
    mkdir ../${useful_work_dir}
fi
ls ../${work_dir} | while read rows
do
    if [ -f "../${useful_work_dir}/${rows}" ]; then
    rm ../${useful_work_dir}/${rows}
    fi
    cat ../${work_dir}/${rows} | tr -s '\n' '\n' | while read ev
    do 
        num=`echo ${ev} | cut -d , -f 4`
        if [ `echo "${num}>0.9" | bc` -eq 1 ];then
        echo ${ev} >> ../${useful_work_dir}/${rows}
        fi
    done
done
