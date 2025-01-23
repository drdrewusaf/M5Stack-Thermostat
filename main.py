import os, sys, io
import M5
from M5 import *
from unit import Relay2Unit
from hardware import WDT
from hardware import I2C
from hardware import Pin
import time
from unit import ENVPROUnit
from unit import ENVUnit
import network
try:
    import usocket as socket
except:
    import socket



lbl_env_iv_temp = None
lbl_env_iv_hum = None
lbl_env_iv_pres = None
lbl_env_pro_temp = None
lbl_env_pro_hum = None
lbl_env_pro_pres = None
lbl_env_pro_alt = None
img_pro_humidity = None
img_pressure = None
img_power_off = None
img_power_on = None
img_altitude = None
lbl_furn_set_temp = None
lbl_fan_set_temp = None
img_flame_out = None
img_fan_out = None
img_settings = None
img_home = None
lbl_scrn_bright = None
lbl_scrn_bright_max = None
lbl_scrn_bright_min = None
img_scrn_bright_min = None
img_scrn_bright_max = None
lbl_scrn_timeout = None
line_settings_1 = None
img_timeout_set = None
img_next = None
img_iv_humidity = None
lbl_sensor_freq = None
img_freq_set_on = None
lbl_sys_on = None
lbl_sys_off = None
img_freq_set_off = None
rect_slider = None
circle_furn_set_deg = None
img_flame = None
img_fan = None
rect_btn_furn = None
rect_btn_fan = None
circle_fan_set_deg = None
lbl_scrn_min_set = None
lbl_scrn_max_set = None
lbl_scrn_timeout_set = None
lbl_timeout_ms_set = None
img_back = None
lbl_freq_ms_on = None
lbl_freq_on_set = None
lbl_freq_ms_off = None
lbl_freq_off_set = None
circle_slider = None
circle_pro_deg = None
circle_iv_deg = None
title_settings_1 = None
title_settings_2 = None
wdt = None
i2c0 = None
wlan = None
oldData2 = None
oldData3 = None
file_0 = None
env4_0 = None
envpro_0 = None
relay2_0 = None


import math

html_btn_press = None
var = None
screen_num = None
num = None
t_or_d = None
pressure = None
relay_num = None
relay_action = None
alt = None
temp = None
furnace_or_fan = None
set_bar_selected = None
slider_action = None
html = None
settings_change = None
env_iv_hum = None
relay_1_state = None
sys_active = None
html_sys_btn_color = None
html_fan_txt = None
env_pro_temp = None
screen_bright_min = None
touch_set = None
env_iv_pres = None
screen_bright_max = None
relay_2_state = None
screen_bright_timeout = None
env_iv_temp = None
sens_read_on = None
sens_read_off = None
html_furn_txt = None
env_pro_hum = None
first_run = None
sens_read_delay = None
set_fan_temp = None
set_furnace_temp = None
slider_x = None
settings = None
curr_touch = None
html_sys_act_txt = None
env_pro_pres = None
now = None
env_pro_alt = None
env_pro_gas = None
slider_y = None
screen_now = None
slider_r = None
wr_set_temps = None
last_save = None
resp = None
s = None
conn = None
request = None
conn_accept = None
count = None
i = None

# Describe this function...
def web_page(html_btn_press):
  global var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if html_btn_press == 6:
    if sys_active == False:
      sys_active = True
    else:
      sys_active = False
    sys_act()
    html_btn_press = -1
  if sys_active == True:
    html_sys_btn_color = 'green'
  else:
    html_sys_btn_color = 'red'
  html_fan_txt = bool_to_html_txt(relay_2_state)
  html_furn_txt = bool_to_html_txt(relay_1_state)
  html_sys_act_txt = bool_to_html_txt(sys_active)
  html = """<!doctype html><html lang="en"><head><meta http-equiv="refresh" content="10; URL=/"><style>body {background-color: rgb(36, 36, 36);font-family: Verdana, Geneva, Tahoma, sans-serif; font-size: x-large; color: lightgray;} button {padding: 5px; font-size: x-large;} td {padding-left: 10px; padding-right: 10px;}</style><title>Ruby's Thermostat</title></head><body><p align="center">System is <a href="/?sys=chg"><button style="background-color: """ + str(html_sys_btn_color) + """;" >"""+ str(html_sys_act_txt) +"""</button></a></p><table align="center"><tr><td>Trailer Temp:</td><td><b>"""+ str(env_pro_temp) +"""</b></td></tr><tr><td>Underbelly Temp:</td><td><b>"""+ str(env_iv_temp) +"""</b></td></tr><tr><td>Furnace is:</td><td><b>"""+ str(html_furn_txt) +"""</b></td></tr><tr><td>Fan is:</td><td><b>"""+ str(html_fan_txt) +"""</b></td></tr></table></body></html>"""
  return html

