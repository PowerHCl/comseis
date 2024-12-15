#!/bin/bash
export SAC_DISPLAY_COPYRIGHT=0
stalstdir="useful_stalstpair"   #data pair can be used!
pair_data="pair_data_v2"
filenum=0
if [ ! -d "./${pair_data}" ]; then
    mkdir ${pair_data}
fi
sed -n '2,$p' comseis.csv | cut -d , -f1 | while read rows
    do
        filenum=$(($filenum+1))
        year=${rows:0:4}
        month=${rows:5:2}
        day=${rows:8:2}
        hour=${rows:11:2}
        minute=${rows:14:2}
        second=${rows:17:2}
        dir="Event_${year}_${month}_${day}_${hour}_${minute}_${second}"
        if [ $(($filenum%2)) -eq 1 ];then
            dir1=${dir}
        else
            dir2=${dir}
            work_file="${stalstdir}/stalst_${dir1:6:10}__${dir2:6:10}.txt"
            work_dir="work_source/dir_${dir1:6:10}__${dir2:6:10}"

            if [ -f "${pair_data}/data_${dir1:6:10}__${dir2:6:10}.txt" ];then
                rm "${pair_data}/data_${dir1:6:10}__${dir2:6:10}.txt"
            fi
            echo "${work_dir}"
            cat ${work_file} | while read st
            do
                echo processing: $(ls ${work_dir}/${dir1}/${st} | cut -d / -f 4)
                f1=${work_dir}/${dir2}/${st}
                f2=${work_dir}/${dir1}/${st}
                data=$(python cc_v2.py t6 ${f1} ${f2})
		#echo ${data}
                echo ${data} >> ${pair_data}/data_${dir1:6:10}__${dir2:6:10}.txt


            done
        fi
    done
