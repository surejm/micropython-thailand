import networkimport timeimport gc, jsonfrom machine import Timerwlan=Nonertc = Nonetimer0 = Timer(0)def ntp_sync():  global rtc  rtc.ntp_sync(server="pool.ntp.org")  print('ntp synced...')def connect():  global wlan  global rtc  f = open('config.json')  cfg = json.loads(f.read())  f.close()    wlan=network.WLAN(network.STA_IF)   wlan.active(True)  wlan.connect(cfg['ap']['ssid'], cfg['ap']['pwd'])  _count = 0  while not wlan.isconnected():    time.sleep(1)    print('Waiting for connect')    _count = _count +1    if _count == 10:      break;  if wlan.isconnected():    import machine    print('IPAddress: {}'.format(wlan.ifconfig()[0]))    print('Start telnet server...')    network.telnet.start()    print('Start ftp server...')    network.ftp.start()    print('Sync ntp server...')    rtc = machine.RTC()    rtc.ntp_sync(server="pool.ntp.org")    while not rtc.synced():      time.sleep(.5)    timer0.init(period=(60000 * 10), mode=Timer.PERIODIC, callback=lambda t:ntp_sync())  else:    print('Can not connect WIFI: ', cfg['ap']['ssid'])  gc.collect()  def get_ip():  if wlan.isconnected():    return wlan.ifconfig()[0]  else:    return None