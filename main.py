import os, sys, io
import M5
from M5 import *
from unit import Relay2Unit
from hardware import *
from unit import ENVPROUnit
import time
from unit import ENVUnit
lbl_env_iv_temp = None
circle_curr_deg = None
img_humidity = None
img_pressure = None
img_power_off = None
img_power_on = None
img_altitude = None
img_flame_out = None
img_fan_out = None
lbl_env_pro_temp = None
lbl_env_pro_hum = None
lbl_env_pro_pres = None
lbl_env_pro_alt = None
rect_slider = None
img_flame = None
img_fan = None
rect_btn_furn = None
lbl_env_iv_hum = None
lbl_env_iv_pres = None
lbl_furn_set_temp = None
circle_furn_set_deg = None
circle_slider = None
rect_btn_fan = None
circle_fan_set_deg = None
lbl_fan_set_temp = None
oldData1 = None
i2c0 = None
oldData2 = None
oldData3 = None
file_0 = None
env4_0 = None
envpro_0 = None
relay2_0 = None
import math
set_bar_selected = None
slider_action = None
relay_num = None
relay_action = None
furnace_or_fan = None
temp = None
pressure = None
alt = None
env_iv_hum = None
relay_1_state = None
env_pro_temp = None
screen_now = None
env_iv_pres = None
sys_active = None
relay_2_state = None
env_pro_hum = None
env_iv_temp = None
slider_x = None
first_run = None
sens_read_delay = None
env_pro_pres = None
set_fan_temp = None
now = None
env_pro_alt = None
set_furnace_temp = None
slider_y = None
env_pro_gas = None
screen_bright_delay = None
slider_r = None
set_temps = None
wr_set_temps = None
screen_num = None
# Describe this function...
def btn_touch():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if M5.Touch.getTouchPointRaw() != oldData1:
    oldData1 = M5.Touch.getTouchPointRaw()
    Widgets.setBrightness(255)
    screen_now = time.time()
    if first_run == False:
      pass
    else:
      if (M5.Touch.getX()) >= 238 and (M5.Touch.getX()) <= 318 and (M5.Touch.getY()) >= 0 and (M5.Touch.getY()) <= 85:
        if sys_active == False:
          sys_active = True
        else:
          sys_active = False
        sys_act()
      elif (M5.Touch.getY()) >= 130 and (M5.Touch.getY()) <= 160 and (M5.Touch.getY()) >= 12 and (M5.Touch.getY()) <= 306:
        update_slider(set_bar_selected, 'change_pos')
      elif (M5.Touch.getX()) >= 0 and (M5.Touch.getX()) <= 160 and (M5.Touch.getY()) >= 233 and (M5.Touch.getY()) <= 310:
        set_bar_selected = 'furnace'
        update_slider(set_bar_selected, 'change_sys')
      elif (M5.Touch.getX()) >= 160 and (M5.Touch.getX()) <= 320 and (M5.Touch.getY()) >= 233 and (M5.Touch.getY()) <= 310:
        set_bar_selected = 'fan'
        update_slider(set_bar_selected, 'change_sys')
  else:
    pass
# Describe this function...
def update_slider(set_bar_selected, slider_action):
  global relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
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
def update_sensors():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
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
    if set_temps[0] != set_furnace_temp or set_temps[1] != set_fan_temp:
      print('Writing new temps.')
      set_temps[0] = set_furnace_temp
      set_temps[1] = set_fan_temp
      wr_set_temps = [str(set_furnace_temp), str(set_fan_temp)]
      file_0 = open('/flash/res/set_temps.txt', 'w')
      file_0.write(','.join(wr_set_temps))
      file_0.close()
    first_run = True
  else:
    pass
# Describe this function...
def clr_screen():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  lbl_env_iv_temp.setVisible(False)
  lbl_env_iv_hum.setVisible(False)
  lbl_env_iv_pres.setVisible(False)
  lbl_env_pro_temp.setVisible(False)
  lbl_env_pro_hum.setVisible(False)
  lbl_env_pro_pres.setVisible(False)
  lbl_env_pro_alt.setVisible(False)
  lbl_furn_set_temp.setVisible(False)
  lbl_fan_set_temp.setVisible(False)
  rect_slider.setVisible(False)
  rect_btn_furn.setVisible(False)
  rect_btn_fan.setVisible(False)
  circle_curr_deg.setVisible(False)
  circle_furn_set_deg.setVisible(False)
  circle_slider.setVisible(False)
  circle_fan_set_deg.setVisible(False)
  img_humidity.setVisible(False)
  img_pressure.setVisible(False)
  img_power_off.setVisible(False)
  img_power_on.setVisible(False)
  img_altitude.setVisible(False)
  img_flame.setVisible(False)
  img_fan.setVisible(False)
  img_flame_out.setVisible(False)
  img_fan_out.setVisible(False)
