'use strict';

const Hapi = require('hapi');

// Create a server with a host and port
const server = Hapi.server({
	host: 'localhost',
	port: 4910
});

server.route({
	method: 'GET',
	path: '/',
	handler: function (request, reply) {
		reply('Hello, world!');
	}
});
// Add the route
server.route({
	method: 'GET',
	path: '/{name}',
	handler: function (request, reply) {
		reply('Hello, ' + encodeURIComponent(request.params.name) + '!');
	}
});


// Start the server
async function start() {

	try {
		await server.start();
	}
	catch (err) {
		console.log(err);
		process.exit(1);
	}

	console.log('Server running at:', server.info.uri);
};

start();
