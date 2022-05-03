var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  mode: "development",
  entry: './core/static/js/script.js',
  output: {
      path: path.resolve('./core/static/webpack_bundles/'),
      filename: "bunble.js"
  },
  watch: true,
  devtool: "source-map",
  module: {},

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}