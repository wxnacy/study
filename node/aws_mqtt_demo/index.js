const awsIot = require('aws-iot-device-sdk')
// https://github.com/aws/aws-iot-device-sdk-js

AWS_MQTT_ACCESS_KEY_ID = ''
AWS_MQTT_SECRET_ACCESS_KEY = ''
AWS_MQTT_ENDPOINT = ''
AWS_MQTT_REGION = 'us-west-2'


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
    device.subscribe('check_alive');
    let pub = device.publish('check_alive', JSON.stringify({test_data: 1}));
    console.log(pub);
  });
device
  .on('message', (topic, payload) => {
    console.log('message', topic, payload.toString());
    // device.unsubscribe('screen_')
    // device.end()
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
