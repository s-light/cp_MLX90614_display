# SPDX-FileCopyrightText: 2026 stefan krüger
# SPDX-License-Identifier: MIT

import time
import board

import adafruit_mlx90614

# The MLX90614 only works at the default I2C bus speed of 100kHz.
# A higher speed, such as 400kHz, will not work.
# uses board.SCL and board.SDA
i2c = board.I2C()  
mlx = adafruit_mlx90614.MLX90614(i2c)


# ── main ───────────────────────────────────────────────────────────────────────
print("cp_MLX90614_display - ready")

while True:
    # temperature results in celsius
    print("Ambent Temp: ", mlx.ambient_temperature)
    print("Object Temp: ", mlx.object_temperature)
    time.sleep(1.0)

