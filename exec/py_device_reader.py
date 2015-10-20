import tornado.ioloop
import tornado.websocket
from tornado.options import define, options, parse_command_line
import pywinusb
import pywinusb.hid as HID

class Morus_Reader():
  """This class is built on top of pywinusb and designed to explicitly read the
     digital scale we expect to be connected to this app
  """

  # Initiating class properties #
  suspended = False

  tare = []

  scale = False

  messages = {
    'CONNECTED': 'Scale is connected',
    'NOT_CONNECTED': 'Could not find anticipated scale',
    'DISCONNECT': 'Scale disconnecting'
  }

  connection = False
  # --------------------------- #

  def start(self, vendor_id, product_id, socket):
    """The entry point for the reader app.

    Args:
       self: The class
       vendor_id: Vendor ID of the scale to be connected
       product_id: Product ID of same
       socket: The specific websocket connection to communicate scale info
    """
    
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
    # Suspending the Reader app
    if not self.suspended:
      self.suspended = True

  def tell(self, data):
    # broadcast data to the console and the client
    print(data)
    self.connection.write_message(data)

  def resume(self, connection):
    # Resuming the reader app
    if self.suspended:
      self.suspended = False
      if connection != self.connection:
        self.connection = connection

  def found_scale(self):
    # Open the HID scale and set the listener with the data broadcaster method
    self.scale.open()
    self.scale.set_raw_data_handler(self.listen_for_weight)

  def couldnt_find_scale(self):
    # broadcast the bad news and close the websocket connection
    self.tell(self.messages['NOT_CONNECTED'])

  def listen_for_weight(self, data):
    # send the data from the scale when weight is received
    if not self.suspended and data != self.tare:
      self.tare = data
      weights_array = []
      for num in data:
        weights_array.append(num)
      self.tell(bytes(weights_array))

  def terminate(self):
    # broadcast termination message and close the websocket connection
    print('terminating')
    self.connection.close()

define("port", default=3000, help="run on the given port", type=int)

class ScaleSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
  
    def open(self):
              
        if not reader.suspended:
          print('M.O.R.U.S')
          
          reader.start(2338, 32775, self)
        else:
          print('M.O.R.U.S resuming...')
          reader.resume(self)

    def on_close(self):
        print('m.o.r.u.s connection closing')
        reader.suspend()

if __name__ == '__main__':
    print('M.O.R.U.S  (c)2015 Dmitry White')
    print('Contact at white.dmitry@gmail.com for technical support')
    print('Type Ctrl+C or close this window to end program')
    reader = Morus_Reader()
    app = tornado.web.Application([
      (r'/', ScaleSocketHandler),     
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    

    
    
