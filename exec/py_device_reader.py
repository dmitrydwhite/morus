import pywinusb.hid as HID

class Morus_Reader():
  suspended = False

  tare = []

  scale = False

  messages = {
    'CONNECTED': 'Scale is connected',
    'NOT_CONNECTED': 'Could not find anticipated scale',
    'DISCONNECT': 'Scale disconnecting'
  }

  def start(self, vendor_id, product_id, socket):
    # first check for our target device
    devices = HID.find_all_hid_devices()
    for device in devices:
      if device.vendor_id == vendor_id and device.product_id == product_id:
        self.scale = device
        break

    if self.scale:
      self.found_scale()
    else:
      self.couldnt_find_scale()

  def suspend(self):
    if not self.suspended:
      self.suspended = True

  def tell(self, data):
    # broadcast data to the console and the client
    print(data)

  def resume(self):
    if self.suspended:
      self.suspended = False

  def found_scale(self):
    # broadcast the goodnews and begin listening
    self.tell(self.messages['CONNECTED'])
    self.scale.open()
    self.scale.set_raw_data_handler(self.listen_for_weight)

  def couldnt_find_scale(self):
    # broadcast the bad news and close the websocket connection
    print('ugh')

  def listen_for_weight(self, data):
    # listen for weight, and send the message when weight is received
    if not self.suspended and data != self.tare:
      self.tare = data
      self.tell(data)

  def terminate(self):
    # broadcast termination message and close the websocket connection
    print('terminating')

if __name__ == "__main__":
  Morus_Reader()