# Describe this function...
def bool_to_html_txt(var):
  global html_btn_press, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if var == True:
    var = 'ON'
  else:
    var = 'OFF'
  return var

# Describe this function...
def connection_handler():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  try:
  	conn, addr = s.accept()
  	request = conn.recv(1024)
  	request = str(request)
  	html_btn_press = request.find('/?sys=chg')
  	resp = web_page(html_btn_press)
  	conn.send('HTTP/1.1 200 OK\n')
  	conn.send('Content-Type: text/html\n')
  	conn.send('Connection: close\n\n')
  	conn.sendall(resp)
  	conn.close()
  except:
  	pass

# Describe this function...
def update_screen_data(screen_num):
  global html_btn_press, var, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if screen_num==0:
    lbl_env_pro_temp.setText(str(env_pro_temp))
    lbl_env_pro_hum.setText(str(env_pro_hum))
    lbl_env_pro_pres.setText(str(env_pro_pres))
    lbl_env_pro_alt.setText(str(env_pro_alt))
    lbl_furn_set_temp.setText(str(set_furnace_temp))
    lbl_fan_set_temp.setText(str(set_fan_temp))
    lbl_env_iv_temp.setText(str(env_iv_temp))
    lbl_env_iv_hum.setText(str(env_iv_hum))
    if relay_1_state != oldData2:
      oldData2 = relay_1_state
      if relay_1_state == True:
        img_flame_out.setVisible(False)
        img_flame.setVisible(True)
      elif relay_1_state == False:
        img_flame.setVisible(False)
        img_flame_out.setVisible(True)
    else:
      pass

    if relay_2_state != oldData3:
      oldData3 = relay_2_state
      if relay_2_state == True:
        img_fan_out.setVisible(False)
        img_fan.setVisible(True)
      elif relay_2_state == False:
        img_fan.setVisible(False)
        img_fan_out.setVisible(True)
    else:
      pass

  elif screen_num==1:
    lbl_scrn_min_set.setText(str(screen_bright_min))
    if len(str(screen_bright_min)) == 1:
      lbl_scrn_min_set.setCursor(x=75, y=70)
    elif len(str(screen_bright_min)) == 2:
      lbl_scrn_min_set.setCursor(x=71, y=70)
    elif len(str(screen_bright_min)) == 3:
      lbl_scrn_min_set.setCursor(x=67, y=70)
    lbl_scrn_max_set.setText(str(screen_bright_max))
    if len(str(screen_bright_max)) == 1:
      lbl_scrn_max_set.setCursor(x=235, y=70)
    elif len(str(screen_bright_max)) == 2:
      lbl_scrn_max_set.setCursor(x=231, y=70)
    elif len(str(screen_bright_max)) == 3:
      lbl_scrn_max_set.setCursor(x=227, y=70)
    if screen_bright_timeout <= 59:
      lbl_scrn_timeout_set.setText(str(screen_bright_timeout))
      lbl_timeout_ms_set.setText(str(' Seconds '))
      if len(str(screen_bright_timeout)) == 1:
        lbl_scrn_timeout_set.setCursor(x=99, y=171)
      elif len(str(screen_bright_timeout)) == 2:
        lbl_scrn_timeout_set.setCursor(x=95, y=171)
    else:
      lbl_scrn_timeout_set.setText(str(divide_by_60(screen_bright_timeout, 'd')))
      lbl_timeout_ms_set.setText(str(' Minutes '))
      if divide_by_60(screen_bright_timeout, 't') == 1:
        lbl_scrn_timeout_set.setCursor(x=99, y=171)
      elif divide_by_60(screen_bright_timeout, 't') == 2:
        lbl_scrn_timeout_set.setCursor(x=95, y=171)
      elif divide_by_60(screen_bright_timeout, 't') == 3:
        lbl_scrn_timeout_set.setCursor(x=91, y=171)
  elif screen_num==2:
    if sens_read_on <= 59:
      lbl_freq_on_set.setText(str(sens_read_on))
      lbl_freq_ms_on.setText(str(' Seconds '))
      if len(str(sens_read_on)) == 1:
        lbl_freq_on_set.setCursor(x=99, y=73)
      elif len(str(sens_read_on)) == 2:
        lbl_freq_on_set.setCursor(x=95, y=73)
    else:
      lbl_freq_on_set.setText(str(divide_by_60(sens_read_on, 'd')))
      lbl_freq_ms_on.setText(str(' Minutes '))
      if divide_by_60(sens_read_on, 't') == 1:
        lbl_freq_on_set.setCursor(x=99, y=73)
      elif divide_by_60(sens_read_on, 't') == 2:
        lbl_freq_on_set.setCursor(x=95, y=73)
      elif divide_by_60(sens_read_on, 't') == 3:
        lbl_freq_on_set.setCursor(x=91, y=73)
    if sens_read_off <= 59:
      lbl_freq_off_set.setText(str(sens_read_off))
      lbl_freq_ms_off.setText(str(' Seconds '))
      if len(str(sens_read_off)) == 1:
        lbl_freq_off_set.setCursor(x=99, y=171)
      elif len(str(sens_read_off)) == 2:
        lbl_freq_off_set.setCursor(x=95, y=171)
    else:
      lbl_freq_off_set.setText(str(divide_by_60(sens_read_off, 'd')))
      lbl_freq_ms_off.setText(str(' Minutes '))
      if divide_by_60(sens_read_off, 't') == 1:
        lbl_freq_off_set.setCursor(x=99, y=171)
      elif divide_by_60(sens_read_off, 't') == 2:
        lbl_freq_off_set.setCursor(x=95, y=171)
      elif divide_by_60(sens_read_off, 't') == 3:
        lbl_freq_off_set.setCursor(x=91, y=171)
  else:
    pass

