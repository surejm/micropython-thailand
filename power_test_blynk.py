from upower import BtPower
import _thread as th
import BlynkLib
import wifi_connect as wlan


wlan.connect()
oled.text(wlan.get_ip(), 3, 35)
blynk = BlynkLib.Blynk('04bf32882c1f4b758b253605c6793893', '27.254.63.34')
def loop():
      # BLYNK
      blynk.virtual_write(0, '{0:.0f}'.format(value[0]))
      blynk.virtual_write(1, '{0:.2f}'.format(value[1]))
      blynk.virtual_write(2, '{0:.0f}'.format(value[2]))
      blynk.virtual_write(3, '{0:.0f}'.format(value[3]))
      blynk.virtual_write(4, '{0:.0f}'.format(value[0]))
      blynk.virtual_write(5, '{0:.2f}'.format(value[1]))
    
th.start_new_thread(blynk.run, ())
th.start_new_thread(loop, ())