# Describe this function...
def sys_act():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  if sys_active == False:
    img_power_on.setVisible(False)
    img_power_off.setVisible(True)
    sens_read_delay = 240
  else:
    img_power_off.setVisible(False)
    img_power_on.setVisible(True)
    sens_read_delay = 60
# Describe this function...
def relay_control(relay_num, relay_action):
  global set_bar_selected, slider_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
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
def update_screen_data():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  lbl_env_pro_temp.setText(str(env_pro_temp))
  lbl_env_pro_hum.setText(str(env_pro_hum))
  lbl_env_pro_pres.setText(str(env_pro_pres))
  lbl_env_pro_alt.setText(str(env_pro_alt))
  lbl_furn_set_temp.setText(str(set_furnace_temp))
  lbl_fan_set_temp.setText(str(set_fan_temp))
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
# Describe this function...
def furnace_fan_control(furnace_or_fan):
  global set_bar_selected, slider_action, relay_num, relay_action, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
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
def c_to_f(temp):
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  temp = 1.8 * temp + 32
  return int(temp)
# Describe this function...
def hpa_to_inhg(pressure):
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  pressure = 0.02953 * pressure
  return "%.2f"%(pressure)
# Describe this function...
def m_to_ft(alt):
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  alt = 3.28 * alt
  return int(alt)
# Describe this function...
def load_screen_elements():
  global set_bar_selected, slider_action, relay_num, relay_action, furnace_or_fan, temp, pressure, alt, env_iv_hum, relay_1_state, env_pro_temp, screen_now, env_iv_pres, sys_active, relay_2_state, env_pro_hum, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num, lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0
  sys_act()
  lbl_env_pro_temp.setVisible(True)
  lbl_furn_set_temp.setVisible(True)
  lbl_fan_set_temp.setVisible(True)
  circle_slider.setCursor(x=slider_x, y=slider_y)
  rect_slider.setVisible(True)
  circle_slider.setVisible(True)
  circle_furn_set_deg.setVisible(True)
  circle_fan_set_deg.setVisible(True)
  circle_curr_deg.setVisible(True)
  rect_btn_furn.setVisible(True)
  rect_btn_fan.setVisible(True)
  img_pressure.setVisible(True)
  img_humidity.setVisible(True)
  img_altitude.setVisible(True)
  img_flame_out.setVisible(True)
  img_fan_out.setVisible(True)
