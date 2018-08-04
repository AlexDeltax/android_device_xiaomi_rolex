# Releasetools
TARGET_RELEASETOOLS_EXTENSIONS := device/xiaomi/rolex

# Patch for sound riva
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/patch/riva/vendor/etc/mixer_paths_qrd_sku1.xml:install/patch/riva/vendor/etc/mixer_paths_qrd_sku1.xml \
    $(LOCAL_PATH)/patch/riva/vendor/etc/mixer_paths_qrd_sku2.xml:install/patch/riva/vendor/etc/mixer_paths_qrd_sku2.xml