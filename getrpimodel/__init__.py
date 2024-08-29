# -*- coding: utf-8 -*-
#
# © Takeyuki UEDA 2016 -.

#import getpirevision
import re

# setting
version = "0.1.26"

# model definition table from revision info.
# refer https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
# refer https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-revision-codes
model_a          = ["0007","0008","0009",]
model_b          = ["0002","0004","0005","0006","000d","000e","000e","000f",]
model_b_beta     = ["Beta",]
model_b_ECN0001  = ["0003",]
model_cm         = ["0011","0014","900061",]
model_cm3        = ["a020a0","a220a0",]
model_cm3_plus   = ["a02100",]
model_cm4        = ["a03140","b03140","c03140","d03140",]
model_a_plus     = ["0012","0015","900021",]
model_b_plus     = ["0010","0013","900032",]
model_2b         = ["a01040","a01041","a21041","a22042",]
model_2b_2837    = ["a02042","a22042",]
model_3b         = ["a02082","a22082","a32082","a52082","a22083"]
model_3a_plus    = ["9020e0","9020e1","a020d3","a020d4",]
model_3b_plus    = ["a020d3",]
model_4b         = ["a03111", "b03111", "b03112", "b03114", "b03115", "c03111", "c03112", "c03114", "c03115", "d03114", "d03115"]
model_zero       = ["900092","900093","920092","920093",]
model_zero_w     = ["9000c1",]
model_zero_2_w   = ["902120",]
model_400        = ["c03130",]
model_5          = ["b04170","c04170","d04170",]

def revision():
  revision = "unknown"
  with open('/proc/cpuinfo', 'r') as f:
    for line in f:
      m = re.search('Revision.*: ([0123456789abcdef]*)', line)
      if m:
        revision = m.group(1)
        return revision

def model_strict():
#  rev = getpirevision.revision()
  rev = revision()
  if rev in model_a:
    return "A"
  elif rev in model_b:
    return "B"
  elif rev in model_b_beta:
    return "B (Beta)"
  elif rev in model_b_ECN0001:
    return "B (ECN0001)"
  elif rev in model_cm:
    return "Compute Module"
  elif rev in model_cm3:
    return "Compute Module 3(and CM3 Lite)"
  elif rev in model_cm3_plus:
    return "Compute Module 3+"
  elif rev in model_cm4:
    return "Compute Module 4"
  elif rev in model_a_plus:
    return "A+"
  elif rev in model_b_plus:
    return "B+"
  elif rev in model_2b:
    return "2 Model B"
  elif rev in model_2b_2837:
    return "2 Model B (with BCM2837)"
  elif rev in model_3b:
    return "3 Model B"
  elif rev in model_3a_plus:
    return "3 Model A+"
  elif rev in model_3b_plus:
    return "3 Model B+"
  elif rev in model_4b:
    return "4 Model B"
  elif rev in model_zero:
    return "Zero"
  elif rev in model_zero_w:
    return "Zero W"
  elif rev in model_zero_2_w:
    return "Zero 2 W"
  elif rev in model_400:
    return "Pi 400"
  elif rev in model_5:
    return "5"
  else:
    return rev
#    return None

def model():
#  rev = getpirevision.revision()
  rev = revision()
  if rev in model_a:
    return "A"
  elif rev in model_b + model_b_beta + model_b_ECN0001:
    return "B"
  elif rev in model_cm + model_cm3 + model_cm3_plus + model_cm4:
    return "Compute Module"
  elif rev in model_a_plus:
    return "A+"
  elif rev in model_b_plus:
    return "B+"
  elif rev in model_2b + model_2b_2837:
    return "2 Model B"
  elif rev in model_3a_plus:
    return "3 Model A"
  elif rev in model_3b + model_3b_plus:
    return "3 Model B"
  elif rev in model_4b:
    return "4 Model B"
  elif rev in model_zero + model_zero_w:
    return "Zero"
  elif rev in model_zero_2_w:
    return "Zero 2"
  elif rev in model_400:
    return "Pi 400"
  elif rev in model_5:
    return "5"
  else:
#    return rev
    return None
