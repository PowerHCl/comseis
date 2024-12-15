#!/bin/bash
file_dir='/home/gpu/projects/G3/pair_data_u'
file='data_2009_02_23__2016_09_01.txt'
sacFileDir='/home/gpu/projects/G3/work_source/dir_2009_02_23__2016_09_01/Event_2009_02_23_05_56_31'
sed -n '1,$p' ${file_dir}/${file} | cut -d , -f1,3 | while read rows
do
    sacFileName=`echo ${rows} | cut -d , -f1`
    magRate=`echo ${rows} | cut -d , -f2`
    gcarc=`saclst gcarc f ${sacFileDir}/${sacFileName} | awk '{print $2}'`
    echo ${gcarc}, ${magRate}
done