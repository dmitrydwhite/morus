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

  connection = False

  def start(self, vendor_id, product_id, socket):
    print('M.O.R.U.S')
    self.connection = socket
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
    self.connection.write_message(data)

  def resume(self):
    if self.suspended:
      self.suspended = False

  def found_scale(self):
    # broadcast the goodnews and begin listening
    # self.tell(self.messages['CONNECTED'])
    self.scale.open()
    self.scale.set_raw_data_handler(self.listen_for_weight)

  def couldnt_find_scale(self):
    # broadcast the bad news and close the websocket connection
    self.tell(self.messages['NOT_CONNECTED'])
    # self.socket.close()

  def listen_for_weight(self, data):
    # listen for weight, and send the message when weight is received
    if not self.suspended and data != self.tare:
      self.tare = data
      weights_array = []
      for num in data:
        weights_array.append(num)
      self.tell(bytes(weights_array))

  def terminate(self):
    # broadcast termination message and close the websocket connection
    print('terminating')

import tornado.ioloop
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=3000, help="run on the given port", type=int)

class ScaleSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
  
    def open(self):
        print('M.O.R.U.S')
        reader = Morus_Reader()
        reader.start(2338, 32775, self)
      

if __name__ == '__main__':
    app = tornado.web.Application([
      (r'/', ScaleSocketHandler),     
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    

    
    
