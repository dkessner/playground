//
// webpack.config.js
//

const path = require('path');


module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'functions_bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
};