# Describe this function...
def btn_power():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 110 and curr_touch[0] <= 205 and curr_touch[1] >= 0 and curr_touch[1] <= 80:
    if sys_active == False:
      sys_active = True
    else:
      sys_active = False
    touch_set = True
    sys_act()

# Describe this function...
def btn_settings_home():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 125 and curr_touch[0] <= 195 and curr_touch[1] >= 220 and curr_touch[1] <= 310:
    if screen_num != 0:
      screen_num = 0
    else:
      screen_num = 1
    touch_set = True
    change_screen(screen_num)

# Describe this function...
def btn_back_next():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 0 and curr_touch[0] <= 100 and curr_touch[1] >= 220 and curr_touch[1] <= 310 or curr_touch[0] >= 220 and curr_touch[0] <= 320 and curr_touch[1] >= 220 and curr_touch[1] <= 310:
    if screen_num == 1:
      screen_num = 2
    else:
      screen_num = 1
    touch_set = True
    change_screen(screen_num)

# Describe this function...
def btn_temp_slider():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 12 and curr_touch[0] <= 306 and curr_touch[1] >= 130 and curr_touch[1] <= 170:
    update_slider(set_bar_selected, 'change_pos')

# Describe this function...
def btn_furnace():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 0 and curr_touch[0] <= 100 and curr_touch[1] >= 230 and curr_touch[1] <= 310:
    set_bar_selected = 'furnace'
    update_slider(set_bar_selected, 'change_sys')
    touch_set = True

# Describe this function...
def update_sensors():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if now + sens_read_delay < (time.time()) or first_run == False:
    env_iv_hum = (str((int(env4_0.read_humidity()))) + str('%'))
    env_iv_pres = (str((hpa_to_inhg(env4_0.read_pressure()))) + str(' inHg'))
    env_iv_temp = c_to_f(env4_0.read_temperature())
    env_pro_alt = (str((m_to_ft(envpro_0.get_altitude()))) + str(' ft'))
    env_pro_gas = envpro_0.get_gas_resistance()
    env_pro_hum = (str((int(envpro_0.get_humidity()))) + str('%'))
    env_pro_pres = (str((hpa_to_inhg(envpro_0.get_pressure()))) + str(' inHg'))
    env_pro_temp = c_to_f(envpro_0.get_temperature())
    relay_1_state = relay2_0.get_relay_status(1)
    relay_2_state = relay2_0.get_relay_status(2)
    now = time.time()
    first_run = True
  else:
    pass

# Describe this function...
def btn_fan():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 220 and curr_touch[0] <= 320 and curr_touch[1] >= 230 and curr_touch[1] <= 310:
    set_bar_selected = 'fan'
    update_slider(set_bar_selected, 'change_sys')
    touch_set = True

# Describe this function...
def btn_bright_min_up():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 44 and curr_touch[0] <= 115 and curr_touch[1] >= 38 and curr_touch[1] <= 75:
    if screen_bright_min <= 254:
      screen_bright_min = screen_bright_min + 5
    touch_set = True

# Describe this function...
def clr_screen():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  Widgets.fillScreen(0x000000)

# Describe this function...
def change_screen(screen_num):
  global html_btn_press, var, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  clr_screen()
  update_settings_file()
  if screen_num==0:
    load_screen_0()
  elif screen_num==1:
    load_screen_1()
  elif screen_num==2:
    load_screen_2()
  else:
    load_screen_0()
  update_screen_data(screen_num)

