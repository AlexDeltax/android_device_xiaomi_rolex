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
    ifelse(\n\
        getprop("ro.product.device") == "rolex", \n\
        (\n\
          ui_print("Flashing MIUI V8.8.30 Global Dev Firmware for rolex");\n\
          package_extract_file("install/firmware-update/rolex/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");\n\
          package_extract_file("install/firmware-update/rolex/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
          package_extract_file("install/firmware-update/rolex/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
          package_extract_file("install/firmware-update/rolex/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
          package_extract_file("install/firmware-update/rolex/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
          package_extract_file("install/firmware-update/rolex/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
          package_extract_file("install/firmware-update/rolex/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
          package_extract_file("install/firmware-update/rolex/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
          package_extract_file("install/firmware-update/rolex/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
          package_extract_file("install/firmware-update/rolex/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");\n\
          package_extract_file("install/firmware-update/rolex/adspso.bin", "/dev/block/bootdevice/by-name/dsp");\n\
        ),\n\
        ( \n\
          ui_print("Flashing MIUI V8.8.30 Global Dev Firmware for riva");\n\
          package_extract_file("install/firmware-update/riva/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");\n\
          package_extract_file("install/firmware-update/riva/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
          package_extract_file("install/firmware-update/riva/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
          package_extract_file("install/firmware-update/riva/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
          package_extract_file("install/firmware-update/riva/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
          package_extract_file("install/firmware-update/riva/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
          package_extract_file("install/firmware-update/riva/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
          package_extract_file("install/firmware-update/riva/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
          package_extract_file("install/firmware-update/riva/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
          package_extract_file("install/firmware-update/riva/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");\n\
          package_extract_file("install/firmware-update/riva/adspso.bin", "/dev/block/bootdevice/by-name/dsp");\n\
          package_extract_file("install/firmware-update/riva/mdtp.img", "/dev/block/bootdevice/by-name/mdtp");\n\
          ui_print("Patches for riva");\n\
          run_program("/sbin/busybox", "mount", "/vendor");\n\
          package_extract_dir("install/patch/riva/vendor", "/vendor");\n\
          run_program("/sbin/busybox", "umount", "/vendor");\n\
        )\n\
    );\n\
  ')

def ImportBkpBootloaderFirmware(info):
  info.script.AppendExtra('\
    ifelse(\n\
        getprop("ro.product.device") == "rolex", \n\
        (\n\
          ui_print("Flashing MIUI V8.8.30 Global Dev Firmware for rolex");\n\
          package_extract_file("install/firmware-update/rolex/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");\n\
          package_extract_file("install/firmware-update/rolex/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
          package_extract_file("install/firmware-update/rolex/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
          package_extract_file("install/firmware-update/rolex/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
          package_extract_file("install/firmware-update/rolex/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
          package_extract_file("install/firmware-update/rolex/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
          package_extract_file("install/firmware-update/rolex/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
          package_extract_file("install/firmware-update/rolex/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
          package_extract_file("install/firmware-update/rolex/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
          ui_print("Flashing Done.");\n\
        ),\n\
        ( \n\
          ui_print("Flashing MIUI V8.8.30 Global Dev Firmware for riva");\n\
          package_extract_file("install/firmware-update/riva/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");\n\
          package_extract_file("install/firmware-update/riva/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");\n\
          package_extract_file("install/firmware-update/riva/rpm.mbn", "/dev/block/bootdevice/by-name/rpm");\n\
          package_extract_file("install/firmware-update/riva/tz.mbn", "/dev/block/bootdevice/by-name/tz");\n\
          package_extract_file("install/firmware-update/riva/emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");\n\
          package_extract_file("install/firmware-update/riva/lksecapp.mbn", "/dev/block/bootdevice/by-name/lksecapp");\n\
          package_extract_file("install/firmware-update/riva/sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");\n\
          package_extract_file("install/firmware-update/riva/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");\n\
          package_extract_file("install/firmware-update/riva/keymaster.mbn", "/dev/block/bootdevice/by-name/keymaster");\n\
          package_extract_file("install/firmware-update/riva/mdtp.img", "/dev/block/bootdevice/by-name/mdtp");\n\
          ui_print("Patches for riva");\n\
          run_program("/sbin/busybox", "mount", "/vendor");\n\
          package_extract_dir("install/patch/riva/vendor", "/vendor");\n\
          run_program("/sbin/busybox", "umount", "/vendor");\n\
        )\n\
    );\n\
  ')