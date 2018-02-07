var { graphql, buildSchema  } = require('graphql');

var schema = buildSchema(`
    type Query {
        hello: String
        user: User
    }
    type User {
        id: Int
        name: String
    }
  `);

var root = {
    hello: () => 'Hello world!'
    user: () => 

};

graphql(schema, '{ hello  }', root).then((response) => {
    console.log(response);

}
)
