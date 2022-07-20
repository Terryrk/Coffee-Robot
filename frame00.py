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

'''
右臂夹取程序
'''
if __name__ == '__main__':

    rightip = '192.168.1.22'
    leftip = '192.168.1.23'

    ubot_r = UtraApiTcp(rightip)
    fixi_r = UtraFlxiE2Api(ubot_r, 101)
    ubot_l = UtraApiTcp(leftip)
    fixi_l = UtraFlxiE2Api(ubot_l, 101)

    ret_r = ubot_r.reset_err()  # Reset error
    print("reset_error   :%d" % (ret_r))
    ret_r = ubot_r.set_motion_mode(0)  # Set the operating mode of the arm, 0: position control mode
    print("set_motion_mode   :%d" % (ret_r))
    ret_r = ubot_r.set_motion_enable(8, 1)  # Set the enable state of the arm
    print("set_motion_enable :%d" % (ret_r))
    ret_r = ubot_r.set_motion_status(0)  # Set the running status of the arm, 0: Set to ready
    print("set_motion_status :%d" % (ret_r))

    ret_l = ubot_l.reset_err()  # Reset error
    print("reset_error   :%d" % (ret_l))
    ret_l = ubot_l.set_motion_mode(0)  # Set the operating mode of the arm, 0: position control mode
    print("set_motion_mode   :%d" % (ret_l))
    ret_l = ubot_l.set_motion_enable(8, 1)  # Set the enable state of the arm
    print("set_motion_enable :%d" % (ret_l))
    ret_l = ubot_l.set_motion_status(0)  # Set the running status of the arm, 0: Set to ready
    print("set_motion_status :%d" % (ret_l))

    speed = 10 / 57.296
    acc = 3

    joint_l1 = [226.5 / 57.296, 64.8 / 57.296, -90.1 / 57.296, -145.4 / 57.296, -23.1 / 57.296, 14.8 / 57.296]
    ret = ubot_l.moveto_joint_p2p(joint_l1, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret))

    joint_r1 = [154.8 / 57.296, 62.4 / 57.296, -71.3 / 57.296, -47.4 / 57.296, 28.3 / 57.296, 16.5 / 57.296]
    ret = ubot_r.moveto_joint_p2p(joint_r1, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret))

    ret = ubot_r.move_sleep(1)
    print("move_sleep :%d" % (ret))
    ret = fixi_r.set_motion_mode(1, False)
    print("set_motion_mode: %d" % (ret))
    ret = fixi_r.set_motion_enable(1, False)
    print("set_motion_enable: %d" % (ret))

    ret = fixi_r.set_pos_target(40, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_r.move_sleep(3)
    print("move_sleep :%d" % (ret))

    ret = fixi_r.set_pos_target(25, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_r.move_sleep(3)
    print("move_sleep :%d" % (ret))


    joint_l2 = [230.6 / 57.296, 115.5 / 57.296, -11.1 / 57.296, -94.4 / 57.296, -29.8 / 57.296, -18.2 / 57.296]
    ret_l = ubot_l.moveto_joint_p2p(joint_l2, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))

    ret = ubot_l.move_sleep(1)
    print("move_sleep :%d" % (ret))
    ret = fixi_l.set_motion_mode(1, False)
    print("set_motion_mode: %d" % (ret))
    ret = fixi_l.set_motion_enable(1, False)
    print("set_motion_enable: %d" % (ret))

    ret = fixi_l.set_pos_target(40, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_l.move_sleep(3)
    print("move_sleep :%d" % (ret))

    ret = fixi_l.set_pos_target(25, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_l.move_sleep(3)
    print("move_sleep :%d" % (ret))

    ret = fixi_l.set_pos_target(40, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_l.move_sleep(3)
    print("move_sleep :%d" % (ret))

    joint_l3 = [216.6 / 57.296, 93.7 / 57.296, -26.6 / 57.296, -131.2 / 57.296, -37 / 57.296, 0 / 57.296]
    ret_l = ubot_l.moveto_joint_p2p(joint_l3, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))

    joint_r2 = [132.4 / 57.296, 39.7 / 57.296, -89.9 / 57.296, -37.6 / 57.296, 47.3 / 57.296, -13.9 / 57.296]
    joint_r3 = [136 / 57.296, 87.3 / 57.296, -9.8 / 57.296, -44.3 / 57.296, 34.6 / 57.296, -23.6 / 57.296]
    ret_r = ubot_r.moveto_joint_p2p(joint_r2, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))
    ret_r = ubot_r.moveto_joint_p2p(joint_r3, speed, acc, 5.0)
    print("moveto_joint_p2p   :%d" % (ret_r))
    
    ret = fixi_r.set_pos_target(40, False)
    print("set_pos_target: %d" % (ret))
    ret = ubot_r.move_sleep(3)
    print("move_sleep :%d" % (ret))

    jointr0 = [143.3 / 57.296, 56.7 / 57.296, -113.1/ 57.296, -44.2/ 57.296, 3.2 / 57.296, -23.7/ 57.296]
    ret = ubot_r.moveto_joint_p2p(jointr0, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
    jointl0 = [217/ 57.296, 80 / 57.296, -103 / 57.296, -127.9 / 57.296, 5.8 / 57.296, 0 / 57.296]
    ret = ubot_l.moveto_joint_p2p(jointl0, speed, acc, 60)
    print("moveto_joint_p2p   :%d" % (ret))
    ret = ubot_r.move_sleep(1)
    print("move_sleep :%d" % (ret))
    ret = ubot_l.move_sleep(1)
    print("move_sleep :%d" % (ret))




