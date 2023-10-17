// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/login', // Proxy requests to this URL
        createProxyMiddleware({
            target: 'https://accounts.spotify.com',
            changeOrigin: true,
        })
    );
};
