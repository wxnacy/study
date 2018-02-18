const fetchRequest = (url, params={}, timeout=10000) => {
    let isTimeout = false;
    return new Promise(function(resolve, reject) {
        const TO = setTimeout(function() {
            isTimeout = true;
            reject(new Error('Fetch timeout'));
        }, timeout);

        fetch(url, params)
            .then(res => {
                clearTimeout(TO)
                if(!isTimeout) {
                    resolve(res)
                }
            }).catch(e => {
                if( isTimeout ){
                    return
                }
                reject(e)
            })
    })
}

fetchRequest('https://ipapi.co/json', null).then(res => {
    console.log(res);
})
fetchRequest('http://localhost:8010/test', null, 1000).catch(e => {
    console.log(e)
})
