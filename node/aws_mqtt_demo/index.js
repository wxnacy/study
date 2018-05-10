const awsIot = require('aws-iot-device-sdk')
// https://github.com/aws/aws-iot-device-sdk-js


AWS_MQTT_ACCESS_KEY_ID = 'AKIAIHQ4C6EPFMSTMDDQ'
AWS_MQTT_SECRET_ACCESS_KEY = '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'
AWS_MQTT_ENDPOINT = 'a3bdyb5rk1w4po.iot.us-west-2.amazonaws.com'
AWS_MQTT_REGION = 'us-west-2'
AWS_MQTT_CLIENT_ID = 'iotconsole-1498824269837-3'



const device = awsIot.device({
  protocol: "wss",
  accessKeyId: AWS_MQTT_ACCESS_KEY_ID,
  secretKey: AWS_MQTT_SECRET_ACCESS_KEY,
  sessionToken: null,
  host: AWS_MQTT_ENDPOINT
});

// Device is an instance returned by mqtt.Client(), see mqtt.js for full
// documentation.
device
  .on('connect',  ()=> {
    console.log("connect");
    device.subscribe('screen_');
    device.publish('screen_', JSON.stringify({test_data: 1}));
  });
device
  .on('message', (topic, payload) => {
    console.log('message', topic, payload.toString());
    device.unsubscribe('screen_')
    device.end()
  });
device
  .on('close', ()=> {
    console.log('close');
  });
device
  .on('reconnect', ()=> {
    console.log('reconnect');
  });
device
  .on('offline', ()=> {
    console.log('offline');
  });
device
  .on('error', (error)=> {
    console.error('error', error);
  });