# Describe this function...
def btn_bright_min_down():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 44 and curr_touch[0] <= 115 and curr_touch[1] >= 85 and curr_touch[1] <= 122:
    if screen_bright_min > 0:
      screen_bright_min = screen_bright_min - 5
    touch_set = True

# Describe this function...
def sys_act():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if sys_active == False:
    img_power_on.setVisible(False)
    img_power_off.setVisible(True)
    sens_read_delay = sens_read_off
  else:
    img_power_off.setVisible(False)
    img_power_on.setVisible(True)
    sens_read_delay = sens_read_on

# Describe this function...
def divide_by_60(num, t_or_d):
  global html_btn_press, var, screen_num, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if t_or_d == 't':
    num = len(str((int(num / 60))))
  else:
    num = int(num / 60)
  return num

# Describe this function...
def btn_bright_max_up():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 204 and curr_touch[0] <= 275 and curr_touch[1] >= 38 and curr_touch[1] <= 75:
    if screen_bright_max <= 254:
      screen_bright_max = screen_bright_max + 5
    touch_set = True

# Describe this function...
def hpa_to_inhg(pressure):
  global html_btn_press, var, screen_num, num, t_or_d, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  pressure = 0.02953 * pressure
  return "%.2f"%(pressure)

# Describe this function...
def relay_control(relay_num, relay_action):
  global html_btn_press, var, screen_num, num, t_or_d, pressure, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if relay_action=='on':
    if relay_num==1:
      if relay_1_state == False:
        relay2_0.set_relay_cntrl(relay_num, 1)
    elif relay_num==2:
      if relay_2_state == False:
        relay2_0.set_relay_cntrl(relay_num, 1)
    else:
      pass
  elif relay_action=='off':
    relay2_0.set_relay_cntrl(relay_num, 0)
  else:
    pass
  relay_1_state = relay2_0.get_relay_status(1)
  relay_2_state = relay2_0.get_relay_status(2)

# Describe this function...
def load_screen_0():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  sys_act()
  lbl_env_pro_temp.setVisible(True)
  lbl_env_iv_temp.setVisible(True)
  lbl_env_iv_hum.setVisible(True)
  lbl_env_pro_hum.setVisible(True)
  lbl_env_pro_pres.setVisible(True)
  lbl_env_pro_alt.setVisible(True)
  lbl_furn_set_temp.setVisible(True)
  lbl_fan_set_temp.setVisible(True)
  circle_slider.setCursor(x=slider_x, y=slider_y)
  rect_slider.setVisible(True)
  circle_slider.setVisible(True)
  circle_furn_set_deg.setVisible(True)
  circle_fan_set_deg.setVisible(True)
  circle_pro_deg.setVisible(True)
  circle_iv_deg.setVisible(True)
  rect_btn_furn.setVisible(True)
  rect_btn_fan.setVisible(True)
  img_pressure.setVisible(True)
  img_pro_humidity.setVisible(True)
  img_iv_humidity.setVisible(True)
  img_altitude.setVisible(True)
  img_flame_out.setVisible(True)
  img_fan_out.setVisible(True)
  img_settings.setVisible(True)

# Describe this function...
def m_to_ft(alt):
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  alt = 3.28 * alt
  return int(alt)

# Describe this function...
def c_to_f(temp):
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  temp = 1.8 * temp + 32
  return int(temp)

# Describe this function...
def btn_bright_max_down():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 204 and curr_touch[0] <= 275 and curr_touch[1] >= 85 and curr_touch[1] <= 122:
    if screen_bright_max > 0:
      screen_bright_max = screen_bright_max - 5
    touch_set = True

# Describe this function...
def btn_timeout_up():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 139 and curr_touch[1] <= 176:
    if screen_bright_timeout >= 60 and screen_bright_timeout <= 1740:
      screen_bright_timeout = screen_bright_timeout + 60
    elif screen_bright_timeout < 60:
      screen_bright_timeout = screen_bright_timeout + 5
    touch_set = True

# Describe this function...
def furnace_fan_control(furnace_or_fan):
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if furnace_or_fan == 'furnace':
    if env_pro_temp==env_pro_temp < set_furnace_temp - 2:
      relay_control(1, 'on')
    elif env_pro_temp==env_pro_temp >= set_furnace_temp + 1:
      relay_control(1, 'off')
    else:
      pass
  elif furnace_or_fan == 'fan':
    if env_iv_temp==env_iv_temp < set_fan_temp:
      relay_control(2, 'on')
    elif env_iv_temp==env_iv_temp >= set_fan_temp + 2:
      relay_control(2, 'off')
    else:
      pass

