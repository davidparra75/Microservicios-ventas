const mongoose = require("mongoose")

const SaleSchema = new mongoose.Schema({
    user: {
        type: String,
        required: true
    },
    product: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    }
})

module.exports = mongoose.model("Sale", SaleSchema)