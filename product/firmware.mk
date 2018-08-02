# Releasetools
TARGET_RELEASETOOLS_EXTENSIONS := device/xiaomi/rolex

# Ship Miui Firmware 8.7.19
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/firmware/rolex/adspso.bin:install/firmware-update/rolex/adspso.bin \
    $(LOCAL_PATH)/firmware/rolex/cmnlib64.mbn:install/firmware-update/rolex/cmnlib64.mbn \
    $(LOCAL_PATH)/firmware/rolex/cmnlib.mbn:install/firmware-update/rolex/cmnlib.mbn \
    $(LOCAL_PATH)/firmware/rolex/devcfg.mbn:install/firmware-update/rolex/devcfg.mbn \
    $(LOCAL_PATH)/firmware/rolex/emmc_appsboot.mbn:install/firmware-update/rolex/emmc_appsboot.mbn \
    $(LOCAL_PATH)/firmware/rolex/keymaster.mbn:install/firmware-update/rolex/keymaster.mbn \
    $(LOCAL_PATH)/firmware/rolex/lksecapp.mbn:install/firmware-update/rolex/lksecapp.mbn \
    $(LOCAL_PATH)/firmware/rolex/NON-HLOS.bin:install/firmware-update/rolex/NON-HLOS.bin \
    $(LOCAL_PATH)/firmware/rolex/rpm.mbn:install/firmware-update/rolex/rpm.mbn \
    $(LOCAL_PATH)/firmware/rolex/sbl1.mbn:install/firmware-update/rolex/sbl1.mbn \
    $(LOCAL_PATH)/firmware/rolex/tz.mbn:install/firmware-update/rolex/tz.mbn \
    $(LOCAL_PATH)/firmware/riva/adspso.bin:install/firmware-update/riva/adspso.bin \
    $(LOCAL_PATH)/firmware/riva/cmnlib64.mbn:install/firmware-update/riva/cmnlib64.mbn \
    $(LOCAL_PATH)/firmware/riva/cmnlib.mbn:install/firmware-update/riva/cmnlib.mbn \
    $(LOCAL_PATH)/firmware/riva/devcfg.mbn:install/firmware-update/riva/devcfg.mbn \
    $(LOCAL_PATH)/firmware/riva/emmc_appsboot.mbn:install/firmware-update/riva/emmc_appsboot.mbn \
    $(LOCAL_PATH)/firmware/riva/keymaster.mbn:install/firmware-update/riva/keymaster.mbn \
    $(LOCAL_PATH)/firmware/riva/lksecapp.mbn:install/firmware-update/riva/lksecapp.mbn \
    $(LOCAL_PATH)/firmware/riva/NON-HLOS.bin:install/firmware-update/riva/NON-HLOS.bin \
    $(LOCAL_PATH)/firmware/riva/rpm.mbn:install/firmware-update/riva/rpm.mbn \
    $(LOCAL_PATH)/firmware/riva/sbl1.mbn:install/firmware-update/riva/sbl1.mbn \
    $(LOCAL_PATH)/firmware/riva/tz.mbn:install/firmware-update/riva/tz.mbn \
    $(LOCAL_PATH)/firmware/riva/mdtp.img:install/firmware-update/riva/mdtp.img