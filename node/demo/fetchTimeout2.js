const FETCH_TIMEOUT = 2000;
let didTimeOut = false;

new Promise(function(resolve, reject) {
	const timeout = setTimeout(function() {
		didTimeOut = true;
		reject(new Error('Request timed out'));
	}, FETCH_TIMEOUT);

	fetch('http://localhost:8010/tmdapi/v1/test')
	.then(function(response) {
		// Clear the timeout as cleanup
		clearTimeout(timeout);
		if(!didTimeOut) {
			console.log('fetch good! ', response);
			resolve(response);
		}
	})
	.catch(function(err) {
		console.log('fetch failed! ', err);

		// Rejection already happened with setTimeout
		if(didTimeOut) return;
		// Reject with error
		reject(err);
	});
})
.then(function() {
	// Request success and no timeout
	console.log('good promise, no timeout! ');
})
.catch(function(err) {
	// Error: response error, request timeout or runtime error
	console.log('promise error! ', err);
});

const fetchRequest = (url, params, timeout) => {
    return new Promise(function(resolve, reject) {
        const TO = setTimeout(function() {

        })
    })
}
