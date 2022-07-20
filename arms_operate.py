#!/usr/bin/env python3
#
# Copyright (C) 2021 UmbraTek Inc. All Rights Reserved.
#
# Software License Agreement (BSD License)
#
# Author: Jimy Zhang <jimy.zhang@umbratek.com> <jimy92@163.com>
# =============================================================================
import sys
import argparse
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from utapi.utra.utra_api_tcp import UtraApiTcp
from utapi.utra.utra_flxie_api import UtraFlxiE2Api

if __name__ == '__main__':
    """双臂，建议使用关节角度运动，测试时使用建议把速度设定为10
    """
    # 参数解析
    '''
    parserl = argparse.ArgumentParser()
    parserl.description = 'UTRA demo'
    parserl.add_argument("--ip", help=" ", default="127.0.0.1", type=str)
    argsl = parserl.parse_args()

    parserr = argparse.ArgumentParser()
    parserr.description = 'UTRA demo'
    parserr.add_argument("--ip", help=" ", default="127.0.0.1", type=str)
    argsr = parserr.parse_args()
    '''

    leftip = '192.168.1.23'
    rightip = '192.168.1.22'

    # ubot_l 左机械臂，fixi_l 左手爪
    ubot_l = UtraApiTcp(leftip)
    fixi_l = UtraFlxiE2Api(ubot_l, 101)
    # ubot_r 右机械臂，fixi_r 右手爪
    ubot_r = UtraApiTcp(rightip)
    fixi_r = UtraFlxiE2Api(ubot_r, 101)

    # 左机械臂模式，使能，状态
    ret_l = ubot_l.reset_err()  # Reset error
    print("reset_error   :%d" % (ret_l))
    ret_l = ubot_l.set_motion_mode(0)  # Set the operating mode of the arm, 0: position control mode
    print("set_motion_mode   :%d" % (ret_l))
    ret_l = ubot_l.set_motion_enable(8, 1)  # Set the enable state of the arm
    print("set_motion_enable :%d" % (ret_l))
    ret_l = ubot_l.set_motion_status(0)  # Set the running status of the arm, 0: Set to ready
    print("set_motion_status :%d" % (ret_l))

    # 右机械臂模式，使能，状态
    ret_r = ubot_r.reset_err()  # Reset error
    print("reset_error   :%d" % (ret_r))
    ret_r = ubot_r.set_motion_mode(0)  # Set the operating mode of the arm, 0: position control mode
    print("set_motion_mode   :%d" % (ret_r))
    ret_r = ubot_r.set_motion_enable(8, 1)  # Set the enable state of the arm
    print("set_motion_enable :%d" % (ret_r))
    ret_r = ubot_r.set_motion_status(0)  # Set the running status of the arm, 0: Set to ready
    print("set_motion_status :%d" % (ret_r))

    # speed速度，acc加速度
    speed = 10 / 57.296
    acc = 3
    ret_l = ubot_l.moveto_home_p2p(speed, acc, 60)
    ret_r = ubot_r.moveto_home_p2p(speed, acc, 60)

    # J1~J6 各关节角度，弧度制
    joint_l0 = [0 / 57.296, -30 / 57.296, 50 / 57.296, -10 / 57.296, 90 / 57.296, 0 / 57.296]
    ret_l = ubot_l.moveto_joint_p2p(joint_l0, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret_l))

    joint_l1 = [170.5 / 57.296, 3.5 / 57.296, -125.6 / 57.296, -39.1 / 57.296, -90 / 57.296, -9.5 / 57.296]
    joint_l2 = [133.8 / 57.296, 13.1 / 57.296, -114.3 / 57.296, -37.3 / 57.296, -90 / 57.296, -46.2 / 57.296]
    ret_l = ubot_l.moveto_joint_p2p(joint_l1, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_l))
    ret_l = ubot_l.moveto_joint_p2p(joint_l2, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_l))

    ret_l = ubot_l.move_sleep(1)
    print("move_sleep :%d" % (ret_l))

    ret = fixi_r.set_motion_mode(1)
    print("set_motion_mode: %d" % (ret))
    ret = fixi_r.set_motion_enable(1)
    print("set_motion_enable: %d" % (ret))

    ret = fixi_r.set_pos_target(0)
    print("set_pos_target: %d" % (ret))
    time.sleep(3)
    ret = fixi_r.set_pos_target(20)
    print("set_pos_target: %d" % (ret))

    joint_r1 = [170.5 / 57.296, 3.5 / 57.296, -125.6 / 57.296, -39.1 / 57.296, -90 / 57.296, -9.5 / 57.296]
    joint_r2 = [133.8 / 57.296, 13.1 / 57.296, -114.3 / 57.296, -37.3 / 57.296, -90 / 57.296, -46.2 / 57.296]
    ret_r = ubot_r.moveto_joint_p2p(joint_r1, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))
    ret_r = ubot_r.moveto_joint_p2p(joint_r2, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))
