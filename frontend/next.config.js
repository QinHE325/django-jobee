/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    API_URL: "http://127.0.0.1:8000",
    MAPBOX_ACCESS_TOKEN: 'pk.eyJ1IjoiaGVsaXVtMzI1IiwiYSI6ImNsNHJqaGthMDAyYXIzbHVhNGYzdzZqa3IifQ.WwKn8Ixzph6JS2PkU4H0Hw'
  },
}

module.exports = nextConfig
