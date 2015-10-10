import pywinusb.hid as HID

class Morus_Reader:
  suspended = False

  scale = False

  messages = {
    CONNECTED: 'Scale is connected',
    NOT_CONNECTED: 'Could not find anticipated scale'
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

  def tell(data):
    # broadcast data to the console and the client

  def resume(self):
    if self.suspended:
      self.suspended = False

  def found_scale():
    # broadcast the goodnews and begin listening

  def couldnt_find_scale():
    # broadcast the bad news and close the websocket connection

  def listen_for_weight():
    # listen for weight, and send the message when weight is received

  def terminate():
    # broadcast termination message and close the websocket connection