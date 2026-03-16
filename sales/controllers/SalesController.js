const Sale = require("../models/Sale")

// Crear venta
exports.createSale = async (req, res) => {
    try {
        const sale = new Sale(req.body)
        await sale.save()
        res.status(201).json(sale)
    } catch (error) {
        res.status(500).json({ error: error.message })
    }
}

// Obtener todas las ventas
exports.getSales = async (req, res) => {
    try {
        const sales = await Sale.find()
        res.json(sales)
    } catch (error) {
        res.status(500).json({ error: error.message })
    }
}

// Ventas por usuario
exports.getSalesByUser = async (req, res) => {
    try {
        const sales = await Sale.find({ user: req.params.user })
        res.json(sales)
    } catch (error) {
        res.status(500).json({ error: error.message })
    }
}

// Ventas por fecha
exports.getSalesByDate = async (req, res) => {
    try {
        const date = new Date(req.params.date)
        const sales = await Sale.find({
            date: {
                $gte: date,
                $lt: new Date(date.getTime() + 24 * 60 * 60 * 1000)
            }
        })
        res.json(sales)
    } catch (error) {
        res.status(500).json({ error: error.message })
    }
}