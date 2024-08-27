var DOCUMENTATION_VERSIONS = {
    DEFAULTS: { has_targets: false,
                supported_targets: [ "esp32s2" ]
              },
    IDF_TARGETS: [
       { text: "ESP32-S2", value: "esp32s2"},
       { text: "ESP32-S3", value: "esp32s3"},
       { text: "ESP32-C3", value: "esp32c3"},
       { text: "ESP32-C6", value: "esp32c6"},
       { text: "ESP32-H2", value: "esp32h2"},
       { text: "ESP32-C2", value: "esp32c2"},
    ]
  };

if (DOCUMENTATION_OPTIONS.LANGUAGE === 'zh-CN') {
    DOCUMENTATION_OPTIONS.LANGUAGE = 'zh_CN';
}
