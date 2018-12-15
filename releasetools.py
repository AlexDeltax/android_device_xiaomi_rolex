# Copyright (C) 2018 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def IncrementalOTA_InstallEnd(info):
  ImportMainBootloaderFirmware(info)
  ImportBkpBootloaderFirmware(info)

def FullOTA_InstallEnd(info):
  ImportMainBootloaderFirmware(info)
  ImportBkpBootloaderFirmware(info)

def ImportMainBootloaderFirmware(info):
  info.script.AppendExtra('\
    ui_print("Flashing MIUI HM4AGlobal_V10.1.1.0.NCCMIFI Firmware.");\n\
    package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");\n\
    package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
    package_extract_file("install/firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
    package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
    package_extract_file("install/firmware-update/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
    package_extract_file("install/firmware-update/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
    package_extract_file("install/firmware-update/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
    package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
    package_extract_file("install/firmware-update/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
    package_extract_file("install/firmware-update/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");\n\
    package_extract_file("install/firmware-update/adspso.bin", "/dev/block/bootdevice/by-name/dsp");\n\
    package_extract_file("install/firmware-update/splash.img", "/dev/block/bootdevice/by-name/splash");\n\
  ')

def ImportBkpBootloaderFirmware(info):
  info.script.AppendExtra('\
    ui_print("Flashing Backup MIUI HM4AGlobal_V10.1.1.0.NCCMIFI Firmware.");\n\
    package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64bak");\n\
    package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
    package_extract_file("install/firmware-update/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
    package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
    package_extract_file("install/firmware-update/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
    package_extract_file("install/firmware-update/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
    package_extract_file("install/firmware-update/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
    package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
    package_extract_file("install/firmware-update/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
    ui_print("Flashing Done.");\n\
  ')
