#!/bin/bash

#while true ; do
    echo "开始获取大乐透数据"
    python get_data.py  --name dlt
    echo "开始训练大乐透模型"
    python run_train_model.py --name dlt
    echo "大乐透训练完成"
    echo "开始预测"
    python run_predict.py  --name dlt
#    echo "开始获取双色球数据"
    # python get_data.py  --name ssq
    # echo "开始训练双色球模型"
    # python run_train_model.py --name ssq
    # echo "双色球训练完成"
    # echo "开始双色球预测"
    # python run_predict.py  --name ssq
#    sleep 360
#done


