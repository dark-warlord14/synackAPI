#!/usr/bin/env python3
from synack import synack
import sys

s1 = synack()
s1.headless = True
s1.configFile = "~/.synack/synack.conf"
s1.connectToPlatform()
s1.getSessionToken()
s1.getAllTargets()
#s1.getProfile()
