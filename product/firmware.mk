# Releasetools
TARGET_RELEASETOOLS_EXTENSIONS := device/xiaomi/rolex

# Ship miui_HM4AGlobal_V9.6.5.0.NCCMIFD Firmware.
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/firmware/adspso.bin:install/firmware-update/adspso.bin \
    $(LOCAL_PATH)/firmware/cmnlib64.mbn:install/firmware-update/cmnlib64.mbn \
    $(LOCAL_PATH)/firmware/cmnlib.mbn:install/firmware-update/cmnlib.mbn \
    $(LOCAL_PATH)/firmware/devcfg.mbn:install/firmware-update/devcfg.mbn \
    $(LOCAL_PATH)/firmware/emmc_appsboot.mbn:install/firmware-update/emmc_appsboot.mbn \
    $(LOCAL_PATH)/firmware/keymaster.mbn:install/firmware-update/keymaster.mbn \
    $(LOCAL_PATH)/firmware/lksecapp.mbn:install/firmware-update/lksecapp.mbn \
    $(LOCAL_PATH)/firmware/NON-HLOS.bin:install/firmware-update/NON-HLOS.bin \
    $(LOCAL_PATH)/firmware/rpm.mbn:install/firmware-update/rpm.mbn \
    $(LOCAL_PATH)/firmware/sbl1.mbn:install/firmware-update/sbl1.mbn \
    $(LOCAL_PATH)/firmware/tz.mbn:install/firmware-update/tz.mbn \
    $(LOCAL_PATH)/firmware/splash.img:install/firmware-update/splash.img