# Describe this function...
def btn_timeout_down():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 188 and curr_touch[1] <= 225:
    if screen_bright_timeout >= 120 and screen_bright_timeout <= 1800:
      screen_bright_timeout = screen_bright_timeout - 60
    elif screen_bright_timeout <= 60:
      screen_bright_timeout = screen_bright_timeout - 5
    touch_set = True

# Describe this function...
def load_screen_1():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  title_settings_1.setVisible(True)
  img_scrn_bright_min.setVisible(True)
  img_scrn_bright_max.setVisible(True)
  img_timeout_set.setVisible(True)
  img_back.setVisible(True)
  img_next.setVisible(True)
  img_home.setVisible(True)
  lbl_scrn_bright.setVisible(True)
  lbl_scrn_bright_min.setVisible(True)
  lbl_scrn_bright_max.setVisible(True)
  lbl_scrn_min_set.setVisible(True)
  lbl_scrn_max_set.setVisible(True)
  lbl_scrn_timeout.setVisible(True)
  lbl_scrn_timeout_set.setVisible(True)
  lbl_timeout_ms_set.setVisible(True)

# Describe this function...
def btn_sens_read_on_up():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 43 and curr_touch[1] <= 77:
    if sens_read_on >= 60 and sens_read_on <= 1740:
      sens_read_on = sens_read_on + 60
    elif sens_read_on < 60:
      sens_read_on = sens_read_on + 5
    touch_set = True

# Describe this function...
def load_screen_2():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  title_settings_2.setVisible(True)
  img_freq_set_on.setVisible(True)
  img_freq_set_off.setVisible(True)
  img_back.setVisible(True)
  img_next.setVisible(True)
  img_home.setVisible(True)
  lbl_sensor_freq.setVisible(True)
  lbl_sys_on.setVisible(True)
  lbl_sys_off.setVisible(True)
  lbl_freq_on_set.setVisible(True)
  lbl_freq_off_set.setVisible(True)
  lbl_freq_ms_on.setVisible(True)
  lbl_freq_ms_off.setVisible(True)

# Describe this function...
def btn_sens_read_on_down():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 89 and curr_touch[1] <= 125:
    if sens_read_on >= 120 and sens_read_on <= 1800:
      sens_read_on = sens_read_on - 60
    elif sens_read_on <= 60:
      sens_read_on = sens_read_on - 5
    touch_set = True

# Describe this function...
def check_settings_change():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  settings_change = False
  if settings[0] != set_furnace_temp:
    settings_change = True
  elif settings[1] != set_fan_temp:
    settings_change = True
  elif settings[2] != screen_bright_min:
    settings_change = True
  elif settings[3] != screen_bright_max:
    settings_change = True
  elif settings[4] != screen_bright_timeout:
    settings_change = True
  elif settings[5] != sens_read_on:
    settings_change = True
  elif settings[6] != sens_read_off:
    settings_change = True
  elif settings[7] != sys_active:
    settings_change = True
  return settings_change

# Describe this function...
def update_slider(set_bar_selected, slider_action):
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if slider_action=='change_pos':
    rect_slider.setVisible(False)
    circle_slider.setVisible(False)
    slider_x = math.ceil((math.ceil(((M5.Touch.getX()) - slider_r) / 7) * 7) + 12)
    circle_slider.setCursor(x=slider_x, y=slider_y)
    rect_slider.setVisible(True)
    circle_slider.setVisible(True)
    if set_bar_selected=='furnace':
      set_furnace_temp = int((slider_x - 12) / 7 + 35)
    elif set_bar_selected=='fan':
      set_fan_temp = int((slider_x - 12) / 7 + 35)
    else:
      pass
  elif slider_action=='change_sys':
    if set_bar_selected=='furnace':
      rect_slider.setVisible(False)
      circle_slider.setVisible(False)
      rect_slider.setColor(color=0xffffff, fill_c=0xcc6600)
      circle_slider.setColor(color=0xffffff, fill_c=0xcc6600)
      slider_x = math.ceil((set_furnace_temp - 35) * 7 + slider_r)
      circle_slider.setCursor(x=slider_x, y=slider_y)
      rect_slider.setVisible(True)
      circle_slider.setVisible(True)
    elif set_bar_selected=='fan':
      rect_slider.setVisible(False)
      circle_slider.setVisible(False)
      rect_slider.setColor(color=0xffffff, fill_c=0x339999)
      circle_slider.setColor(color=0xffffff, fill_c=0x339999)
      slider_x = math.ceil((set_fan_temp - 35) * 7 + slider_r)
      circle_slider.setCursor(x=slider_x, y=slider_y)
      rect_slider.setVisible(True)
      circle_slider.setVisible(True)
    else:
      pass
  else:
    pass

