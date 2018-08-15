const awsIot = require('aws-iot-device-sdk')
// https://github.com/aws/aws-iot-device-sdk-js
//
AWS_MQTT_ACCESS_KEY_ID = 'AKIAJGY4DNP7MGYLOFKQ'
AWS_MQTT_SECRET_ACCESS_KEY = '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'
AWS_MQTT_ENDPOINT = 'a3bdyb5rk1w4po.iot.us-west-2.amazonaws.com'
AWS_MQTT_REGION = 'us-west-2'
AWS_MQTT_CLIENT_ID = 'iotconsole-1525948483203-1'

class MQTT {
  constructor(accessKeyId, accessKeySecret, region, host, clientId) {
    this.accessKeyId = accessKeyId;
    this.accessKeySecret = accessKeySecret;
    this.region = region;
    this.host = host;
    this.clientId = clientId;
  }

  _init() {
    this.client = awsIot.device({
      protocol: "wss",
      accessKeyId: this.accessKeyId,
      secretKey: this.accessKeySecret,
      sessionToken: null,
      host: this.host
    });
  }

  connect(){
    let device = this.client;
    return new Promise(resolve, reject){
      device.on('connect',  ()=> {
        console.log("connect");
      });
      device.on('error', (error)=> {
        console.error('error', error);
      });
    }
  }

  publish(topic, payload) {
    if( typeof payload == 'object' ){
      
    }
    let device = this.client;
    device.publish(topicEle.value, msgEle.value);
  }

}


subEle.addEventListener('click', e => {
  device.subscribe(topicEle.value);
}, false);

sendEle.addEventListener('click', e => {
  device.publish(topicEle.value, msgEle.value);
}, false);

closeEle.addEventListener('click', e => {
  device.unsubscribe(topicEle.value)
}, false);

device
  .on('message', (topic, payload) => {
    console.log('message', topic, payload.toString());
    $('#output').append($(`<li>${payload.toString()}<li>`))
  });
device
  .on('close', ()=> {
    console.log('close');
  });
device.on('reconnect', ()=> {
    console.log('reconnect');
  });
device
  .on('offline', ()=> {
    console.log('offline');
  });
