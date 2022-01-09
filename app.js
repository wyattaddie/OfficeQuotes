const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'content-type': 'text/html' })
    if(req.url == '/111'){
        fs.createReadStream('111.html').pipe(res)
    }else{
        fs.createReadStream('Home.html').pipe(res)  
    }
    
})

server.listen(9999,console.log('listening at: http://localhost:9999'))