# Describe this function...
def btn_sens_read_off_up():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 139 and curr_touch[1] <= 176:
    if sens_read_off >= 60 and sens_read_off <= 1740:
      sens_read_off = sens_read_off + 60
    elif sens_read_off < 60:
      sens_read_off = sens_read_off + 5
    touch_set = True

# Describe this function...
def btn_sens_read_off_down():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if curr_touch[0] >= 68 and curr_touch[0] <= 139 and curr_touch[1] >= 188 and curr_touch[1] <= 225:
    if sens_read_off >= 120 and sens_read_off <= 1800:
      sens_read_off = sens_read_off - 60
    elif sens_read_off <= 60:
      sens_read_off = sens_read_off - 5
    touch_set = True

# Describe this function...
def update_settings_file():
  global html_btn_press, var, screen_num, num, t_or_d, pressure, relay_num, relay_action, alt, temp, furnace_or_fan, set_bar_selected, slider_action, html, settings_change, env_iv_hum, relay_1_state, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, screen_bright_max, relay_2_state, screen_bright_timeout, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i, lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if check_settings_change():
    print('Writing new settings.')
    settings[0] = set_furnace_temp
    settings[1] = set_fan_temp
    settings[2] = screen_bright_min
    settings[3] = screen_bright_max
    settings[4] = screen_bright_timeout
    settings[5] = sens_read_on
    settings[6] = sens_read_off
    settings[6] = sys_active
    wr_set_temps = [str(set_furnace_temp), str(set_fan_temp), str(screen_bright_min), str(screen_bright_max), str(screen_bright_timeout), str(sens_read_on), str(sens_read_off), str(sys_active)]
    file_0 = open('/flash/res/settings.txt', 'w')
    file_0.write(','.join(wr_set_temps))
    file_0.close()
    last_save = time.time()


