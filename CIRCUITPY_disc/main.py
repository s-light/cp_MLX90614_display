# SPDX-FileCopyrightText: 2026 stefan krüger
# SPDX-License-Identifier: MIT

import time
import board

import adafruit_mlx90614

import terminalio
import displayio
from adafruit_display_text import label

# The MLX90614 only works at the default I2C bus speed of 100kHz.
# A higher speed, such as 400kHz, will not work.
# uses board.SCL and board.SDA
i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)

FONTSCALE = 2
TEXT_COLOR = 0xFFFF00


display = board.DISPLAY

base = displayio.Group()
display.root_group = base

ambient_template = "Ambient:    {:>6.2f}C"
object_max_template = "Max:    {:>6.2f}C"
object_min_template = "Min:    {:>6.2f}C"
object_template = "{:>6.2f}"

object_max = 0.0
object_min = 0.0

text_area_ambient = label.Label(
    terminalio.FONT,
    text=ambient_template.format(0),
    color=TEXT_COLOR,
    scale=FONTSCALE,
)
text_area_ambient.anchor_point = (1.0, 0.0)
text_area_ambient.anchored_position = (display.width, 0)
base.append(text_area_ambient)

line_height = text_area_ambient.bounding_box[3] + 7

text_area_object_max = label.Label(
    terminalio.FONT,
    text=object_max_template.format(0),
    color=TEXT_COLOR,
    scale=FONTSCALE,
)
text_area_object_max.anchor_point = (1.0, 0.0)
text_area_object_max.anchored_position = (display.width, line_height* 1)
base.append(text_area_object_max)

text_area_object_min = label.Label(
    terminalio.FONT,
    text=object_min_template.format(0),
    color=TEXT_COLOR,
    scale=FONTSCALE,
)
text_area_object_min.anchor_point = (1.0, 0.0)
text_area_object_min.anchored_position = (display.width, line_height* 2)
base.append(text_area_object_min)


text_area_object_value = label.Label(
    terminalio.FONT, text=object_template.format(0), color=TEXT_COLOR, scale=6
)
text_area_object_value.anchor_point = (1.0, 1.0)
text_area_object_value.anchored_position = (display.width, display.height)

print(f"display.width '{display.width}'")
base.append(text_area_object_value)


# ── main ───────────────────────────────────────────────────────────────────────
print("cp_MLX90614_display - ready")

while True:
    # temperature results in celsius
    # print("Ambient Temp: ", mlx.ambient_temperature)
    # print("Object  Temp: ", mlx.object_temperature)
    # time.sleep(1.0)
    text_area_ambient.text = ambient_template.format(mlx.ambient_temperature)
    if object_min > mlx.object_temperature:
        object_min = mlx.object_temperature
    if object_max < mlx.object_temperature:
        object_max = mlx.object_temperature
    text_area_object_value.text = object_template.format(mlx.object_temperature)
    text_area_object_max.text = object_max_template.format(object_max)
    text_area_object_min.text = object_min_template.format(object_min)
    time.sleep(0.2)
