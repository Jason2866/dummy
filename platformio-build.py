# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://arduino.cc/en/Reference/HomePage
"""

# Extends: https://github.com/platformio/platform-espressif32/blob/develop/builder/main.py

from os.path import basename, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduinoespressif32")
FRAMEWORK_SDK_DIR = join(FRAMEWORK_DIR, "tools", "esp32-arduino-libs")

board_config = env.BoardConfig()

flatten_cppdefines = env.Flatten(env['CPPDEFINES'])

#
# zigbee libs
#
if "ZIGBEE_MODE_ZCZR" in flatten_cppdefines:
    env.Append(
        LIBS=[
            "-lesp_zb_api_zczr",
            "-lesp_zb_cli_command",
            "-lzboss_stack.zczr",
            "-lzboss_port"
        ]
    )
if "ZIGBEE_MODE_ED" in flatten_cppdefines:
    env.Append(
        LIBS=[
            "-lesp_zb_api_ed",
            "-lesp_zb_cli_command",
            "-lzboss_stack.ed",
            "-lzboss_port"
        ]
    )
if "ZIGBEE_MODE_RCP" in flatten_cppdefines:
    env.Append(
        LIBS=[
            "-lesp_zb_api_rcp",
            "-lesp_zb_cli_command",
            "-lzboss_stack.rcp",
            "-lzboss_port"
        ]
    )

env.Append(
    ASFLAGS=[
        "-mlongcalls"
    ],

    ASPPFLAGS=[
        "-x", "assembler-with-cpp"
    ],

    CFLAGS=[
        "-flto=auto",
        "-Wno-frame-address",
        "-fno-builtin-memcpy",
        "-fno-builtin-memset",
        "-fno-builtin-bzero",
        "-fno-builtin-stpcpy",
        "-fno-builtin-strncpy",
        "-std=gnu17",
        "-Wno-old-style-declaration",
        "-Wno-enum-int-mismatch"
    ],

    CXXFLAGS=[
        "-flto=auto",
        "-Wno-frame-address",
        "-fno-builtin-memcpy",
        "-fno-builtin-memset",
        "-fno-builtin-bzero",
        "-fno-builtin-stpcpy",
        "-fno-builtin-strncpy",
        "-std=gnu++2b",
        "-fno-exceptions",
        "-fno-rtti",
        "-Wno-self-move",
        "-Wno-dangling-reference"
    ],

    CCFLAGS=[
        "-flto=auto",
        "-Os",
        "-mlongcalls",
        "-ffunction-sections",
        "-fdata-sections",
        "-Wno-error=unused-function",
        "-Wno-error=unused-variable",
        "-Wno-error=unused-but-set-variable",
        "-Wno-error=deprecated-declarations",
        "-Wno-unused-parameter",
        "-Wno-sign-compare",
        "-Wno-enum-conversion",
        "-gdwarf-4",
        "-ggdb",
        "-freorder-blocks",
        "-Wno-address",
        "-Wno-use-after-free",
        "-Wno-xor-used-as-pow",
        "-fstrict-volatile-bitfields",
        "-fno-jump-tables",
        "-fno-tree-switch-conversion",
        "-MMD"
    ],

    LINKFLAGS=[
        "-flto",
        "-mlongcalls",
        "-Wno-frame-address",
        "-Wl,--cref",
        "-Wl,--defsym=IDF_TARGET_ESP32=0",
        "-Wl,--no-warn-rwx-segments",
        "-fno-rtti",
        "-Wl,--gc-sections",
        "-Wl,--warn-common",
        "-Wl,--wrap=longjmp",
        "-Wl,--undefined=FreeRTOS_openocd_params",
        "--specs=nano.specs",
        "-Wl,--wrap=__register_frame_info_bases",
        "-Wl,--wrap=__register_frame_info",
        "-Wl,--wrap=__register_frame",
        "-Wl,--wrap=__register_frame_info_table_bases",
        "-Wl,--wrap=__register_frame_info_table",
        "-Wl,--wrap=__register_frame_table",
        "-Wl,--wrap=__deregister_frame_info_bases",
        "-Wl,--wrap=__deregister_frame_info",
        "-Wl,--wrap=_Unwind_Find_FDE",
        "-Wl,--wrap=_Unwind_GetGR",
        "-Wl,--wrap=_Unwind_GetCFA",
        "-Wl,--wrap=_Unwind_GetIP",
        "-Wl,--wrap=_Unwind_GetIPInfo",
        "-Wl,--wrap=_Unwind_GetRegionStart",
        "-Wl,--wrap=_Unwind_GetDataRelBase",
        "-Wl,--wrap=_Unwind_GetTextRelBase",
        "-Wl,--wrap=_Unwind_SetIP",
        "-Wl,--wrap=_Unwind_SetGR",
        "-Wl,--wrap=_Unwind_GetLanguageSpecificData",
        "-Wl,--wrap=_Unwind_FindEnclosingFunction",
        "-Wl,--wrap=_Unwind_Resume",
        "-Wl,--wrap=_Unwind_RaiseException",
        "-Wl,--wrap=_Unwind_DeleteException",
        "-Wl,--wrap=_Unwind_ForcedUnwind",
        "-Wl,--wrap=_Unwind_Resume_or_Rethrow",
        "-Wl,--wrap=_Unwind_Backtrace",
        "-Wl,--wrap=__cxa_call_unexpected",
        "-Wl,--wrap=__gxx_personality_v0",
        "-Wl,--wrap=__cxa_throw",
        "-Wl,--wrap=__cxa_allocate_exception",
        "-T", "esp32.rom.redefined.ld",
        "-T", "esp32.peripherals.ld",
        "-T", "esp32.rom.ld",
        "-T", "esp32.rom.api.ld",
        "-T", "esp32.rom.libgcc.ld",
        "-T", "esp32.rom.newlib-data.ld",
        "-T", "esp32.rom.syscalls.ld",
        "-T", "esp32.rom.newlib-funcs.ld",
        "-T", "memory.ld",
        "-T", "sections.ld",
        "-u", "esp_system_include_coredump_init",
        "-u", "nvs_sec_provider_include_impl",
        "-u", "ld_include_hli_vectors_bt",
        "-u", "_Z5setupv",
        "-u", "_Z4loopv",
        "-u", "esp_app_desc",
        "-u", "esp_efuse_startup_include_func",
        "-u", "ld_include_highint_hdl",
        "-u", "start_app",
        "-u", "__ubsan_include",
        "-u", "esp_system_include_startup_funcs",
        "-u", "esp_dport_access_reg_read",
        "-u", "app_main",
        "-u", "newlib_include_heap_impl",
        "-u", "newlib_include_syscalls_impl",
        "-u", "newlib_include_pthread_impl",
        "-u", "newlib_include_assert_impl",
        "-u", "newlib_include_init_funcs",
        "-u", "pthread_include_pthread_impl",
        "-u", "pthread_include_pthread_cond_var_impl",
        "-u", "pthread_include_pthread_local_storage_impl",
        "-u", "pthread_include_pthread_rwlock_impl",
        "-u", "pthread_include_pthread_semaphore_impl",
        "-u", "__cxa_guard_dummy",
        "-u", "__cxx_init_dummy",
        "-u", "__cxx_fatal_exception",
        "-u", "esp_timer_init_include_func",
        "-u", "uart_vfs_include_dev_init",
        "-u", "include_esp_phy_override",
        "-u", "esp_vfs_include_console_register",
        "-u", "vfs_include_syscalls_impl",
        '-Wl,-Map="%s"' % join("${BUILD_DIR}", "${PROGNAME}.map")
    ],

    CPPPATH=[
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "newlib", "platform_include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "config", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "config", "include", "freertos"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "config", "xtensa", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "FreeRTOS-Kernel", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "FreeRTOS-Kernel", "portable", "xtensa", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "FreeRTOS-Kernel", "portable", "xtensa", "include", "freertos"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "freertos", "esp_additions", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "include", "soc"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "include", "soc", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "dma", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "ldo", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "port", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hw_support", "port", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "heap", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "log", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "soc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "soc", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "soc", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "hal", "platform_port", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "hal", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "hal", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_rom", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_rom", "include", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_rom", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_common", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_system", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_system", "port", "soc"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_system", "port", "include", "private"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "xtensa", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "xtensa", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "xtensa", "deprecated_include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "include", "apps"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "include", "apps", "sntp"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "lwip", "src", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "port", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "port", "freertos", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "port", "esp32xx", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "port", "esp32xx", "include", "arch"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "lwip", "port", "esp32xx", "include", "sys"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp32-camera", "driver", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp32-camera", "conversions", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "driver", "deprecated"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "driver", "i2c", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "driver", "touch_sensor", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "driver", "twai", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "driver", "touch_sensor", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_pm", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_ringbuf", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_gpio", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_pcnt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_gptimer", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_spi", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_mcpwm", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_ana_cmpr", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_i2s", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_sdmmc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "sdmmc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_sdspi", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_sdio", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_dac", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_rmt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_tsens", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_sdm", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_i2c", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_uart", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "vfs", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_ledc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_parlio", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_usb_serial_jtag", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "port", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "mbedtls", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "mbedtls", "library"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "esp_crt_bundle", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "mbedtls", "3rdparty", "everest", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "mbedtls", "3rdparty", "p256-m"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mbedtls", "mbedtls", "3rdparty", "p256-m", "p256-m"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_app_format", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_bootloader_format", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "app_update", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bootloader_support", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bootloader_support", "bootloader_flash", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_partition", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "efuse", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "efuse", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_mm", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "spi_flash", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "pthread", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_timer", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "app_trace", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_event", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "nvs_flash", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_phy", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_phy", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_vfs_console", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_netif", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "wpa_supplicant", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "wpa_supplicant", "port", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "wpa_supplicant", "esp_supplicant", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_coex", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_wifi", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_wifi", "wifi_apps", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_wifi", "wifi_apps", "nan_app", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_wifi", "include", "local"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "include", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "common", "osi", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "common", "api", "include", "api"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "common", "btc", "profile", "esp", "blufi", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "common", "btc", "profile", "esp", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "common", "hci_log", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "porting", "ext", "tinycrypt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "ans", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "bas", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "dis", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "gap", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "gatt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "hr", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "htp", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "ias", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "ipss", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "lls", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "prox", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "cts", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "tps", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "hid", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "sps", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "services", "cte", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "util", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "store", "ram", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "host", "store", "config", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "porting", "nimble", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "port", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "nimble", "transport", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "porting", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "nimble", "porting", "npl", "freertos", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "bt", "host", "nimble", "esp-hci", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "unity", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "unity", "unity", "src"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "cmock", "CMock", "src"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "console"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "http_parser"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp-tls"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp-tls", "esp-tls-crypto"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_adc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_adc", "interface"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_adc", "esp32", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_adc", "deprecated", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_isp", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_cam", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_cam", "interface"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_jpeg", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_driver_ppa", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_eth", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_gdbstub", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_hid", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "tcp_transport", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_http_client", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_http_server", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_https_ota", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_https_server", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_psram", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_lcd", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_lcd", "interface"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protobuf-c", "protobuf-c"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protocomm", "include", "common"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protocomm", "include", "security"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protocomm", "include", "transports"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protocomm", "include", "crypto", "srp6a"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "protocomm", "proto-c"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "esp_local_ctrl", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espcoredump", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espcoredump", "include", "port", "xtensa"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "wear_levelling", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "fatfs", "diskio"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "fatfs", "src"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "fatfs", "vfs"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "idf_test", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "idf_test", "include", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "ieee802154", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "json", "cJSON"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "mqtt", "esp-mqtt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "nvs_sec_provider", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "perfmon", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "ulp", "ulp_common", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "ulp", "ulp_fsm", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "ulp", "ulp_fsm", "include", "esp32"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__mdns", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "joltwallet__littlefs", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "dotprod", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "support", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "support", "mem", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "hann", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "blackman", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "blackman_harris", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "blackman_nuttall", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "nuttall", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "windows", "flat_top", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "iir", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "fir", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "add", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "sub", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "mul", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "addc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "mulc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "math", "sqrt", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "mul", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "add", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "addc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "mulc", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "sub", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "fft", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "dct", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "conv", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "common", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "matrix", "mul", "test", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "kalman", "ekf", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp-dsp", "modules", "kalman", "ekf_imu13states", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "espressif__esp_modem", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", "include", "fb_gfx", "include"),
        join(FRAMEWORK_SDK_DIR, "esp32", board_config.get("build.arduino.memory_type", (board_config.get("build.flash_mode", "dio") + "_qspi")), "include"),
        join(FRAMEWORK_DIR, "cores", board_config.get("build.core"))
    ],

    LIBPATH=[
        join(FRAMEWORK_SDK_DIR, "esp32", "lib"),
        join(FRAMEWORK_SDK_DIR, "esp32", "ld"),
        join(FRAMEWORK_SDK_DIR, "esp32", board_config.get("build.arduino.memory_type", (board_config.get("build.flash_mode", "dio") + "_qspi")))
    ],

    LIBS=[
        "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lapp_trace", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lbt", "-lunity", "-lcmock", "-lconsole", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_driver_cam", "-lesp_eth", "-lesp_gdbstub", "-lesp_hid", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lesp_https_server", "-lesp_lcd", "-lprotobuf-c", "-lprotocomm", "-lesp_local_ctrl", "-lespcoredump", "-lwear_levelling", "-lfatfs", "-ljson", "-lmqtt", "-lnvs_sec_provider", "-lperfmon", "-lulp", "-lespressif__esp32-camera", "-lespressif__mdns", "-ljoltwallet__littlefs", "-lespressif__esp-dsp", "-lespressif__esp_modem", "-lfb_gfx", "-lapp_trace", "-lapp_trace", "-lcmock", "-lunity", "-lesp_driver_cam", "-lesp_lcd", "-lesp_local_ctrl", "-lesp_https_server", "-lprotocomm", "-lprotobuf-c", "-lespcoredump", "-ljson", "-lmqtt", "-lnvs_sec_provider", "-lperfmon", "-lespressif__esp32-camera", "-lesp_hid", "-lbt", "-lfatfs", "-lwear_levelling", "-lespressif__mdns", "-lconsole", "-ljoltwallet__littlefs", "-lespressif__esp-dsp", "-lespressif__esp_modem", "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_eth", "-lesp_gdbstub", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lulp", "-lmbedtls_2", "-lmbedcrypto", "-lmbedx509", "-leverest", "-lp256m", "-lcoexist", "-lcore", "-lespnow", "-lmesh", "-lnet80211", "-lpp", "-lsmartconfig", "-lwapi", "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_eth", "-lesp_gdbstub", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lulp", "-lmbedtls_2", "-lmbedcrypto", "-lmbedx509", "-leverest", "-lp256m", "-lcoexist", "-lcore", "-lespnow", "-lmesh", "-lnet80211", "-lpp", "-lsmartconfig", "-lwapi", "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_eth", "-lesp_gdbstub", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lulp", "-lmbedtls_2", "-lmbedcrypto", "-lmbedx509", "-leverest", "-lp256m", "-lcoexist", "-lcore", "-lespnow", "-lmesh", "-lnet80211", "-lpp", "-lsmartconfig", "-lwapi", "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_eth", "-lesp_gdbstub", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lulp", "-lmbedtls_2", "-lmbedcrypto", "-lmbedx509", "-leverest", "-lp256m", "-lcoexist", "-lcore", "-lespnow", "-lmesh", "-lnet80211", "-lpp", "-lsmartconfig", "-lwapi", "-lxtensa", "-lesp_driver_gpio", "-lesp_pm", "-lmbedtls", "-lesp_app_format", "-lesp_bootloader_format", "-lapp_update", "-lesp_partition", "-lefuse", "-lbootloader_support", "-lesp_mm", "-lspi_flash", "-lesp_system", "-lesp_common", "-lesp_rom", "-lhal", "-llog", "-lheap", "-lsoc", "-lesp_hw_support", "-lfreertos", "-lnewlib", "-lpthread", "-lcxx", "-lesp_timer", "-lesp_driver_gptimer", "-lesp_ringbuf", "-lesp_driver_uart", "-lesp_event", "-lnvs_flash", "-lesp_driver_pcnt", "-lesp_driver_spi", "-lesp_driver_mcpwm", "-lesp_driver_i2s", "-lsdmmc", "-lesp_driver_sdmmc", "-lesp_driver_sdspi", "-lesp_driver_sdio", "-lesp_driver_dac", "-lesp_driver_rmt", "-lesp_driver_sdm_2", "-lesp_driver_i2c", "-lesp_driver_ledc", "-ldriver", "-lesp_phy", "-lesp_vfs_console", "-lvfs", "-llwip", "-lesp_netif", "-lwpa_supplicant", "-lesp_coex", "-lesp_wifi", "-lhttp_parser", "-lesp-tls", "-lesp_adc", "-lesp_eth", "-lesp_gdbstub", "-ltcp_transport", "-lesp_http_client", "-lesp_http_server", "-lesp_https_ota", "-lulp", "-lmbedtls_2", "-lmbedcrypto", "-lmbedx509", "-leverest", "-lp256m", "-lcoexist", "-lcore", "-lespnow", "-lmesh", "-lnet80211", "-lpp", "-lsmartconfig", "-lwapi", "-lxt_hal", "-lc", "-lm", "-lstdc++", "-lpthread", "-lnewlib", "-lgcc", "-lcxx", "-lphy", "-lrtc", "-lesp_phy", "-lphy", "-lrtc", "-lesp_phy", "-lphy", "-lrtc", "-lbtdm_app"
    ],

    CPPDEFINES=[
        "ESP32_ARDUINO_LIB_BUILDER",
        "ESP_PLATFORM",
        ("IDF_VER", '\\"5.3.1.241016\\"'),
        "LFS_MULTIVERSION",
        ("MBEDTLS_CONFIG_FILE", '\\"mbedtls/esp_config.h\\"'),
        "NDEBUG",
        ("SOC_MMU_PAGE_SIZE", 'CONFIG_MMU_PAGE_SIZE'),
        ("SOC_XTAL_FREQ_MHZ", 'CONFIG_XTAL_FREQ'),
        "UNITY_INCLUDE_CONFIG_H",
        "_GLIBCXX_HAVE_POSIX_SEMAPHORE",
        "_GLIBCXX_USE_POSIX_SEMAPHORE",
        "_GNU_SOURCE",
        "_POSIX_READER_WRITER_LOCKS",
        "ARDUINO_ARCH_ESP32",
        ("ESP32", "ESP32"),
        ("F_CPU", "$BOARD_F_CPU"),
        ("ARDUINO", 10812),
        ("ARDUINO_VARIANT", '\\"%s\\"' % board_config.get("build.variant").replace('"', "")),
        ("ARDUINO_BOARD", '\\"%s\\"' % board_config.get("name").replace('"', "")),
        "ARDUINO_PARTITION_%s" % basename(board_config.get(
            "build.partitions", "default.csv")).replace(".csv", "").replace("-", "_")
    ]
)