def setup():
  global lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0, html, var, num, pressure, alt, temp, settings_change, screen_num, set_bar_selected, env_iv_hum, relay_action, relay_1_state, slider_action, html_btn_press, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, t_or_d, screen_bright_max, relay_num, relay_2_state, screen_bright_timeout, furnace_or_fan, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i

  M5.begin()
  lbl_env_iv_temp = Widgets.Label("35", 202, 0, 1.0, 0xd1ffff, 0x000000, Widgets.FONTS.DejaVu72)
  lbl_env_iv_hum = Widgets.Label("99%", 264, 196, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_iv_pres = Widgets.Label("29.99 inHg", 182, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_pro_temp = Widgets.Label("70", 0, 0, 1.0, 0xffe7d7, 0x000000, Widgets.FONTS.DejaVu72)
  lbl_env_pro_hum = Widgets.Label("99%", 22, 196, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_pro_pres = Widgets.Label("29.99 inHg", 182, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_pro_alt = Widgets.Label("1000 ft", 40, 164, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  img_pro_humidity = Widgets.Image("res/img/1humidity.png", 0, 191, scale_x=1, scale_y=1)
  img_pressure = Widgets.Image("res/img/1pressure.png", 151, 165, scale_x=1, scale_y=1)
  img_power_off = Widgets.Image("res/img/1power_off.png", 124, 0, scale_x=1, scale_y=1)
  img_power_on = Widgets.Image("res/img/1power_on.png", 124, 0, scale_x=1, scale_y=1)
  img_altitude = Widgets.Image("res/img/1altitude.png", 1, 162, scale_x=1, scale_y=1)
  lbl_furn_set_temp = Widgets.Label("70", 0, 90, 1.0, 0xcc6600, 0x000000, Widgets.FONTS.DejaVu40)
  lbl_fan_set_temp = Widgets.Label("35", 256, 90, 1.0, 0x339999, 0x000000, Widgets.FONTS.DejaVu40)
  img_flame_out = Widgets.Image("res/img/1heating_out.png", 95, 75, scale_x=1, scale_y=1)
  img_fan_out = Widgets.Image("res/img/1fan_out.png", 178, 75, scale_x=1, scale_y=1)
  img_settings = Widgets.Image("res/img/1settings.png", 136, 217, scale_x=1, scale_y=1)
  img_home = Widgets.Image("res/img/1home.png", 137, 209, scale_x=1, scale_y=1)
  lbl_scrn_bright = Widgets.Label("Screen Brightness", 95, 10, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_scrn_bright_max = Widgets.Label("Max", 225, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_scrn_bright_min = Widgets.Label("Min", 66, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  img_scrn_bright_min = Widgets.Image("res/img/1set_roller.png", 47, 37, scale_x=1, scale_y=1)
  img_scrn_bright_max = Widgets.Image("res/img/1set_roller.png", 207, 37, scale_x=1, scale_y=1)
  lbl_scrn_timeout = Widgets.Label("Screen Brightness Timeout", 73, 121, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  line_settings_1 = Widgets.Line(2, 120, 314, 120, 0xa3a26a)
  img_timeout_set = Widgets.Image("res/img/1set_roller.png", 71, 138, scale_x=1, scale_y=1)
  img_next = Widgets.Image("res/img/1next.png", 259, 222, scale_x=1, scale_y=1)
  img_iv_humidity = Widgets.Image("res/img/1humidity.png", 242, 191, scale_x=1, scale_y=1)
  lbl_sensor_freq = Widgets.Label("Sensor Read Frequency", 83, 10, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  img_freq_set_on = Widgets.Image("res/img/1set_roller.png", 71, 40, scale_x=1, scale_y=1)
  lbl_sys_on = Widgets.Label("System On", 127, 23, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_sys_off = Widgets.Label("System Off", 126, 121, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  img_freq_set_off = Widgets.Image("res/img/1set_roller.png", 71, 139, scale_x=1, scale_y=1)
  rect_slider = Widgets.Rectangle(5, 146, 310, 5, 0xffffff, 0xcc6600)
  circle_furn_set_deg = Widgets.Circle(58, 98, 5, 0xcc6600, 0x000000)
  img_flame = Widgets.Image("res/img/1heating.png", 95, 75, scale_x=1, scale_y=1)
  img_fan = Widgets.Image("res/img/1fan.png", 178, 75, scale_x=1, scale_y=1)
  rect_btn_furn = Widgets.Rectangle(0, 233, 90, 5, 0xcc6600, 0xcc6600)
  rect_btn_fan = Widgets.Rectangle(228, 233, 90, 5, 0x339999, 0x339999)
  circle_fan_set_deg = Widgets.Circle(313, 98, 5, 0x339999, 0x000000)
  lbl_scrn_min_set = Widgets.Label("0", 75, 70, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_scrn_max_set = Widgets.Label("255", 227, 70, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_scrn_timeout_set = Widgets.Label("30", 95, 171, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_timeout_ms_set = Widgets.Label(" Seconds ", 162, 166, 1.0, 0xffffff, 0xa3a26a, Widgets.FONTS.DejaVu18)
  img_back = Widgets.Image("res/img/1back.png", 11, 223, scale_x=1, scale_y=1)
  lbl_freq_ms_on = Widgets.Label(" Seconds ", 163, 69, 1.0, 0xffffff, 0xa3a26a, Widgets.FONTS.DejaVu18)
  lbl_freq_on_set = Widgets.Label("30", 95, 73, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  lbl_freq_ms_off = Widgets.Label(" Seconds ", 162, 166, 1.0, 0xffffff, 0xa3a26a, Widgets.FONTS.DejaVu18)
  lbl_freq_off_set = Widgets.Label("30", 95, 171, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  circle_slider = Widgets.Circle(11, 148, 11, 0xffffff, 0xcc6600)
  circle_pro_deg = Widgets.Circle(104, 15, 10, 0xffe7d7, 0x000000)
  circle_iv_deg = Widgets.Circle(307, 12, 10, 0xd1ffff, 0x000000)
  title_settings_1 = Widgets.Title("Settings 1/2", 125, 0xffffff, 0xa3a26a, Widgets.FONTS.DejaVu9)
  title_settings_2 = Widgets.Title("Settings 2/2", 125, 0xffffff, 0xa3a26a, Widgets.FONTS.DejaVu9)

  wdt = WDT(timeout=90000)
  i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
  envpro_0 = ENVPROUnit(i2c0)
  env4_0 = ENVUnit(i2c=i2c0, type=4)
  relay2_0 = Relay2Unit((8, 9))
  clr_screen()
  wlan = network.WLAN(network.AP_IF)
  wlan.active(True)
  wlan.config(password='Rub!c0n1')
  wlan.config(authmode=network.AUTH_WPA2_PSK)
  wlan.config(essid='RubyTherm')
  resp = 'None'
  s = 'None'
  conn = 'None'
  request = 'None'
  conn_accept = False
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.settimeout(0.01)
  s.bind(('192.168.4.1',80))
  s.listen(5)
  envpro_0.set_iir_filter_coefficient(7)
  relay2_0.set_relay_cntrl(1, 0)
  relay2_0.set_relay_cntrl(2, 0)
  file_0 = open('/flash/res/settings.txt', 'r')
  settings = (file_0.readline()).split(',')
  file_0.close()
  count = 1
  for i in settings:
    if count == 8:
      if settings[7] == 'True':
        sys_active = True
      else:
        sys_active = False
    else:
      settings[int(count - 1)] = int(i)
    count = count + 1
  set_furnace_temp = settings[0]
  set_fan_temp = settings[1]
  screen_bright_min = settings[2]
  screen_bright_max = settings[3]
  screen_bright_timeout = settings[4]
  sens_read_on = settings[5]
  sens_read_off = settings[6]
  sens_read_delay = sens_read_off
  relay_1_state = False
  relay_2_state = False
  now = time.time()
  screen_now = time.time()
  last_save = time.time()
  first_run = False
  screen_num = 0
  slider_r = 12
  slider_y = 148
  slider_x = math.ceil((set_furnace_temp - 35) * 7 + slider_r)
  set_bar_selected = 'furnace'
  curr_touch = [0, 0]
  touch_set = False
  update_sensors()
  change_screen(screen_num)


def loop():
  global lbl_env_iv_temp, lbl_env_iv_hum, lbl_env_iv_pres, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, img_pro_humidity, img_pressure, img_power_off, img_power_on, img_altitude, lbl_furn_set_temp, lbl_fan_set_temp, img_flame_out, img_fan_out, img_settings, img_home, lbl_scrn_bright, lbl_scrn_bright_max, lbl_scrn_bright_min, img_scrn_bright_min, img_scrn_bright_max, lbl_scrn_timeout, line_settings_1, img_timeout_set, img_next, img_iv_humidity, lbl_sensor_freq, img_freq_set_on, lbl_sys_on, lbl_sys_off, img_freq_set_off, rect_slider, circle_furn_set_deg, img_flame, img_fan, rect_btn_furn, rect_btn_fan, circle_fan_set_deg, lbl_scrn_min_set, lbl_scrn_max_set, lbl_scrn_timeout_set, lbl_timeout_ms_set, img_back, lbl_freq_ms_on, lbl_freq_on_set, lbl_freq_ms_off, lbl_freq_off_set, circle_slider, circle_pro_deg, circle_iv_deg, title_settings_1, title_settings_2, wdt, i2c0, wlan, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0, html, var, num, pressure, alt, temp, settings_change, screen_num, set_bar_selected, env_iv_hum, relay_action, relay_1_state, slider_action, html_btn_press, sys_active, html_sys_btn_color, html_fan_txt, env_pro_temp, screen_bright_min, touch_set, env_iv_pres, t_or_d, screen_bright_max, relay_num, relay_2_state, screen_bright_timeout, furnace_or_fan, env_iv_temp, sens_read_on, sens_read_off, html_furn_txt, env_pro_hum, first_run, sens_read_delay, set_fan_temp, set_furnace_temp, slider_x, settings, curr_touch, html_sys_act_txt, env_pro_pres, now, env_pro_alt, env_pro_gas, slider_y, screen_now, slider_r, wr_set_temps, last_save, resp, s, conn, request, conn_accept, count, i
  M5.update()
  if (M5.Touch.getCount()) == 1 and touch_set == False:
    curr_touch[0] = M5.Touch.getX()
    curr_touch[1] = M5.Touch.getY()
    Widgets.setBrightness(screen_bright_max)
    screen_now = time.time()
  elif (M5.Touch.getCount()) == 0 and touch_set == True:
    touch_set = False
  connection_handler()
  if screen_num==0:
    if touch_set == False:
      pass
    btn_power()
    btn_settings_home()
    btn_temp_slider()
    btn_fan()
    btn_furnace()
  elif screen_num==1:
    if touch_set == False:
      pass
    btn_back_next()
    btn_settings_home()
    btn_bright_min_up()
    btn_bright_min_down()
    btn_bright_max_up()
    btn_bright_max_down()
    btn_timeout_up()
    btn_timeout_down()
  elif screen_num==2:
    if touch_set == False:
      pass
    btn_back_next()
    btn_settings_home()
    btn_sens_read_on_up()
    btn_sens_read_on_down()
    btn_sens_read_off_up()
    btn_sens_read_off_down()
  else:
    pass
  if sys_active == True:
    furnace_fan_control('furnace')
    furnace_fan_control('fan')
  elif sys_active == False:
    relay_control(1, 'off')
    relay_control(2, 'off')
  curr_touch[0] = 0
  curr_touch[1] = 0
  if screen_now + screen_bright_timeout < (time.time()):
    Widgets.setBrightness(screen_bright_min)
  if last_save + 300 < (time.time()):
    update_settings_file()
  update_screen_data(screen_num)
  update_sensors()
  wdt.feed()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
