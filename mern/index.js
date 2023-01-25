const express = require('express');
const mongoose = require('mongoose');

mongoString = "mongodb+srv://sanjivkannaa:sanjivkannaa@cluster0.enchhog.mongodb.net/?retryWrites=true&w=majority"
mongoose.connect(mongoString);
const database = mongoose.connection

const dataSchema = new mongoose.Schema({
    id: {
        required: true,
        type: Number
    },
    value1: {
        required: true,
        type: Number
    },
    value2: {
        required: true,
        type: Number
    },
    value3: {
        required: true,
        type: Number
    }
})

module.exports = mongoose.model('Data', dataSchema)

database.on('error', (error) => {
    console.log(error)
})

database.once('connected', () => {
    console.log('Database Connected');
})

const app = express();
app.use(express.json());

app.listen(3000, () => {
    console.log(`Server Started at ${3000}`)
})