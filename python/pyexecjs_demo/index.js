var uglifyjs = require('uglify-js');

const test = (text) => {
    return uglifyjs.minify(text);
}

let res = test('function add(first, second) { return first + second;   }')
console.log(res);

