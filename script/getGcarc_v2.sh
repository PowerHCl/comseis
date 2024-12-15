#!/bin/bash
file_dir='/home/gpu/projects/G3/pair_data_u_v2'
file='data_2005_02_06__2005_07_02.txt'
sacFileDir='/home/gpu/projects/G3/work_source/dir_2005_02_06__2005_07_02/Event_2005_02_06_04_24_18'
sed -n '1,$p' ${file_dir}/${file} | cut -d , -f1,3 | while read rows
do
    sacFileName=`echo ${rows} | cut -d , -f1`
    magRate=`echo ${rows} | cut -d , -f2`
    gcarc=`saclst gcarc f ${sacFileDir}/${sacFileName} | awk '{print $2}'`
    echo ${gcarc}, ${magRate}
done