def setup():
  global lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0, temp, pressure, alt, slider_action, env_iv_hum, relay_action, relay_1_state, env_pro_temp, screen_now, set_bar_selected, env_iv_pres, sys_active, relay_num, relay_2_state, env_pro_hum, furnace_or_fan, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num
  M5.begin()
  lbl_env_iv_temp = Widgets.Label("70", 0, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu72)
  circle_curr_deg = Widgets.Circle(104, 15, 10, 0xffffff, 0x000000)
  img_humidity = Widgets.Image("res/img/1humidity.png", 0, 165, scale_x=0.6, scale_y=0.6)
  img_pressure = Widgets.Image("res/img/1pressure.png", 151, 165, scale_x=0.6, scale_y=0.6)
  img_power_off = Widgets.Image("res/img/1power_off.png", 238, 0, scale_x=1, scale_y=1)
  img_power_on = Widgets.Image("res/img/1power_on.png", 238, 0, scale_x=1, scale_y=1)
  img_altitude = Widgets.Image("res/img/1altitude.png", 177, 197, scale_x=0.6, scale_y=0.5)
  img_flame_out = Widgets.Image("res/img/1heating_out.png", 95, 75, scale_x=1, scale_y=1)
  img_fan_out = Widgets.Image("res/img/1fan_out.png", 178, 75, scale_x=1, scale_y=1)
  lbl_env_pro_temp = Widgets.Label("70", 0, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu72)
  lbl_env_pro_hum = Widgets.Label("99%", 34, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_pro_pres = Widgets.Label("29.99 inHg", 182, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_pro_alt = Widgets.Label("1000 ft", 225, 199, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  rect_slider = Widgets.Rectangle(5, 146, 310, 5, 0xffffff, 0xcc6600)
  img_flame = Widgets.Image("res/img/1heating.png", 95, 75, scale_x=1, scale_y=1)
  img_fan = Widgets.Image("res/img/1fan.png", 178, 75, scale_x=1, scale_y=1)
  rect_btn_furn = Widgets.Rectangle(0, 233, 90, 5, 0xcc6600, 0xcc6600)
  lbl_env_iv_hum = Widgets.Label("99%", 34, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_env_iv_pres = Widgets.Label("29.99 inHg", 182, 166, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu24)
  lbl_furn_set_temp = Widgets.Label("70", 0, 90, 1.0, 0xcc6600, 0x000000, Widgets.FONTS.DejaVu40)
  circle_furn_set_deg = Widgets.Circle(58, 98, 5, 0xcc6600, 0x000000)
  circle_slider = Widgets.Circle(11, 148, 11, 0xffffff, 0xcc6600)
  rect_btn_fan = Widgets.Rectangle(228, 233, 90, 5, 0x339999, 0x339999)
  circle_fan_set_deg = Widgets.Circle(313, 98, 5, 0x339999, 0x000000)
  lbl_fan_set_temp = Widgets.Label("35", 256, 90, 1.0, 0x339999, 0x000000, Widgets.FONTS.DejaVu40)
  i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
  envpro_0 = ENVPROUnit(i2c0)
  env4_0 = ENVUnit(i2c=i2c0, type=4)
  relay2_0 = Relay2Unit((8, 9))
  clr_screen()
  envpro_0.set_iir_filter_coefficient(7)
  relay2_0.set_relay_cntrl(1, 0)
  relay2_0.set_relay_cntrl(2, 0)
  file_0 = open('/flash/res/set_temps.txt', 'r')
  set_temps = (file_0.readline()).split(',')
  file_0.close()
  relay_1_state = False
  relay_2_state = False
  sys_active = False
  sens_read_delay = 10
  screen_bright_delay = 5
  set_furnace_temp = int(set_temps[0])
  set_fan_temp = int(set_temps[1])
  set_temps[0] = set_furnace_temp
  set_temps[1] = set_fan_temp
  now = time.time()
  screen_now = time.time()
  first_run = False
  screen_num = 0
  slider_r = 12
  slider_y = 148
  slider_x = math.ceil((set_furnace_temp - 35) * 7 + slider_r)
  set_bar_selected = 'furnace'
  update_sensors()
  load_screen_elements()
def loop():
  global lbl_env_iv_temp, circle_curr_deg, img_humidity, img_pressure, img_power_off, img_power_on, img_altitude, img_flame_out, img_fan_out, lbl_env_pro_temp, lbl_env_pro_hum, lbl_env_pro_pres, lbl_env_pro_alt, rect_slider, img_flame, img_fan, rect_btn_furn, lbl_env_iv_hum, lbl_env_iv_pres, lbl_furn_set_temp, circle_furn_set_deg, circle_slider, rect_btn_fan, circle_fan_set_deg, lbl_fan_set_temp, oldData1, i2c0, oldData2, oldData3, file_0, env4_0, envpro_0, relay2_0, temp, pressure, alt, slider_action, env_iv_hum, relay_action, relay_1_state, env_pro_temp, screen_now, set_bar_selected, env_iv_pres, sys_active, relay_num, relay_2_state, env_pro_hum, furnace_or_fan, env_iv_temp, slider_x, first_run, sens_read_delay, env_pro_pres, set_fan_temp, now, env_pro_alt, set_furnace_temp, slider_y, env_pro_gas, screen_bright_delay, slider_r, set_temps, wr_set_temps, screen_num
  M5.update()
  btn_touch()
  update_sensors()
  if sys_active == True:
    furnace_fan_control('furnace')
    furnace_fan_control('fan')
  elif sys_active == False:
    relay_control(1, 'off')
    relay_control(2, 'off')
  if screen_now + screen_bright_delay < (time.time()):
    Widgets.setBrightness(35)
  update_screen_data()
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
