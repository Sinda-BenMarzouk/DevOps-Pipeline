const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello bochra')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})

const helloWorld = () => {
    return 'hello bochra'
}

module.exports= {helloWorld}