var express = require('express');
var graphqlHTTP = require('express-graphql');
var { buildSchema } = require('graphql');

// Construct a schema, using GraphQL schema language

var userSchema = `
    type User {
        id: Int
        name: String
    }
`
var schema = buildSchema(`
	type Query {
		hello: String
        name(like: String): String
        age(a: Int!, b: Int): String
        user: User
        users: [User]
	}
    ${userSchema}
`);

class User{
    constructor(name) {
        this.name = name
        this.id = 1
    }

}

// The root provides a resolver function for each API endpoint
var root = {
	hello: () => {
		return 'Hello world!';
	},
    name: ({like}) => {
        return like || 'wxnacy'
    },
    age: (args) => {
        return `${args.a} ${args.b}`
    },
    user: () => {
        return new User('wxnacy')
    },
    users: () => {
        return [new User('haha'), new User('wxnacy')]
    }
};

var app = express();
app.use('/graphql', graphqlHTTP({
	schema: schema,
	rootValue: root,
	graphiql: true,
}));
app.listen(4900);
console.log('Running a GraphQL API server at localhost:4000/graphql');
